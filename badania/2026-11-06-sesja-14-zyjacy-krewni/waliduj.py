from pathlib import Path
import csv,datetime,hashlib,io,json,subprocess,openpyxl

ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
BASE='028e3b3'
def old(path):return subprocess.check_output(['git','show',f'{BASE}:{path}'],cwd=ROOT)
book='Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
a=openpyxl.load_workbook(io.BytesIO(old(book)));b=openpyxl.load_workbook(ROOT/book)
assert a.sheetnames==b.sheetnames and len(b.sheetnames)==23
allowed={
 'ZRODLA_I_SKANY':{'180 źródeł':set()},
 'RODZINA_Z_RELACJI':{'P09':{8,9},'P10':{8,9}},
 'KANDYDACI_I_HOMONIMY':{'C19':{5,6,7,8},'C20':{7,8},'C21':{8}},
 'HIPOTEZY_OTWARTE':{'H003':{2,3,4}},
 'WIARYGODNOSC_RELACJI':{'V048':{5,6,7}},
 'WIARYGODNOSC_OSOB':{k:{6,7,8} for k in ['P09','P10','C19']}}
changes=[]
for name in a.sheetnames:
    av=list(a[name].values);bv=list(b[name].values)
    assert len(bv)>=len(av),name
    for n,r in enumerate(av):
        for col,val in enumerate(r):
            if val==bv[n][col]:continue
            assert (name=='ZRODLA_I_SKANY' and n==1 and col==0) or col in allowed.get(name,{}).get(r[0],set()),(name,n,col,val,bv[n][col])
            changes.append([name,n+1,col+1])
    first=[r[0] for r in bv if isinstance(r[0],str) and __import__('re').fullmatch(r'[A-Z]+-?\d+',r[0])]
    assert len(first)==len(set(first)),name
for sheet,expected in [('ZRODLA_I_SKANY',180),('DZIENNIK_KWEREND',152),('PLIKI_DOWODOWE',124),('RELACJE_ZRODLOWE',16)]:
    rows=[r for r in b[sheet].values if isinstance(r[0],str) and __import__('re').fullmatch(r'[A-Z]+-?\d+',r[0])]
    assert len(rows)==expected,(sheet,len(rows))
for sn,file in [('WIARYGODNOSC_OSOB','AUDYT_OSOB.csv'),('WIARYGODNOSC_RELACJI','AUDYT_RELACJI.csv')]:
    expected=[['' if v is None else str(v) for v in r] for r in b[sn].values]
    with (ROOT/'badania/2026-11-06-trzy-poziomy'/file).open(newline='') as f:actual=list(csv.reader(f))
    assert actual==expected,sn
for file in ['Marysia_PAKIET_ZRODEL_2026-11-05.zip','Marysia_LINIA_MATKI_repo_ready_2026-11-06.zip']:
    assert hashlib.sha256((ROOT/file).read_bytes()).digest()==hashlib.sha256(old(file)).digest(),file
data=json.loads((ROOT/'witryna/wiarygodnosc.json').read_text());before=json.loads(old('witryna/wiarygodnosc.json'))
assert data['edges']==before['edges']
assert len(data['relations'])==len(before['relations'])
for old_rel,new_rel in zip(before['relations'],data['relations']):
    for key in old_rel:
        if old_rel['id']=='V048' and key in ['reason','missing','sources']:continue
        assert old_rel[key]==new_rel[key],(old_rel['id'],key)
assert len(data['people'])==51 and len(data['edges'])==75
bp={p['id']:p for p in before['people']};p={p['id']:p for p in data['people']}
for ident,v in bp.items():
    if ident not in ['P09','P10','C19']:assert v==p[ident],ident
for ident in ['P09','P10','C19']:
    for field in ['level','identityLevel','connectionLevel']:assert bp[ident][field]==p[ident][field]
assert 'niepotwierdzone' in p['C19']['note'] and 'nie ma co do tego pewności' in p['P09']['note']
html=(ROOT/'witryna/public/index.html').read_text()
embedded=json.loads(html.split('<script id="family-data" type="application/json">')[1].split('</script>')[0].replace('<\\/','</'))
assert embedded['people']==data['people'] and embedded['edges']==data['edges']
assert len(embedded['news'])==7
assert not any(t in html.lower() for t in ['niewidom','blind'])
for person in data['people']:
    for src in person.get('source',[]):assert src in data['sources'],(person['id'],src)
queries=json.loads((HERE/'zrodla/web/kwerendy_i_odczyty.json').read_text())['calls']
count=sum(len(v.get('queries',[])) for v in queries.values())
count+=len(json.loads((HERE/'zrodla/web/piotr_po_ocenie_rodziny.json').read_text())['queries'])
assert count==44,count
reused=json.loads((HERE/'zrodla/ponownie_uzyte_pliki.json').read_text())
for v in reused:assert hashlib.sha256((ROOT/v['path']).read_bytes()).hexdigest()==v['sha256']
manifest=[]
for f in sorted((HERE/'zrodla').rglob('*')):
    if f.is_file():manifest.append(dict(path=str(f.relative_to(HERE)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
(HERE/'manifest_zrodel_sesji.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
report=dict(result='PASS',baseline_commit=BASE,at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),sheets=23,sources=180,new_sources=6,queries=44,firecrawl_queries=1,reviewed_index_entries=199,new_people=0,new_relationships=0,people=51,edges=75,news=7,old_rows_preserved_except_listed_cells=changes,old_zip_bytes_unchanged=True,audits_match=True,maternal_branch_unchanged=True,P10_C19_not_merged=True,source_files=len(manifest),source_bytes=sum(x['bytes'] for x in manifest))
(HERE/'WALIDACJA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='old_rows_preserved_except_listed_cells'},ensure_ascii=False))
