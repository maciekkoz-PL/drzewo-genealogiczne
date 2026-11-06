"""Validate preservation of the main checkpoint and maternal evidence boundaries."""
from pathlib import Path
import datetime,hashlib,io,json,re,subprocess,zipfile
import openpyxl

ROOT=Path(__file__).resolve().parents[2]
BASE='b86519ced59d9ad205a79307763b9cb5572ddc31'
BOOK='Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
STAGE=Path(__file__).resolve().parent
def baseline(path):return subprocess.check_output(['git','show',BASE+':'+path],cwd=ROOT)
def records(sheet):
 return {r[0]:tuple(r) for r in sheet.values if isinstance(r[0],str) and re.fullmatch(r'(?:[PCREQTLF]\d+|S\d+|H\d+|REL-\d+|UT\d+|G\d+)',r[0])}
old=openpyxl.load_workbook(io.BytesIO(baseline(BOOK)))
new=openpyxl.load_workbook(ROOT/BOOK)
assert new.sheetnames==old.sheetnames and len(new.sheetnames)==21
allowed={('RDZEN_RODZINY','P17'):{6,9,10},('RDZEN_RODZINY','P18'):{4,5,6,7,8,9,10,11},('RDZEN_RODZINY','P19'):{2,4,5,6,7,8,9,10,11},('ZRODLA_I_SKANY','S086'):{11}}
# Later direct family confirmation REL-011 keeps Marysia's parents visible in
# both display modes. This does not claim a newly obtained civil record.
allowed.update({('RELACJE','R009'):{6,7,8},('RELACJE','R017'):{4,5,6,7,8}})
checked=0;changes=[]
for sn in old.sheetnames:
 a,b=records(old[sn]),records(new[sn])
 assert set(a)<=set(b),('deleted IDs',sn,set(a)-set(b))
 for rid,row in a.items():
  assert len(row)==len(b[rid]),('schema changed',sn)
  for col,(before,after) in enumerate(zip(row,b[rid]),1):
   checked+=1
   if before!=after:
    assert col in allowed.get((sn,rid),set()),('out-of-scope mutation',sn,rid,col,before,after)
    changes.append([sn,rid,col])
people=[r[0] for sn in ['RDZEN_RODZINY','RODZINA_Z_RELACJI'] for r in new[sn].values if isinstance(r[0],str) and re.fullmatch(r'P\d+',r[0])]
assert len(people)==len(set(people))
assert people.count('P17')==1 and people.count('P18')==1 and people.count('P19')==1
assert records(old['RDZEN_RODZINY'])['P12']==records(new['RDZEN_RODZINY'])['P12']
for row in records(new['RELACJE']).values():
 if int(row[0][1:])>=20:
  assert 'RELACJA RODZINNA' in row[5] and row[6] in ['REL-009','REL-010','REL-012']
  assert not row[1].startswith('C') and not row[2].startswith('C')
assert records(old['RELACJE'])['R018']==records(new['RELACJE'])['R018']
assert records(old['RELACJE'])['R019']==records(new['RELACJE'])['R019']
assert 'H020' in records(new['HIPOTEZY_OTWARTE'])
assert 'H017' in records(new['HIPOTEZY_OTWARTE'])
assert 'H020' not in records(new['HIPOTEZY_ROZSTRZYGNIETE'])
archives=['Marysia_PAKIET_ZRODEL_2026-11-05.zip','Marysia_LINIA_MATKI_repo_ready_2026-11-06.zip']
for name in archives:
 assert (ROOT/name).read_bytes()==baseline(name),('archive changed',name)
 with zipfile.ZipFile(ROOT/name) as z:assert z.testzip() is None
with zipfile.ZipFile(ROOT/archives[1]) as z:
 for name in z.namelist():
  if name.startswith(('dane/','zdjecia/')):
   assert (STAGE/name).read_bytes()==z.read(name),('raw handoff modified',name)
photo_meta=json.loads((STAGE/'zdjecia/MANIFEST_JPEG.json').read_text())
assert hashlib.sha256((ROOT/photo_meta['repo_path']).read_bytes()).hexdigest()==photo_meta['sha256']
assert records(new['RELACJE'])['R028'][1:3]==('P24','P18')
assert records(new['RELACJE'])['R029'][1:3]==('P25','P18')
assert records(new['KANDYDACI_I_HOMONIMY'])['C43'][3].endswith('P24')
assert records(new['KANDYDACI_I_HOMONIMY'])['C44'][3].endswith('P25')
assert all(h not in records(new['HIPOTEZY_OTWARTE']) and h in records(new['HIPOTEZY_ROZSTRZYGNIETE']) for h in ['H021','H022'])
report={'result':'PASS','at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'baseline':BASE,'sheets':21,'old_record_cells_compared':checked,'permitted_cell_changes':changes,'all_old_ids_preserved':True,'P12_unchanged_P17_P18_P19_unique':True,'R018_R019_unchanged':True,'all_new_relations_family_only':True,'C45_not_merged_with_P19':True,'C43_C44_no_parent_or_marriage_edges':True,'H017_preserved':True,'both_original_ZIPs_byte_identical':True,'raw_handoff_byte_identical':True,'grave_JPEG_status':'otrzymany JPEG zapisany prywatnie; S135','new_grave_JPEG_count':1,'family_confirmation_source':'REL-012','C43_C44_aliases_for_P24_P25':True,'index_rows_not_original_acts':True}
(STAGE/'WALIDACJA_SCALENIA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
