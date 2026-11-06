from pathlib import Path
from copy import copy
import json,hashlib,shutil,re
import openpyxl

stage=Path('badania/2026-11-06-sesja-10-siostry-czeslawa');src=stage/'zrodla';src.mkdir(parents=True,exist_ok=True)
for p in Path('work/s09/sisters').rglob('*'):
    if p.is_file() and '_preview' not in p.name:
        q=src/p.relative_to('work/s09/sisters');q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
for name in ['sisters1907_images.json','sisters1917_images.json','sisters_targets_jobs.json','julianna_target_job.json','julianna_retry_jobs.json','sisters_catalogue.py']:
    shutil.copy2(Path('work/s09')/name,src/name)
shutil.copy2('work/s09/web/paternal09_sisters.json',src/'zapytania_internetowe.json')
for folder in ['swa_jednostka_10505112','swa_jednostka_32082739','browser_scan_sisters1907_images','browser_scan_sisters1917_images','browser_scan_sisters_targets_jobs','browser_scan_julianna_target_job','browser_scan_julianna_retry_jobs']:
    p=Path('work')/folder
    for f in p.glob('*'):
        if f.suffix in ['.json','.html','.txt'] or (f.suffix=='.body' and f.stat().st_size<600000):
            q=src/'proweniencja'/folder/f.name;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,q)

book=Path('Marysia_KOMPLET_BAZA_2026-11-05.xlsx');w=openpyxl.load_workbook(book)
def add(sn,row):
    s=w[sn];assert not any(r[0].value==row[0] for r in s),row[0]
    n=s.max_row+1;s.append(row)
    for col in range(1,s.max_column+1):
        a=s.cell(n-1,col);b=s.cell(n,col)
        if a.has_style:b._style=copy(a._style)
        b.hyperlink=None
    if s.auto_filter.ref:s.auto_filter.ref=f'A{1 if sn.startswith("HIPOTEZY") or sn.startswith("WIARYGODNOSC") else 3}:{openpyxl.utils.get_column_letter(s.max_column)}{n}'
def cells(sn,id):return next(r for r in w[sn] if r[0].value==id)
us='https://www.szukajwarchiwach.gov.pl/skan/-/skan/9d10d7cde36c6bc6600d52eb97d4ef1c0a384f9a98bbfd52bb23f9c62f65084e'
uj='https://www.szukajwarchiwach.gov.pl/skan/-/skan/9a130e8ffe855ef7ea744ffba5207c1d4c197eec550bc4925b0a7056e0dddf34'
for sid,title,date,person,sig,url,path,limit in [
('S147','Sabina Chmielewska — urodzenie124/1917','1917-07-14','P26;P05;P06','88/639/0/-/42; SwA32082739; obraz64/209,id59439545,k64,akt124',us,'1917_64.jpg','RodziceWincenty45/AgnieszkaMiszczyszyn32, Rogoźno. PorównaniezS071potwierdza siostręCzesława. Nie potwierdza dat rodzicówBogusława ani Tczewa. Adnotacja zgonu nad aktem dotyczy123Jana, nie Sabiny.'),
('S148','Julianna Chmielewska — urodzenie360/1907','1907-11-09','P27;P05;P06','88/639/0/-/32; SwA10505112; obraz83/223,id59221698,k81,akt360',uj,'1907_83.jpg','RodziceWincenty/AgnieszkaMiszczyszyn, Rogoźno, matka23. Ojciec30 wtym akcie — rozbieżność względem33w1905,36w1909; nie poprawiono i nie wyliczonoDOB. Zgodneoboje rodzice/miejscowość/wiekmatki identyfikują rodzeństwo. Bez Tczewa i późniejszych losów.'),
]:add('ZRODLA_I_SKANY',[sid,title,'SKAN PIERWOTNY',date,person,'AP Zamość / parafia Tomaszów Lubelski',sig,url,'ODCZYTANO ORYGINALNY OBRAZ',str(src/path),limit])
for pid,name,date,refs,limit,url in [
('P26','Sabina Chmielewska','ur.14.07.1917; chrzest/rejestracja22.07.1917','S147; S071; S061','Akt124: ojciecWincenty45, matkaAgnieszka32. Brak udokumentowanych późniejszych losów, nazwiska poślubnego i związku zTczewem.',us),
('P27','Julianna Chmielewska','ur.09.11.1907greg.; chrzest/rejestracja15.11.1907greg.','S148; S071; S147','Akt360: matkaAgnieszka23, ojciecWincenty30, wiek ojca rozbieżny zinnymi aktami. Rzadkie zgodneoboje rodzice iRogoźno oraz wiekmatki przemawiają za tą rodziną. Brak późniejszych losów/Tczewa.',uj),
]:add('RDZEN_RODZINY',[pid,name,'siostra CzesławaP03; przyporządkowanie całej gałęzi doBogusława nadalH017',date,'Rogoźno, parafiaTomaszówLubelski','brak daty i miejsca zgonu','córkaWincentegoP05/AgnieszkiP06; siostraCzesławaP03 iRomanaP12','SKAN URODZENIA; RODZEŃSTWO PRZEZ PORÓWNANIE AKTÓW',refs,limit,url])
rels=[
('R030','P05','P26','ojciec–córka','14.07.1917','S147','Wincenty wymieniony w akcie124/1917.',us),
('R031','P06','P26','matka–córka','14.07.1917','S147','Agnieszka zMiszczyszynów wymieniona w akcie124/1917.',us),
('R032','P03','P26','brat–siostra','urodzenia1909/1917','S071; S147','Ci sami oboje rodzice zrodowymmatki, Rogoźno, zgodny przybliżony wiek. Nie jest siostrąBogusława.',us),
('R033','P05','P27','ojciec–córka','09.11.1907','S148','Wincenty wymieniony w akcie360/1907; jego wpisanywiek30zachowano.',uj),
('R034','P06','P27','matka–córka','09.11.1907','S148','Agnieszka zMiszczyszynów wymieniona w akcie360/1907.',uj),
('R035','P03','P27','brat–siostra','urodzenia1907/1909','S148; S071; S147','Ci sami oboje rodzice, rzadkie rodowe matki, Rogoźno i wiekmatki. Rozbieżnośćwiekuojca jawnieQ74. Nie jest siostrąBogusława.',uj),
]
for rid,a,b,kind,date,refs,reason,url in rels:
    add('RELACJE',[rid,a,b,kind,date,'WNIOSEK Z AKTÓW PIERWOTNYCH' if kind=='brat–siostra' else 'SKAN PIERWOTNY',refs,reason,url])
for cid,pid,sid,data,reason,url in [
('C04','P26','S147','14.07.1917Rogoźno; Wincenty45/AgnieszkaMiszczyszyn32,akt124','Rodzice iRogoźno zgodni zCzesławemS071, matka iojciec wprzybliżeniu zgodni wiekiem.',us),
('C02','P27','S148','09.11.1907greg.Rogoźno; Wincenty30/AgnieszkaMiszczyszyn23,akt360','Oboje rodzice, Rogoźno iwiekmatki zgodni; odmiennywiekWincentego zachowanoQ74.',uj),
]:
    r=cells('KANDYDACI_I_HOMONIMY',cid)
    r[2].value=data;r[3].value='potwierdzona siostraCzesława → '+pid;r[5].value='ROZSTRZYGNIĘTO: '+pid+'; '+cid+' ZACHOWANY JAKO ALIAS'
    r[6].value=reason;r[7].value+='; '+sid+'; S071';r[8].value='Nie dublować osoby. Szukać późniejszych losów, ślubu, potomków. Tczew nadalniepotwierdzony.';r[9].value=url
for pid in ['P03','P05','P06']:
    r=cells('RDZEN_RODZINY',pid);r[6].value+='; SabinaP26 iJuliannaP27 — '+('siostry' if pid=='P03' else 'córki')
    r[8].value+='; S147; S148'
for sid,original in [('S009','S147'),('S015','S147'),('S007','S148')]:
    r=cells('ZRODLA_I_SKANY',sid);r[10].value+=' Etap10: oryginał odczytano jako'+original+'; wcześniejsze „nieodczytany” tostan historyczny. Potwierdzono siostrę Czesława.'
cells('HIPOTEZY_OTWARTE','H019')[2].value+=' Etap10: metrykiS147/S148potwierdzają siostryCzesławaSabinęP26/JuliannęP27, ale nie ich pobyt wTczewie i nie tożsamość zprzekazem.'
for hid,name,sid,limit in [('H026','SabinaC04siostrąCzesława?','S147','P26; związekcałejgałęzi zBogusławemH017osobny.'),('H027','JuliannaC02siostrąCzesława?','S148','P27; rozbieżnośćwiekuWincentegoQ74zachowana, Tczewnieustalony.')]:
    add('HIPOTEZY_ROZSTRZYGNIETE',[hid,name,'POTWIERDZONO Z PORÓWNANIA AKTÓW URODZENIA','Te sameoboje rodzice, rodowematki, Rogoźno. '+limit,sid+'; S071','2026-11-06'])
for eid,pid,date,text,refs,url,note in [
('E058','P26','14.07.1917','Sabina, córkaWincentego iAgnieszkiMiszczyszyn, urodzona wRogoźnie.','S147; S071',us,'Rejestracja/chrzest22.07.1917. To siostraCzesława, nieBogusława.'),
('E059','P27','09.11.1907','Julianna, córkaWincentego iAgnieszkiMiszczyszyn, urodzona wRogoźnie.','S148; S071',uj,'Data gregoriańska zapisana w nawiasie; chrzest15.11.1907greg. WiekWincentego30rozbieżny, Q74.'),
]:add('ZDARZENIA_I_FAKTY',[eid,date,pid+';P05;P06','urodzenie',text,'SKAN PIERWOTNY; RODZEŃSTWO Z PORÓWNANIA',refs,url,note])
for lid,scope,result,limit,refs in [
('L119','Katalog49jednostekTomaszów83263, manifesty1907(223) i1917(209)','Odnaleziono1907unit10505112i1917unit32082739, właściweobrazy83i64.','Odczytano wybrane obrazy, nie432metryki. Stronypróbne służyły lokalizacji.','S010; S147; S148'),
('L120','OryginałSabina124/1917; porównaniezCzesławem241/1909 iRomanem226/1919','Wincenty/AgnieszkaMiszczyszyn, Rogoźno, zbliżonewieki; P26, C04alias.','Brak późniejszych losów/Tczewa. Adnotacja nad124należy doJana123.','S147; S071; S061'),
('L121','OryginałJulianna360/1907 i porównanie rodziców','Wincenty/AgnieszkaMiszczyszyn, Rogoźno, matka23; P27, C02alias.','Ojciec30w1907wobec33w1905/36w1909. Nie korygowano oryginału, nieobliczanoDOB; Tczewnieustalony.','S148; S071; S072; S147'),
]:add('DZIENNIK_KWEREND',[lid,'2026-11-06',scope,result,limit,refs])
add('KOREKTY_I_SPRZECZNOSCI',['Q74','ROZBIEŻNOŚĆ WIEKU','Wincenty ma30lat w360/1907, choć33w1905 i36w1909','Zachowano odczyt30; matka23zgodniez21w1905 i25w1909; oboje rodzice iRogoźno zgodne. Nieprzypisano dokładnegoDOBojca.','ORYGINALNE AKTY, KONFLIKT ZACHOWANY','S148; S072; S071','Oceniaćłącznie nazwiskaobojga rodziców, rodowematki, miejscowość i wieki. Nie wyrównywać wieku bez dowodu.',uj])
for fid,path,refs,title in [('F93','1917_64.jpg','S147','Sabina124/1917, strona64'),('F94','1907_83.jpg','S148','Julianna360/1907, strona81'),('F95','units/units.json','S010; S147; S148','49jednostek; manifesty223/209oddzielnie')]:
    add('PLIKI_DOWODOWE',[fid,str(src/path),'SKAN / KATALOG',refs,title,'SHA256 w manifeścieetapu10'])
w['START']['A2']='Etap10: odczytano metryki i potwierdzono siostryCzesławaSabinęP26/JuliannęP27. TczewH019i przyporządkowanie rodzicówBogusławaH017 nadalotwarte. Obowiązują3poziomy wiarygodności, zachowano23arkusze.'
add('DRZEWO_SCHEMAT',['RodzeństwoCzesława','SabinaP26 iJuliannaP27','SiostryCzesławaP03, córkiWincentego/Agnieszki','S147; S148; S071. Daty14.07.1917 i09.11.1907. H017osobno, Tczewnieustalony.',None,None,None])
w['ZRODLA_I_SKANY']['A2']='148 źródeł. S147/S148: odczytaneakty urodzenia sióstrCzesława. Nie rozszerzają dowoduH017 na rodzicówBogusława.'
w['RDZEN_RODZINY']['A2']='14rekordów rdzenia; noweP26Sabina/P27Julianna to siostryCzesława, z odczytanych aktów. CałeprzyporządkowaniegałęzidoBogusława nadalH017.'
w['KANDYDACI_I_HOMONIMY']['A2']='61rekordów; C02→P27 iC04→P26 są aliasami, nieosobnymi osobami. C59nadalniepołączony.'
w.save(book)
manifest=[]
for p in sorted(src.rglob('*')):
    if p.is_file():
        b=p.read_bytes();manifest.append({'path':str(p),'size':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(stage/'manifest_zrodel_sesji.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('P26/P27; S147/S148; R030–R035; E058/E059; H026/H027 rozstrzygnięte, H017/H019otwarte.')
