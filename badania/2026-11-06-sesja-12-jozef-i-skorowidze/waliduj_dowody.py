from pathlib import Path
import io,subprocess,openpyxl,json,hashlib,re,datetime,csv
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];baseline='7322882'
old=openpyxl.load_workbook(io.BytesIO(subprocess.check_output(['git','show',baseline+':Marysia_KOMPLET_BAZA_2026-11-05.xlsx'],cwd=ROOT)),read_only=True,data_only=True)
w=openpyxl.load_workbook(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx',read_only=True,data_only=True)
assert w.sheetnames==old.sheetnames and len(w.sheetnames)==23
def rows(b,s,p):return {r[0]:r for r in b[s].values if isinstance(r[0],str) and re.fullmatch(p+r'\d+',r[0])}
allowed={('RDZEN_RODZINY','P29'),('ZRODLA_I_SKANY','S153')}
changed=[]
for sn,prefix in [('RDZEN_RODZINY','P'),('RODZINA_Z_RELACJI','P'),('RELACJE','R'),('KANDYDACI_I_HOMONIMY','C'),('ZDARZENIA_I_FAKTY','E'),('ZRODLA_I_SKANY','S'),('DZIENNIK_KWEREND','L'),('KOREKTY_I_SPRZECZNOSCI','Q'),('RELACJE_ZRODLOWE','REL-'),('HIPOTEZY_OTWARTE','H'),('HIPOTEZY_ROZSTRZYGNIETE','H')]:
 a=rows(old,sn,prefix);b=rows(w,sn,prefix);assert a.keys()<=b.keys()
 for k,v in a.items():
  if b[k]!=v:assert (sn,k) in allowed,(sn,k);changed.append([sn,k])
assert set(rows(w,'ZRODLA_I_SKANY','S'))-set(rows(old,'ZRODLA_I_SKANY','S'))=={f'S{x}' for x in range(161,167)}
assert rows(w,'RELACJE','R')==rows(old,'RELACJE','R')
assert '22.07.1897' in rows(w,'RDZEN_RODZINY','P')['P29'][3]
assert '35 lat' in rows(w,'RDZEN_RODZINY','P')['P29'][3]
assert {'H017','H019','H028','H030','H032'}<=rows(w,'HIPOTEZY_OTWARTE','H').keys()
assert 'H031' in rows(w,'HIPOTEZY_ROZSTRZYGNIETE','H')
assert rows(w,'ZDARZENIA_I_FAKTY','E')['E065'][1]=='22.07.1897'
manifest=json.loads((HERE/'manifest_zrodel_sesji.json').read_text())
for m in manifest:
 b=(ROOT/m['path']).read_bytes();assert len(b)==m['size'] and hashlib.sha256(b).hexdigest()==m['sha256']
for m in json.loads((HERE/'ODCZYTANE_SKOROWIDZE.json').read_text()):assert hashlib.sha256((ROOT/m['local']).read_bytes()).hexdigest()==m['sha256']
for path in subprocess.check_output(['git','ls-tree','-r','--name-only',baseline],cwd=ROOT,text=True).splitlines():
 if path.endswith('.zip'):assert (ROOT/path).read_bytes()==subprocess.check_output(['git','show',baseline+':'+path],cwd=ROOT)
for sn,file in [('WIARYGODNOSC_OSOB','AUDYT_OSOB.csv'),('WIARYGODNOSC_RELACJI','AUDYT_RELACJI.csv')]:
 with (ROOT/'badania/2026-11-06-trzy-poziomy'/file).open() as f: actual=list(csv.reader(f))
 assert actual==[['' if v is None else str(v) for v in row] for row in w[sn].values]
d=json.loads((ROOT/'witryna/wiarygodnosc.json').read_text());j=next(x for x in d['people'] if x['id']=='P29')
assert '22.07.1897' in j['dates'] and 'S166' in j['source'] and '35 lat' in j['note']
old_d=json.loads(subprocess.check_output(['git','show',baseline+':witryna/wiarygodnosc.json'],cwd=ROOT))
for person in old_d['people']:
 if person['id']!='P29':assert next(x for x in d['people'] if x['id']==person['id'])==person
assert d['relations']==old_d['relations'] and d['edges']==old_d['edges']
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),baseline=baseline,sheets=23,source_hashes_checked=len(manifest),reused_index_images=12,new_sources=6,new_events=1,changed_prior_records=changed,all_prior_relationships_and_maternal_data_preserved=True,H017_H019_H028_H030_open=True,original_zips_unchanged=True)
(HERE/'WALIDACJA_DOWODOW.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
