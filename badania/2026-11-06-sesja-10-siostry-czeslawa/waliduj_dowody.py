"""Kontrola zmian genealogicznych względem6371264; bez pobierania i mutacji bazy."""
from pathlib import Path
import datetime,hashlib,io,json,re,subprocess,zipfile
import openpyxl
from PIL import Image
stage=Path(__file__).parent;book=Path('Marysia_KOMPLET_BAZA_2026-11-05.xlsx');baseline='6371264'
old=openpyxl.load_workbook(io.BytesIO(subprocess.check_output(['git','show',baseline+':'+str(book)])),read_only=True)
new=openpyxl.load_workbook(book,read_only=True);assert old.sheetnames==new.sheetnames and len(new.sheetnames)==23
changes=[]
for sn in old.sheetnames:
    if sn.startswith('WIARYGODNOSC_'):continue # odrębna kontrola publikacji/audytu
    a=list(old[sn].values);b=list(new[sn].values)
    for i,row in enumerate(a):
        for j,v in enumerate(row):
            if v==b[i][j]:continue
            allowed=(i==1 and j==0 and sn in ['START','RDZEN_RODZINY','ZRODLA_I_SKANY','KANDYDACI_I_HOMONIMY']) or (sn=='RDZEN_RODZINY' and row[0] in ['P03','P05','P06'] and j in [6,8]) or (sn=='ZRODLA_I_SKANY' and row[0] in ['S007','S009','S015'] and j==10) or (sn=='KANDYDACI_I_HOMONIMY' and row[0] in ['C02','C04'] and j in [2,3,5,6,7,8,9]) or (sn=='HIPOTEZY_OTWARTE' and row[0]=='H019' and j==2)
            assert allowed,(sn,i+1,j+1,v,b[i][j]);changes.append([sn,i+1,j+1])
ids={}
for sn in new.sheetnames:
    rows=[r for r in new[sn].values if isinstance(r[0],str) and re.fullmatch(r'(?:P|R|E|S|C|L|F|Q|H|UT)\d+',r[0])]
    assert len(rows)==len({r[0] for r in rows}),sn;ids[sn]={r[0]:r for r in rows}
for sn,expected in [('RDZEN_RODZINY',{'P26','P27'}),('RELACJE',{f'R{i:03}' for i in range(30,36)}),('ZDARZENIA_I_FAKTY',{'E058','E059'}),('ZRODLA_I_SKANY',{'S147','S148'})]:
    prev={r[0] for r in old[sn].values};assert set(ids[sn])-prev==expected,(sn,set(ids[sn])-prev)
for rid,parent,child,sid in [('R030','P05','P26','S147'),('R031','P06','P26','S147'),('R033','P05','P27','S148'),('R034','P06','P27','S148')]:
    r=ids['RELACJE'][rid];assert r[1:3]==(parent,child) and sid in r[6]
for cid,pid in [('C04','P26'),('C02','P27')]:assert pid in ids['KANDYDACI_I_HOMONIMY'][cid][5]
assert 'H017' in ids['HIPOTEZY_OTWARTE'] and 'H019' in ids['HIPOTEZY_OTWARTE']
assert all(h in ids['HIPOTEZY_ROZSTRZYGNIETE'] for h in ['H026','H027'])
for sn in new.sheetnames:
    for row in new[sn].values:
        for v in row:
            if isinstance(v,str):
                for sid in re.findall(r'\bS\d{3}\b',v):assert sid in ids['ZRODLA_I_SKANY'],(sn,sid)
for r in ids['ZRODLA_I_SKANY'].values():
    if isinstance(r[9],str) and r[9].startswith('badania/'):assert Path(r[9]).exists(),r[0]
for p in Path('badania').glob('*/manifest_zrodel_sesji.json'):
    for r in json.loads(p.read_text()):
        b=Path(r['path']).read_bytes();assert len(b)==r['size'] and hashlib.sha256(b).hexdigest()==r['sha256'],r['path']
images=list((stage/'zrodla').rglob('*.jpg'))
for p in images:
    with Image.open(p) as im:assert im.format=='JPEG';im.verify()
for p in ['Marysia_PAKIET_ZRODEL_2026-11-05.zip','Marysia_LINIA_MATKI_repo_ready_2026-11-06.zip']:
    assert hashlib.sha256(subprocess.check_output(['git','show',baseline+':'+p])).hexdigest()==hashlib.sha256(Path(p).read_bytes()).hexdigest()
    with zipfile.ZipFile(p) as z:assert z.testzip() is None
links=0
for p in [Path('README.md'),Path('Marysia_INSTRUKCJA_DLA_AGENTA.md'),Path('ZBADANE_ZRODLA.md')]+list(stage.glob('*.md')):
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        if target.startswith(('http://','https://','#','mailto:')):continue
        assert (p.parent/target.split('#')[0]).exists(),(str(p),target);links+=1
report={'result':'PASS','at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'baseline':baseline,'sheets':23,'new_people':['P26','P27'],'new_relations':['R030','R031','R032','R033','R034','R035'],'prior_relationships_and_events_unchanged':True,'H017_H019_open':True,'aliases_preserved':True,'age_conflict_Q74_preserved':True,'existing_cells_changed':changes,'jpeg_checked':len(images),'markdown_links_checked':links,'zips_unchanged':True,'workbook_sha256':hashlib.sha256(book.read_bytes()).hexdigest()}
(stage/'WALIDACJA_DOWODOW.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2))
