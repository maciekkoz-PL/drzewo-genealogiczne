#!/usr/bin/env python3
"""Download public Arolsen document pages, their linked scans and index data.

Uses only document IDs already found in a public catalogue/result. It does not
submit research requests, forms concerning relatives, or messages.
"""
import argparse
import datetime
import hashlib
import json
import re
from pathlib import Path
import urllib.parse
import urllib.request
from lxml import html


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('doc_ids', nargs='+', help='Known numeric DocIDs')
    parser.add_argument('--outdir', default='work/arolsen')
    parser.add_argument('--log', default='work/arolsen_downloads.jsonl')
    parser.add_argument('--refresh', action='store_true')
    parser.add_argument('--max-images', type=int, default=0,
                        help='Maximum linked scans per document; 0 downloads all.')
    args = parser.parse_args()
    output = Path(args.outdir)
    output.mkdir(parents=True, exist_ok=True)
    log = Path(args.log)
    log.parent.mkdir(parents=True, exist_ok=True)

    def fetch(url, path, payload=None, image=False):
        if path.exists() and not args.refresh:
            return path.read_bytes()
        row = {'url': url, 'path': str(path), 'method': 'POST index lookup' if payload else 'GET'}
        if payload is not None:
            row['params'] = payload
        try:
            request = urllib.request.Request(
                url, data=json.dumps(payload).encode() if payload is not None else None,
                headers={'Content-Type': 'application/json; charset=UTF-8',
                         'Referer': 'https://collections.arolsen-archives.org/'})
            with urllib.request.urlopen(request, timeout=40) as response:
                body = response.read()
                row.update(status=response.status, final_url=response.url,
                           content_type=response.headers.get('Content-Type'),
                           size=len(body), sha256=hashlib.sha256(body).hexdigest())
            if image and not body.startswith(b'\xff\xd8\xff'):
                path = path.with_suffix('.odpowiedz')
                row['path'] = str(path)
                path.write_bytes(body)
                raise ValueError('Response is not a JPEG; saved as .odpowiedz')
            path.write_bytes(body)
            return body
        except Exception as error:
            row['error'] = str(error)
            raise
        finally:
            row['access_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
            with log.open('a') as stream:
                stream.write(json.dumps(row, ensure_ascii=False) + '\n')

    for doc in args.doc_ids:
        if not doc.isdigit():
            raise ValueError('DocID must be numeric')
        try:
            page = fetch('https://collections.arolsen-archives.org/en/document/' + doc,
                         output / f'Arolsen_D{doc}.html')
            tree = html.fromstring(page)
            links = list(dict.fromkeys(
                re.sub(r'^https?:/+', 'https://', s.replace('\\', '/'))
                for s in tree.xpath('//img/@src')
                if 'collections-server.arolsen-archives.org/' in s))
            if not links:
                raise ValueError('No linked archival scans found')
            scans = links[:args.max_images] if args.max_images > 0 else links
            for position, scan in enumerate(scans, 1):
                if urllib.parse.urlsplit(scan).hostname != 'collections-server.arolsen-archives.org':
                    raise ValueError('Unexpected image host')
                scan = urllib.parse.quote(scan, safe=':/%?=&')
                name = (f'Arolsen_D{doc}.jpg' if len(links) == 1
                        else f'Arolsen_D{doc}_{position:03d}.jpg')
                fetch(scan, output / name, image=True)
            fetch('https://collections-server.arolsen-archives.org/ITS-WS.asmx/GetPersonListByDocId',
                  output / f'Arolsen_D{doc}_person.json', {'lang': 'en', 'docId': doc})
            print(f'{doc}: saved page, {len(scans)}/{len(links)} linked scans '
                  'and public index data', flush=True)
        except Exception as error:
            print(f'{doc}: {error}', flush=True)


if __name__ == '__main__':
    main()
