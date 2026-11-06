"""Publiczny widok z jawnie wybranymi polami; bez kopiowania prywatnego Excela."""
from pathlib import Path
import json,subprocess,datetime
from zoneinfo import ZoneInfo
ROOT=Path(__file__).resolve().parents[1];HERE=Path(__file__).resolve().parent
# Ręcznie wybrane dane publiczne i niezależne oceny relacji: wiarygodnosc.json.
events=[
('92b5fe18e544485b56adefb222e7cf8ad6287af8','Australijski trop Romana i jego dzieci','Dokumenty migracyjne wskazują Romana Chmielewskiego (06.06.1919), żonę Annę i synów Romana (1946) oraz Ernesta (1947). Data urodzenia ojca jest zgodna z bratem Czesława, ale ich tożsamość i obecne życie potomków wymagają potwierdzenia.','ważny trop'),
('139877276c1abf111e9b5dae3897b4da3bb180c1','Potwierdzono przyrodnią siostrę Czesława i jej małżeństwo','Emilia Chmielewska, urodzona 26.01.1904 w Rachaniach, była córką Wincentego i jego pierwszej żony Julii z Jabłońskich. W 1932 r. poślubiła Józefa Mandziuka. Ich dzieci pozostają nieustalone.','odkrycie'),
('54fe3e02fad045457095647f57678653e4838b50','Potwierdzono dwie siostry Czesława','Akty urodzenia Sabiny (14.07.1917) i Julianny (09.11.1907) wskazują Wincentego Chmielewskiego i Agnieszkę z Miszczyszynów z Rogoźna — tych samych rodziców co akt Czesława. Związek sióstr z Tczewem pozostaje nieustalony.','odkrycie'),
('309edd1da848f3ae1bd3446e6a247e2cc027524f','Uzupełniono rodzinę mamy i potwierdzenie pradziadków','Rodzina potwierdziła Józefa i Czesławę jako pradziadków Marysi, rodziców Romana. Dostarczone zdjęcie potwierdza cztery inskrypcje; wcześniejsze dane rodzeństwa Marii i linii Kulas zachowują swoje źródła.','uzupełnienie'),
('2843053','Odnaleziono akt możliwego brata Bogusława','Czesław zmarł w Łodzi 3 lutego 1940 r., mając osiem dni. Rodziców zapisano jako Czesława i Janinę z Poprawskich; pokrewieństwo z rodziną wymaga potwierdzenia.','ważny akt'),
('ea0d189','Potwierdzono nazwiska rodziców Bogusława','Jego odpis ślubu wskazuje Czesława Chmielewskiego i Janinę Poprawkę.','odkrycie'),
('e2b9c5c','Potwierdzono urodzenie Czesława i jego brata Romana','Akt z 1909 r. pozwolił ustalić datę urodzenia Czesława i potwierdzić wspólnych rodziców obu braci.','odkrycie'),
('4108653','Odnaleziono akt urodzenia Janiny Poprawki','Akt z 1910 r. wskazuje jej rodziców: Józefa Poprawkę i Mariannę Kacprzak.','odkrycie')]
news=[]
for commit,title,body,kind in events:
 stamp=subprocess.check_output(['git','show','-s','--format=%cI',commit],cwd=ROOT,text=True).strip()
 news.append(dict(at=stamp,title=title,body=body,kind=kind))
curated=json.loads((HERE/'wiarygodnosc.json').read_text())
people,edges,sources=curated['people'],curated['edges'],curated['sources']
data=dict(people=people,edges=edges,sources=sources,relations=curated['relations'],news=news,updated=max(x['at'] for x in news),generated=datetime.datetime.now(datetime.timezone.utc).isoformat())
(HERE/'public').mkdir(exist_ok=True)
template=(HERE/'szablon.html').read_text()
(HERE/'public/index.html').write_text(template.replace('__DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/')).replace('__SCRIPT__',(HERE/'interakcje.js').read_text()))
print('Publiczny widok:',len(people),'osób,',len(news),'wpisów; znane dane rodzinne i rozdzielone poziomy dowodu.')
