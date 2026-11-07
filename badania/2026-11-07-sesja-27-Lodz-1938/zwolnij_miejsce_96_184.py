"""Po archiwizacji: usuń tylko zweryfikowane robocze kopie, zachowując spis."""
from pathlib import Path
from hashlib import sha256
import json
R=Path(__file__).resolve().parents[2]
D=Path(__file__).resolve().parent
data=json.loads((D/'zrodla/zakres_odczytu_96-184.json').read_text())
assert sha256((D/'zrodla/LodzW1938_126.jpg').read_bytes()).hexdigest()==data['zakres'][30]['sha256']
removed=[]
previous={r['obraz']:r for r in json.loads((D/'usuniete_kopie_96_184.json').read_text())} if (D/'usuniete_kopie_96_184.json').exists() else {}
for row in data['zakres']:
 n=row['obraz'];p=R/f'work/s25/LodzW1938_{n}.jpg'
 assert (p.exists() and sha256(p.read_bytes()).hexdigest()==row['sha256']) or (n!=126 and previous.get(n,{}).get('sha256')==row['sha256'])
 if n!=126:
  removed.append({'obraz':n,'sha256':row['sha256'],'bytes':row['bytes'],'url':row['url']})
(D/'usuniete_kopie_96_184.json').write_text(json.dumps(removed,ensure_ascii=False,indent=2)+'\n')
for row in removed:
 p=R/f"work/s25/LodzW1938_{row['obraz']}.jpg"
 if p.exists():p.unlink()
for p in (R/'work/s25/lodz_kontakty').glob('*.jpg'):
 if p.stem.startswith('pelna_'):p.unlink();continue
 if p.stem[0].isdigit() and int(p.stem.split('-')[0])>=96:p.unlink()
print(len(removed),'roboczych obrazów usunięto po SHA256; oryginał 126 w repozytorium')
