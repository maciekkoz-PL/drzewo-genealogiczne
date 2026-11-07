"""Weryfikuje 95 pobranych stron; usuwa tylko robocze kopie już przejrzanych stron.

Oryginały dowodowe 8 i 74 są zachowane w Git. Pozostałe URL są w manifeście
SwA etapu25, SHA256 w zakresie etapu26. Dziennik usunięć pozostaje w repo.
"""
from pathlib import Path
import hashlib, json

R=Path(__file__).resolve().parents[2]
H=Path(__file__).resolve().parent
old=R/'badania/2026-11-07-sesja-26-Wladyslaw-1938'
scope=json.loads((old/'zrodla/zakres_odczytu.json').read_text())['lodz_wyjazdy']['oryginaly']
assert [x['obraz'] for x in scope]==list(range(1,96))
records=[]
for x in scope:
 n=x['obraz'];p=R/f'work/s25/LodzW1938_{n}.jpg'
 assert p.is_file(),p
 b=p.read_bytes();assert b.startswith(b'\xff\xd8\xff') and hashlib.sha256(b).hexdigest()==x['sha256'],p
 if n in (8,74):
  assert b==(old/f'zrodla/LodzW1938_{n}.jpg').read_bytes()
 else: records.append({'obraz':n,'robocza_sciezka':str(p.relative_to(R)),'sha256':x['sha256'],'bytes':len(b)})
(H/'usuniete_kopie_robocze.json').write_text(json.dumps({'zasada':'Tylko strony1–95 poza8/74; pełne URL w manifeście jednostki6209685 etapu25; SHA256 w zakresie etapu26. Usunięte są kopie robocze, nie archiwalne oryginały dowodowe.','pliki':records},ensure_ascii=False,indent=2)+'\n')
for x in records:(R/x['robocza_sciezka']).unlink()
print('Weryfikowano95; zachowano2 w Git; usunięto93 kopie robocze:',sum(x['bytes'] for x in records),'bajtów')
