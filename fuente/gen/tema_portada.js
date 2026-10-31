// ------------------------------------------------------------------ portada
// La primera página del blog se convierte en la portada: los posts que pone Tumblr (los más frescos) se completan
// con los datos ligeros del repositorio (portada.json, efemérides, avisos).
var DIAS=['domingo','lunes','martes','miércoles','jueves','viernes','sábado'];
var PROY={k:'Proyectos »',t:'SISMOLIVE',p:'Todos los terremotos del planeta, en directo y con datos abiertos.',u:'/post/830276402210291712/sismolive',
 im:'https://64.media.tumblr.com/347064713ce39bc8f64fb6d78fe035f4/039e04832269dcd6-b8/s1280x1920/39c0be6a2669b9cde1527ba6c603feb6e1032f73.jpg'};
var TINTAS=['ht-c','ht-k','ht-y','ht-m'];
function hoyISO(){var d=new Date();return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2);}
function romano(n){var x='',m=[[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],[50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']];m.forEach(function(q){while(n>=q[0]){x+=q[1];n-=q[0];}});return x;}
function ddmm(d){return d.slice(8,10)+'.'+d.slice(5,7);}
function primeras(t,n){t=(t||'').replace(/<([^<>]{1,120})>/g,'$1').replace(/^[\s⩔]+/,'').replace(/\s+/g,' ').trim();var re=/[^.!?]+[.!?]+(?=\s|$)/g,r='',m;
 while((m=re.exec(t))){var x=m[0].trim();if(!r){r=x;if(r.length>=70)break;}else if((r+' '+x).length<=n){r+=' '+x;break;}else break;}
 r=r||t;if(r.length>n){r=r.slice(0,n).replace(/\s+\S*$/,'').replace(/[,;:\s]+$/,'')+'…';}return r;}
function img(u,alt,cls){return u?'<img loading="lazy" src="'+esc(u)+'" alt="'+esc(alt||'')+'"'+(cls?' class="'+cls+'"':'')+' onerror="this.remove()">':'';}
function medioN(cat,n){return cat.medios.find(function(m){return m.n===n;})||{n:n};}
function deco(s){var t=document.createElement('textarea');t.innerHTML=s;return t.value;}
function ls(k,v){try{if(v===undefined)return JSON.parse(localStorage.getItem(k)||'null');localStorage.setItem(k,JSON.stringify(v));}catch(e){return null;}}

function deTarjeta(c,meta,cat){
 var id=rid(c),mt=meta[id],tags=(c.dataset.tags||'').toLowerCase().split('|').filter(Boolean);
 var tg=function(r){return tags.some(function(t){return r.test(t);});};
 var s=mt?mt[0]:tg(/^mucho ?m[aá]s$/)?'m':tg(/^extra!?$/)?'x':tg(/^detallitos$/)?'d':tg(/^metablog$/)?'b':'';
 var d=c.dataset.date||'';
 var ims=[],hr=(c.dataset.hr||'').trim().split(/\s+/).filter(Boolean),sm=(c.dataset.img||'').trim().split(/\s+/).filter(Boolean);
 hr.forEach(function(u,i){ims.push({big:u,sm:sm[i]||u});});
 var tp=c.querySelector('template.lb-body'),body=null;
 if(tp){body=document.createElement('div');body.innerHTML=tp.innerHTML;unwrap(body);
  [].forEach.call(body.querySelectorAll('img'),function(i){if(i.closest('blockquote'))return;
   ims.push({big:srcDe(i,1280),sm:srcDe(i,640),w:+(i.getAttribute('data-orig-width')||0),h:+(i.getAttribute('data-orig-height')||0)});});}
 ims=ims.filter(function(im,k){return !esPortadilla(s,k,im,d||'2099');});
 var t=(c.querySelector('.tt')||{}).textContent||'',bh=body&&body.querySelector('h1');t=t.trim()||TIT[id]||(bh?bh.textContent.trim():'');
 var txt=deco(c.dataset.txt||'').replace(/^[\s⩔]+/,'');if(c.dataset.root)txt=txt.replace(/^[\w.-]+:\s*/,'').replace(/^[\s⩔]+/,'');
 if(bh&&txt.indexOf(bh.textContent.trim())===0)txt=txt.slice(bh.textContent.trim().length).replace(/^[\s⩔]+/,'');
 if(!t)t=primeras(txt,110);
 return {id:id,tags:tags,u:c.getAttribute('href'),d:d,s:s,k:mt?mt[1]:[],meds:mt?mt[2].map(function(i){return cat.medios[i];}).filter(Boolean):[],
  auts:mt?mt[3].map(function(i){return cat.autores[i];}):[],ims:ims,t:t,txt:txt,body:body};
}
function deDato(r,cat){return {id:r[0],u:'/post/'+r[1],d:r[2],s:r[3],k:r[4],meds:r[7].map(function(n){return medioN(cat,n);}),auts:[],
 ims:r[8]?[{big:r[8],sm:r[8]}]:[],t:r[5],txt:r[6],body:null};}

var META0={};
function espDe(p){var sl=(META0[p.id]||[])[5];return sl&&cat0&&cat0.esp&&cat0.esp[sl]?{slug:sl,n:cat0.esp[sl]}:null;}
function espK(p,cls){var e=espDe(p);return e?'<span class="'+(cls||'k-esp')+'">'+esc(e.n)+' »</span>':'';}
function tituloDe(p){return p.s==='m'?'mucho más':p.t;}
function kicker(p,cls){return '<span class="'+(cls||'kicker')+(p.meds.length>1?' muchos':'')+'">'+(p.meds.length?medsK(p.meds)+' · ':'» ')+ddmm(p.d)+'</span>';}

// ---------- piezas
function hero(p){var im=p.ims[0];
 var ki=p.s==='b'?'metablog »':p.s==='o'?'offtopic »':p.k[0]?esc(TN[p.k[0]])+' »':'Lo último »';
 return '<section class="hero">'+(im?'<a href="'+esc(p.u)+'" class="hero-img"><div class="ph ht-k">'+img(im.big,(TN[p.k[0]]||'Imagen')+(p.meds[0]?' de '+p.meds[0].n:''))+'</div></a>':'')+
  '<div class="hero-card'+(im?'':' solo')+(p.col?' c-'+p.col:'')+'"><span class="caps" style="letter-spacing:3px">'+ki+(espDe(p)?' <a class="k-esp" href="/especiales#'+esc(espDe(p).slug)+'">'+esc(espDe(p).n)+' »</a>':'')+'</span><h1 class="soft"><a href="'+esc(p.u)+'">'+destaca(p.t)+'</a></h1>'+
  (p.txt?'<p>'+esc(primeras(p.txt.indexOf(quita(p.t))===0?p.txt.slice(quita(p.t).length):p.txt,230))+'</p>':'')+
  '<div class="hero-meta">'+(p.meds.length?'<span class="hm-avs">'+p.meds.map(function(m){return '<a href="'+fichaMedio(m)+'" title="'+esc(m.n)+'" aria-label="Ficha de '+esc(m.n)+'">'+(m.avw?'<img class="k-av" src="'+esc(m.avw)+'" alt="" onerror="this.parentNode.textContent=\''+esc(m.n.charAt(0))+'\'">':esc(m.n.charAt(0)))+'</a>';}).join('')+'</span><span class="hm-n">» '+(p.meds.length>3?p.meds.length+' medios':p.meds.map(function(m){return '<a href="'+fichaMedio(m)+'">'+esc(m.n)+'</a>';}).join(', ').replace(/, (<a [^>]*>[^<]*<\/a>)$/,' y $1'))+'</span>':'')+'<span>'+p.d.split('-').reverse().join('.')+'</span></div></div></section>';}

// versión lite: «lo último» como lista sencilla (miniatura, medio y título)
function liteFila(p){var im=p.ims[0],t=p.s==='m'?'mucho más » '+quita(p.t).replace(/^mucho m[aá]s\s*[»·]?\s*/i,''):p.s==='x'?(p.mes?'EXTRA! · lo mejor de '+p.mes:quita(p.t)):p.t;
 return '<a class="lf'+(p.s?' s-'+p.s:'')+'" href="'+esc(p.u)+'"><span class="lf-ph">'+(im?img(im.sm):'')+'</span><span class="lf-tx">'+(p.s&&SECN[p.s]?'<span class="lf-s">'+SECN[p.s]+' »</span>':espK(p,'lf-s'))+kicker(p,'lf-k')+'<span class="lf-t">'+(p.s==='m'||p.s==='x'?esc(t):destaca(t))+'</span></span></a>';}
function hoja(p,i,pos){
 var st=' style="grid-column:'+pos.c+';margin-top:'+pos.mt+'px;transform:rotate('+pos.r+'deg)"',tape='<span class="tape" aria-hidden="true"></span>';
 var a='<a href="'+esc(p.u)+'" ';
 if(p.s==='d'){return a+'class="clip"'+st+'><svg class="pc" viewBox="0 0 22 58" aria-hidden="true"><path d="M6 4 V42 a5 5 0 0 0 10 0 V10 a3.5 3.5 0 0 0 -7 0 V40" fill="none" stroke="#7A766C" stroke-width="2.4" stroke-linecap="round"/></svg><span class="clip-sec">detallitos</span>'+
  '<div class="clip-g'+(p.ims.length>1?' two':'')+'">'+p.ims.slice(0,2).map(function(im){return '<div class="ph ht-k" style="height:170px">'+img(im.sm)+'</div>';}).join('')+'</div>'+kicker(p,'clip-cap')+'<span class="clip-t">'+esc(quita(p.t))+'</span></a>';}
 if(p.s==='x'){return a+'class="xsheet"'+st+'>'+tape+'<div class="xs-top"><span class="xword" aria-label="EXTRA!">Extra!</span><span class="caps xs-n">'+(p.num?'Nº '+p.num+'<br>':'')+(p.mes?'lo mejor de '+esc(p.mes):'')+'</span></div>'+
  '<div class="xfan" aria-hidden="true">'+p.ims.slice(0,3).map(function(im){return '<div class="ph ht-k">'+img(im.sm)+'</div>';}).join('')+'</div>'+
  '<span class="tt">'+(p.mes?'Lo mejor del diseño de prensa de '+esc(p.mes):esc(quita(p.t)))+'</span>'+(p.meds.length?'<span class="xs-m">'+esc(p.meds.map(function(m){return m.n;}).join(', '))+'.</span>':'')+'</a>';}
 if(p.s==='b'||p.s==='o'){return a+'class="tsheet"'+st+'>'+tape+'<div class="ts-t"><span class="caps">'+SECN[p.s]+' »</span><h3 class="soft'+(quita(p.t).length>60?' largo':'')+'">'+destaca(p.t)+'</h3>'+(p.txt?'<p>'+esc(primeras(p.txt,170))+'</p>':'')+'<span class="caps" style="color:var(--accent)">Seguir leyendo »</span></div>'+
  (p.ims.length?'<div class="tcoll" aria-hidden="true">'+p.ims.slice(0,3).map(function(im){return '<div class="ph ht-k">'+img(im.sm)+'</div>';}).join('')+'</div>':'')+'</a>';}
 var dark=p.k.indexOf('port')>=0&&p.k.length===1;
 if(p.col==='negro')dark=true;return a+'class="sheet'+(dark?' dark':'')+(p.col&&p.col!=='negro'?' c-'+p.col:'')+'"'+st+'>'+tape+icoP(p.id,p.k[0],'ico '+(i%2?'tl':'tr'))+
  (p.ims[0]?'<div class="ph '+TINTAS[i%4]+'" style="height:'+pos.h+'px">'+img(p.ims[0].sm,(TN[p.k[0]]||'Imagen')+(p.meds[0]?' de '+p.meds[0].n:''))+'</div>':'')+
  espK(p)+kicker(p)+'<span class="tt">'+esc(quita(p.t))+'</span>'+(p.auts.length?'<span class="by">por '+esc(p.auts.slice(0,3).join(', ').replace(/, ([^,]*)$/,' y $1'))+'</span>':'')+'</a>';}

// colocación en la rejilla de 12 columnas: piezas alternas a izquierda y derecha, con giros y desniveles
function colocar(L){var out=[],R=[-1.5,1,-2.5,.6,1.4,-2,-1,2,-.8],H=[400,320,360,300,380,340],MA=[0,30,10,40,0,20],MB=[110,60,140,80,120,50];
 var peso=function(p){return p.tam==='grande'?8:p.tam==='mediana'?6:p.tam==='pequeña'?4:p.s==='d'?3:p.s==='b'||p.s==='o'?7:p.s==='x'?7:5;};
 for(var i=0,f=0;i<L.length;i+=2,f++){var a=L[i],b=L[i+1],h=function(p,k){return p.tam==='grande'?480:p.tam==='pequeña'?260:H[k%H.length];};
  if(!b){out.push({c:'3/11',mt:MA[f%6],r:R[i%9],h:h(a,i)});break;}
  var pa=peso(a),pb=peso(b),wa=Math.max(3,Math.min(8,Math.round(11*pa/(pa+pb))));
  if(f%2&&pa===pb)wa=11-wa;   // alterna el lado ancho en las filas de piezas iguales
  out.push({c:'1/'+(1+wa),mt:MA[f%6],r:R[i%9],h:h(a,i)});out.push({c:(2+wa)+'/13',mt:MB[f%6],r:R[(i+1)%9],h:h(b,i+1)});}
 return out;}

function mmSec(m,top){var fr=m.fr||[],num=(m.t.match(/semana\s+([IVXLCDM]+)/i)||[])[1]||'';
 var lab=top?(m.d===hoyISO()?'Hoy, '+DIAS[new Date().getDay()]+' »':'Recién salido »'):'';
 return '<section class="mm"'+(top?' style="margin-top:44px"':'')+'><div class="wrap inner"><div class="mm-top"><div style="display:flex;flex-direction:column;gap:4px">'+
  (lab?'<span class="caps mm-hoy">'+lab+'</span>':'')+'<span class="caps" style="font-size:15px;letter-spacing:3px">La semana en infografías</span><span class="mm-title soft">mucho más »</span></div>'+
  '<a href="'+esc(m.u)+'" class="btn-yellow">Ver '+(fr.length>1?'las '+(m.n&&m.n>fr.length?fr.length:fr.length):'el post')+' »</a></div>'+
  (num?'<div class="mm-num" aria-hidden="true">'+num.toUpperCase()+'</div>':'')+
  '<div class="film"><div class="perf"></div><div class="frames">'+fr.slice(0,7).map(function(f,i){return '<a class="frame" href="'+esc(m.u)+'#mm-'+(i+1)+'"><div class="ph">'+img(f[0])+'</div><span>'+esc(f[1]||'')+(f[1]?' ▸':'')+'</span></a>';}).join('')+'</div><div class="perf"></div></div></div></section>';}

// especial web (etiqueta «especial web»): banda blanca a todo el ancho con el GIF en un navegador y una tira de contactos
function webSec(p,W){var w=W&&W.i===p.id?W:{u:p.u,t:p.t,b:p.txt,g:p.ims[0]&&p.ims[0].big,fr:p.ims.slice(1).map(function(im){return [im.sm,''];})};
 var lk=w.lk||p.u,dom=(lk.match(/^https?:\/\/([^/?#]+)(\/[^?#]*)?/)||[]);var url=dom[1]?(dom[1].replace(/^www\./,'')+(dom[2]&&dom[2]!=='/'?dom[2]:'')):'inconsolata.com'+(lk.charAt(0)==='/'?lk:'');
 var ext=/^https?:/.test(lk)&&!/inconsolata\.com|tumblr\.com/.test(lk);
 return '<section class="ew"><div class="wrap ew-in"><div class="ew-tx"><span class="caps ew-k">'+(p.d===hoyISO()?'Hoy » ':'')+'Especial » la web</span><h2 class="soft"><a href="'+esc(lk)+'"'+(ext?' rel="noopener"':'')+'>'+destaca(p.t)+'</a></h2>'+
  (w.b?'<p>'+esc(primeras(w.b,240))+'</p>':'')+'<a class="ew-cta" href="'+esc(lk)+'">Ver la presentación »</a><a class="ew-post" href="'+esc(p.u)+'">Leer el post »</a></div>'+
  (w.g?'<a class="ew-nav" href="'+esc(lk)+'" aria-hidden="true" tabindex="-1"><span class="ew-bar"><i></i><i></i><i></i><span>'+esc(url)+'</span></span><span class="ew-win"><img src="'+esc(w.g)+'" alt=""></span></a>':'')+'</div>'+
  ((w.fr||[]).length?'<div class="ew-tira"><div class="ew-tr">'+w.fr.map(function(f){return '<a href="'+esc(lk)+'"><img loading="lazy" src="'+esc(f[0])+'" alt="'+esc(f[1]||'')+'">'+(f[1]?'<span class="caps">'+esc(f[1])+' ▸</span>':'')+'</a>';}).join('')+'</div></div>':'')+'</section>';}
function xdaySec(x){return '<section class="xday"><div class="in"><a href="'+esc(x.u)+'" class="xd-a"><span class="caps xd-k">'+(x.d===hoyISO()?'Hoy sale el EXTRA! »':'Recién salido »')+'</span>'+
 '<div class="w" aria-label="EXTRA!">Extra!</div><div class="t">'+(x.num?'Nº '+x.num+' · ':'')+'lo mejor del diseño de prensa'+(x.mes?' de '+esc(x.mes):'')+'</div>'+
 (x.meds.length?'<p>'+esc(x.meds.length)+' medios en esta entrega: '+esc(x.meds.map(function(m){return m.n;}).join(', '))+'.</p>':'')+'<span class="go">Abrir el EXTRA! »</span></a>'+
 '<a href="'+esc(x.u)+'" class="fan" aria-hidden="true" tabindex="-1">'+x.ims.slice(0,5).map(function(im){return '<span class="xf">'+img(im.sm)+'</span>';}).join('')+'</a></div></section>';}

function mesDe(p){var t=(p.txt||'')+' ',re=new RegExp('(destacamos|recopilaci|selecci[oó]n)[^.]*?\\b('+MESES.join('|')+')\\b','i'),m=t.match(re);
 if(m)return m[2].toLowerCase();var d=new Date(p.d);d.setMonth(d.getMonth()-1);return MESES[d.getMonth()];}

function hoySec(ef){var y=new Date().getFullYear();
 var rows=(ef||[]).filter(function(r){return +r[0]<y;}).slice(0,3);
 if(!rows.length)return '';
 return '<div class="hoy"><h2 class="serif">tal día <em class="soft">como hoy</em></h2>'+rows.map(function(r,i){
  return '<a href="/post/'+esc(r[1])+'" class="hoy-row"><span class="hoy-year">'+r[0]+'</span><span class="hoy-txt">'+esc(quita(r[2]))+(r[3][0]?'<small>» '+esc(r[3][0])+'</small>':'')+'</span><span class="hoy-thumb ph '+['ht-m','ht-c','ht-y'][i]+'" aria-hidden="true">'+img(r[4])+'</span></a>';}).join('')+'</div>';}

function temasSec(P,cat,esp){
 var PT=P.temas.filter(function(t){return !t[5];}),V=PT.filter(function(t){return t[2]>=8&&t[4].length;}),COL=['t-ink','t-yel','t-cya','t-pap','t-mag'];
 var fijo=esp?{n:esp.t,c:esp.n,b:'Especial',u:'/especiales#'+esp.slug,im:esp.im,ic:esp.ic}:null;
 if(!fijo){var tp=V.slice().sort(function(a,b){return b[2]-a[2];})[0];fijo={n:tp[1],c:tp[2],b:tp[3],u:'/buscador#h='+tp[0],im:tp[4][0],ic:TS[tp[0]]};}
 var tile=function(t,cl,big){return '<a href="'+esc(t.u)+'" class="tema '+cl+(big?' big vit-fix':'')+'"><div class="tm-ph">'+img(t.im)+'</div>'+
  (t.ic?'<svg class="tm-ico'+(big?'':' tm-ico-s')+'" viewBox="0 0 64 64" aria-hidden="true"><use href="#'+t.ic+'" class="k"/><use href="#'+t.ic+'" class="m" x="3" y="2.5"/></svg>':'')+
  (big?'<span class="tm-k">'+esc(t.b)+'</span>':'<span class="tm-b">'+esc(t.b)+'</span>')+'<span class="tm-n soft">'+esc(t.n)+'</span><span class="tm-c">'+t.c+(t.c===1?' post':' posts')+'</span></a>';};
 var bloques={};PT.forEach(function(t){(bloques[t[3]]=bloques[t[3]]||[]).push(t);});
 var dlg='<dialog class="tdl" id="tm-dlg" aria-labelledby="tdl-h"><div class="tdl-top"><h2 id="tdl-h" class="soft">Todos los <em>temas</em></h2><button type="button" class="tdl-x" data-close aria-label="Cerrar">×</button></div>'+
  '<p class="tdl-sub">'+PT.length+' temas en '+(new Date().getFullYear()-(+P.anios))+' años de archivo. Pulsa uno para ver todas sus entradas.</p>'+
  (P.esp.length?'<div class="tdl-b tdl-esp"><h3>Especiales <span>· acontecimientos e historias concretas, cada uno dentro de su tema</span></h3><div class="tdl-c">'+P.esp.filter(function(e){return !e[6];}).sort(function(a,b){return (b[4]||'').localeCompare(a[4]||'');}).map(function(e){var ti=cat.temas.findIndex(function(t){return t.n===e[2];});
   return '<a href="/especiales#'+esc(e[1])+'">'+(ti>=0?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+TS[ti]+'"/></svg>':'')+esc(e[0])+'<small>'+e[3]+'</small></a>';}).join('')+'</div></div>':'')+
  Object.keys(bloques).map(function(b){return '<div class="tdl-b"><h3>'+esc(b)+'</h3><div class="tdl-c">'+bloques[b].map(function(t){return '<a href="/buscador#h='+t[0]+'"><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+TS[t[0]]+'"/></svg>'+esc(t[1])+'<small>'+t[2]+'</small></a>';}).join('')+'</div></div>';}).join('')+'</dialog>';
 var EG={};P.esp.filter(function(e){return !e[6];}).forEach(function(e){(EG[e[5]]=EG[e[5]]||[]).push(e);});
 var nCap=function(sl){return P.esp.filter(function(e){return e[6]===sl;}).length;};
 dlg+='<dialog class="tdl" id="es-dlg" aria-labelledby="esd-h"><div class="tdl-top"><h2 id="esd-h" class="soft">Todos los <em>especiales</em></h2><button type="button" class="tdl-x" data-close aria-label="Cerrar">×</button></div>'+
  '<p class="tdl-sub">Acontecimientos e historias con página propia, cada uno dentro de su tema. <a href="/especiales" style="border-bottom:2px solid var(--accent)">Ver la página de especiales »</a></p>'+
  cat.temas.map(function(t){return t.n;}).filter(function(n){return EG[n];}).map(function(n){return '<div class="tdl-b"><h3>'+esc(n)+'</h3><div class="tdl-c">'+EG[n].sort(function(a,b){return (b[4]||'').localeCompare(a[4]||'');}).map(function(e){var ti=cat.temas.findIndex(function(t){return t.n===e[2];});var nc=nCap(e[1]);
   return '<a href="/especiales#'+esc(e[1])+'">'+(ti>=0?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+TS[ti]+'"/></svg>':'')+esc(e[0])+'<small>'+e[3]+(nc?' · '+nc+' cap.':'')+'</small></a>';}).join('')+'</div></div>';}).join('')+'</dialog>';
 return {html:'<section class="temas-sec" aria-labelledby="tm-h"><div class="sec-head tm-head"><h2 id="tm-h" class="serif"><em class="soft">temas</em></h2><div class="tm-btns"><button type="button" class="tm-allbtn" data-open="tm-dlg" aria-haspopup="dialog">Todos los temas <b>'+PT.length+'</b> »</button><button type="button" class="tm-allbtn" data-open="es-dlg" aria-haspopup="dialog">Todos los especiales <b>'+P.esp.filter(function(e){return !e[6];}).length+'</b> »</button></div></div>'+
  '<div class="vit">'+tile(fijo,'t-mag',true)+'<div class="vit-stage" id="vit"><div class="vit-slot"></div><div class="vit-slot"></div><div class="vit-slot"></div><div class="vit-slot"></div></div></div>'+dlg+'</section>',
  init:function(){
   var T=V.map(function(t){return {n:t[1],c:t[2],b:t[3],u:'/buscador#h='+t[0],ims:t[4],ic:TS[t[0]]};});
   for(var i=T.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),x=T[i];T[i]=T[j];T[j]=x;}
   var slots=document.querySelectorAll('#vit .vit-slot'),q=0,ci=0,last=-1,paused=false;
   var t2=function(t){var o={n:t.n,c:t.c,b:t.b,u:t.u,ic:t.ic,im:t.ims[Math.floor(Math.random()*t.ims.length)]};ci=(ci+1)%COL.length;return tile(o,COL[ci]);};
   [].forEach.call(slots,function(s){s.innerHTML=t2(T[q++%T.length]);});
   if(matchMedia('(prefers-reduced-motion: reduce)').matches||!T.length)return;
   (function sched(){setTimeout(function(){if(!paused&&!document.hidden){var k;do{k=Math.floor(Math.random()*slots.length);}while(k===last&&slots.length>1);last=k;var sl=slots[k],h=t2(T[q++%T.length]);
    sl.classList.add('out');setTimeout(function(){sl.classList.remove('out');sl.innerHTML=h;sl.classList.add('in');setTimeout(function(){sl.classList.remove('in');},450);},320);}sched();},2600+Math.random()*3400);})();
   var st=document.getElementById('vit');['mouseenter','focusin'].forEach(function(e){st.addEventListener(e,function(){paused=true;});});['mouseleave','focusout'].forEach(function(e){st.addEventListener(e,function(){paused=false;});});
  }};}

function mediosSec(P,cat){var M=P.med,y=M.y,L=M.l.filter(function(r){return r[1]>0;});
 var top=L.slice(0,6),mx=top[0]?top[0][1]:1;
 var con=L.map(function(r){var m=medioN(cat,r[0]);return {m:m,y:r[1],t:r[2]};});
 var logos=con.filter(function(o){return o.m.logo;}).slice(0,9);
 var run=y+' <i>»</i> <b>'+L.length+'</b> medios <i>»</i> <b>'+M.posts+'</b> entradas <i>»</i> '+top.map(function(r){return esc(r[0])+' <b>'+r[1]+'</b>';}).join(' <i>»</i> ')+' <i>»</i> ';
 var todos=M.l.map(function(r){return {m:medioN(cat,r[0]),y:r[1],t:r[2]};}).filter(function(o){return o.m.ficha;});
 return '<section class="medios" aria-labelledby="md-h"><div class="sec-head md-head"><h2 id="md-h" class="serif"><em class="soft">medios</em></h2>'+
  '<a class="cinta" href="/estadisticas#'+y+'" aria-label="Estadísticas de medios de '+y+': '+L.length+' medios, '+M.posts+' entradas. Ver todas las estadísticas"><span class="ci-k"><b>'+y+'</b> en cifras</span><span class="ci-bars" aria-hidden="true">'+
  top.map(function(r){return '<span class="cb" style="height:'+Math.max(12,Math.round(r[1]/mx*100))+'%" title="'+esc(r[0])+': '+r[1]+'"></span>';}).join('')+'</span><span class="ci-tk" aria-hidden="true"><span class="ci-run">'+run+run+'</span></span><span class="ci-go">Ver »</span></a></div>'+
  '<div class="logos">'+logos.map(function(o){return '<a href="'+fichaMedio(o.m)+'" aria-label="Ficha de '+esc(o.m.n)+'" class="logo-a"><div class="logo-slot logo-img"><img src="'+esc(o.m.logo)+'" alt="'+esc(o.m.n)+'" onerror="this.replaceWith(this.alt)"></div></a>';}).join('')+
  '<button type="button" class="logo-more" data-open="md-dlg" aria-haspopup="dialog"><span class="logo-slot">Todos los medios »</span></button></div>'+
  '<dialog class="tdl mdl" id="md-dlg" aria-labelledby="mdl-h"><div class="tdl-top"><h2 id="mdl-h" class="soft">Todos los <em>medios</em></h2><button type="button" class="tdl-x" data-close aria-label="Cerrar">×</button></div>'+
  '<div class="mdl-tools"><p class="tdl-sub">'+todos.length+' medios con ficha, ordenados por entradas en '+y+'. Pulsa uno para ir a su ficha.</p><label class="sr" for="md-q">Buscar medio</label><input id="md-q" type="search" placeholder="Buscar medio…" autocomplete="off"></div>'+
  '<div class="mdl-grid" id="md-grid">'+todos.map(function(o){return '<a class="mdc" href="'+fichaMedio(o.m)+'" data-n="'+esc(fold(o.m.n))+'">'+(o.m.av?'<span class="mdc-av" aria-hidden="true"><img src="'+esc(o.m.av)+'" alt=""></span>':'')+'<span class="mdc-n">'+esc(o.m.n)+'</span><span class="mdc-c">'+(o.y?'<b>'+o.y+'</b> en '+y+' · ':'')+o.t+' en total</span></a>';}).join('')+'</div></dialog></section>';}

// ---------- avisos: prueba de imprenta (grandes) y marca de registro (ligeros)
var BAR=['#00A0DC','#E5007E','#FFD400','#16140F','#7FCFED','#F27FBF','#FFE97F','#8B8A87','#16140F','#D1006F'];
function avisoId(a){return a.id||a.u||a.t;}
// icono que no es de un tema (p. ej. «Tren»): su símbolo se llama t-<nombre>
function symN(n){if(!n)return '';if(/^t-/.test(n))return n;var id='t-'+fold(n).replace(/\s+/g,'-');return document.getElementById(id)?id:n;}
function avMedia(a){
 if(a.ico){var ti=cat0.temas.findIndex(function(t){return t.n===a.ico||TS[cat0.temas.indexOf(t)]===a.ico;}),sy=ti>=0?TS[ti]:symN(a.ico);
  return '<span class="pv-md ico">'+['#00A0DC','#E5007E','#FFD400','#16140F'].map(function(c){return '<span style="color:'+c+'"><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+esc(sy)+'"/></svg></span>';}).join('')+'</span>';}
 if(a.imgs&&a.imgs.length)return '<span class="pv-md trio">'+a.imgs.slice(0,3).map(function(u){return '<span>'+img(u)+'</span>';}).join('')+'</span>';
 if(a.img)return '<span class="pv-md">'+img(a.img)+'</span>';
 return '';}
var cat0=null;
// la prueba de imprenta se coloca a la derecha del logo medido de verdad (letras ya cargadas y animación acabada);
// si aun así no cabe, baja debajo del logo
// columna de aviso: en el escritorio, en el hueco a la derecha de la imagen del destacado; si no hay destacado o la pantalla es estrecha, bajo la cabecera
function colocaPrueba(){var pr=document.getElementById('prueba'),hero=document.querySelector('.v-home .hero'),mh=document.querySelector('.v-home .masthead');if(!pr||!mh)return;
 var ok=hero&&hero.querySelector('.hero-img')&&matchMedia('(min-width:1000px)').matches&&!document.documentElement.classList.contains('lite');
 if(ok&&pr.parentNode!==hero){hero.appendChild(pr);pr.classList.add('en-hero');}
 else if(!ok&&pr.parentNode===hero){var t=document.getElementById('tira');(t||mh).insertAdjacentElement('afterend',pr);pr.classList.remove('en-hero');}
 // sin destacado (día de especial web): en el escritorio, junto al título de «lo último»
 var sh=document.querySelector('.v-home .ew')&&document.querySelector('.v-home .ew+.wrap .sec-head');
 if(!hero&&sh&&matchMedia('(min-width:1000px)').matches&&!document.documentElement.classList.contains('lite')){if(pr.parentNode!==sh){sh.appendChild(pr);pr.classList.add('en-sh');}}
 else if(pr.classList.contains('en-sh')){var t2=document.getElementById('tira');(t2||mh).insertAdjacentElement('afterend',pr);pr.classList.remove('en-sh');}}
function avisos(A){var hoy=hoyISO(),vig=function(a){return (!a.desde||a.desde<=hoy)&&(!a.hasta||a.hasta>=hoy);};
 var cerr=ls('inc-avisos-cerrados')||[],G=(A.grandes||[]).filter(function(a){return vig(a)&&cerr.indexOf(avisoId(a))<0;}),cur=0;
 var box=document.getElementById('prueba');G=G.filter(function(a){return !a.off&&a.t;});
 var BAR4='<span class="cbar" aria-hidden="true"><i style="background:#00A0DC"></i><i style="background:#E5007E"></i><i style="background:#FFD400"></i><i style="background:#16140F"></i></span>';
 function pinta(anim){if(!G.length){box.hidden=true;return;}var a=G[cur];
  box.innerHTML='<div class="cl-k"><span>'+esc(a.k||'Aviso')+' »</span><span class="cl-c">'+(G.length>1?'<button data-prev aria-label="Aviso anterior">‹</button><span>'+(cur+1)+'/'+G.length+'</span><button data-next aria-label="Aviso siguiente">›</button>':'')+'<button class="x" data-cerrar aria-label="Cerrar aviso">×</button></span></div>'+
   '<a class="cl-t soft" href="'+esc(a.u||'#')+'">'+destaca(a.t)+'</a>'+BAR4;
  box.hidden=false;colocaPrueba();if(anim){box.classList.remove('go');void box.offsetWidth;box.classList.add('go');}}
 box.addEventListener('click',function(e){
  if(e.target.closest('[data-cerrar]')){cerr.push(avisoId(G[cur]));ls('inc-avisos-cerrados',cerr.slice(-40));G.splice(cur,1);cur=0;pinta(false);}
  if(e.target.closest('[data-next]')){cur=(cur+1)%G.length;pinta(false);}
  if(e.target.closest('[data-prev]')){cur=(cur+G.length-1)%G.length;pinta(false);}});
 setTimeout(function(){pinta(true);},matchMedia('(prefers-reduced-motion: reduce)').matches?0:900);
 addEventListener('resize',colocaPrueba);
 // tira bajo la cabecera
 var T=A.tira,tb=document.getElementById('tira');
 if(tb&&T&&T.t&&vig(T)&&cerr.indexOf('tira:'+avisoId(T))<0){
  tb.innerHTML='<span class="tr-k">'+esc(T.k||'Aviso')+'</span><a class="tr-t soft" href="'+esc(T.u||'#')+'">'+destaca(T.t)+(/»\s*$/.test(T.t)?'':' <span class="tr-q">»</span>')+'</a><button class="x" aria-label="Cerrar aviso">×</button>';tb.hidden=false;
  tb.querySelector('.x').addEventListener('click',function(){cerr.push('tira:'+avisoId(T));ls('inc-avisos-cerrados',cerr.slice(-40));tb.hidden=true;});}
 // ligeros
 var Lg=(A.ligeros||[]).filter(function(a){return !a.desde||a.desde<=hoy;}).sort(function(a,b){return (b.f||'').localeCompare(a.f||'');});
 // una novedad sigue marcada durante una semana desde su fecha; abrir la lista solo para la animación
 var lim=new Date(Date.now()-7*864e5).toISOString().slice(0,10),visto=ls('inc-novedades-visto')||'',nuevos=Lg.filter(function(a){return (a.f||'')>=lim;}).length;
 var b=document.getElementById('rbtn'),pn=document.getElementById('panel');if(!b)return;
 var lbn=document.getElementById('lb-n');if(lbn&&nuevos){lbn.textContent=nuevos;lbn.hidden=false;}
 if(!Lg.length){b.closest('.reg-w').classList.add('vacio');return;}
 function lista(){pn.querySelector('ul').innerHTML=Lg.slice(0,Math.max(5,nuevos)).map(function(a,i){var ti=a.ico?cat0.temas.findIndex(function(t){return t.n===a.ico;}):-1,sy=ti>=0?TS[ti]:symN(a.ico);
  var inn='<span class="ic'+(sy?'':' bl soft')+'">'+(sy?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+esc(sy)+'"/></svg>':'»')+'</span><span><span class="fe">'+(a.f?+a.f.slice(8)+' '+MESES[+a.f.slice(5,7)-1].slice(0,3):'')+'</span><span class="tx">'+esc(a.t)+'</span></span>';
  return '<li class="'+((a.f||'')>=lim?'nv':'')+'">'+(a.u?'<a href="'+esc(a.u)+'">'+inn+'</a>':'<div>'+inn+'</div>')+'</li>';}).join('');}
 function marca(){b.classList.toggle('new',nuevos>0);b.classList.toggle('visto',!!Lg[0]&&visto>=(Lg[0].f||''));var d=b.querySelector('.dot');d.textContent=nuevos;b.querySelector('.sr').textContent=nuevos?'Novedades de la web: '+nuevos+' sin ver':'Novedades de la web';}
 lista();marca();
 function cierra(){pn.hidden=true;b.setAttribute('aria-expanded','false');visto=Lg[0].f||hoy;ls('inc-novedades-visto',visto);marca();}
 b.addEventListener('click',function(){if(pn.hidden){pn.hidden=false;b.setAttribute('aria-expanded','true');pn.classList.remove('op');void pn.offsetWidth;pn.classList.add('op');}else cierra();});
 document.addEventListener('click',function(e){if(!pn.hidden&&!e.target.closest('.reg-w'))cierra();});
 document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!pn.hidden){cierra();b.focus();}});
}

function cabecera(){var d=new Date(),t=d.toLocaleDateString('es-ES',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
 var n=d.getFullYear()-2011+((d.getMonth()>9||(d.getMonth()===9&&d.getDate()>=27))?1:0);
 var fold='onsolata'.split('').map(function(ch,i){return '<span class="mf m'+(8-i)+'">'+ch+'</span>';}).join('');
 return '<div class="topbar"><span><span class="cmyk" aria-hidden="true"><span style="background:#00A0DC"></span><span style="background:#E5007E"></span><span style="background:#FFD400"></span><span style="background:#16140F"></span></span>'+
  esc(t.charAt(0).toUpperCase()+t.slice(1))+'&nbsp;·&nbsp;Año '+romano(n)+'</span><div class="hd-slot"></div></div>'+
  '<div class="wrap"><header class="masthead"><a href="/" class="mast soft" aria-label="inconsolata», ir a la portada">inc'+fold+'<span class="reg q">»<span class="reg-y" aria-hidden="true">»</span><span class="reg-c" aria-hidden="true">»</span></span></a>'+
  
  '<div class="side"><div class="side-top"><div class="reg-w"><button class="rbtn" id="rbtn" aria-expanded="false" aria-controls="panel"><span class="sr">Novedades de la web</span><svg viewBox="0 0 64 64" fill="none" stroke-width="1.6" aria-hidden="true"><circle cx="32" cy="32" r="16"/><circle cx="32" cy="32" r="8"/><path d="M32 4v56M4 32h56"/></svg><span class="dot" aria-hidden="true"></span></button>'+
  '<div class="panel" id="panel" hidden><h3><span>Novedades de la web</span><span class="cmyk" aria-hidden="true"><span style="background:#00A0DC"></span><span style="background:#E5007E"></span><span style="background:#FFD400"></span><span style="background:#16140F"></span></span></h3><ul></ul><a class="all" href="/novedades">Todas las novedades »</a></div></div></div>'+
  '<span class="mini soft">inconsolata<span style="color:var(--accent)">»</span></span><span class="tagline">la web del diseño periodístico</span></div></header>'+
  '<aside class="tira" id="tira" aria-label="Aviso" hidden></aside><aside class="colav" id="prueba" aria-label="Aviso" hidden></aside></div>';}

function faldon(f,cat){if(!f||!f.t||(f.hasta&&f.hasta<hoyISO()))return '';
 var ti=f.ico?cat.temas.findIndex(function(t){return t.n===f.ico;}):-1,sy=ti>=0?TS[ti]:symN(f.ico);
 var run=esc(f.t).replace(/\s*»\s*/g,' <i>»</i> ')+' <i>»</i> ';run=run+run;
 return '<a href="'+esc(f.u||'#')+'" class="faldon" aria-label="'+esc(f.t.replace(/»/g,'·'))+'">'+(sy?'<span class="f-icon" aria-hidden="true"><svg viewBox="0 0 64 64"><use href="#'+esc(sy)+'" class="k"/><use href="#'+esc(sy)+'" class="m" x="3" y="2.5"/></svg></span>':'')+
  '<span class="f-track"><span class="f-run">'+run+'</span><span class="f-run" aria-hidden="true">'+run+'</span></span></a>';}

function portada(meta,cat){
 cat0=cat;
 document.body.classList.add('es-portada');
 var home=document.getElementById('home');
 var pag=[].map.call(document.querySelectorAll('.lst .lc'),function(c){return deTarjeta(c,meta,cat);});
 Promise.all([get('portada'),get('avisos').catch(function(){return {};}),get('efemerides/'+hoyISO().slice(5,7)).catch(function(){return {};}),get('portada_manual').catch(function(){return {};})]).then(function(r){
  var P=r[0],A=r[1]||{},EF=r[2]||{},M=r[3]||{};
  META0=meta||{};
  var vistos={},L=[];
  var oc=M.ocultos||[];
  pag.concat(P.rec.concat(P.man||[]).map(function(x){return deDato(x,cat);})).filter(function(p){return oc.indexOf(p.id)<0;}).forEach(function(p){if(!vistos[p.id]){vistos[p.id]=1;L.push(p);}});
  L.sort(function(a,b){return (b.d||'').localeCompare(a.d||'');});
  var COLS=M.colores||{};L.forEach(function(p){p.col=COLS[p.id]||'';});
  // completa con los datos lo que falte en los posts de la página (fotogramas de mucho más y EXTRA!, número…)
  L.forEach(function(p){
   if(p.s==='x'){p.mes=mesDe(p);if(P.x&&P.x.i===p.id){p.num=P.x.num;if(p.ims.length<3)p.ims=P.x.fr.map(function(f){return {sm:f[0],big:f[0]};});}}});
  // elección manual: etiqueta #apertura en Tumblr o el archivo portada_manual.json
  var hoy=hoyISO(),vig=function(o){return o&&(!o.hasta||o.hasta>=hoy)&&(!o.desde||o.desde<=hoy);},obj=function(o){return typeof o==='string'?{id:o}:o;};
  var porId=function(i){return L.find(function(p){return p.id===String(i);});};
  var apO=obj(M.apertura),aper=pag.find(function(p){return p.tags.indexOf('apertura')>=0;})||(vig(apO)&&porId(apO.id))||null;
  if(aper&&apO&&apO.img&&aper.id===String(apO.id))aper.ims=[{big:apO.img,sm:apO.img}];
  var fx=(M.fijos||[]).map(obj).filter(vig).map(function(o){var p=porId(o.id);if(p){p.tam=o.tam;if(o.img)p.ims=[{big:o.img,sm:o.img}];}return p;}).filter(Boolean);
  var top=aper?null:L[0],arriba='',usados={},mm=null;
  var mmP=L.find(function(p){return p.s==='m';});
  if(mmP){mm={u:mmP.u,d:mmP.d,t:mmP.t+' '+(mmP.txt||'').slice(0,80),fr:null,n:0};
   if(P.m&&P.m.i===mmP.id){mm.fr=P.m.fr;mm.t=P.m.t;mm.n=P.m.n;}
   else if(mmP.body){var it=[];[].forEach.call(mmP.body.querySelectorAll('img'),function(i,k){if(i.closest('blockquote'))return;var el=i.closest('.npf_row')||i.closest('figure')||i,nx=el.nextElementSibling,
     md=nx&&(nx.innerHTML.match(/Medio\s*<\/i>\s*:\s*<b>([^<]*)<\/b>/)||[])[1];it.push([srcDe(i,400),md||'',+(i.getAttribute('data-orig-width')||0),+(i.getAttribute('data-orig-height')||0)]);});
    mm.fr=it.filter(function(f,k){return !esPortadilla('m',k,{w:f[2],h:f[3]},mmP.d);}).map(function(f){return [f[0],f[1]];});}
   if(!mm.fr)mm.fr=mmP.ims.map(function(im){return [im.sm,''];});usados[mmP.id]=1;}
  if(top&&top.s==='m'&&mm){arriba=mmSec(mm,true);mm.arriba=true;}
  else if(top&&top.s==='x'){arriba=xdaySec(top);usados[top.id]=1;}
  else if(top&&top.s==='w'){arriba=webSec(top,P.w);usados[top.id]=1;var sinHero=true;}
  var resto=L.filter(function(p){return !usados[p.id];});
  var h=sinHero?null:aper||resto.find(function(p){return p.s!=='d'&&p.s!=='x'&&p.ims.length;})||resto[0];
  if(h)usados[h.id]=1;
  fx=fx.filter(function(p){return !usados[p.id];});fx.forEach(function(p){usados[p.id]=1;});
  var ult=fx.concat(L.filter(function(p){return !usados[p.id]&&p.s!=='m';})).slice(0,Math.max(9,fx.length));
  var de=obj(M.destacado),dd=PROY;
  if(vig(de)){var dp=de.id?porId(de.id):null;dd={k:de.k||(dp&&dp.s==='b'?'metablog »':'Destacado »'),t:de.t||(dp?quita(dp.t):''),p:de.p||(dp?primeras(dp.txt,150):''),u:de.u||(dp?dp.u:'#'),im:de.img||(dp&&dp.ims[0]?dp.ims[0].big:'')};}
  var pos=colocar(ult);
  // especial destacado: el del faldón, si lo hay
  var esp=null,f=A.faldon;
  if(f&&f.especial){var e=P.esp.find(function(x){return x[1]===f.especial;});if(e){var ti=cat.temas.findIndex(function(t){return t.n===e[2];});
   var tt=ti>=0?P.temas.find(function(t){return t[0]===ti;}):null;esp={t:e[0],slug:e[1],n:e[3],im:f.img||(tt&&tt[4][0])||'',ic:ti>=0?TS[ti]:''};}}
  var tm=temasSec(P,cat,esp);
  home.innerHTML='<div class="v-home">'+cabecera()+faldon(f,cat)+arriba+'<div class="wrap">'+(h?hero(h):'')+
   '<section><div class="sec-head"><h2 class="serif">lo <em class="soft">último</em></h2><a href="/archive" class="underline">Todo el archivo »</a></div>'+
   (document.documentElement.classList.contains('lite')?'<div class="lite-lista">'+ult.map(liteFila).join('')+'</div>':'<div class="scatter">'+ult.map(function(p,i){return hoja(p,i,pos[i]);}).join('')+'</div>')+'<div class="mas"><a href="/page/2" class="btn-ink">Más entradas »</a></div></section></div>'+
   (mm&&!mm.arriba?mmSec(mm,false):'')+
   '<div class="wrap"><section class="duo"><a href="'+esc(dd.u)+'" class="proj"><div class="ph">'+img(dd.im,dd.t)+'</div><div class="txt"><span class="caps" style="font-size:14px;letter-spacing:3px">'+esc(dd.k)+'</span><h3 class="soft'+(dd.t.length>14?' largo':'')+'">'+esc(dd.t)+'</h3><p>'+esc(dd.p)+'</p></div></a>'+
   hoySec(EF[hoyISO().slice(8)])+'</section>'+tm.html+mediosSec(P,cat)+'</div></div>';
  // el menú de siempre pasa a la barra superior
  var hr=document.querySelector('.page>.head .hd-right');if(hr)home.querySelector('.hd-slot').appendChild(hr);
  tm.init();avisos(A);
  home.addEventListener('click',function(e){var o=e.target.closest('[data-open]');if(o){var d=document.getElementById(o.dataset.open);if(d.showModal)d.showModal();else d.setAttribute('open','');}
   var c=e.target.closest('[data-close]');if(c){var dl=c.closest('dialog');dl.close?dl.close():dl.removeAttribute('open');}
   if(e.target.tagName==='DIALOG')e.target.close();});
  var q=document.getElementById('md-q');if(q)q.addEventListener('input',function(){var v=fold(this.value.trim());[].forEach.call(document.querySelectorAll('#md-grid .mdc'),function(c){c.hidden=v&&c.dataset.n.indexOf(v)<0;});});
 }).catch(function(e){console.error('inconsolata»: portada',e);document.body.classList.remove('es-portada');listado(meta,cat);});
}
