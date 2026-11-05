#!/usr/bin/env python3
"""Read-only validation of IDs, stored evidence and a genealogy checkpoint.

Run from the repository root. --baseline compares relationship/event evidence
with a chosen Git checkpoint. Does not download records or mutate the workbook.
"""
import argparse
import datetime
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import zipfile

import openpyxl
from PIL import Image


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', help='Git commit before this research stage')
    parser.add_argument('--stage', default='badania/2026-11-05-sesja-03-polaczenie')
    parser.add_argument('--output', help='Write validation JSON at this path')
    args = parser.parse_args()
    stage = Path(args.stage)
    book = Path('Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
    w = openpyxl.load_workbook(book, read_only=True)
    registry = {
        'ZRODLA_I_SKANY': 'S', 'KANDYDACI_I_HOMONIMY': 'C',
        'RELACJE': 'R', 'ZDARZENIA_I_FAKTY': 'E',
        'DZIENNIK_KWEREND': 'L', 'PLIKI_DOWODOWE': 'F',
        'KOREKTY_I_SPRZECZNOSCI': 'Q', 'ZADANIA_AGENTA': 'T',
    }
    tables, counts = {}, {}
    for sn, prefix in registry.items():
        rows = [tuple(row) for row in w[sn].iter_rows(values_only=True)
                if isinstance(row[0], str) and re.fullmatch(prefix + r'\d+', row[0])]
        assert len({r[0] for r in rows}) == len(rows), ('duplicate ID', sn)
        tables[sn] = {r[0]: r for r in rows}
        counts[sn] = len(rows)
    known_sources = set(tables['ZRODLA_I_SKANY'])
    known_candidates = set(tables['KANDYDACI_I_HOMONIMY'])
    people = {row[0] for sn in ['RDZEN_RODZINY', 'RODZINA_Z_RELACJI']
              for row in w[sn].iter_rows(values_only=True)
              if isinstance(row[0], str) and re.fullmatch(r'P\d+', row[0])}
    unresolved = {row[0] for row in w['HIPOTEZY_OTWARTE'].iter_rows(values_only=True)
                  if isinstance(row[0], str) and re.fullmatch(r'H\d+', row[0])}
    resolved = {row[0] for row in w['HIPOTEZY_ROZSTRZYGNIETE'].iter_rows(values_only=True)
                if isinstance(row[0], str) and re.fullmatch(r'H\d+', row[0])}
    assert not unresolved & resolved
    assert 'H001' in resolved and 'H017' in unresolved
    assert 'H017' not in resolved
    source_references = 0
    for sn in w.sheetnames:
        for row in w[sn].iter_rows(values_only=True):
            for value in row:
                if isinstance(value, str):
                    for sid in re.findall(r'\bS\d{3}\b', value):
                        assert sid in known_sources, ('unknown source', sn, sid)
                        source_references += 1
    for row in tables['RELACJE'].values():
        assert row[1] in people | known_candidates, ('unknown relation endpoint', row)
        assert row[2] in people | known_candidates, ('unknown relation endpoint', row)
    for row in tables['ZRODLA_I_SKANY'].values():
        if isinstance(row[9], str) and row[9].startswith('badania/'):
            assert Path(row[9]).exists(), ('missing source path', row[0], row[9])
    for row in tables['PLIKI_DOWODOWE'].values():
        if isinstance(row[1], str) and row[1].startswith('badania/'):
            assert Path(row[1]).exists(), ('missing evidence path', row[0], row[1])
    assert all('RELACJA' in tables['RELACJE'][rid][5] for rid in ['R011','R012','R017'])
    assert all('S086' in tables['RELACJE'][rid][6] for rid in ['R007','R008'])

    manifest_counts = {}
    for manifest in sorted(Path('badania').glob('*/manifest_zrodel_sesji.json')):
        entries = json.loads(manifest.read_text())
        for entry in entries:
            path = Path(entry['path'])
            body = path.read_bytes()
            assert hashlib.sha256(body).hexdigest() == entry['sha256'], ('hash mismatch', path)
            assert len(body) == entry['size'], ('size mismatch', path)
        manifest_counts[str(manifest)] = len(entries)
    images = list((stage / 'zrodla').rglob('*.jpg'))
    for path in images:
        with Image.open(path) as picture:
            assert picture.format == 'JPEG'
            picture.verify()
    archive = Path('Marysia_PAKIET_ZRODEL_2026-11-05.zip')
    with zipfile.ZipFile(archive) as handle:
        assert handle.testzip() is None
        zip_entries = len(handle.infolist())
    draft = stage / 'WNIOSEK_BOGUSLAW_WARSZAWA_BEZ_PESEL_SZKIC.docx'
    with zipfile.ZipFile(draft) as handle:
        assert handle.testzip() is None
        xml = handle.read('word/document.xml').decode()
        assert 'BOGUSŁAW KAZIMIERZ CHMIELEWSKI' in xml
        assert 'POPRAWKA' in xml and 'NIEZNANY' in xml
        assert 'SZKIC' in xml and 'NIEWYSŁANY' in xml

    link_files = [Path('README.md'), Path('RODZICE_BOGUSLAWA_PRIORYTET.md'),
                  Path('Marysia_INSTRUKCJA_DLA_AGENTA.md'), Path('procedury/README.md'),
                  Path('ZBADANE_ZRODLA.md')] + list(stage.glob('*.md'))
    local_links = 0
    for path in link_files:
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if target.startswith(('http://','https://','#','mailto:')):
                continue
            target = target.split('#')[0]
            assert (path.parent / target).exists(), ('broken Markdown link', path, target)
            local_links += 1

    baseline_check = None
    if args.baseline:
        blob = subprocess.check_output(['git','show',args.baseline+':'+str(book)])
        old = openpyxl.load_workbook(io.BytesIO(blob), read_only=True)
        for sn in ['RELACJE','ZDARZENIA_I_FAKTY']:
            prefix = registry[sn]
            old_rows = {row[0]: tuple(row) for row in old[sn].iter_rows(values_only=True)
                        if isinstance(row[0], str) and re.fullmatch(prefix+r'\d+', row[0])}
            assert old_rows == tables[sn], ('unexpected relationship/event mutation', sn)
        old_people = {row[0] for sn in ['RDZEN_RODZINY','RODZINA_Z_RELACJI']
                      for row in old[sn].iter_rows(values_only=True)
                      if isinstance(row[0], str) and re.fullmatch(r'P\d+', row[0])}
        assert old_people == people, 'unexpected family members added'
        for row in old['ZADANIA_AGENTA'].iter_rows(values_only=True):
            if isinstance(row[0], str) and re.fullmatch(r'T\d+', row[0]) and row[0] not in ['T01','T02','T08','T28']:
                assert tuple(row) == tables['ZADANIA_AGENTA'][row[0]], ('out-of-scope task changed', row[0])
        old_archive = subprocess.check_output(['git','show',args.baseline+':'+str(archive)])
        assert hashlib.sha256(old_archive).digest() == hashlib.sha256(archive.read_bytes()).digest()
        baseline_check = {'commit': args.baseline, 'all_relationships_and_events_unchanged': True,
                          'family_ids_unchanged': True, 'other_tasks_unchanged': True,
                          'original_zip_unchanged': True}
    report = {
        'validated_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'result': 'PASS', 'workbook_sha256': hashlib.sha256(book.read_bytes()).hexdigest(),
        'sheets': len(w.sheetnames), 'counts': counts,
        'open_hypotheses': len(unresolved), 'resolved_hypotheses': len(resolved),
        'source_reference_occurrences_checked': source_references,
        'manifest_files_verified': manifest_counts, 'new_jpeg_verified': len(images),
        'original_zip_entries_crc_ok': zip_entries, 'local_markdown_links_checked': local_links,
        'draft_crc_and_identifying_data_ok': True, 'baseline_check': baseline_check,
        'evidence_limits': {'H001_parent_names_resolved_by_S086': True,
                            'H017_additional_parent_identifiers_unresolved': True,
                            'S086_original_image_local': False,
                            'new_search_rows_are_index_not_images': 280,
                            'outreach_applications_and_payments': 0},
    }
    if args.output:
        Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
