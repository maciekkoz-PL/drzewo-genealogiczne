"""Kontrola dowodów, zakresów i ochrony danych rodziny; bez sieci."""
from pathlib import Path
import collections, datetime, hashlib, json, re, zipfile
import openpyxl
from PIL import Image

D=Path(__file__).resolve().parent;R=D.parents[1];Z=D/'zrodla'
old=openpyxl.load_workbook(D/'baza_przed_etapem33.xlsx');new=openpyxl.load_workbook(R/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
assert old.sheetnames==new.sheetnames and len(new.sheetnames)==25
changes=json.loads((D/'ZMIANY_KOMOREK.json').read_text());allowed={(x['sheet'],x['cell'])for x in changes};actual=[]
for sn in old.sheetnames:
    for row in old[sn].iter_rows():
        for c in row:
            if c.value!=new[sn][c.coordinate].value:
                assert(sn,c.coordinate)in allowed,(sn,c.coordinate,'unlogged change');actual.append((sn,c.coordinate))
assert len(actual)==37 and len(allowed)==37
for x in changes:
    assert old[x['sheet']][x['cell']].value==x['before'],x
    assert new[x['sheet']][x['cell']].value==x['after'],x
protected=['RDZEN_RODZINY','RODZINA_Z_RELACJI','RELACJE','RELACJE_ZRODLOWE','POTWIERDZONE_AKTEM_1936']
for sn in protected:assert list(old[sn].values)==list(new[sn].values),sn
spec={'ZRODLA_I_SKANY':(r'S\d+',325),'DZIENNIK_KWEREND':(r'L\d+',336),'KANDYDACI_I_HOMONIMY':(r'C\d+',109),'PLIKI_DOWODOWE':(r'F\d+',595),'INDEKS_MELDUNKOW':(r'IM\d+',115)}
counts={}
for sn,(pattern,count)in spec.items():
    ids=[r[0]for r in new[sn].values if isinstance(r[0],str)and re.fullmatch(pattern,r[0])]
    assert len(ids)==count and len(set(ids))==count,(sn,len(ids));counts[sn]=count
src={r[0]for r in new['ZRODLA_I_SKANY'].values if isinstance(r[0],str)and re.fullmatch(r'S\d+',r[0])}
for sn in new.sheetnames:
    for row in new[sn].values:
        if not row[0]or not isinstance(row[0],str):continue
        # Every appended row, plus every changed existing cell, must use real S-IDs.
        for v in row:
            if isinstance(v,str):
                for s in re.findall(r'(?<![A-Za-z])S\d{3}(?!\d)',v):
                    if row[0]in {x['id']for x in changes if x['sheet']==sn}or row[0]in[f'S{i}'for i in range(318,326)]or row[0]in[f'L{i}'for i in range(322,337)]:assert s in src,(sn,row[0],s)
for row in new['PLIKI_DOWODOWE'].values:
    if isinstance(row[0],str)and re.fullmatch(r'F\d+',row[0])and int(row[0][1:])>=472:
        p=R/row[1];assert p.is_file(),row[1];assert hashlib.sha256(p.read_bytes()).hexdigest()==row[5].split(' ',1)[1],row[0]
for book,total,names,sheets,originals in [('25507',149,142,18,30),('25509',187,181,23,26)]:
    scope=json.loads((Z/f'{book}_zakres.json').read_text());manifest=json.loads((Z/f'{book}_manifest.json').read_text())['elementy'];checks=json.loads((Z/f'{book}_pobrane_sha256.json').read_text())
    assert len(manifest)==len(checks)==total
    assert sum(b-a+1 for a,b in scope['name_columns_read'])==names
    assert len(list(Z.glob(f'{book}_???.jpg')))==originals
    uu={x['pozycja']:x['src']for x in manifest};hh={x['image']:x for x in checks}
    for n in uu:assert uu[n]==hh[n]['url']
    for p in Z.glob(f'{book}_???.jpg'):assert hashlib.sha256(p.read_bytes()).hexdigest()==hh[int(p.stem[-3:])]['sha256']
    with zipfile.ZipFile(Z/f'{book}_kolumny_nazwisk.zip')as z:assert z.testzip()is None and len(z.namelist())==sheets
rows1939=json.loads((Z/'25509_wybrane_odczyty.json').read_text());hit=[x for x in rows1939 if x['entry']=='3693'];assert len(hit)==1 and hit[0]['given_name']=='Stanisława i Zygm.'
assert hit[0]['current_address']=='Grabowa4'and hit[0]['image']==165
p272=json.loads((Z/'S272_zakres_nowego_kryterium.json').read_text());assert p272['name_columns_reread']==[[136,247]]and p272['record_images']==112
assert len(json.loads((Z/'S272_wybrane_odczyty.json').read_text()))==10
ar=json.loads((Z/'arolsen_zygmunt_odczyty.json').read_text());assert len(ar)==6 and sum(x['images']for x in ar)==10
assert len(list((Z/'arolsen_zygmunt').glob('*.jpg')))==10
for p in Z.rglob('*.jpg'):
    with Image.open(p)as im:im.verify()
mail=json.loads((Z/'odpowiedzi_instytucji_wypisy.json').read_text());assert {x['source']for x in mail}=={'S322','S323','S324','S325'}
for m in mail:
    assert '@'not in m['verbatim_reply']and re.fullmatch('[a-f0-9]{64}',m['sha256_original_body'])
    assert m['gmail_message_id']in m['url']and m['received_original']
sent=json.loads((Z/'potwierdzone_wysylki_historyczne_metadane.json').read_text());assert len(sent)==4
assert all(x['labels']==['SENT']and x['sent_utc']<'2026-11-09'for x in sent)
rows={r[0]:r for r in new['KANDYDACI_I_HOMONIMY'].values if isinstance(r[0],str)}
assert '1982'not in rows['C10'][2]and '1922'in rows['C62'][2]
assert 'NIEZGODNA'in rows['C17'][5]and 'Zygm.'in rows['C109'][1]
for p in D.rglob('*.json'):json.loads(p.read_text())
out=dict(passed=True,at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),sheets_retained=25,protected_family_sheets_identical=protected,existing_changes_logged=len(actual),counts=counts,new_proven_relationships=0,downloaded_ledger_images=336,new_ledger_name_images=323,new_criterion_identity_images=112,arolsen_new_docids=6,arolsen_new_images=10,mail_replies=4,new_emails_sent=0,source_hashes_and_paths_valid=True,contact_archives_valid=True)
(D/'WALIDACJA.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
manifest=[]
for p in sorted(D.rglob('*')):
    if p.is_file()and p.name!='manifest_plikow.json'and'__pycache__'not in p.parts:manifest.append(dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(D/'manifest_plikow.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False));print('manifest_files',len(manifest),'bytes',sum(x['bytes']for x in manifest))
