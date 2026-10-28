// ------------------------------------------------------------------ páginas propias
// /buscador, /medios(#slug), /autores(#nombre), /estadisticas(#año), /especiales(#slug), /novedades, /cronologia(#año)
var RUTA=(location.pathname.match(/\/(buscador|medios|autores|estadisticas|especiales|novedades|cronologia)(?:\.html)?\/?$/)||[])[1]||'';
var Y1=new Date().getFullYear(),TIPOS_ORD=['info','carto','port','ilus','foto','video','publi','online'];
var MES3=['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'];
function fcorta(d){return +d.slice(8,10)+' '+MES3[+d.slice(5,7)-1]+' '+d.slice(0,4);}
function crumbs(a){return '<div class="crumbs caps"><a href="/">Portada</a>'+a.map(function(x){return '<i>»</i>'+(x[1]?'<a href="'+x[1]+'">'+esc(x[0])+'</a>':'<span>'+esc(x[0])+'</span>');}).join('')+'</div>';}
function tituloP(p){return quita(TIT[p.i]||p.t||'')||'Entrada sin título';}
function contar(ps,f){var c={};ps.forEach(function(p){f(p).forEach(function(v){c[v]=(c[v]||0)+1;});});return Object.keys(c).sort(function(a,b){return c[b]-c[a];}).map(function(k){return [k,c[k]];});}
function cartaP(A,p,i){var meds=p.m.slice(0,2).map(function(j){return A.medios[j].n;}).join(' · '),auts=p.a.slice(0,3).map(function(j){return A.autores[j].n;});
 return '<a href="/post/'+esc(p.u)+'" class="card" data-k="'+p.k.join(' ')+'"><span class="tape" aria-hidden="true"></span>'+(p.k[0]?ico(p.k[0],'ico'):'')+
  '<div class="ph">'+(p.im?'<img loading="lazy" src="'+esc(p.im)+'" alt="" onerror="this.remove()">':'')+'</div><span class="caps">» '+esc(meds||(SECN[p.s]||''))+' · '+fcorta(p.d)+'</span>'+
  '<span class="tt">'+esc(tituloP(p))+'</span>'+(auts.length?'<span class="by">por '+esc(auts.join(', '))+(p.a.length>3?' y '+(p.a.length-3)+' más':'')+'</span>':'')+'</a>';}
function barrasAnios(ps){var c={},mx=1,h='',ax='';ps.forEach(function(p){var y=+p.d.slice(0,4);c[y]=(c[y]||0)+1;});
 for(var y=2011;y<=Y1;y++)mx=Math.max(mx,c[y]||0);var n=Y1-2010;
 for(y=2011;y<=Y1;y++){h+='<div class="bar real" style="height:'+Math.max(2,(c[y]||0)/mx*100)+'%" title="'+y+': '+(c[y]||0)+' entradas"><span>'+(c[y]||'')+'</span></div>';ax+='<span>'+String(y).slice(2)+'</span>';}
 return '<section class="years"><div class="caps" style="margin-bottom:14px">Entradas por año »</div><div class="chart" style="grid-template-columns:repeat('+n+',minmax(0,1fr))">'+h+'</div><div class="yax" style="grid-template-columns:repeat('+n+',minmax(0,1fr))">'+ax+'</div></section>';}
function entradas(A,ps){var ks=contar(ps,function(p){return p.k;}).slice(0,6);
 return '<section class="entries"><div class="fbar"><span class="caps" style="margin-right:6px">Todas las entradas »</span><button type="button" aria-pressed="true" data-f="">Todas · '+ps.length+'</button>'+
  ks.map(function(k){return '<button type="button" aria-pressed="false" data-f="'+k[0]+'">'+esc(TN[k[0]])+' · '+k[1]+'</button>';}).join('')+'</div><div class="grid" id="e-grid"></div><button type="button" class="more-btn" id="e-more">Cargar más »</button></section>';}
function activaEntradas(A,ps){var f='',n=0,g=document.getElementById('e-grid'),mb=document.getElementById('e-more');
 function lista(){return f?ps.filter(function(p){return p.k.indexOf(f)>=0;}):ps;}
 function mas(){var L=lista();var k=document.documentElement.classList.contains('lite')?6:24;g.insertAdjacentHTML('beforeend',L.slice(n,n+k).map(function(p,i){return cartaP(A,p,i);}).join(''));n+=k;mb.hidden=n>=L.length;}
 function reset(){g.innerHTML='';n=0;mas();}
 document.querySelector('.entries .fbar').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
  [].forEach.call(this.querySelectorAll('button'),function(x){x.setAttribute('aria-pressed',String(x===b));});f=b.dataset.f;reset();});
 mb.addEventListener('click',mas);reset();}
function tiposBanda(ps,q){var c={};ps.forEach(function(p){p.k.forEach(function(k){c[k]=(c[k]||0)+1;});});
 return '<div class="tipos">'+TIPOS_ORD.map(function(t){return '<a href="/buscador#'+q+'&k='+t+'"><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#i-'+t+'" class="k"/></svg><b>'+(c[t]||0)+'</b><span>'+esc(TN[t])+'</span></a>';}).join('')+'</div>';}
function fechasBanda(ps){if(!ps.length)return '';var a=ps[ps.length-1],b=ps[0];
 return '<div class="fl-dates"><span>Primera entrada en inconsolata»: <a href="/post/'+esc(a.u)+'">'+fcorta(a.d)+'</a></span><span>Última: <a href="/post/'+esc(b.u)+'">'+fcorta(b.d)+'</a></span></div>';}
function inicial(n){return '<span class="mdc-av ini" aria-hidden="true">'+esc((n||'?').replace(/^(the|el|la|le|les|los|las|il|die|der)\s+/i,'').charAt(0).toUpperCase())+'</span>';}

// ---------- medios
function medioIdx(A,cat){
 var y=String(Y1),L=A.medios.map(function(m,i){return {i:i,n:m.n,p:m.p,c:cat.medios[i]||{},y:0};});
 A.posts.forEach(function(p){if(p.d.slice(0,4)===y)p.m.forEach(function(i){L[i].y++;});});
 L=L.filter(function(o){return o.p>0;});
 var html=crumbs([['Medios']])+'<div class="idx-top"><div><h1 class="soft">Todos los <em>medios</em></h1><p>'+L.length+' medios han pasado por inconsolata» desde 2011. Los que tienen ficha llevan su logo; el resto te lleva a sus entradas en el buscador.</p></div>'+
  '<div class="idx-tools"><label class="sr" for="mq">Buscar medio</label><input id="mq" type="search" placeholder="Buscar medio…" autocomplete="off"><label class="sr" for="mo">Ordenar</label><select id="mo"><option value="p">Más entradas</option><option value="y">Más entradas en '+y+'</option><option value="n">A–Z</option></select>'+
  '<a class="btn-ink" href="/estadisticas">Estadísticas »</a></div></div><div class="mgrid" id="mgrid"></div>';
 return {html:'<div class="wrap">'+html+'</div>',init:function(){
  function pinta(){var q=fold(document.getElementById('mq').value.trim()),o=document.getElementById('mo').value;
   var R=L.filter(function(x){return !q||fold(x.n).indexOf(q)>=0;}).sort(function(a,b){return o==='n'?a.n.localeCompare(b.n,'es'):o==='y'?(b.y-a.y||b.p-a.p):b.p-a.p;});
   document.getElementById('mgrid').innerHTML=R.map(function(x){var f=x.c.ficha;return '<a class="mdc'+(f?'':' off')+'" href="'+(f?fichaMedio(x.c):'/buscador#m='+x.i)+'">'+(x.c.av?'<span class="mdc-av" aria-hidden="true"><img src="'+esc(x.c.av)+'" alt="" loading="lazy"></span>':inicial(x.n))+
    '<span class="mdc-n">'+esc(x.n)+'</span><span class="mdc-c"><b>'+x.p+'</b> entradas'+(x.y?' · '+x.y+' en '+y:'')+'</span></a>';}).join('');}
  document.getElementById('mq').addEventListener('input',pinta);document.getElementById('mo').addEventListener('change',pinta);pinta();}};}

// ---------- autores
function autorIdx(A){var L=A.autores.map(function(a,i){return {i:i,n:a.n,p:a.p,m:a.m||[],y:a.y||[]};}).filter(function(a){return a.p>0;});
 var html=crumbs([['Autores']])+'<div class="idx-top"><div><h1 class="soft">Los <em>autores</em></h1><p>'+L.length.toLocaleString('es-ES')+' periodistas, infografistas e ilustradores citados en el archivo. Busca por nombre o mira los más presentes.</p></div>'+
  '<div class="idx-tools"><label class="sr" for="aq">Buscar autor</label><input id="aq" type="search" placeholder="Buscar autor…" autocomplete="off"></div></div><div class="mgrid" id="agrid"></div>';
 return {html:'<div class="wrap">'+html+'</div>',init:function(){function pinta(){var q=fold(document.getElementById('aq').value.trim());
   var R=L.filter(function(a){return !q||fold(a.n).indexOf(q)>=0;}).sort(function(a,b){return b.p-a.p;}).slice(0,q?200:120);
   document.getElementById('agrid').innerHTML=R.map(function(a){return '<a class="mdc" href="'+fichaAutor(a.n)+'">'+inicial(a.n)+'<span class="mdc-n">'+esc(a.n)+'</span><span class="mdc-c"><b>'+a.p+'</b> entradas'+(a.m[0]?' · '+esc(a.m[0]):'')+'</span></a>';}).join('')||'<div class="vacio" style="grid-column:1/-1">No hay ningún autor con ese nombre.</div>';}
  document.getElementById('aq').addEventListener('input',pinta);pinta();}};}
// datos de Wikidata (en español) y resumen de la Wikipedia en español
var WD='https://www.wikidata.org/w/api.php?format=json&origin=*&action=wbgetentities&';
function cacheJ(k,f){try{var c=JSON.parse(sessionStorage.getItem(k)||'null');if(c)return Promise.resolve(c);}catch(e){}
 return f().then(function(j){try{sessionStorage.setItem(k,JSON.stringify(j));}catch(e){}return j;});}
function wikidata(q){return cacheJ('inc-wd-'+q,function(){
 return fetch(WD+'ids='+q+'&props=claims|sitelinks').then(function(r){return r.json();}).then(function(j){var e=j.entities[q],c=e.claims||{},o={};
  var it=function(p){return (c[p]||[]).filter(function(x){return x.rank!=='deprecated';}).map(function(x){var v=x.mainsnak.datavalue;return v&&v.value&&v.value.id;}).filter(Boolean);};
  var st=function(p){return (c[p]||[]).map(function(x){var v=x.mainsnak.datavalue;return v&&v.value;}).filter(function(v){return typeof v==='string';});};
  var ti=function(p){var v=(c[p]||[])[0];v=v&&v.mainsnak.datavalue;return v&&v.value.time?v.value.time.slice(1,5):'';};
  o.tipo=it('P31');o.fund=it('P112');o.sede=it('P159').slice(0,1);o.prop=it('P127').slice(0,2);o.idioma=it('P407').slice(0,2);o.formato=it('P3912').slice(0,1);
  o.anio=ti('P571');o.fin=ti('P576');o.web=st('P856')[0]||'';o.x=st('P2002')[0]||'';o.ig=st('P2003')[0]||'';o.bsky=st('P12361')[0]||'';o.issn=st('P236')[0]||'';
  o.es=(e.sitelinks&&e.sitelinks.eswiki||{}).title||'';
  var ids=[].concat(o.tipo,o.fund,o.sede,o.prop,o.idioma,o.formato);
  if(!ids.length)return o;
  return fetch(WD+'ids='+ids.slice(0,50).join('|')+'&props=labels&languages=es|en').then(function(r){return r.json();}).then(function(l){o.l={};
   Object.keys(l.entities||{}).forEach(function(k){var x=l.entities[k].labels||{};o.l[k]=(x.es||x.en||{}).value||'';});return o;});});});}
function resumenES(t){return cacheJ('inc-wp-'+t,function(){return fetch('https://es.wikipedia.org/api/rest_v1/page/summary/'+encodeURIComponent(t.replace(/ /g,'_'))).then(function(r){return r.json();}).then(function(j){return {x:j.extract||''};});});}
function corto(t,n){var s=(t||'').match(/[^.]+\.(\s|$)/g)||[t||''],r='';for(var i=0;i<s.length;i++){if(r&&(r+s[i]).length>n)break;r+=s[i];}r=r.trim();return r.length>n+60?r.slice(0,n).replace(/\s+\S*$/,'')+'…':r;}
var TIPO_ES={Q11032:'periódico',Q1110794:'diario',Q41298:'revista',Q1153191:'periódico digital',Q1002697:'periódico',Q2305295:'revista semanal',Q35127:'web',Q1047113:'revista especializada',Q685935:'revista'};
function bandera(cc){return cc?'<img class="flag" src="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/flags/4x3/'+esc(cc.toLowerCase())+'.svg" alt="" width="24" height="18">':'';}
// iconos de los enlaces de las fichas
var ICR={x:'<path fill="currentColor" d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"/>',
 bsky:'<path fill="currentColor" d="M12 10.8c-1.087-2.114-4.046-6.053-6.798-7.995C2.566.944 1.561 1.266.902 1.565.139 1.908 0 3.08 0 3.768c0 .69.378 5.65.624 6.479.815 2.736 3.713 3.66 6.383 3.364-3.912.58-7.387 2.005-2.83 7.078 5.013 5.19 6.87-1.113 7.823-4.308.953 3.195 2.05 9.271 7.733 4.308 4.267-4.308 1.172-6.498-2.74-7.078 2.67.297 5.568-.628 6.383-3.364.246-.828.624-5.79.624-6.478 0-.69-.139-1.861-.902-2.206-.659-.298-1.664-.62-4.3 1.24C16.046 4.748 13.087 8.687 12 10.8Z"/>',
 ig:'<rect x="2.5" y="2.5" width="19" height="19" rx="5.5" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="12" cy="12" r="4.4" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="17.6" cy="6.4" r="1.4" fill="currentColor"/>',
 li:'<rect x="2" y="2" width="20" height="20" rx="3" fill="currentColor"/><path fill="#fff" d="M6.2 9.6h2.6V18H6.2zM7.5 5.6a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3zM10.4 9.6h2.5v1.2c.4-.7 1.3-1.4 2.6-1.4 2.7 0 3.2 1.8 3.2 4.1V18h-2.6v-4c0-1 0-2.2-1.3-2.2s-1.6 1-1.6 2.1V18h-2.6z"/>',
 wiki:'<text x="12" y="17.5" text-anchor="middle" font-family="Georgia,serif" font-size="17" font-weight="700" fill="currentColor">W</text>',
 be:'<text x="12" y="17" text-anchor="middle" font-family="Archivo,Arial,sans-serif" font-size="13" font-weight="900" fill="currentColor">Bē</text>',
 web:'<circle cx="12" cy="12" r="9.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M2.5 12h19M12 2.5c3 3.2 3 15.8 0 19M12 2.5c-3 3.2-3 15.8 0 19" fill="none" stroke="currentColor" stroke-width="1.8"/>',
 bus:'<circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2.6"/><path d="M15.5 15.5l5.5 5.5" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/>',
 link:'<path d="M10 14a4.5 4.5 0 0 0 6.4 0l3.2-3.2a4.5 4.5 0 0 0-6.4-6.4L11.6 6M14 10a4.5 4.5 0 0 0-6.4 0l-3.2 3.2a4.5 4.5 0 0 0 6.4 6.4l1.6-1.6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>'};
function oficioG(t,g){t=t||'';if(g!=='autor'&&g!=='autora')return t;return t.replace(/([^\s\/]+?)(o)?\/a\b/g,function(m,a,o){return g==='autora'?a+'a':a+(o||'');});}
function boton(l,u){var k=l==='X'?'x':l==='Bluesky'?'bsky':l==='Instagram'?'ig':l==='LinkedIn'||/linkedin\./.test(u)?'li':l==='Wikipedia'?'wiki':/behance\./.test(u)?'be':l==='En el buscador'?'bus':l==='Web'?'web':'link';
 if(k==='be')l='Behance';if(k==='li')l='LinkedIn';var ext=/^https?:/.test(u);
 return '<a href="'+esc(u)+'"'+(ext?' target="_blank" rel="noopener"':'')+' class="red"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">'+ICR[k]+'</svg>'+esc(l)+'</a>';}
function redes(o){var L=[];(o.otros||'').split(/\n+/).forEach(function(u){u=u.trim();if(/^https?:/.test(u))L.push([u.replace(/^https?:\/\/(www\.)?/,'').split('/')[0],u]);});if(o.web)L.push(['Web',o.web]);if(o.x)L.push(['X','https://x.com/'+o.x.replace(/^@/,'')]);if(o.bsky)L.push(['Bluesky','https://bsky.app/profile/'+o.bsky.replace(/^@/,'')]);
 if(o.ig)L.push(['Instagram','https://instagram.com/'+o.ig.replace(/^@/,'')]);if(o.linkedin)L.push(['LinkedIn',o.linkedin]);return L;}

// ---------- extras de la ficha de medio: propiedad en árbol, formato dibujado y coronas
var PAISES_CC={'España':'es','Estados Unidos':'us','EEUU':'us','EE. UU.':'us','Reino Unido':'gb','Francia':'fr','Italia':'it','Alemania':'de','México':'mx','Argentina':'ar','Chile':'cl','Brasil':'br','China':'cn','Portugal':'pt','Bélgica':'be','Canadá':'ca','Omán':'om','Uruguay':'uy','Ciudad del Vaticano':'va','Vaticano':'va','Ecuador':'ec','Colombia':'co','Perú':'pe','Venezuela':'ve','Suiza':'ch','Países Bajos':'nl','Holanda':'nl','Austria':'at','Suecia':'se','Noruega':'no','Dinamarca':'dk','Finlandia':'fi','Irlanda':'ie','Polonia':'pl','Grecia':'gr','Rusia':'ru','Ucrania':'ua','Japón':'jp','Corea del Sur':'kr','India':'in','Australia':'au','Nueva Zelanda':'nz','Sudáfrica':'za','Israel':'il','Turquía':'tr','Catar':'qa','Qatar':'qa','Emiratos Árabes Unidos':'ae','Hong Kong':'hk','Singapur':'sg','Cuba':'cu','Luxemburgo':'lu','Hungría':'hu','República Checa':'cz','Egipto':'eg','Marruecos':'ma','Taiwán':'tw','Arabia Saudí':'sa','Mongolia':'mn','Andorra':'ad'};
// «PRISA (España)» y debajo, con guion o con %, los que la controlan: «- Amber Capital (Reino Unido, 29,9%)»
function arbolProp(t){
 var L=[];String(t||'').split(/\n+/).forEach(function(l){if(!l.trim())return;
  var nv=(l.match(/^\s*(-+|·+|>+)/)||[''])[0].replace(/\s/g,'').length;l=l.replace(/^\s*[-·>]+\s*/,'');
  // varias en una línea: «A (España), B (Francia, 20%)»
  (l.match(/[^,(]+(\([^)]*\))?/g)||[]).forEach(function(x){x=x.trim();if(x)L.push([nv,x]);});});
 var raiz=-1;L=L.map(function(it){var m=it[1].match(/^(.*?)\s*\(([^)]*)\)\s*$/),n=m?m[1]:it[1],dentro=m?m[2]:'',pm=dentro.match(/(\d+(?:[.,]\d+)?)\s*%/),pct=pm?pm[1]+'%':'',pais=dentro.replace(/(\d+(?:[.,]\d+)?)\s*%/,'').replace(/^[\s,;]+|[\s,;]+$/g,'');
  var nv=it[0];if(!nv&&pct&&raiz>=0)nv=1;if(!nv)raiz=1;return {n:n,pais:pais,pct:pct,nv:nv};});
 if(!L.length)return '';
 return '<ul class="prop">'+L.map(function(o){var cc=PAISES_CC[o.pais];return '<li class="nv'+Math.min(o.nv,3)+'">'+(o.nv?'<span class="rama" aria-hidden="true"></span>':'')+
  '<span class="pnom">'+(cc?bandera(cc):'')+esc(o.n)+(o.pais&&!cc?' <small>('+esc(o.pais)+')</small>':'')+'</span>'+
  (o.pct?'<span class="pct"><i style="width:'+Math.min(100,parseFloat(o.pct.replace(',','.'))||0)+'%"></i><b>'+esc(o.pct)+'</b></span>':'')+'</li>';}).join('')+'</ul>';}
// tamaños de página habituales (mm, ancho × alto)
var FORMATOS=[['sábana',380,600,/s[aá]bana|broadsheet|gran formato/i],['berlinés',315,470,/berlin/i],['tabloide',280,430,/tabloid|compact/i],['revista (A4)',210,297,/revista|a4|magazine/i]];
function formatoSVG(t,nom){t=t||'';var k=FORMATOS.findIndex(function(f){return f[3].test(t);}),m=t.match(/(\d+(?:[.,]\d+)?)\s*[x×]\s*(\d+(?:[.,]\d+)?)/i),dim=null;
 if(m){var a=parseFloat(m[1].replace(',','.')),b=parseFloat(m[2].replace(',','.'));if(a<100&&b<100){a*=10;b*=10;}dim=[Math.round(Math.min(a,b)),Math.round(Math.max(a,b))];}
 if(k<0&&!dim)return '';var S=.2,W=Math.max(FORMATOS[0][1],dim?dim[0]:0)*S+20,H=Math.max(FORMATOS[0][2],dim?dim[1]:0)*S+20,h='';
 FORMATOS.slice().reverse().forEach(function(f,i){var w=f[1]*S,hh=f[2]*S;h+='<rect x="10" y="'+(H-10-hh)+'" width="'+w+'" height="'+hh+'"/>';});
 var sel=dim||[FORMATOS[k][1],FORMATOS[k][2]];h+='<rect class="on" x="10" y="'+(H-10-sel[1]*S)+'" width="'+sel[0]*S+'" height="'+sel[1]*S+'"/>';
 return '<span class="fmt"><svg viewBox="0 0 '+W+' '+H+'" width="'+W+'" height="'+H+'" role="img" aria-label="Página de '+sel[0]+' por '+sel[1]+' milímetros comparada con otros formatos">'+h+'</svg><small>'+(nom?'<em>'+esc(nom)+'</em>':'')+'<b>'+(sel[0]/10)+' × '+(sel[1]/10)+' cm'+'</b><br>'+FORMATOS.map(function(f,i){return '<i class="'+(i===k?'on':'')+'">'+f[0]+'</i>';}).join('<span class="sep"> · </span>')+'</small></span>';}
// coronas: años en que el medio fue el 1.º, 2.º o 3.º más presente
function coronas(ST,n){if(!ST||!ST.years)return '';var y1=String(new Date().getFullYear()),out=[];
 Object.keys(ST.years).sort().forEach(function(y){var L=ST.years[y].medios||[];for(var i=0;i<3&&i<L.length;i++)if(L[i][0]===n)out.push([y,i]);});
 if(!out.length)return '';var C=['oro','plata','bronce'],T=['1.º','2.º','3.º'];
 return '<div class="coronas">'+out.map(function(o){var tx=T[o[1]]+' medio más presente en inconsolata» en '+o[0]+(o[0]===y1?' (provisional: el año no ha terminado)':'');return '<span class="cor '+C[o[1]]+(o[0]===y1?' prov':'')+'" tabindex="0" aria-label="'+tx+'" data-tip="'+tx+'"><svg viewBox="0 0 64 44" aria-hidden="true"><path d="M4 40 L2 8 L18 22 L32 2 L46 22 L62 8 L60 40 Z"/></svg><b>'+o[0]+'</b></span>';}).join('')+'</div>';}

function medioFicha(A,cat,FM,mi,ST){
 var m=A.medios[mi],c=cat.medios[mi]||{},f=FM[m.n]||{},ps=A.posts.filter(function(p){return p.m.indexOf(mi)>=0;});
 document.title=m.n+' · inconsolata»';
 var auts=contar(ps,function(p){return p.a.filter(function(a){return (A.autores[a].m||[]).indexOf(m.n)>=0;});}).slice(0,8);
 var fund=+f.fundacion||0,cierre=+f.cierre||0;
 var tieneFmt=!!(f.formato),vis=(c.logo||tieneFmt)?'<div class="fvis">'+(c.logo?'<div class="logo-big logo-wk"><img src="'+esc(c.logo)+'" alt="Logo de '+esc(m.n)+'" onerror="var v=this.closest(\'.fvis\');this.closest(\'.logo-big\').remove();if(!v.querySelector(\'.fmt-box *\')){v.closest(\'.fhero\').classList.add(\'novis\');v.remove();}"></div>':'')+'<div class="fmt-box" id="m-fmt"></div></div>':'';
 var big2=fund?'<div class="stat"><b>'+((cierre||Y1)-fund)+'</b><span>'+(cierre?'años publicándose · de '+fund+' a '+cierre:'años publicándose · desde '+fund)+'</span></div>':
  '<div class="stat"><b>'+(new Set(ps.map(function(p){return p.d.slice(0,4);})).size)+'</b><span>años apareciendo en inconsolata»</span></div>';
 var html=crumbs([['Medios','/medios'],[m.n]])+'<section class="fhero'+(vis?'':' novis')+'">'+vis+'<div class="finfo"><span class="caps ante" style="color:var(--accent)">Medio » '+bandera(f.cc)+esc(f.pais||'')+'<span id="m-tipo"></span>'+(f.desaparecido||cierre?' · ya no se publica':'')+'</span>'+
  '<h1 class="soft">'+esc(m.n)+'</h1>'+
  '<div class="wk" id="wk"><div class="wk-h"><span class="caps">Datos »</span><a class="wk-src" id="wk-src" href="'+esc(f.wikipedia||'#')+'" target="_blank" rel="noopener"'+(f.wikipedia?'':' hidden')+'>Fuente: Wikidata y Wikipedia · CC BY-SA »</a></div>'+
  '<div class="wk-top">'+(c.av?'<span class="av-slot" aria-hidden="true"><img src="'+esc(c.av)+'" alt=""></span>':'')+'<p class="wk-r'+(f.nota?' propio':'')+'" id="wk-r"'+(f.nota?'':' hidden')+'>'+esc(f.nota||'')+'</p></div><dl id="wk-dl"></dl></div>'+
  '<div class="flinks" id="m-links"></div></div></section>';
 function datos(o){o=o||{};var lab=function(ids){return (ids||[]).map(function(i){return (o.l||{})[i];}).filter(Boolean);};
  var tipo=f.tipo||(o.tipo||[]).map(function(i){return TIPO_ES[i]||(o.l||{})[i];}).filter(Boolean)[0]||'';if(tipo)document.getElementById('m-tipo').textContent=' · '+tipo;
  var d=[],anio=f.fundacion||o.anio,fin=f.cierre||o.fin;
  if(anio)d.push(['Fundación',anio+(fin?' · cierre en '+fin:'')]);var fu=f.fundador?[f.fundador]:lab(o.fund);if(fu.length)d.push([fu.length>1?'Fundadores':'Fundador',fu.slice(0,3).join(', ')]);
  var se=f.sede?[f.sede]:lab(o.sede);if(se.length)d.push(['Sede',se[0]]);var pr=f.propietario?[f.propietario]:lab(o.prop);if(pr.length)d.push(['Propietario',f.propietario?arbolProp(f.propietario):esc(pr.join(', ')),1]);if(f.director)d.push(['Dirección',esc(f.director)+(f.director_desde?' <small class="dd">'+esc(f.director_desde)+'</small>':''),1]);
  var fo=f.formato?[f.formato]:lab(o.formato);var fb=document.getElementById('m-fmt');if(fo.length){var fn=fo[0].replace(/\s*\([^)]*\)/g,'').trim();if(fb)fb.innerHTML='<span class="caps">Formato »</span>'+(formatoSVG(fo[0],fn)||'<b>'+esc(fn)+'</b>');else d.push(['Formato',esc(fn)+formatoSVG(fo[0]),1]);}var id=f.idioma?[f.idioma]:lab(o.idioma);if(id.length)d.push(['Idioma',id.join(', ')]);
  if(f.pais)d.push(['País',f.pais]);if(o.issn)d.push(['ISSN',o.issn]);
  var web=f.web||o.web;if(web)d.push(['Web','<a href="'+esc(web)+'" target="_blank" rel="noopener">'+esc(web.replace(/^https?:\/\/(www\.)?/,'').replace(/\/$/,''))+'</a>']);
  d.sort(function(a,b){return (a[0]==='Propietario'||a[0]==='Formato')-(b[0]==='Propietario'||b[0]==='Formato');});
  document.getElementById('wk-dl').innerHTML=d.map(function(x){return '<div'+(x[0]==='Propietario'||x[0]==='Formato'?' class="ancho"':'')+'><dt>'+x[0]+'</dt><dd>'+(x[0]==='Web'||x[2]?x[1]:esc(x[1]))+'</dd></div>';}).join('');
  var L=redes({web:web,x:f.x||o.x,bsky:f.bsky||o.bsky,ig:f.ig||o.ig});var wp=o.es?'https://es.wikipedia.org/wiki/'+encodeURIComponent(o.es.replace(/ /g,'_')):(f.wikipedia&&/\/\/es\./.test(f.wikipedia)?f.wikipedia:'');
  if(wp)L.push(['Wikipedia',wp]);
  document.getElementById('m-links').innerHTML=L.map(function(x){return boton(x[0],x[1]);}).join('')+boton('En el buscador','/buscador#m='+mi);
  if(wp){var s=document.getElementById('wk-src');s.href=wp;s.hidden=false;}
  if(!d.length&&!wp)document.getElementById('wk').hidden=true;
  var t=o.es||(f.wikipedia&&/\/\/es\./.test(f.wikipedia)?decodeURIComponent(f.wikipedia.split('/wiki/')[1]||'').replace(/_/g,' '):'');
  if(t&&!f.nota)resumenES(t).then(function(j){var r=document.getElementById('wk-r');if(r&&j.x){r.textContent=corto(j.x,200);r.hidden=false;}}).catch(function(){});}
 return {html:'<div class="wrap">'+html+'</div><section class="band">'+(c.avw?'<img class="wm-av" src="'+esc(c.avw)+'" alt="" aria-hidden="true">':'')+'<div class="wrap in">'+
  '<div class="stat"><b>'+ps.length+'</b><span>entradas en inconsolata»</span>'+coronas(ST,m.n)+'</div>'+big2+
  (auts.length?'<div class="stat"><span>Autores más citados</span><ol class="tops">'+auts.map(function(a){return '<li><a href="'+fichaAutor(A.autores[a[0]].n)+'">'+esc(A.autores[a[0]].n)+'<small>'+a[1]+'</small></a></li>';}).join('')+'</ol></div>':'')+
  '<div class="stat" style="grid-column:1/-1"><span>Tipos de pieza</span>'+tiposBanda(ps,'m='+mi)+fechasBanda(ps)+'</div></div></section>'+
  '<div class="wrap">'+barrasAnios(ps)+entradas(A,ps)+'</div>',
  init:function(){activaEntradas(A,ps);datos(null);if(f.qid)wikidata(f.qid).then(datos).catch(function(){});}};}

function chipMedio(cat,n){var c=cat.medios.find(function(x){return x.n===n;}),i=cat.medios.indexOf(c);
 return '<a class="ch-av" href="'+(c&&c.ficha?fichaMedio(c):'/buscador#m='+i)+'">'+(c&&c.avw?'<img src="'+esc(c.avw)+'" alt="">':'')+esc(n)+'</a>';}
function autorFicha(A,cat,FM,AX,ai){var a=A.autores[ai],ps=A.posts.filter(function(p){return p.a.indexOf(ai)>=0;}),x=AX[a.n]||{};
 document.title=a.n+' · inconsolata»';
 var md=x.medio||(a.m||[])[0],mc=md?cat.medios.find(function(m){return m.n===md;}):null,fm=FM[md]||{};
 var pais=x.pais||fm.pais||'',cc=x.cc||fm.cc||'';
 var otros=md?A.autores.map(function(o,i){return {i:i,n:o.n,p:o.p,m:o.m||[]};}).filter(function(o){return o.i!==ai&&o.m.indexOf(md)>=0&&o.p>0;}).sort(function(p,q){return q.p-p.p;}).slice(0,8):[];
 var ys=ps.map(function(p){return +p.d.slice(0,4);}),y0=Math.min.apply(null,ys),y1=Math.max.apply(null,ys),ny=new Set(ys).size;
 var W=ps.filter(function(p){return p.im&&p.a.length<=6;}).slice().reverse();
 var vis=W.length?'<div class="fvis"><figure class="work"><span class="tape" aria-hidden="true"></span><a class="wph" id="work-a" href="#" aria-label="Abrir esta pieza en inconsolata»"><img id="work-img" alt="" src=""></a>'+
  (W.length>1?'<button type="button" class="wnext" id="work-next" aria-label="Ver otra pieza al azar"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M4 7h11l-3-3M20 17H9l3 3M15 4l3 3-3 3M9 20l-3-3 3-3" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg><span>otra</span></button>':'')+
  '<figcaption><span class="wn">Pieza <b id="work-n"></b> de <b>'+W.length+'</b> en el archivo</span><span class="wm" id="work-m"></span></figcaption></figure></div>':'';
 var L=redes(x);
 var html='<div class="wrap">'+crumbs([['Autores','/autores'],[a.n]])+'<section class="fhero'+(vis?'':' novis')+'">'+vis+'<div class="finfo"><span class="caps ante" style="color:var(--accent)">'+(x.genero==='autora'?'Autora':x.genero==='autor'?'Autor':'Periodista')+(a.m&&a.m.length?' » '+esc(a.m.slice(0,3).join(' · ')):'')+'</span>'+
  '<div class="name-row"><h1 class="soft autor">'+esc(a.n)+'</h1>'+(mc?'<a class="av-medio" href="'+fichaMedio(mc)+'" aria-label="Trabaja en '+esc(md)+'">'+(mc.av?'<span class="av-slot" aria-hidden="true"><img src="'+esc(mc.av)+'" alt=""></span>':'')+'<span>'+esc(md)+' »</span></a>':'')+'</div>'+(pais||x.oficio?'<p class="nac">'+bandera(cc)+'<span>'+esc(pais)+(pais&&x.oficio?' · ':'')+esc(oficioG(x.oficio,x.genero))+'</span></p>':'')+
  (x.texto?'<div class="ftext">'+esc(x.texto)+'</div>':'')+
  '<div class="flinks">'+L.map(function(l){return boton(l[0],l[1]);}).join('')+boton('En el buscador','/buscador#a='+ai)+'</div></div></section></div>'+
  '<section class="band"><div class="wrap in"><div class="stat"><b>'+ps.length+'</b><span>entradas en inconsolata»</span></div>'+
  '<div class="stat"><b>'+ny+'</b><span>años apareciendo en inconsolata» · de '+y0+' a '+y1+'</span></div>'+
  (a.m&&a.m.length?'<div class="stat"><span>Medios</span><div class="chips">'+a.m.map(function(n){return chipMedio(cat,n);}).join('')+'</div></div>':'')+
  (otros.length?'<div class="stat"><span>Otros autores de '+esc(md)+'</span><ol class="tops">'+otros.map(function(o){return '<li><a href="'+fichaAutor(o.n)+'">'+esc(o.n)+'<small>'+o.p+'</small></a></li>';}).join('')+'</ol></div>':'')+
  '<div class="stat" style="grid-column:1/-1"><span>Tipos de pieza</span>'+tiposBanda(ps,'a='+ai)+fechasBanda(ps)+'</div></div></section>'+
  '<div class="wrap">'+barrasAnios(ps)+entradas(A,ps)+'</div>';
 return {html:html,init:function(){activaEntradas(A,ps);if(!W.length)return;var i=Math.floor(Math.random()*W.length);
  function show(){var w=W[i%W.length];document.getElementById('work-a').href='/post/'+w.u;document.getElementById('work-img').setAttribute('s'+'rc',w.im);
   document.getElementById('work-n').textContent=(i%W.length)+1;document.getElementById('work-m').textContent='» '+w.m.slice(0,2).map(function(j){return A.medios[j].n;}).join(', ')+' · '+fcorta(w.d);}
  show();var nb=document.getElementById('work-next');if(nb)nb.addEventListener('click',function(){i+=1+Math.floor(Math.random()*(W.length-1));show();});}};}

// ---------- especiales
function rangoE(a,b){var f=function(d,y){return +d.slice(8,10)+' de '+MESES[+d.slice(5,7)-1]+(y?' de '+d.slice(0,4):'');};
 return a===b?f(a,1):a.slice(0,4)===b.slice(0,4)?'del '+f(a,0)+' al '+f(b,1):'del '+f(a,1)+' al '+f(b,1);}
function icoE(cat,e){var ti=cat.temas.findIndex(function(t){return t.n===e.tema;});if(ti<0)ti=cat.temas.findIndex(function(t){return t.n===e.padre;});return ti>=0?TS[ti]:'';}
function espIdx(ES,cat){
 var top=ES.filter(function(e){return !e.cap_de;}),by={};ES.forEach(function(e){by[e.slug]=e;});
 var g={};top.forEach(function(e){(g[e.padre]=g[e.padre]||[]).push(e);});
 var orden=cat.temas.map(function(t){return t.n;}).filter(function(n){return g[n];});
 var html=crumbs([['Especiales']])+'<div class="idx-top"><div><h1 class="soft">Los <em>especiales</em></h1><p>'+top.length+' acontecimientos e historias con página propia, cada uno dentro de su tema. Algunos se dividen en capítulos.</p></div></div><div class="esp-idx">'+
  orden.map(function(t){var ti=cat.temas.findIndex(function(x){return x.n===t;});return '<div class="esp-g"><h2><a href="/buscador#h='+ti+'">'+esc(t)+' »</a></h2><div class="esp-l">'+g[t].sort(function(a,b){return (b.hasta||'').localeCompare(a.hasta||'');}).map(function(e){var ic=icoE(cat,e);
   return '<div class="esp-i"><a class="esp-a" href="/especiales#'+esc(e.slug)+'">'+(ic?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+ic+'"/></svg>':'')+'<span>'+esc(e.titulo)+'</span><small>'+e.posts.length+'</small></a>'+
    ((e.capitulos||[]).length?'<span class="esp-caps">'+e.capitulos.map(function(c){return by[c];}).filter(Boolean).sort(function(a,b){return (a.desde||'').localeCompare(b.desde||'');}).map(function(c){return '<a href="/especiales#'+esc(c.slug)+'">'+esc(c.titulo)+'</a>';}).join('')+'</span>':'')+'</div>';}).join('')+'</div></div>';}).join('')+'</div>';
 return {html:'<div class="wrap">'+html+'</div>',init:function(){}};}
function espPag(A,cat,ES,x){var byId={},by={};A.posts.forEach(function(p){byId[p.i]=p;});ES.forEach(function(e){by[e.slug]=e;});
 var ps=x.posts.map(function(i){return byId[i];}).filter(Boolean).sort(function(a,b){return b.d.localeCompare(a.d);});
 document.title=x.titulo+' · especial · inconsolata»';
 var pi=cat.temas.findIndex(function(t){return t.n===x.padre;}),ic=icoE(cat,x),madre=x.cap_de?by[x.cap_de]:null;
 var carta=function(p){var meds=p.m.slice(0,2).map(function(i){return A.medios[i].n;}).join(' · '),auts=p.a.slice(0,3).map(function(i){return A.autores[i].n;});
  return '<a class="ec" href="/post/'+esc(p.u)+'"><div class="ph">'+(p.im?'<img loading="lazy" src="'+esc(p.im)+'" alt="" onerror="this.remove()">':'')+(p.s?'<span class="sec">'+esc(SECN[p.s])+'</span>':'')+
   '<span class="ico">'+p.k.slice(0,3).map(function(k){return '<span title="'+esc(TN[k])+'"><svg viewBox="0 0 64 64" aria-hidden="true" style="overflow:visible"><use href="#i-'+k+'"/></svg></span>';}).join('')+'</span></div>'+
   '<span class="meta"><b>'+(+p.d.slice(8,10))+' '+MES3[+p.d.slice(5,7)-1]+'</b>'+(meds?' · '+esc(meds):'')+'</span><span class="tt">'+esc(tituloP(p))+'</span>'+(auts.length?'<span class="by">por '+esc(auts.join(', '))+'</span>':'')+'</a>';};
 var meses=function(L){var gr={};L.forEach(function(p){(gr[p.d.slice(0,7)]=gr[p.d.slice(0,7)]||[]).push(p);});
  return Object.keys(gr).map(function(k){var v=gr[k];return '<section class="mo"><h3>'+MESES[+k.slice(5,7)-1].replace(/^./,function(c){return c.toUpperCase();})+'<small>'+k.slice(0,4)+' · '+v.length+' '+(v.length===1?'entrada':'entradas')+'</small></h3><div class="g">'+v.map(carta).join('')+'</div></section>';}).join('');};
 var caps=(x.capitulos||[]).map(function(c){return by[c];}).filter(Boolean).sort(function(a,b){return (b.hasta||'').localeCompare(a.hasta||'');}),tl='';
 if(caps.length){var usados={};
  tl=caps.map(function(c){var L=c.posts.map(function(i){return byId[i];}).filter(Boolean).sort(function(a,b){return b.d.localeCompare(a.d);});L.forEach(function(p){usados[p.i]=1;});
   return '<div class="cap"><div class="cap-h"><h2 class="soft"><a href="/especiales#'+esc(c.slug)+'">'+esc(c.titulo)+'</a></h2><span>'+L.length+' '+(L.length===1?'entrada':'entradas')+(c.desde?' · '+rangoE(c.desde,c.hasta||c.desde):'')+'</span></div>'+meses(L)+'</div>';}).join('');
  var resto=ps.filter(function(p){return !usados[p.i];});
  if(resto.length)tl+='<div class="cap"><div class="cap-h"><h2 class="soft">Otras entradas</h2><span>'+resto.length+' '+(resto.length===1?'entrada':'entradas')+'</span></div>'+meses(resto)+'</div>';}
 else tl=meses(ps);
 var cm=contar(ps,function(p){return p.m;}).slice(0,12),ca=contar(ps,function(p){return p.a;}).slice(0,12);
 var her=ES.filter(function(y){return !y.cap_de&&y.padre===x.padre&&y!==x&&y!==madre;});
 var cr=[['Especiales','/especiales']];if(madre)cr.push([madre.titulo,'/especiales#'+madre.slug]);cr.push([x.titulo]);
 var html='<div class="wrap">'+crumbs(cr)+'</div><section class="eh"><div class="wrap in"><div><span class="kick">'+(madre?'Capítulo de «'+esc(madre.titulo)+'» »':'Especial »')+'</span><h1 class="soft">'+esc(x.titulo)+'</h1><div class="meta"><span>'+ps.length+' '+(ps.length===1?'entrada':'entradas')+'</span>'+(x.desde?'<span>'+rangoE(x.desde,x.hasta||x.desde)+'</span>':'')+
  (caps.length?'<span>'+caps.length+' capítulos</span>':'')+(pi>=0?'<span>Dentro de: <a href="/buscador#h='+pi+'">'+esc(x.padre)+' »</a></span>':'')+'</div></div>'+(ic?'<svg class="big" viewBox="0 0 64 64" aria-hidden="true"><use href="#'+ic+'" class="k"/><use href="#'+ic+'" class="m" x="3" y="2.5"/></svg>':'')+'</div></section>'+
  '<div class="wrap">'+(x.texto?'<div class="etext">'+esc(x.texto)+'</div>':'')+
  (caps.length?'<nav class="caps-nav" aria-label="Capítulos"><span class="caps">Capítulos »</span>'+caps.map(function(c){return '<a href="/especiales#'+esc(c.slug)+'">'+esc(c.titulo)+'<small>'+c.posts.length+'</small></a>';}).join('')+'</nav>':'')+
  '<div class="who"><div><h2>Medios</h2><div class="chips">'+cm.map(function(c){var m=cat.medios[c[0]];return '<a href="'+(m&&m.ficha?fichaMedio(m):'/buscador#m='+c[0])+'">'+esc(A.medios[c[0]].n)+'<small>'+c[1]+'</small></a>';}).join('')+'</div></div>'+
  '<div><h2>Autores</h2><div class="chips">'+(ca.map(function(c){return '<a href="'+fichaAutor(A.autores[c[0]].n)+'">'+esc(A.autores[c[0]].n)+'<small>'+c[1]+'</small></a>';}).join('')||'<span style="font-size:14px;color:var(--muted)">Sin autores identificados</span>')+'</div></div></div>'+
  '<div class="tl-bar"><h2 class="soft">La cobertura, <em>'+(caps.length?'capítulo a capítulo':'mes a mes')+'</em></h2><button type="button" id="order" aria-pressed="true">Ver en orden cronológico »</button></div><div class="tl" id="tl">'+tl+'</div>'+
  (her.length?'<section class="others"><h2>Otros especiales de '+esc(x.padre)+'</h2><div class="chips">'+her.map(function(y){var i2=icoE(cat,y);return '<a href="/especiales#'+esc(y.slug)+'">'+(i2?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+i2+'"/></svg>':'')+esc(y.titulo)+'<small>'+y.posts.length+'</small></a>';}).join('')+'</div></section>':'')+
  '<p style="margin:56px 0 0"><a class="btn-ink todos" href="/especiales">Todos los especiales »</a></p></div>';
 return {html:html,init:function(){document.getElementById('order').addEventListener('click',function(){var tl=document.getElementById('tl'),b=this,rev=b.getAttribute('aria-pressed')!=='true';
  var rv=function(box,sel){[].slice.call(box.querySelectorAll(sel)).reverse().forEach(function(c){box.appendChild(c);});};
  rv(tl,':scope>.cap');rv(tl,':scope>.mo');[].forEach.call(tl.querySelectorAll('.cap'),function(c){rv(c,':scope>.mo');});[].forEach.call(tl.querySelectorAll('.g'),function(g){rv(g,':scope>*');});
  b.setAttribute('aria-pressed',rev);b.textContent=rev?'Ver en orden cronológico »':'Ver lo más reciente primero »';});}};}

// ---------- novedades
function novPag(A,cat){var L=((A&&A.ligeros)||[]).slice().sort(function(a,b){return (b.f||'').localeCompare(a.f||'');});
 var html='<div class="wrap">'+crumbs([['Novedades de la web']])+'<div class="nov-top"><h1 class="soft">Novedades <em>de la web</em></h1><p>Mejoras, arreglos y cosas nuevas de inconsolata», de la más reciente a la más antigua.</p></div>'+
  '<ul class="nov-list">'+(L.map(function(a){var ti=a.ico?cat.temas.findIndex(function(t){return t.n===a.ico;}):-1,sy=ti>=0?TS[ti]:a.ico;
   return '<li><span class="f">'+(a.f?(+a.f.slice(8))+' '+MES3[+a.f.slice(5,7)-1]+'<small>'+a.f.slice(0,4)+'</small>':'')+'</span><span class="ic'+(sy?'':' bl')+'">'+(sy?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+esc(sy)+'"/></svg>':'»')+'</span>'+
    (a.u?'<a class="t" href="'+esc(a.u)+'">'+esc(a.t)+'</a>':'<span class="t">'+esc(a.t)+'</span>')+'</li>';}).join('')||'<li><span class="t">Todavía no hay novedades.</span></li>')+'</ul></div>';
 if(L[0])ls('inc-novedades-visto',L[0].f||'');
 return {html:html,init:function(){}};}

// ---------- cronología: una tira horizontal con 15 años de la web
function cronoPag(A,cat,ES,CR){
 document.title='Cronología · inconsolata»';
 var byId={},by={};A.posts.forEach(function(p){byId[p.i]=p;});ES.forEach(function(e){by[e.slug]=e;});
 var DIA=2.6,PAD=420,FIN=200,t0=new Date(A.posts.reduce(function(m,p){return p.d<m?p.d:m;},'9999').slice(0,4)+'-01-01T12:00:00').getTime(),hoy=new Date().toISOString().slice(0,10);
 var X=function(d){return PAD+Math.round((new Date(d+'T12:00:00').getTime()-t0)/864e5*DIA);},W=X(hoy)+FIN;
 var fd=function(d){return (+d.slice(8,10))+' '+MES3[+d.slice(5,7)-1]+' '+d.slice(0,4);};
 var KIT={noticia:'Noticia',pieza:'Pieza',web:'La web',cobertura:'Cobertura'};
 // hitos puntuales
 var pts=[],barras=[],hilos=[];
 (CR.hitos||[]).forEach(function(h){
  if(h.esp){var e=by[h.esp];if(!e)return;
   // el tramo vivo del especial: del 10 % al 90 % de sus entradas (los aniversarios sueltos no alargan la barra)
   var ds=e.posts.map(function(i){return byId[i]&&byId[i].d;}).filter(Boolean).sort(),q=function(f){return ds[Math.min(ds.length-1,Math.floor(f*(ds.length-1)))];};
   var a=h.desde||(ds.length>4?q(.1):e.desde),b=h.hasta||(ds.length>4?q(.9):e.hasta)||a,dias=(new Date(b)-new Date(a))/864e5;
   (dias>300&&ds.length>=20?hilos:barras).push({e:e,a:a,b:b,t:h.t||e.titulo,n:e.posts.length,ic:icoE(cat,e),u:'/especiales#'+e.slug});return;}
  var p=h.id?byId[h.id]:null,d=h.d||(p&&p.d);if(!d)return;
  pts.push({tipo:h.tipo||'pieza',d:d,t:h.t||(p?tituloP(p):''),u:h.u||(p?'/post/'+p.u:'#'),im:h.img||(p&&p.im)||'',nota:h.nota||'',m:p?p.m.slice(0,2).map(function(i){return A.medios[i].n;}).join(' · '):''});});
 pts.sort(function(a,b){return a.d.localeCompare(b.d);});
 // carriles: cada pieza en el primero que esté libre
 function carriles(L,ancho,max){var fin=[];L.forEach(function(o){var x=o.x,w=ancho(o),k=-1;for(var i=0;i<fin.length;i++)if(fin[i]<=x){k=i;break;}
   if(k<0){if(fin.length<max){k=fin.length;fin.push(0);}else{k=0;for(var j=1;j<fin.length;j++)if(fin[j]<fin[k])k=j;}}o.lane=k;o.xc=Math.max(x,fin[k]);fin[k]=o.xc+w;});return Math.max(1,fin.length);}
 pts.forEach(function(o){o.x=X(o.d);});var CW=170,LH=168,nl=carriles(pts,function(){return CW+16;},3);
 var SP=nl*LH+40;
 barras.sort(function(a,b){return a.a.localeCompare(b.a);});barras.forEach(function(o){o.x=X(o.a);o.w=Math.min(Math.max(X(o.b)-o.x,14),Math.round(180*DIA));o.lw=Math.max(o.w,o.t.length*7.4+58);});
 var nb=carriles(barras,function(o){return o.lw+12;},4);
 hilos.sort(function(a,b){return a.a.localeCompare(b.a);});hilos.forEach(function(o){o.x=X(o.a);o.w=X(o.b)-o.x;});
 var nh=carriles(hilos,function(o){return Math.max(o.w,o.t.length*8.5+70)+24;},7);
 var yB=SP+70,yH=yB+nb*36+40,H=yH+nh*26+24;
 // actividad semanal
 var sem={},mx=1;A.posts.forEach(function(p){var k=Math.floor((X(p.d)-PAD)/(7*DIA));sem[k]=(sem[k]||0)+1;if(sem[k]>mx)mx=sem[k];});
 var act=Object.keys(sem).map(function(k){var v=sem[k];return '<i style="left:'+(PAD+k*7*DIA)+'px;height:'+Math.round(v/mx*34)+'px"></i>';}).join('');
 var y0=+A.posts.reduce(function(m,p){return p.d<m?p.d:m;},'9999').slice(0,4),anios=[];for(var y=y0;y<=+hoy.slice(0,4);y++)anios.push(y);
 var marcas=anios.map(function(y){var x=X(y+'-01-01');return '<div class="cr-y" style="left:'+x+'px" id="cr-'+y+'"><span class="big soft" aria-hidden="true">'+y+'</span><b>'+y+'</b></div>'+
   MES3.map(function(m,i){if(!i)return '';var xm=X(y+'-'+String(i+1).padStart(2,'0')+'-01');return xm<W-FIN?'<span class="cr-m" style="left:'+xm+'px">'+m+'</span>':'';}).join('');}).join('');
 var cartas=pts.map(function(o,i){var top=o.lane*LH+20,alto=SP-top-118;
  var dx=o.x-o.xc;
  return '<div class="cr-p t-'+o.tipo+'" style="left:'+(o.xc-10)+'px;top:'+top+'px"><a class="cr-c" href="'+esc(o.u)+'">'+(o.im?'<span class="ph"><img loading="lazy" src="'+esc(o.im)+'" alt="" onerror="this.parentNode.remove()"></span>':'')+
   '<span class="k">'+KIT[o.tipo]+' »</span><span class="f">'+fd(o.d)+'</span><span class="tt">'+destaca(o.t)+'</span>'+(o.nota?'<span class="nt">'+esc(o.nota)+'</span>':'')+'</a>'+
   (dx<-2?'<i class="ld" style="top:'+(SP-top-30)+'px;height:30px;left:'+(10+dx)+'px"></i>':'<i class="ld" style="height:'+(SP-top)+'px"></i>')+(dx<-2?'<i class="ld-h" style="left:'+(10+dx)+'px;width:'+(-dx)+'px;top:'+(SP-top-30)+'px"></i><i class="ld-v" style="top:40px;height:'+(SP-top-70)+'px"></i>':'')+'</div>';}).join('');
 var bs=barras.map(function(o){return '<a class="cr-b" href="'+esc(o.u)+'" style="left:'+o.x+'px;top:'+(yB+o.lane*36)+'px" title="'+esc(o.t)+' · '+o.n+' entradas · '+fd(o.a)+(o.b!==o.a?' – '+fd(o.b):'')+'"><i style="width:'+o.w+'px"></i>'+
   (o.ic?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+o.ic+'"/></svg>':'')+'<span>'+esc(o.t)+'</span></a>';}).join('');
 var hs=hilos.map(function(o){return '<a class="cr-h" href="'+esc(o.u)+'" style="left:'+o.x+'px;top:'+(yH+o.lane*26)+'px;width:'+o.w+'px" title="'+esc(o.t)+' · '+o.n+' entradas · '+fd(o.a)+' – '+fd(o.b)+'"><span>'+(o.ic?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+o.ic+'"/></svg>':'')+esc(o.t)+' <small>'+o.n+'</small></span></a>';}).join('');
 // minimapa
 var mm=anios.map(function(y){return '<button type="button" data-y="'+y+'" style="left:'+((X(y+'-01-01')-PAD)/(W-PAD-FIN)*100)+'%">'+String(y).slice(2)+'</button>';}).join('')+
  pts.map(function(o){return '<i class="t-'+o.tipo+'" style="left:'+((o.x-PAD)/(W-PAD-FIN)*100)+'%"></i>';}).join('');
 var cuenta=function(t){return t==='cobertura'?barras.length+hilos.length:pts.filter(function(o){return o.tipo===t;}).length;};
 var html='<div class="wrap">'+crumbs([['Archivo','/archive'],['Cronología']])+'<div class="cr-top"><h1 class="soft">Crono<em>logía</em></h1><p>'+(+hoy.slice(0,4)-y0)+' años de diseño de noticias en una tira: las grandes coberturas, las noticias que llenaron portadas y las piezas que no hemos olvidado.</p></div>'+
  '<div class="cr-ctl"><div class="cr-f" role="group" aria-label="Mostrar">'+['noticia','pieza','cobertura','web'].map(function(t){return '<button type="button" class="t-'+t+'" data-f="'+t+'" aria-pressed="true"><i></i>'+(t==='cobertura'?'Coberturas':t==='web'?'La web':KIT[t]+'s')+' <small>'+cuenta(t)+'</small></button>';}).join('')+'</div>'+
  '<div class="cr-nav"><button type="button" data-ir="ini">« Inicio</button><button type="button" data-ir="hoy">Hoy »</button></div></div></div>'+
  '<div class="cr-sc" id="cr-sc" tabindex="0" aria-label="Línea del tiempo; desplázate en horizontal"><div class="cr-in" style="width:'+W+'px;height:'+H+'px;--sp:'+SP+'px">'+
  '<div class="cr-intro" style="height:'+SP+'px"><span class="caps">Octubre de '+y0+'</span><p class="soft">Aquí empieza inconsolata».</p><span class="caps">Arrastra hacia la izquierda »</span></div>'+
  marcas+'<div class="cr-sp" style="top:'+SP+'px"></div><div class="cr-act" style="top:'+(SP+3)+'px">'+act+'</div>'+
  '<span class="cr-lab" style="top:'+(yB-24)+'px">Coberturas especiales »</span>'+bs+(hilos.length?'<span class="cr-lab" style="top:'+(yH-24)+'px">Grandes historias »</span>'+hs:'')+cartas+
  '<div class="cr-hoy" style="left:'+X(hoy)+'px;height:'+SP+'px"><span>Hoy</span></div></div></div>'+
  '<div class="wrap"><div class="cr-mm" id="cr-mm">'+mm+'<span class="vw" id="cr-vw"></span></div><p class="cr-nota">Arrastra la tira, usa la barra de abajo o pulsa un año. Las coberturas enlazan a su especial; el resto, al post.</p></div>';
 // mientras no se publique (cronologia.json «visible»: true), solo un adelanto borroso con «Próximamente»
 if(!CR.visible){var i0=html.indexOf('<div class="cr-sc"'),i1=html.indexOf('<div class="wrap"><div class="cr-mm"');
  var tira=html.slice(i0,i1).replace('id="cr-sc" tabindex="0"','id="cr-sc" tabindex="-1" inert');
  var pre='<div class="wrap">'+crumbs([['Archivo','/archive'],['Cronología']])+'<div class="cr-top"><h1 class="soft">Crono<em>logía</em></h1><p>'+(+hoy.slice(0,4)-y0)+' años de diseño de noticias en una sola tira: las grandes coberturas, las noticias que llenaron portadas y las piezas que no hemos olvidado.</p></div></div>';
  return {html:pre+'<div class="cr-pronto">'+tira+'<div class="cr-velo"><span class="caps">Próximamente »</span><p class="soft">Estamos terminando de colocar quince años de historia.</p><a class="btn-ink" href="/archive">Mientras, el archivo »</a></div></div><div class="wrap"><p class="cr-nota" style="margin-top:18px">La cronología se abrirá muy pronto.</p></div>',
   init:function(){var sc=document.getElementById('cr-sc');if(sc)sc.scrollLeft=X('2014-06-01')-80;}};}
 return {html:html,init:function(){
  var sc=document.getElementById('cr-sc'),vw=document.getElementById('cr-vw'),mmEl=document.getElementById('cr-mm'),box=sc.closest('.v-pag'),R=W-PAD-FIN;
  function pinta(){var b=Math.min(1,sc.clientWidth/R),a=Math.min(Math.max(0,(sc.scrollLeft-PAD)/R),1-b);vw.style.left=a*100+'%';vw.style.width=b*100+'%';}
  function ir(x,suave){sc.scrollTo({left:Math.max(0,x),behavior:suave?'smooth':'auto'});}
  sc.addEventListener('scroll',pinta);addEventListener('resize',pinta);
  sc.addEventListener('keydown',function(e){if(e.key==='ArrowRight'){sc.scrollLeft+=320;e.preventDefault();}if(e.key==='ArrowLeft'){sc.scrollLeft-=320;e.preventDefault();}});
  var arr=null,mov=0;sc.addEventListener('pointerdown',function(e){if(e.pointerType!=='mouse'||e.button)return;arr={x:e.clientX,s:sc.scrollLeft};mov=0;});
  addEventListener('pointermove',function(e){if(!arr)return;var d=e.clientX-arr.x;if(Math.abs(d)>4){mov=1;sc.classList.add('arr');}sc.scrollLeft=arr.s-d;});
  addEventListener('pointerup',function(){arr=null;setTimeout(function(){sc.classList.remove('arr');},0);});
  sc.addEventListener('click',function(e){if(mov&&e.target.closest('a')){e.preventDefault();mov=0;}},true);
  sc.addEventListener('dragstart',function(e){e.preventDefault();});
  function aMM(e){var r=mmEl.getBoundingClientRect(),f=(e.clientX-r.left)/r.width;ir(PAD+f*R-sc.clientWidth/2,false);}
  var mmArr=false;mmEl.addEventListener('pointerdown',function(e){if(e.target.closest('button'))return;mmArr=true;aMM(e);});addEventListener('pointermove',function(e){if(mmArr)aMM(e);});addEventListener('pointerup',function(){mmArr=false;});
  box.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
   if(b.dataset.y){ir(X(b.dataset.y+'-01-01')-40,true);try{history.replaceState(null,'','#'+b.dataset.y);}catch(x){}}
   if(b.dataset.ir)ir(b.dataset.ir==='ini'?0:sc.scrollWidth,true);
   if(b.dataset.f){var on=b.getAttribute('aria-pressed')!=='true';b.setAttribute('aria-pressed',on);sc.classList.toggle('sin-'+b.dataset.f,!on);}});
  var y=+location.hash.slice(1);if(y>=y0)ir(X(y+'-01-01')-40,false);pinta();}};}

// ---------- montaje
function fichaN(n){var c=(cat0&&cat0.medios||[]).find(function(m){return m.n===n;});return c&&c.ficha?fichaMedio(c):'/buscador#q='+encodeURIComponent(n);}
function buscadorPag(D){
 __BUS_JS__
 document.querySelector('.v-buscador .y-now').textContent=Y1;
}
function estadisticasPag(ST){
 __EST_JS__
}
function pagina(meta,cat){
 cat0=cat;var home=document.getElementById('home');
 home.innerHTML='<div class="v-pag v-'+RUTA+'"><div class="wrap"><p class="cargando-pag" style="padding:60px 0;font-family:Fraunces,serif;font-style:italic;font-size:22px">Cargando…</p></div></div>';
 var box=home.firstChild,hash=function(){return decodeURIComponent(location.hash.slice(1));};
 var pon=function(r,cls){box.className='v-pag v-'+RUTA+(cls?' '+cls:'');box.innerHTML=r.html;r.init();};
 var falla=function(e){console.error('inconsolata»: página',e);box.innerHTML='<div class="wrap"><p style="padding:60px 0">No se han podido cargar los datos. Prueba a recargar la página.</p></div>';};
 if(RUTA==='buscador'){document.title='Buscador · inconsolata»';get('indice').then(function(D){box.innerHTML=__BUS_HTML__;buscadorPag(D);}).catch(falla);return;}
 if(RUTA==='estadisticas'){document.title='Estadísticas · inconsolata»';get('estadisticas').then(function(ST){box.innerHTML=__EST_HTML__;estadisticasPag(ST);}).catch(falla);return;}
 if(RUTA==='cronologia'){Promise.all([get('archivo'),get('especiales'),get('cronologia')]).then(function(r){pon(cronoPag(r[0],cat,r[1],r[2]));}).catch(falla);return;}
 if(RUTA==='novedades'){document.title='Novedades · inconsolata»';get('avisos').then(function(A){pon(novPag(A,cat));}).catch(falla);return;}
 if(RUTA==='especiales'){Promise.all([get('archivo'),get('especiales')]).then(function(r){
   function ve(){var s=hash(),x=r[1].find(function(e){return e.slug===s;});pon(x?espPag(r[0],cat,r[1],x):espIdx(r[1],cat));if(!x)document.title='Especiales · inconsolata»';scrollTo(0,0);}
   ve();addEventListener('hashchange',ve);}).catch(falla);return;}
 if(RUTA==='medios'){Promise.all([get('archivo'),get('fichas_medios'),get('estadisticas').catch(function(){return null;})]).then(function(r){
   function ve(){var s=hash(),mi=s?cat.medios.findIndex(function(m){return m.slug===s;}):-1;if(mi<0&&s)mi=r[0].medios.findIndex(function(m){return fold(m.n)===fold(s);});
    if(mi>=0)pon(medioFicha(r[0],cat,r[1],mi,r[2]),'v-ficha');else{document.title='Medios · inconsolata»';pon(medioIdx(r[0],cat),'v-ficha');}scrollTo(0,0);}
   ve();addEventListener('hashchange',ve);}).catch(falla);return;}
 if(RUTA==='autores'){Promise.all([get('archivo'),get('fichas_medios'),get('autores_fichas').catch(function(){return {};})]).then(function(r){var A=r[0];
   function ve(){var s=fold(hash()),ai=s?A.autores.findIndex(function(a){return fold(a.n)===s;}):-1;
    if(ai>=0)pon(autorFicha(A,cat,r[1],r[2],ai),'v-ficha');else{document.title='Autores · inconsolata»';pon(autorIdx(A),'v-ficha');}scrollTo(0,0);}
   ve();addEventListener('hashchange',ve);}).catch(falla);return;}
}
