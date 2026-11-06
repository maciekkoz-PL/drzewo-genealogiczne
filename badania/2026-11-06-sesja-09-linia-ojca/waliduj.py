"""Kontrola etapu09 względem przyjętego stanu019919f. Tylko odczyt."""
from pathlib import Path
import datetime,hashlib,io,json,re,subprocess,zipfile
import openpyxl
from PIL import Image

stage=Path(__file__).parent
baseline='019919f96c2f1fd9d82c28ceb2f27ac2dadc2b01'
book=Path('Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
old=openpyxl.load_workbook(io.BytesIO(subprocess.check_output(['git','show',baseline+':'+str(book)])),read_only=True)
new=openpyxl.load_workbook(book,read_only=True)
parallel='0dd9b99'
remote=openpyxl.load_workbook(io.BytesIO(subprocess.check_output(['git','show',parallel+':'+str(book)])),read_only=True)
assert new.sheetnames[:21]==old.sheetnames and new.sheetnames==remote.sheetnames and len(new.sheetnames)==23
counts={};changes=[]
for sn in new.sheetnames:
    rows=list(new[sn].values);prior=list((old if sn in old.sheetnames else remote)[sn].values)
    for i,row in enumerate(prior):
        for j,v in enumerate(row):
            actual=rows[i][j]
            if v==actual:continue
            allowed=(sn in ['ZRODLA_I_SKANY','KANDYDACI_I_HOMONIMY'] and i==1 and j==0) or (sn=='HIPOTEZY_OTWARTE' and row[0]=='H018' and j in [2,3]) or (sn=='ZRODLA_I_SKANY' and row[0]=='S067' and j in [2,10]) or (sn=='ZRODLA_I_SKANY' and row[0]=='S138' and j==6)
            assert allowed,(sn,i+1,j+1,v,actual)
            changes.append([sn,i+1,j+1])
    keys=[r[0] for r in rows if isinstance(r[0],str) and re.fullmatch(r'(?:S|C|R|E|L|F|Q|T|H|P)\d+',r[0])]
    assert len(set(keys))==len(keys),(sn,'duplicateID')
    counts[sn]=len(keys)
sources={r[0] for r in new['ZRODLA_I_SKANY'].values if isinstance(r[0],str) and re.fullmatch(r'S\d+',r[0])}
for sn in new.sheetnames:
    for row in new[sn].values:
        for v in row:
            if isinstance(v,str):
                for sid in re.findall(r'\bS\d{3}\b',v):assert sid in sources,(sn,sid)
for sn,col in [('ZRODLA_I_SKANY',9),('PLIKI_DOWODOWE',1)]:
    for r in new[sn].values:
        if len(r)>col and isinstance(r[col],str) and r[col].startswith('badania/'):assert Path(r[col]).exists(),r
open_h={r[0] for r in new['HIPOTEZY_OTWARTE'].values}
assert 'H017' in open_h and 'H018' in open_h
for p in Path('badania').glob('*/manifest_zrodel_sesji.json'):
    for r in json.loads(p.read_text()):
        b=Path(r['path']).read_bytes();assert len(b)==r['size'] and hashlib.sha256(b).hexdigest()==r['sha256'],r['path']
images=list((stage/'zrodla').rglob('*.jpg'))
for p in images:
    with Image.open(p) as im:assert im.format=='JPEG';im.verify()
with zipfile.ZipFile('Marysia_PAKIET_ZRODEL_2026-11-05.zip') as z:assert z.testzip() is None
for filename in ['Marysia_PAKIET_ZRODEL_2026-11-05.zip','Marysia_LINIA_MATKI_repo_ready_2026-11-06.zip','witryna/public/index.html']:
    ref=parallel if filename.startswith('witryna/') else baseline
    assert hashlib.sha256(subprocess.check_output(['git','show',ref+':'+filename])).hexdigest()==hashlib.sha256(Path(filename).read_bytes()).hexdigest(),filename
links=0
for p in [Path('README.md'),Path('Marysia_INSTRUKCJA_DLA_AGENTA.md'),Path('ZBADANE_ZRODLA.md')]+list(stage.glob('*.md')):
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        if target.startswith(('https://','http://','#','mailto:')):continue
        assert (p.parent/target.split('#')[0]).exists(),(str(p),target)
        links+=1
report={'result':'PASS','validated_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'baseline':baseline,'parallel_audit_and_publication':parallel,'sheets':len(new.sheetnames),'counts':counts,'existing_cells_changed':changes,'family_relationships_events_and_maternal_updates_unchanged':True,'public_html_unchanged_since_parallel_publication':True,'original_zips_unchanged':True,'jpeg_checked':len(images),'local_links_checked':links,'H017_H018_open':True,'workbook_sha256':hashlib.sha256(book.read_bytes()).hexdigest()}
(stage/'WALIDACJA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
