"""Two new public-index queries; do not rerun without a reason."""
from pathlib import Path
import urllib.request, http.cookiejar, json, datetime, hashlib, uuid

p = Path('work/h017/arolsen_queries')
p.mkdir(parents=True, exist_ok=True)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
log = []

def call(key, method, args):
    url = 'https://collections-server.arolsen-archives.org/ITS-WS.asmx/' + method
    row = {'url': url, 'params': args, 'method': 'POST public index search',
           'access_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        req = urllib.request.Request(url, data=json.dumps(args).encode(), headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Referer': 'https://collections.arolsen-archives.org/'})
        with opener.open(req, timeout=30) as response:
            body = response.read()
            row.update(status=response.status, final_url=response.url)
        path = p / f'{key}_{method}.json'
        path.write_bytes(body)
        row.update(path=str(path), size=len(body), sha256=hashlib.sha256(body).hexdigest())
        data = json.loads(body).get('d')
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except ValueError:
                pass
        print(key, method, 'rows=' + str(len(data)) if isinstance(data, list) else str(data)[:500], flush=True)
        return data
    except Exception as ex:
        row['error'] = str(ex)
        raise
    finally:
        log.append(row)
        (p / 'downloads.json').write_text(json.dumps(log, ensure_ascii=False, indent=2))

for key, query in [('surname1910', 'Chmielewski 1910'), ('maiden_any_given', 'Poprawka')]:
    uid = uuid.uuid4().hex[:20]
    try:
        call(key, 'BuildQueryGlobalForAngular', {'uniqueId': uid, 'lang': 'en', 'archiveIds': [], 'strSearch': query, 'synSearch': True})
        count = call(key, 'GetCount', {'uniqueId': uid, 'lang': 'en', 'searchType': 'person', 'useFilter': False})
        if str(count).isdigit() and 0 < int(count) <= 300:
            call(key, 'GetPersonList', {'uniqueId': uid, 'lang': 'en', 'rowNum': 0, 'orderBy': 'LastName', 'orderType': 'asc'})
    except Exception as ex:
        print(key, str(ex), flush=True)
