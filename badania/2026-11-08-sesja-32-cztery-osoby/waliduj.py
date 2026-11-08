from pathlib import Path
import openpyxl,json,hashlib,re,collections,zipfile
R=Path(__file__).resolve().parents[2];D=R/'badania/2026-11-08-sesja-32-cztery-osoby';old=openpyxl.load_workbook(D/'baza_przed_etapem32.xlsx');new=openpyxl.load_workbook(R/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx');changes=json.loads((D/'ZMIANY_KOMOREK.json').read_text());allowed={(x['sheet'],x['cell'])for x in changes}|{('ZRODLA_I_SKANY','A2'),('KANDYDACI_I_HOMONIMY','A2'),('INDEKS_MELDUNKOW','A2')}
assert old.sheetnames==new.sheetnames and len(new.sheetnames)==25
actual=[]
for sn in old.sheetnames:
 for row in old[sn].iter_rows():
  for c in row:
   if c.value!=new[sn][c.coordinate].value:
    assert (sn,c.coordinate)in allowed,(sn,c.coordinate,c.value,new[sn][c.coordinate].value);actual.append([sn,c.coordinate])
state={}
for x in changes:
 key=(x['sheet'],x['cell']);prev=state.get(key,old[x['sheet']][x['cell']].value);assert prev==x['before'],(key,'change chain mismatch');state[key]=x['after']
for (sn,cell),v in state.items():assert new[sn][cell].value==v,(sn,cell,'final state mismatch')
for sn in ['RDZEN_RODZINY','RODZINA_Z_RELACJI','RELACJE','RELACJE_ZRODLOWE']:
 assert list(old[sn].values)==list(new[sn].values),sn
counts={}
for sn,pat in [('ZRODLA_I_SKANY',r'S\d+'),('DZIENNIK_KWEREND',r'L\d+'),('PLIKI_DOWODOWE',r'F\d+'),('KANDYDACI_I_HOMONIMY',r'C\d+'),('KOREKTY_I_SPRZECZNOSCI',r'Q\d+'),('INDEKS_MELDUNKOW',r'IM\d+')]:
 ids=[r[0]for r in new[sn].values if isinstance(r[0],str)and re.fullmatch(pat,r[0])];assert len(ids)==len(set(ids)),sn;counts[sn]=len(ids)
assert counts['ZRODLA_I_SKANY']==317 and counts['KANDYDACI_I_HOMONIMY']==108 and counts['PLIKI_DOWODOWE']==471
src={r[0]for r in new['ZRODLA_I_SKANY'].values if isinstance(r[0],str)and re.fullmatch(r'S\d+',r[0])}
for sn in ['ZRODLA_I_SKANY','DZIENNIK_KWEREND','KANDYDACI_I_HOMONIMY','KOREKTY_I_SPRZECZNOSCI','INDEKS_MELDUNKOW']:
 for row in new[sn].values:
  if not row[0] or not isinstance(row[0],str):continue
  if not (row[0]in ['C98','H049','H050','H051'] or (sn=='ZRODLA_I_SKANY'and row[0]in [f'S{x}'for x in range(309,318)]) or (sn=='DZIENNIK_KWEREND'and row[0]in [f'L{x}'for x in range(309,322)])):continue
  for v in row:
   if isinstance(v,str):
    for s in re.findall(r'\bS\d{3}\b',v):assert s in src,(sn,row[0],s)
for row in new['PLIKI_DOWODOWE'].values:
 if isinstance(row[0],str)and re.fullmatch(r'F\d+',row[0]) and int(row[0][1:])>=441:assert(R/row[1]).exists(),row[1]
for f in D.rglob('*.json'):json.loads(f.read_text())
with zipfile.ZipFile(D/'zrodla/25506_kolumny_nazwisk.zip')as z:assert z.testzip()is None and len(z.namelist())==25
man=json.load(open(D/'zrodla/referendum_1946_manifest.json'));a=man['elementy'];assert len(a)==283 and all(x['sygnatura']=='39/639/0/-/1'for x in a)
for f in D.glob('zrodla/arcinsys/*'):
 if f.name in ['chmielowski.txt','czeslaw_wild.txt','fritzlar_foreign.txt']:assert 'Ihre Einfache Suche hat keine Treffer erzielt.'in f.read_text(),f
out={'passed':True,'original_sheets_retained':25,'protected_family_sheets_identical':True,'existing_changes_only_logged':len(actual),'counts':counts,'new_source_ids_valid':True,'new_evidence_paths_exist':True,'contact_zip_valid':True,'referendum_manifest_283_only_unit_1':True}
(D/'WALIDACJA.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
manifest=[]
for f in sorted(D.rglob('*')):
 if f.is_file() and f.name!='manifest_plikow.json':manifest.append({'path':str(f.relative_to(R)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
(D/'manifest_plikow.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False));print('files',len(manifest),'bytes',sum(x['bytes']for x in manifest))
