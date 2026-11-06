from pathlib import Path
import json,hashlib,subprocess,io,re,openpyxl,csv,zipfile,datetime
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];baseline='a8a6d12'
old=openpyxl.load_workbook(io.BytesIO(subprocess.check_output(['git','show',baseline+':Marysia_KOMPLET_BAZA_2026-11-05.xlsx'],cwd=ROOT)),read_only=True,data_only=True)
w=openpyxl.load_workbook(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx',read_only=True,data_only=True)
assert w.sheetnames==old.sheetnames and len(w.sheetnames)==23
def rows(b,s,p):return {r[0]:r for r in b[s].values if isinstance(r[0],str) and re.fullmatch(p+r'\d+',r[0])}
allowed={('RODZINA_Z_RELACJI','P31'),('RODZINA_Z_RELACJI','P32'),('KANDYDACI_I_HOMONIMY','C62'),('HIPOTEZY_OTWARTE','H028'),('HIPOTEZY_OTWARTE','H030')}
changed=[]
for s,p in [('RDZEN_RODZINY','P'),('RODZINA_Z_RELACJI','P'),('RELACJE','R'),('KANDYDACI_I_HOMONIMY','C'),('ZDARZENIA_I_FAKTY','E'),('ZRODLA_I_SKANY','S'),('DZIENNIK_KWEREND','L'),('KOREKTY_I_SPRZECZNOSCI','Q'),('RELACJE_ZRODLOWE','REL-'),('HIPOTEZY_OTWARTE','H'),('HIPOTEZY_ROZSTRZYGNIETE','H')]:
 a=rows(old,s,p);b=rows(w,s,p);assert a.keys()<=b.keys()
 for k,v in a.items():
  if b[k]!=v:assert(s,k) in allowed,(s,k);changed.append([s,k])
assert rows(old,'RELACJE','R')==rows(w,'RELACJE','R')
assert rows(old,'RDZEN_RODZINY','P')==rows(w,'RDZEN_RODZINY','P')
assert set(rows(w,'ZRODLA_I_SKANY','S'))-set(rows(old,'ZRODLA_I_SKANY','S'))=={f'S{i}' for i in range(167,175)}
assert {'H017','H019','H028','H030','H033'}<=rows(w,'HIPOTEZY_OTWARTE','H').keys()
assert 'REL-014' in rows(w,'RELACJE_ZRODLOWE','REL-')
manifest=json.loads((HERE/'manifest_zrodel_sesji.json').read_text())
for m in manifest:
 b=(ROOT/m['path']).read_bytes();assert len(b)==m['size'] and hashlib.sha256(b).hexdigest()==m['sha256'],m['path']
with zipfile.ZipFile(HERE/'zrodla/szczurek_korpus.zip') as z:
 members=json.loads(z.read('MANIFEST_CZLONKOW.json'))
 for m in members:
  b=z.read(m['path']);assert len(b)==m['size'] and hashlib.sha256(b).hexdigest()==m['sha256']
read=json.loads((HERE/'zrodla/szczurek_odczyty.json').read_text())
assert len(read)==559 and sum(r.get('status')==200 for r in read)==558 and sum('error'in r for r in read)==1
queries=json.loads((HERE/'zrodla/geneteka/queries.json').read_text())
assert len(queries)==21 and all(r['total']==r['rows'] for r in queries) and sum(r['rows'] for r in queries)==27
d=json.loads((ROOT/'witryna/wiarygodnosc.json').read_text());old_d=json.loads(subprocess.check_output(['git','show',baseline+':witryna/wiarygodnosc.json'],cwd=ROOT));html=(ROOT/'witryna/public/index.html').read_text()
rendered=json.loads(re.search(r'<script id="family-data" type="application/json">(.*?)</script>',html,re.S).group(1))
for k in ['people','edges','relations','sources']:assert rendered[k]==d[k]
for p in old_d['people']:
 if p['id'] not in ['P31','P32']:assert next(x for x in d['people'] if x['id']==p['id'])==p
assert d['relations']==old_d['relations'] and d['edges']==old_d['edges']
assert len(d['people'])==51 and len(d['relations'])==75 and len(rendered['news'])==7
assert not re.search(r'niewid|blind|PZN',html,re.I)
assert 'REL-014' in d['sources'] and all('REL-014' in next(x['source'] for x in d['people'] if x['id']==id) for id in ['P31','P32'])
for sn,file in [('WIARYGODNOSC_OSOB','AUDYT_OSOB.csv'),('WIARYGODNOSC_RELACJI','AUDYT_RELACJI.csv')]:
 with(ROOT/'badania/2026-11-06-trzy-poziomy'/file).open() as f:actual=list(csv.reader(f))
 assert actual==[['' if v is None else str(v) for v in r] for r in w[sn].values]
assert w['WIARYGODNOSC_OSOB'].max_row==97
for path in subprocess.check_output(['git','ls-tree','-r','--name-only',baseline],cwd=ROOT,text=True).splitlines():
 if path.endswith('.zip'):assert (ROOT/path).read_bytes()==subprocess.check_output(['git','show',baseline+':'+path],cwd=ROOT)
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),baseline=baseline,sheets=23,source_files=len(manifest),corpus_members=len(members),articles_read=558,unavailable_article=1,geneteka_regions=21,returned_rows=27,changed_prior_records=changed,prior_relations_and_core_and_maternal_data_preserved=True,no_unproved_marriage_or_father_added=True,no_health_clue_in_public_html=True,public_people=51,public_relations=75,news=7,audit_people=96,original_zips_preserved=True)
(HERE/'WALIDACJA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
