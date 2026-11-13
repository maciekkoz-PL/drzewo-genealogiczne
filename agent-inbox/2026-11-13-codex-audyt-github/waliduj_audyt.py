"""Sprawdzenie liczbowych wniosków audytu, bez sieci i bez zmiany danych rodzinnych."""
from pathlib import Path
import collections, datetime, hashlib, json, subprocess

D = Path(__file__).resolve().parent
Z = D / 'zrodla'
load = lambda name: json.loads((Z / name).read_text())
branches = load('inventory_all_branches.json')
assert len(branches) == 5
by = {x['ref'].split('origin/',1)[1]: x for x in branches}
main = by['main']
for name in ['copilot/help-with-project', 'proposal/agent-handoff-2026-11-13']:
    assert by[name]['sha'] == main['sha'] and by[name]['files'] == main['files']
docs = by['docs/agent-handoff-2026-11-13']
old = {f['path']:f['sha'] for f in main['files']}
new = {f['path']:f['sha'] for f in docs['files']}
changed = sorted(p for p in set(old)|set(new) if old.get(p)!=new.get(p))
assert changed == ['README.md', 'agent-inbox/README.md']
assert sorted(p for p in new if p.startswith('agent-inbox/')) == ['agent-inbox/README.md']
assert len(set(f['path'] for b in branches for f in b['files'])) == 3627
assert len((Z/'all_commits.tsv').read_text().splitlines()) == 120
assert load('github_branches_end.json')['branches'] == []
assert len(load('github_prs.json')['issues']) == 1
assert load('github_issues.json')['issues'] == []
assert load('github_pr1_comments.json')['comments'] == []
assert load('github_pr1_timeline.json')['comments'] == []
assert sorted(load('github_pr1_files.json')['filenames']) == changed
assert load('releases.json') == [[]]
assert load('commit_comments.json') == [[]]
assert sum(len(p['artifacts']) for p in load('artifacts.json')) == 0
assert sum(len(p) for p in load('events.json')) == 87
ev = load('event_commit_refs.json')
assert len(ev['all']) == 86 and not ev['not_local']
meta = load('repository_metadata.json')
assert meta['has_wiki'] is False and meta['has_discussions'] is False and meta['forks_count'] == 0
counts = collections.Counter(k for p in load('work_tree_semantic_diff.json') for k in p['fields'])
assert set(counts) == {'addresses', 'locations', 'place'}
out = dict(passed=True, checked_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    branches=5, commits=120, paths=3627, pr1_changed_files=changed,
    discovery_reports_in_existing_inbox=0, family_changes_from_audit=0,
    releases=0, artifacts=0, commit_comments=0, events=87,
    event_commit_refs_all_available=86)
(D/'WALIDACJA.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
manifest=[]
for p in sorted(D.rglob('*')):
    if p.is_file() and p.name!='manifest_plikow.json' and '__pycache__' not in p.parts:
        manifest.append(dict(path=str(p.relative_to(D)),bytes=p.stat().st_size,
            sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(D/'manifest_plikow.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False))
