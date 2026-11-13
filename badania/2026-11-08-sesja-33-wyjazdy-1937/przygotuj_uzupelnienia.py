"""Kopie odczytanych dokumentów i jawny zakres; bez nowych pobrań."""
from pathlib import Path
import csv, datetime, hashlib, json, shutil
from PIL import Image

D=Path(__file__).resolve().parent;R=D.parents[1];Z=D/'zrodla'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
old=R/'badania/2026-11-07-sesja-21-meldunki-Ch/zrodla'
manifest=json.loads((old/'ptg86616_downloads.json').read_text())
by={x['image']:x for x in manifest}
selected=[1,136,186,193,195,199,205,214,221,232,239,247,248]
checks=[]
for n in selected:
    p=R/'work/s21/ptg1938'/f'86616_{n:03}.jpg'
    sha=hashlib.sha256(p.read_bytes()).hexdigest()
    assert sha==by[n]['sha256'],n
    with Image.open(p)as im:im.verify()
    shutil.copy2(p,Z/p.name)
    checks.append(dict(image=n,url=by[n]['url'],sha256=sha,bytes=p.stat().st_size,previous_download=by[n]['at_utc'],read_at=now))
(Z/'S272_wybrane_oryginaly_sha256.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
data=[
 [186,'1008','Stefan Chmielewski','1898-07-01','m.Koło','1939-04-18','Niecała9'],
 [193,'1144','Krystyna Chmielewska','1922-10-28','Łódź','1939-05-06','Oszmiańska18a'],
 [195,'1197','Władysława Chmielewska','1894-11-06','Dzierązna,pow.sieradzki','1939-05-12','Niecała9'],
 [199,'1275','Abram-Mordka Chmielewski','1892-12-01','Włoszczowa','1939-05-22','Zawadzka15'],
 [205,'1398','Josek-Hersz Chmielewski','1903-03-23','Włoszczowa','1939-06-05','Północna19'],
 [214,'1576','Adam Chmielewski','1902-09-02','Łódź','1939-06-26','Grodzieńska39?'],
 [214,'1577','Bronisława Chmielewska','1910-08-10','Łódź','1939-06-26','Grodzieńska39?'],
 [221,'1703','Helena Chmielewska','1919-08-04','RakowaGóra,pow.radomszczański','1939-07-10','Smocza28'],
 [232,'1938','Juda Chmielewski','1919-01-04','Włoszczowa','1939-08-04','Zawadzka35'],
 [239,'2064','Stanisław Chmielewski','1912-02-15','m.Łódź','1939-08-19','Łączna57']]
keys=['image','entry','name','dob','birthplace','identity_document_date','address']
rows=[]
for a in data:
    r=dict(zip(keys,a));r.update(source='S272',url=by[r['image']]['url'],limitation='Brak wskazanych rodziców lub relacji do rodziny Marysi. Sąsiedztwo i adres nie dowodzą małżeństwa. Daty odczytane w odpowiedniej komórce, nie przesunięte z następnej osoby.');rows.append(r)
(Z/'S272_wybrane_odczyty.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
with(Z/'S272_wybrane_odczyty.csv').open('w',newline='')as out:
    w=csv.DictWriter(out,list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
scope=dict(source='S272',at_utc=now,new_search_criterion='Zygm. z3693; możliwy wariant Zygmunt Chmielewski, nie potwierdzone pełne imię/nazwisko',name_columns_reread=[[136,247]],record_images=112,full_rows=10,selected_full_images=selected,technical_newly_read=[1,248],result='Nie zaobserwowano Zygmunta Chmielewskiego. Dziesięć innych wpisów bez rodzinnego łącznika.',limitations=['Nowe kryterium uzasadnia ten przegląd; wcześniejszy S272 szukał Czesława/Janiny/Agnieszki.','1938/2–134 nie ponowiono pod nowym kryterium.','Nie czytano wszystkich rubryk112obrazów. Nie jest to dowód nieobecności osoby wŁodzi.','Obraz247:nr2221–2223,ostatnie16X1939; nie pokrywa całego roku.','Poświadczenie248mówi254strony i ma datę12VII1937; data oprawy nie jest okresem wpisów.248obrazów PTGniejest gwarancją pełnej fizycznej księgi.'],previous_complete_contact_archive=str((old/'kolumny_86616.zip').relative_to(R)),new_proven_relationships=0)
(Z/'S272_zakres_nowego_kryterium.json').write_text(json.dumps(scope,ensure_ascii=False,indent=2)+'\n')

arolsen=[
 dict(docid='70634058',images=1,reading='Zygmund14V1910; klinikaGöttingen15X–3XI1941; wypisGr.Lengden. Bez rodziców/żony/Łodzi.'),
 dict(docid='78640271',images=1,reading='Sigmund10V1926; gospodarstwoOttlotschin/Otłoczyn,spis21V1941,Anton24VII1896/Valerie17IV1887; brak łącznika zZygm.3693lubP11.'),
 dict(docid='81787522',images=2,reading='Zygmunt41lat,single,Ship-Agent,Poland→Chicago,nr61595/207598. Rewers kartowania1950,nie data urodzenia. Brak rodzinnego łącznika.'),
 dict(docid='81978799',images=2,reading='Zygmunt9IV1905/kartaDP126758;Halina4V1914/126755;Zygmunt15VIII1943,Pforzheim/126759. Brak jawnych ról rodzicielskich. Rewers bez dodatkowej relacji.'),
 dict(docid='81979003',images=2,reading='Ettlingen→Ingolstadt30VIII1946,nr45–47:Zygmunt41latDP126758,Halina32lat126755,Zygmunt3lata126759. Numery kart łączą osoby z81978799; nie z rodziną Marysi. Rewers bez dodatkowych wpisów.'),
 dict(docid='81991022',images=2,reading='Zygmund118138 iAnna118139,G04854612. BrakDOB,Łodzi iStanisławy. Rewers stemple1948/49. Sąsiedztwo nie dowodzi małżeństwa.')]
for a in arolsen:a.update(source='S321',url='https://collections.arolsen-archives.org/en/document/'+a['docid'],read_at=now)
(Z/'arolsen_zygmunt_odczyty.json').write_text(json.dumps(arolsen,ensure_ascii=False,indent=2)+'\n')

# Minimalne wypisy korespondencji mają pełny tekst odpowiedzi merytorycznej,
# ale nie kopię prywatnych nagłówków lub danych kontaktowych żyjących.
private=json.loads((R/'work/audyt-github-2026-11-13/wiadomosci_PROJEKT_PRYWATNE.json').read_text())['responses']
byid={x['id']:x for x in private};p=Z/'odpowiedzi_instytucji_wypisy.json';a=json.loads(p.read_text())
for m in a:
    m['sha256_original_body']=hashlib.sha256(byid[m['gmail_message_id']]['body'].encode()).hexdigest();m['read_at_utc']=now
p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
threads=json.loads((R/'work/audyt-github-2026-11-13/watki_PROJEKT_PRYWATNE.json').read_text())['responses']
sent=[]
for t in threads:
    assert t['truncated']is False
    for m in t['messages']:
        if'SENT'in m['labels']:
            sent.append(dict(message_id=m['id'],thread_id=t['thread_id'],subject=m['subject'],sent_utc=m['email_ts']+'Z',labels=['SENT'],sha256_original_body=hashlib.sha256(m['body'].encode()).hexdigest()))
(Z/'potwierdzone_wysylki_historyczne_metadane.json').write_text(json.dumps(sent,ensure_ascii=False,indent=2)+'\n')
print('Utrwalono13oryginałów S272,10wierszy,6DocID/10obrazów Arolsen,4odpowiedzi i4historyczne SENT. Nie wysłano nowej wiadomości.')
