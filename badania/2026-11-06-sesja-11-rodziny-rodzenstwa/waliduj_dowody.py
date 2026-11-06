from pathlib import Path
import subprocess,io,openpyxl,json,hashlib,re,datetime
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
baseline='890fb62'
old=openpyxl.load_workbook(io.BytesIO(subprocess.check_output(['git','show',baseline+':Marysia_KOMPLET_BAZA_2026-11-05.xlsx'],cwd=ROOT)),read_only=True,data_only=True)
w=openpyxl.load_workbook(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx',read_only=True,data_only=True)
assert w.sheetnames==old.sheetnames and len(w.sheetnames)==23
def rows(book,sn,prefix):return {r[0]:r for r in book[sn].values if isinstance(r[0],str) and re.fullmatch(prefix+r'\d+',r[0])}
allowed={('RDZEN_RODZINY','P03'),('RDZEN_RODZINY','P05'),('KANDYDACI_I_HOMONIMY','C05'),('ZRODLA_I_SKANY','S006'),('ZRODLA_I_SKANY','S072')}
changed=[]
for sn,prefix in [('RDZEN_RODZINY','P'),('RODZINA_Z_RELACJI','P'),('RELACJE','R'),('KANDYDACI_I_HOMONIMY','C'),('ZDARZENIA_I_FAKTY','E'),('ZRODLA_I_SKANY','S'),('DZIENNIK_KWEREND','L'),('KOREKTY_I_SPRZECZNOSCI','Q'),('RELACJE_ZRODLOWE','REL-'),('HIPOTEZY_OTWARTE','H'),('HIPOTEZY_ROZSTRZYGNIETE','H')]:
 a=rows(old,sn,prefix);b=rows(w,sn,prefix)
 assert a.keys()<=b.keys(),sn
 for key,v in a.items():
  if b[key]!=v:
   assert (sn,key) in allowed,(sn,key)
   changed.append([sn,key])
assert set(rows(w,'RDZEN_RODZINY','P'))-set(rows(old,'RDZEN_RODZINY','P'))=={'P28','P29','P30'}
assert set(rows(w,'RODZINA_Z_RELACJI','P'))-set(rows(old,'RODZINA_Z_RELACJI','P'))=={'P31','P32'}
assert set(rows(w,'RELACJE','R'))-set(rows(old,'RELACJE','R'))=={f'R{x:03}' for x in range(36,42)}
assert set(rows(w,'ZRODLA_I_SKANY','S'))-set(rows(old,'ZRODLA_I_SKANY','S'))=={f'S{x:03}' for x in range(149,161)}
assert set(rows(w,'ZDARZENIA_I_FAKTY','E'))-set(rows(old,'ZDARZENIA_I_FAKTY','E'))=={f'E{x:03}' for x in range(60,65)}
rel=rows(w,'RELACJE','R');pids=set(rows(w,'RDZEN_RODZINY','P'))|set(rows(w,'RODZINA_Z_RELACJI','P'))
for r in rel.values():assert r[1] in pids and r[2] in pids,r
assert rel['R036'][1:3]==('P05','P28') and rel['R037'][1:3]==('P30','P28')
assert rel['R039'][1:3]==('P28','P29') and rel['R039'][4]=='22.11.1932'
assert rel['R041'][1:3]==('P31','P32')
assert not any(r[1]=='P12' and r[2] in ['P31','P32'] for r in rel.values())
events=rows(w,'ZDARZENIA_I_FAKTY','E')
assert [events[e][1] for e in ['E060','E061','E062','E063','E064']]==['26.01.1904','22.11.1932','27.02.1979','19.11.1901','08.03.1905']
assert 'adnotacj' in str(events['E062']).lower()
assert {'H017','H019','H028','H030'}<=rows(w,'HIPOTEZY_OTWARTE','H').keys()
assert 'H029' in rows(w,'HIPOTEZY_ROZSTRZYGNIETE','H')
manifest=json.loads((HERE/'manifest_zrodel_sesji.json').read_text())
for m in manifest:
 p=ROOT/m['path'];b=p.read_bytes();assert len(b)==m['size'] and hashlib.sha256(b).hexdigest()==m['sha256'],m['path']
for path in subprocess.check_output(['git','ls-tree','-r','--name-only',baseline],cwd=ROOT,text=True).splitlines():
 if path.lower().endswith('.zip'):assert hashlib.sha256((ROOT/path).read_bytes()).digest()==hashlib.sha256(subprocess.check_output(['git','show',baseline+':'+path],cwd=ROOT)).digest(),path
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),baseline=baseline,sheets=23,new_people=['P28','P29','P30','P31','P32'],new_sources=12,new_document_and_family_relations=6,new_events=5,changed_prior_records=changed,prior_relationships_and_maternal_data_preserved=True,H017_H019_H028_H030_open=True,Roman_not_assigned_as_Czesias_husband_or_sons_father=True,source_hashes_checked=len(manifest),original_zips_unchanged=True)
(HERE/'WALIDACJA_DOWODOW.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
