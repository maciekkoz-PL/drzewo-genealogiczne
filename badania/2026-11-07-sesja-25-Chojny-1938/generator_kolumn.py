from PIL import Image,ImageDraw
from pathlib import Path
import sys
W=Path(__file__).parent;year=int(sys.argv[1]);lo=int(sys.argv[2]);hi=int(sys.argv[3])
for start in range(lo,hi+1,6):
 nums=list(range(start,min(start+6,hi+1)));dest=W/f'p{year}_{start}_{nums[-1]}.jpg'
 if dest.exists():continue
 if not all((W/f'ChojnyP{year}_{n}.jpg').exists() for n in nums):continue
 out=Image.new('RGB',(560*len(nums),2240),'white');d=ImageDraw.Draw(out)
 for j,n in enumerate(nums):
  im=Image.open(W/f'ChojnyP{year}_{n}.jpg');crop=im.crop((100,130,790,im.height-180));crop=crop.resize((560,2140));out.paste(crop,(j*560,80));d.text((j*560+25,20),f'IMAGE {n}',fill='black')
 out.save(dest,quality=92)
 print(dest,flush=True)
