const D=JSON.parse(document.getElementById('family-data').textContent);
const $=id=>document.getElementById(id);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const byId=Object.fromEntries(D.people.map(p=>[p.id,p]));
const dt=s=>new Intl.DateTimeFormat('pl-PL',{dateStyle:'medium',timeStyle:'short',timeZone:'Europe/Warsaw'}).format(new Date(s));
const labels={document:'Dokument',identity:'Identyfikacja w toku',family:'Przekaz rodzinny',candidate:'Pokrewieństwo do sprawdzenia'};
const edgeLabels={parent:'Rodzice Marysi — potwierdzone przez rodzinę',document:'Rodzicielstwo wskazane w dokumencie',marriage:'Małżeństwo potwierdzone dokumentem',identity:'Tożsamość pary wymaga dodatkowego potwierdzenia',family:'Relacja z przekazu rodzinnego',sibling:'Rodzeństwo z przekazu rodzinnego',hypothesis:'Hipoteza rodzeństwa — niepotwierdzona'};
Object.assign(edgeLabels,{hypothesis_parent:'Możliwy rodzic — hipoteza ze wspólnego grobu',identity_candidate:'Możliwa tożsamość — osoby nie zostały scalone',family_marriage:'Małżeństwo według przekazu rodzinnego',hypothesis_marriage:'Możliwe małżeństwo — niepotwierdzone'});
const normalize=s=>s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/ł/g,'l');
const mapUrl=query=>'https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(query);
const locationLinks=p=>(p.locations||[]).map(l=>`<a class="map-link" href="${esc(mapUrl(l.query))}" target="_blank" rel="noopener noreferrer" aria-label="Pokaż na mapie: ${esc(l.label)} — ${esc(p.name)}">⌖ ${esc(l.label)} ↗</a>`).join('');
const placeWithLinks=p=>{
 const places=p.locations||[];const text=p.place||'';let cursor=0,result='';
 while(cursor<text.length){
  const next=places.map(l=>({l,index:text.indexOf(l.label,cursor)})).filter(x=>x.index>=0).sort((a,b)=>a.index-b.index||b.l.label.length-a.l.label.length)[0];
  if(!next){result+=esc(text.slice(cursor));break}
  result+=esc(text.slice(cursor,next.index))+`<a class="map-link" href="${esc(mapUrl(next.l.query))}" target="_blank" rel="noopener noreferrer" aria-label="Pokaż na mapie: ${esc(next.l.label)} — ${esc(p.name)}">${esc(next.l.label)}</a>`;
  cursor=next.index+next.l.label.length;
 }
 return result;
};
const addressDetails=p=>(p.addresses||[]).length?`<h3>Adresy i miejsca ze źródeł</h3>${p.addresses.map(a=>`<div class="source"><strong>${esc(a.label)}</strong><p>${esc(a.when)}</p><p>${esc(a.context)}</p><p>Źródło: ${esc(a.source)} · ${esc(D.sources[a.source].title)}</p><a href="${esc(mapUrl(a.query))}" target="_blank" rel="noopener noreferrer">Wyszukaj na mapie ↗</a></div>`).join('')}${p.addresses.some(a=>/Stocka|Napiórkowskiego/.test(a.label))?'<p class="map-note">Mapa wyszukuje nazwę historyczną. Dzisiejsza nazwa ulicy, numeracja i położenie budynku nie zostały zweryfikowane.</p>':''}`:'';
let currentPeople=[],currentEdges=[],positions={},scale=1,width=1540,height=1080,offsetX=0,offsetY=0;
$('updated').textContent='Aktualizacja: '+dt(D.generated);

let selectedLevel=2;
const levelNames={1:'Udokumentowane',2:'Prawdopodobne',3:'Przypuszczenie'};
const relationByPair=Object.fromEntries(D.relations.map(r=>[r.a+'|'+r.b,r]));
function filteredPeople(){
 const branch=$('branch').value;
 return D.people.filter(p=>(branch==='both'||p.branch==='both'||p.branch===branch)&&p.level<=selectedLevel);
}
function zoom(v){
 const centerX=($('viewport').scrollLeft+$('viewport').clientWidth/2-offsetX)/scale,centerY=($('viewport').scrollTop+$('viewport').clientHeight/2-offsetY)/scale;
 scale=Math.max(.2,Math.min(1.8,v));
 $('canvas').style.transform=`scale(${scale})`;
 updateCanvasBox();
 $('viewport').scrollTo(Math.max(0,offsetX+centerX*scale-$('viewport').clientWidth/2),Math.max(0,offsetY+centerY*scale-$('viewport').clientHeight/2));
}
function updateCanvasBox(){
 offsetX=Math.max(0,($('viewport').clientWidth-width*scale)/2);offsetY=Math.max(0,($('viewport').clientHeight-height*scale)/2);
 $('canvas').style.left=offsetX+'px';$('canvas').style.top=offsetY+'px';
 $('sizer').style.width=Math.max(width*scale,$('viewport').clientWidth)+'px';$('sizer').style.height=Math.max(height*scale,$('viewport').clientHeight)+'px';
}
function fit(){
 const minHeight=innerWidth<700?420:490,maxHeight=Math.min(900,Math.max(minHeight,innerHeight-240));
 zoom(Math.min($('viewport').clientWidth/width,maxHeight/height,1));
 $('viewport').style.height=Math.max(minHeight,Math.min(maxHeight,height*scale+20))+'px';updateCanvasBox();centerMarysia();
}
function centerMarysia(){
 const p=positions.P01;if(!p)return;const node=document.querySelector('[data-id="P01"]');
 $('viewport').scrollTo(Math.max(0,offsetX+(p.x+120)*scale-$('viewport').clientWidth/2),Math.max(0,offsetY+(p.y+node.offsetHeight/2)*scale-$('viewport').clientHeight/2));
}
function renderTree(){
 currentPeople=filteredPeople();const ids=new Set(currentPeople.map(p=>p.id));
 currentEdges=D.edges.filter(([a,b])=>ids.has(a)&&ids.has(b)&&(relationByPair[a+'|'+b].level<=selectedLevel||relationByPair[a+'|'+b].contextInDocumented));
 $('canvas').querySelectorAll('.node').forEach(n=>n.remove());$('lines').replaceChildren();
 const root=byId.P01,centerX=root.x+120,centerY=root.y+71;
 const halfWidth=Math.max(400,...currentPeople.map(p=>Math.max(centerX-p.x,p.x+240-centerX)))+40;
 const halfHeight=Math.max(260,...currentPeople.map(p=>Math.max(centerY-p.y,p.y+142-centerY)))+40;
 const minX=centerX-halfWidth,minY=centerY-halfHeight;
 width=halfWidth*2;height=halfHeight*2;
 $('people').innerHTML='<option value="">Wybierz osobę, aby zobaczyć szczegóły</option>';
 for(const p of currentPeople){
  positions[p.id]={x:p.x-minX,y:p.y-minY};const pos=positions[p.id];
  const b=document.createElement('div');b.className='node '+p.status+' level-'+p.level;b.dataset.id=p.id;b.style.left=pos.x+'px';b.style.top=pos.y+'px';
  b.setAttribute('role','group');b.setAttribute('aria-label',p.name);b.innerHTML=`<span class="badge">${esc(levelNames[p.level])}</span><button class="node-open" aria-label="Szczegóły: ${esc(p.name)}"><span class="name">${esc(p.name)}</span></button><small>${esc(p.role)}</small><div class="dates">${esc(p.dates)}</div>${(p.locations||[]).length?`<div class="node-maps">${locationLinks(p)}</div>`:''}`;
  b.onclick=e=>{if(!e.target.closest('a'))openPerson(p.id)};$('canvas').appendChild(b);
  const o=document.createElement('option');o.value=p.id;o.textContent=p.name+(p.status==='candidate'?' · hipoteza':'');$('people').appendChild(o);
 }
 // Centre the measured root card, whose height can vary with text wrapping.
 const rootNode=document.querySelector('[data-id="P01"]'),shiftY=height/2-(positions.P01.y+rootNode.offsetHeight/2);
 for(const p of currentPeople){positions[p.id].y+=shiftY;document.querySelector(`[data-id="${p.id}"]`).style.top=positions[p.id].y+'px'}
 $('canvas').style.width=width+'px';$('canvas').style.height=height+'px';
 $('lines').style.width=width+'px';$('lines').style.height=height+'px';$('lines').setAttribute('viewBox',`0 0 ${width} ${height}`);
 let lane=0;
 for(const [a,b,kind] of currentEdges){
  const A=positions[a],B=positions[b];let d;
  if(['hypothesis','identity_candidate','hypothesis_marriage'].includes(kind)){
   const top=Math.min(A.y,B.y)-22-(lane++%3)*12;
   d=`M${A.x+120},${A.y} V${top} H${B.x+120} V${B.y}`;
  }else if(kind==='marriage'&&A.y!==B.y){
   const rail=Math.max(...currentPeople.filter(p=>positions[p.id].y>=Math.min(A.y,B.y)&&positions[p.id].y<=Math.max(A.y,B.y)).map(p=>positions[p.id].x+240))+60;
   d=`M${A.x+240},${A.y+66} H${rail} V${B.y+66} H${B.x+240}`;
  }else if(['marriage','sibling','family_marriage'].includes(kind)){
   const left=A.x<B.x?A:B,right=left===A?B:A;
   d=`M${left.x+240},${left.y+66} L${right.x},${right.y+66}`;
  }else{
   const down=B.y>A.y,x=A.x+120,y=A.y+(down?document.querySelector(`[data-id="${a}"]`).offsetHeight:0),X=B.x+120,Y=B.y+(down?0:document.querySelector(`[data-id="${b}"]`).offsetHeight);
   d=`M${x},${y} V${y+(Y-y)*.5} H${X} V${Y}`;
  }
  const path=document.createElementNS('http://www.w3.org/2000/svg','path');path.setAttribute('d',d);path.setAttribute('fill','none');
  path.setAttribute('stroke',['identity','hypothesis','hypothesis_parent','identity_candidate','hypothesis_marriage'].includes(kind)?'#ab7d3e':['family','sibling','family_marriage'].includes(kind)?'#8c9896':kind==='marriage'?'#8e859e':'#729b7c');
  path.setAttribute('stroke-width',kind==='parent'?'2.5':'1.7');path.dataset.kind=kind;path.dataset.from=a;path.dataset.to=b;
  if(kind==='parent'){path.setAttribute('stroke','#2b6c59');path.setAttribute('vector-effect','non-scaling-stroke')}
  const evidence=relationByPair[a+'|'+b];path.dataset.level=evidence.level;
  if(evidence.level>1)path.setAttribute('stroke-dasharray',evidence.level===3?'2 6':'6 5');
  path.setAttribute('stroke',evidence.level===3?'#946528':evidence.level===2?'#73827c':'#2b6c59');
  const title=document.createElementNS('http://www.w3.org/2000/svg','title');title.textContent=levelNames[evidence.level]+': '+evidence.reason;path.appendChild(title);$('lines').appendChild(path);
 }
 $('view-note').textContent=`${currentPeople.length} osób · ${currentEdges.length} relacji. Poziom ${selectedLevel}. Osoby i własne akty są widoczne niezależnie od H017. Przerywane łączniki rodziców Bogusława zachowują oznaczenie identyfikacji w toku.`;
 applySearch();fit();
}
function openPerson(id){
 const p=byId[id];if(!p)return;
 if(!currentPeople.some(x=>x.id===id)){
  selectedLevel=Math.max(selectedLevel,p.level);syncLevels();
  if($('branch').value!=='both'&&p.branch!=='both'&&p.branch!==$('branch').value)$('branch').value='both';
  renderTree();
 }
 const relatives=currentEdges.filter(e=>e[0]===id||e[1]===id).map(e=>({id:e[0]===id?e[1]:e[0],kind:e[2]}));
 const unique=[...new Map(relatives.map(r=>[r.id,r])).values()];
 $('detail').innerHTML=`<div class="eyebrow">${esc(levelNames[p.level])}</div><h2>${esc(p.name)}</h2><p class="detail-dates">${esc(p.dates)}</p><p class="person-place">${placeWithLinks(p)}</p>${addressDetails(p)}<p class="detail-note">${esc(p.note)}</p>${unique.length?`<h3>Powiązane osoby</h3><div class="related">${unique.map(r=>`<button class="pill" data-open="${r.id}">${esc(byId[r.id].name)}${['hypothesis','hypothesis_parent','identity_candidate','hypothesis_marriage'].includes(r.kind)?' · hipoteza':r.kind==='identity'?' · identyfikacja w toku':['family','sibling','family_marriage'].includes(r.kind)?' · przekaz rodzinny':''}</button>`).join('')}</div>`:''}<h3>Podstawa informacji</h3>${p.source.map(sid=>{const s=D.sources[sid];return `<div class="source">${s.url?`<a href="${esc(s.url)}" target="_blank" rel="noopener noreferrer">${esc(s.title)} ↗</a>`:`<strong>${esc(s.title)}</strong>`}${s.description?`<p>${esc(s.description)}</p>`:''}</div>`}).join('')}`;
 const relationDetails=D.relations.filter(r=>r.a===id||r.b===id).map(r=>`<div class="source"><strong>${esc(byId[r.a].name)} → ${esc(byId[r.b].name)} · ${esc(levelNames[r.level])}${r.exception?' · wyjątek rodzinny':''}</strong><p>${esc(r.reason)}</p><p>Do wyższego poziomu: ${esc(r.missing)}</p><p>Źródła: ${esc(r.sources)}</p></div>`).join('');
 $('detail').insertAdjacentHTML('beforeend',`<h3>Ocena danych i połączenia</h3><p>Tożsamość źródłowa: ${esc(levelNames[p.identityLevel])}. Połączenie z rodziną: ${esc(levelNames[p.connectionLevel])}.</p><p>${esc(p.dataEvidence)}</p><p>${esc(p.classificationReason)}</p><p>Potrzebny dowód: ${esc(p.missing)}</p><h3>Relacje ocenione osobno</h3>${relationDetails}`);
 $('detail').querySelectorAll('[data-open]').forEach(b=>b.onclick=()=>openPerson(b.dataset.open));
 if(!$('person').open)$('person').showModal();location.hash='osoba-'+id;
 $('people').value=id;
 const pos=positions[id];$('viewport').scrollTo({left:Math.max(0,offsetX+(pos.x+120)*scale-$('viewport').clientWidth/2),top:Math.max(0,offsetY+(pos.y+70)*scale-$('viewport').clientHeight/2)});
}
function applySearch(){
 const q=normalize($('search').value);
 $('canvas').querySelectorAll('.node').forEach(b=>{const p=byId[b.dataset.id];b.style.opacity=!q||normalize(p.name+' '+p.role+' '+p.place+' '+(p.addresses||[]).map(a=>a.label).join(' ')).includes(q)?'1':'.25'});
}
function changeView(){if($('person').open)$('close').click();renderTree()}
function syncLevels(){document.querySelectorAll('#evidence [data-level]').forEach(b=>b.setAttribute('aria-pressed',String(Number(b.dataset.level)===selectedLevel)))}
document.querySelectorAll('#evidence [data-level]').forEach(b=>b.onclick=()=>{selectedLevel=Number(b.dataset.level);syncLevels();changeView()});
$('branch').onchange=changeView;
$('close').onclick=()=>{$('person').close();location.hash='drzewo'};
$('person').addEventListener('click',e=>{if(e.target===$('person'))$('close').click()});
$('people').onchange=e=>{if(e.target.value)openPerson(e.target.value)};
$('plus').onclick=()=>zoom(scale+.15);$('minus').onclick=()=>zoom(scale-.15);$('fit').onclick=fit;
$('search').oninput=applySearch;
$('search').onkeydown=e=>{if(e.key==='Enter'){e.preventDefault();const q=normalize(e.target.value),p=currentPeople.find(p=>normalize(p.name+' '+p.role+' '+p.place+' '+(p.addresses||[]).map(a=>a.label).join(' ')).includes(q));if(p)openPerson(p.id)}};
function renderNews(){
 const week=$('period').value==='week',cutoff=Date.now()-7*86400000;
 const news=D.news.filter(n=>!week||new Date(n.at).getTime()>=cutoff).sort((a,b)=>new Date(b.at)-new Date(a.at));
 $('news').innerHTML=news.length?news.map(n=>`<article class="entry"><time datetime="${esc(n.at)}">${dt(n.at)}</time><div><h3>${esc(n.title)}</h3><p>${esc(n.body)}</p></div></article>`).join(''):'<p class="empty">Brak nowych zapisów w ostatnich 7 dniach. Wybierz „Wszystkie”, aby zobaczyć wcześniejsze odkrycia.</p>';
}
$('period').onchange=renderNews;renderNews();renderTree();
const match=location.hash.match(/^#osoba-([PC]\d+)$/);if(match&&byId[match[1]])openPerson(match[1]);
