"""Zapis odczytów etapu25. Oryginały kopiowane bez przetwarzania, pochodne opisane."""
from pathlib import Path
import csv,datetime,hashlib,html,io,json,shutil,zipfile
from PIL import Image
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent;Z=HERE/'zrodla';W=ROOT/'work/s25'
Z.mkdir(exist_ok=True);now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
configs={1938:dict(uid=15351997,sig='39/225/0/4/2137',total=197,names=[[5,155],[157,195]],technical=[1,2,3,4,156,196,197],full=[5,22,49,50,155,157,177,182,195],archive=[1,4,5,22,49,50,155,156,157,177,182,195,196,197]),1937:dict(uid=15351995,sig='39/225/0/4/2135',total=205,names=[[5,167],[169,202]],technical=[1,2,3,4,168,203,204,205],full=[5,34,134,179],archive=[1,4,5,34,134,167,168,169,179,202,203])}
urls={};downloaded=[];contacts=[]
for y,c in configs.items():
 m=json.loads((HERE.parent/f'2026-11-07-sesja-24-Chojny-wyjazd/katalog/manifest_{c["uid"]}.json').read_text());urls[y]={e['pozycja']:e['src'] for e in m['elementy']};shutil.copy2(HERE.parent/f'2026-11-07-sesja-24-Chojny-wyjazd/katalog/manifest_{c["uid"]}.json',Z/f'manifest_{c["uid"]}.json')
 for n in range(1,c['total']+1):
  p=W/f'ChojnyP{y}_{n}.jpg';p=p if p.exists() else Z/p.name;b=p.read_bytes();Image.open(io.BytesIO(b)).verify();downloaded.append(dict(year=y,image=n,url=urls[y][n],bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),archived_original=n in c['archive']))
  if n in c['archive']:shutil.copy2(p,Z/p.name)
 with zipfile.ZipFile(Z/f'kolumny_{y}.zip','w',compression=zipfile.ZIP_STORED) as z:
  ps=sorted(W.glob(f'p{y}_*_*.jpg'));assert len(ps)==(32 if y==1938 else 34),(y,len(ps))
  for p in ps:
   im=Image.open(p).convert('L');b=io.BytesIO();im.save(b,format='JPEG',quality=70,optimize=True);raw=b.getvalue();z.writestr(p.name,raw);contacts.append(dict(year=y,file=p.name,sha256=hashlib.sha256(raw).hexdigest(),derivative=True))
(Z/'pobrane_sha256.json').write_text(json.dumps(downloaded,ensure_ascii=False,indent=2)+'\n')
(Z/'kolumny_manifest.json').write_text(json.dumps(contacts,ensure_ascii=False,indent=2)+'\n')
scopes=dict(at_utc=now,books=configs,method='Wzrokowy przegląd kolumn nazwisk i wybranych pełnych rubryk. Nie pełna transkrypcja. Pochodne w ZIP; pełne oryginały wybranych obrazów osobno.',structure1938='Stałe5–155;czasowe157–195;156pieczęć199kart i tytuł czasowych. Metryka1:199+51kart,196skanów;manifest197obrazów. Fizyczne152–199i40–51drugiejczęści niezapisane.',structure1937='Stałe5–167;czasowe169–202;168pieczęć404kart i tytuł czasowych;203pieczęć84kart. Metryka1:404+84kart,204skany;manifest205obrazów. Fizyczne165–404i36–84drugiejczęści niezapisane. Ubytki40i162wgmetryki.',limits='Grupy nie wymieniają wszystkich domowników. Nie wyklucza to nienazwanych osób, pomyłek ani innych ksiąg. Nie ustalono pokrewieństwa, wieku ani rodowego Agnieszki. Nie znaleziono imieniaP11.',new_proven_relationships=0)
(Z/'zakres_odczytu.json').write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n')
with (Z/'zakres_stron.csv').open('w',newline='') as f:
 w=csv.writer(f,lineterminator='\n');w.writerow(['rok','obraz','nazwiska','wybrane_pelne_rubryki','oryginal'])
 for y,c in configs.items():
  for n in range(1,c['total']+1):w.writerow([y,n,'ODCZYTANO' if any(a<=n<=b for a,b in c['names']) else 'TECHNICZNY OBEJRZANY','TAK' if n in c['full'] else 'NIE',urls[y][n]])
hits=[]
def hit(src,y,n,nr,text,card):hits.append(dict(zrodlo=src,sygnatura=configs[y]['sig'],obraz=n,nr_wpisu=str(nr),odczyt_i_granice=text,oryginal=urls[y][n],pochodzenie=f'Etap25; wybrane rubryki; karta{card}'))
hit('S288',1938,22,398,'Agnieszka Chmielewska;2m+3k;poprzednio Łódź,Chełmońskiego9a;otrzymanie zgłoszenia21II1938(ditto po397),dowódA i zapis do rejestru25III1938. Brak daty urodzenia,nazwiska rodowego,imion towarzyszy i adresu wChojnach. C103 niescalona zP06/C99/C102. Zgodność liczebności zC99nie dowodzi tożsamości ani pokrewieństwa.',19)
hit('S289',1938,49,1016,'Bolesław Chmielewski;1m+1k;poprzednio Rawia[odczyt do kontroli],gmWadlew,powPiotrków;zgłoszenie25IV1938(ditto);dowódA12V1938,zapis7VI1938. Bez identyfikatorów rodzinnych; nieprzypisany doP11/rodziny.',45)
hit('S289',1938,50,1054,'Danuta Chmielewska;1k;poprzednio Rawia[odczyt do kontroli],gmWadlew,powPiotrków;zgłoszenie27IV1938(ditto);dowódA12V1938,zapis7VI1938. Podobne dane do1016nie dowodzą relacji. Brak wieku i rodziców.',46)
hit('S289',1938,177,477,'Bolesław Kazimierz CHMIELNICKI;1m;powWłocławek,gmLubień,Siemiany;zgłoszenie16VII1938. Odrzucono błędne podejrzenie odczytu Chmielewski; NIE jest wpisem BogusławaKazimierza i nie tworzy kandydata rodzinnego.',21)
hit('S289',1938,182,587,'Edward Poprawka;1m;Ługi,gmMajaczewice,powSieradz;zgłoszenie22VIII1938. Bez daty urodzenia i rodziców; nie połączono zJaninąPoprawką.',26)
hit('S290',1937,34,685,'Bronisława Chmielewska;1k;powPiotrków,gmŁęka;miejscowość niepewna[roboczo Selachki];zgłoszenie18III1937,dowódA7IV1937,zapis10IV1937. Brak wieku,rodowego i rodzinnego łącznika.',31)
hit('S290',1937,134,2957,'Marian Janusz Chmielewski;1m;rubryka poprzedniego miejsca:odurodzenia(ditto),zgłoszenie20X1937(ditto),zapis4XI1938. Nie ma dokładnej daty urodzenia ani rodziców. Imię MarianJanusz, nie CzesławJan. Nie utożsamiono zP11aniMarianamiS285.',131)
hit('S290',1937,179,234,'Bolesław Chmielewski;1m;gmWadlew,Rawia[odczyt do kontroli],zgłoszenie30IV1937. Pobyt czasowy; bez wieku,rodziców i pokrewieństwa. Zbieżność z1016/1938nie wystarcza do przypisania rodzinie.',12)
(Z/'odczyty_wybrane.json').write_text(json.dumps(hits,ensure_ascii=False,indent=2)+'\n')
for name in ['Agnieszka398_full.jpg','nazwisko477.jpg','Boleslaw234.jpg']:
 shutil.copy2(W/name,Z/name)
oldrows=json.loads((HERE.parent/'2026-11-07-sesja-24-Chojny-wyjazd/indeks_dane.json').read_text());rows=oldrows+hits;assert len(rows)==55
(HERE/'indeks_dane.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
with (Z/'indeks_wybranych_wpisow.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
old=(HERE.parent/'2026-11-07-sesja-24-Chojny-wyjazd/INDEKS.html').read_text()
cells=''.join('<tr>'+''.join('<td>'+html.escape(str(r[k]))+'</td>' for k in ['zrodlo','sygnatura','obraz','nr_wpisu','odczyt_i_granice'])+'<td><a href="'+html.escape(r['oryginal'],quote=True)+'">Skan</a></td></tr>' for r in rows)
(HERE/'INDEKS.html').write_text(old.split('<tbody>')[0].replace('etapów21–24','etapów21–25')+'<tbody>'+cells+'</tbody>'+old.split('</tbody>')[1])
print(dict(downloaded=len(downloaded),names1938=190,names1937=197,index=len(rows),contacts=len(contacts),originals=25))
