// ------------------------------------------------------------------ vistas especiales (mucho más, EXTRA!, metablog)
var MES3=['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'];
var STOP=' a al ante bajo con contra de del desde durante el en entre hacia hasta la las lo los para por que qué se según sin sobre su sus tras un una unos unas y o e u ni como cómo cuando dónde donde es son está están más muy the of and to in for on with ';
function fold(s){return String(s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/^the\s+/,'').replace(/[^a-z0-9]+/g,' ').trim();}
function medioPor(cat,n){var f=fold(n);if(!f)return null;return cat.medios.find(function(m){return fold(m.n)===f;})||cat.medios.find(function(m){var g=fold(m.n);return g.length>3&&(f.indexOf(g)===0||g.indexOf(f)===0);})||null;}
// Título con la palabra destacada en magenta: *palabra* manda; si no, una palabra en mayúsculas o la más larga
function destaca(t){
 if(/\*[^*]+\*/.test(t))return esc(t).replace(/\*([^*]+)\*/,'<em>$1</em>').replace(/\*/g,'');
 var ws=t.split(/(\s+)/),best=-1,bl=0;
 ws.forEach(function(w,i){var c=w.replace(/[«»"“”.,:;!?¿¡()]/g,'');if(c.length>=4&&c===c.toUpperCase()&&/[A-ZÁÉÍÓÚÑ]/.test(c)&&!/^[IVXLCDM]+$/.test(c)&&best<0)best=i;});
 if(best<0)ws.forEach(function(w,i){var c=w.replace(/[«»"“”.,:;!?¿¡()]/g,'');if(c.length>bl&&c.length>=5&&STOP.indexOf(' '+c.toLowerCase()+' ')<0&&!/^[A-ZÁÉÍÓÚÑ]/.test(c)){bl=c.length;best=i;}});
 return ws.map(function(w,i){if(i!==best)return esc(w);var m=w.match(/^([«"“(¿¡]*)(.*?)([»"”.,:;!?)]*)$/);return esc(m[1])+'<em>'+esc(m[2])+'</em>'+esc(m[3]);}).join('');
}
function quita(t){return String(t||'').replace(/\*/g,'');}
function rango(d){var b=new Date(d+'T12:00:00'),a=new Date(b.getTime()-6*864e5);
 return a.getMonth()===b.getMonth()?a.getDate()+'–'+b.getDate()+' '+MES3[b.getMonth()]+' '+b.getFullYear():a.getDate()+' '+MES3[a.getMonth()]+'–'+b.getDate()+' '+MES3[b.getMonth()]+' '+b.getFullYear();}
function anioDe(mes,d){var i=MESES.indexOf(String(mes).toLowerCase());var y=+d.slice(0,4);return (i>=0&&i+1>+d.slice(5,7))?y-1:y;}
function tipoDe(t,def){t=t.toLowerCase();
 if(/portad/.test(t))return 'port';if(/\bmapas?\b|cartogr|\brutas?\b|\bdónde\b|territori/.test(t))return 'carto';
 if(/ilustra|dibuj|viñeta|cómic/.test(t))return 'ilus';if(/gráfic|datos|evoluci|cifras|aumento|subida|precios|encuesta|ranking/.test(t))return 'graf';
 if(/fotogra/.test(t))return 'foto';return def||'info';}
function bloque(el){return el.closest('.npf_row')||(el.closest('p')&&el.closest('.body')!==el.closest('p')?el.closest('p'):null)||el.closest('figure')||el;}
function textoDe(el){var t=document.createElement('div');t.innerHTML=el.innerHTML.replace(/<br\s*\/?>/gi,' | ');return t.textContent.replace(/ /g,' ');}
function nuevoTop(cls){var main=document.querySelector('main.wrap'),top=document.createElement('div');top.className=cls;main.parentNode.insertBefore(top,main);return {main:main,top:top};}
var LEG='<div class="legacy" role="note"><span class="lg-i" aria-hidden="true">»</span><p><b>Post del archivo.</b> Se publicó originalmente en una versión anterior de inconsolata» y puede que algún elemento no se vea como debería. <a href="mailto:inconsolataweb@gmail.com?subject=Algo%20roto%20en%20un%20post">¿Ves algo roto? Avísame »</a></p></div>';
function idMenor(a,b){return a.length<b.length||(a.length===b.length&&a<b);}
function vecino(id,re,antes){var r=null;Object.keys(TIT).forEach(function(k){if(!re.test(TIT[k]))return;
 if(antes?idMenor(k,id)&&(!r||idMenor(r,k)):idMenor(id,k)&&(!r||idMenor(k,r)))r=k;});return r;}
function finRow(art){var sh=art.querySelector('.share'),sp=art.querySelector('.support');
 return '<div class="endrow"><div style="display:flex;flex-direction:column;gap:10px"><span class="caps">Compartir</span>'+(sh?sh.outerHTML:'')+'</div>'+(sp?sp.outerHTML:'')+'</div>';}


// ---------- «retahíla» final de enlaces a entregas anteriores de una serie → bloque de botones como el del EXTRA!
function esPost(a){return /inconsolata\.com\/post\/|^\/post\/|tumblr\.com\/post\//.test(a.getAttribute('href')||'');}
function serieDe(b,id){
 var ps=[].filter.call(b.querySelectorAll('p,div'),function(p){return !p.querySelector('img')&&[].filter.call(p.querySelectorAll('a[href]'),esPost).length>=3&&!p.closest('.fuente');});
 var p=ps[ps.length-1];if(!p)return null;
 var ls=[],h=p.innerHTML.replace(/<a\b[^>]*href="([^"]*)"[^>]*>([\s\S]*?)<\/a>/gi,function(m0,hr,tx){var d=document.createElement('div');d.innerHTML=tx;ls.push({h:hr.replace(/&amp;/g,'&'),t:d.textContent.replace(/\s+/g,' ').trim()});return '\u0001'+(ls.length-1)+'\u0002';});
 h=h.replace(/<br\s*\/?>/gi,'|');var d0=document.createElement('div');d0.innerHTML=h;var tx=d0.textContent.replace(/ /g,' ');
 var label='',rows=[{y:'',ls:[]}],antes=true,nr=function(){if(rows[rows.length-1].ls.length||rows[rows.length-1].y)rows.push({y:'',ls:[]});};
 tx.split(/(\u0001\d+\u0002)/).forEach(function(tk){
  var mm=tk.match(/^\u0001(\d+)\u0002$/);
  if(mm){var l=ls[+mm[1]];if(l&&l.t&&esPost({getAttribute:function(){return l.h;}})){l.cur=!!(id&&l.h.indexOf('/post/'+id)>=0);rows[rows.length-1].ls.push(l);antes=false;}return;}
  tk.split('|').forEach(function(seg,k){
   if(k>0)nr();
   var re=/(\d{4})\s*:/g,m,last=0,pre='';
   while((m=re.exec(seg))){if(antes&&!pre)pre=seg.slice(0,m.index);nr();rows[rows.length-1].y=m[1];last=re.lastIndex;}
   if(antes)label+=' '+(pre||(last?'':seg));
  });
 });
 rows=rows.filter(function(r){return r.ls.length;});
 if(!rows.length)return null;
 label=label.replace(/[…\.]+/g,' ').replace(/\s+de\s*$/,'').replace(/[:·\s]+$/,'').replace(/^\s*[»·\s]+/,'').trim()||'Entregas anteriores';
 // quita también un separador «…» suelto justo antes
 var pr=p.previousElementSibling;if(pr&&pr.tagName==='P'&&/^[\s…\.]*$/.test(pr.textContent)&&!pr.querySelector('img'))pr.remove();
 p.remove();
 return {label:label,rows:rows};
}
function serieHTML(sr){
 return '<section class="serie"><div class="caps">'+esc(sr.label)+' »</div>'+sr.rows.map(function(r){return '<div class="prev-row'+(r.y?' y':'')+'">'+(r.y?'<span class="yr">'+r.y+'</span>':'')+
  '<span class="ls">'+r.ls.map(function(l){return '<a href="'+esc(l.h)+'"'+(l.cur?' class="cur"':'')+'>'+esc(l.t)+'</a>';}).join('')+'</span></div>';}).join('')+'</section>';
}

// ---------- mucho más
function vMM(o){
 document.body.classList.add('v-mm');
 var b=o.body,id=o.id,d=o.d,cat=o.cat,ims=o.ims,n=ims.length;
 var num=((TIT[id]||'')+' '+b.textContent).replace(/ /g,' ').match(/semana\s+([IVXLCDM]+)/i);num=num?num[1].toUpperCase():'';
 var p1=[].find.call(b.querySelectorAll('p'),function(p){var t=p.textContent.trim();return t.length>60&&!/Trabajo\s*:/.test(t)&&!/^[…\.]+$/.test(t);});
 var intro=p1?p1.textContent.replace(/ /g,' ').trim().replace(/\s*[^.!?]*(tras el salto|salto de rigor)[^.!?]*[.!?:]?\s*$/i,'').trim():'';
 var def=o.tipos.length===1?o.tipos[0]:'info';
 var it=ims.map(function(im,i){
  var r={im:im,tr:'',au:[],md:'',fe:'',mo:null};
  if(im.el){var bl=bloque(im.el),nx=bl.nextElementSibling,k=0;
   // el pie es el siguiente párrafo con texto (saltando separadores de puntos y vacíos)
   while(nx&&k<4&&(nx.tagName!=='P'||!nx.textContent.replace(/[\s…\.\u00a0]/g,''))&&!nx.querySelector('img')){nx=nx.nextElementSibling;k++;}
   if(nx&&nx.tagName==='P'&&!nx.querySelector('img')&&nx.textContent.replace(/[\s…\.\u00a0]/g,'')){
    var tx=textoDe(nx),bb=nx.querySelector('b,strong');
    if(/Trabajo\s*:|Medio\s*:/.test(tx)){
     tx.split('|').forEach(function(f){var m=f.match(/^\s*(Trabajo|Autor(?:a|es|as)?|Medio)\s*:\s*(.*)$/i);if(!m)return;
      if(/^Trabajo/i.test(m[1]))r.tr=m[2].trim().replace(/\.$/,'');
      else if(/^Autor/i.test(m[1]))r.au=m[2].split(/\s+y\s+|,\s*/).map(function(a){return a.trim().replace(/\.$/,'');}).filter(Boolean);
      else{r.md=(bb?bb.textContent:m[2].split(',')[0]).trim();}});
    } else {
     // formato antiguo: una frase libre con el medio en negrita
     r.md=bb?bb.textContent.trim():'';var t0=tx.trim();
     var c0=t0.match(/^(.{8,140}?),\s+(el|del|durante|en)\s/);
     if(c0&&t0.length<220)r.tr=c0[1];else r.desc=nx.innerHTML;
    }
    var fm=tx.match(/(\d{1,2})\s+de\s+([a-záéíóú]+)/i);if(fm&&MESES.indexOf(fm[2].toLowerCase())>=0)r.fe=fm[1]+' de '+fm[2].toLowerCase();
   }}
  r.mo=medioPor(cat,r.md);r.tipo=tipoDe(r.tr||r.desc||'',def);return r;});
 var lb=it.map(function(r,i){return {src:r.im.src,cap:(r.md?r.md+' · ':'')+(r.tr||'imagen '+(i+1))+' · '+(i+1)+' de '+n};});
 var cover=n?[it[0],it[Math.floor(n/3)],it[n-1]].filter(function(x,i,a){return a.indexOf(x)===i;}):[];
 var hero='<section class="mm-hero"><div class="wrap inner"><div class="txt"><span class="caps" style="font-size:15px;letter-spacing:3px">La semana en infografías · '+rango(d)+'</span>'+
  '<h1 class="soft">mucho más »</h1><span class="num">semana '+num+'</span>'+(intro?'<p>'+esc(intro)+'</p>':'')+'</div>'+
  '<div class="cover-fan" aria-hidden="true">'+cover.map(function(r){return '<div class="cf"><img src="'+esc(r.im.el?srcDe(r.im.el,700):r.im.src)+'" alt="" onerror="this.remove()"></div>';}).join('')+'</div></div></section>';
 var th='<nav class="index" aria-label="Las '+n+' infografías de la semana"><div class="perf"></div><div class="thumbs" style="grid-template-columns:repeat('+Math.max(n,8)+',minmax(0,1fr))">'+
  it.map(function(r,i){return '<a href="#mm-'+(i+1)+'"><div class="t"><img loading="lazy" src="'+esc(r.im.el?srcDe(r.im.el,250):r.im.src)+'" alt="" onerror="this.remove()"></div><span>'+esc(r.md||('nº '+(i+1)))+'</span></a>';}).join('')+'</div><div class="perf"></div></nav>';
 var items=it.map(function(r,i){
  var al=(TN[r.tipo]||'Imagen')+(r.md?' de '+r.md:'')+(r.tr?': '+r.tr:'');
  var y=r.fe?anioDe(r.fe.split(' de ')[1],d):'';
  return '<article class="item'+(i%2?' alt':'')+'" id="mm-'+(i+1)+'" data-tipo="'+r.tipo+'"><button type="button" class="img" data-lb="'+i+'" aria-label="Ampliar: '+esc(r.tr||('imagen '+(i+1)))+'"><span class="tape" aria-hidden="true"></span><img loading="lazy" src="'+esc(r.im.src)+'" alt="'+esc(al)+'" onerror="this.remove()"><span class="zoom">Ampliar »</span></button>'+
   '<div class="txt">'+ico(r.tipo,'ico')+(r.md?(r.mo&&r.mo.ficha?'<a href="'+fichaMedio(r.mo)+'" class="medio">':'<span class="medio">')+(r.mo&&r.mo.av?'<span class="av" aria-hidden="true"><img src="'+r.mo.av+'" alt=""></span>':'')+esc(r.mo?r.mo.n:r.md)+(r.mo&&r.mo.ficha?'</a>':'</span>'):'')+
   (r.tr?'<h2>'+esc(r.tr)+'</h2>':'')+(r.desc?'<p class="desc">'+r.desc+'</p>':'')+(r.au.length?'<span class="by">por '+r.au.map(function(a){return '<a href="'+fichaAutor(a)+'">'+esc(a)+'</a>';}).join(' y ')+'</span>':'')+
   (r.fe?'<span class="when">'+esc(r.fe)+' de '+y+'</span>':'')+'</div></article>';}).join('');
 var cu={todas:n};it.forEach(function(r){cu[r.tipo]=(cu[r.tipo]||0)+1;});
 var prev=vecino(id,/^Mucho más/i,true),nextw=vecino(id,/^Mucho más/i,false);
 var pn=function(k,lab){if(!k)return '';var t=(TIT[k].match(/semana\s+([IVXLCDM]+)/i)||[])[1]||'';return '<a href="/post/'+k+'" class="pn"><span class="caps">'+lab+'</span><span class="big soft">'+t+'</span></a>';};
 var x=nuevoTop('mm-top');
 x.top.innerHTML=(d<LANZAMIENTO?'<div class="wrap">'+LEG+'</div>':'')+hero+(n?th:'')+(Object.keys(cu).length>2?'<div class="filters"><div class="wrap" id="filters"><span class="caps" style="margin-right:6px">Ver »</span></div></div>':'');
 x.main.innerHTML='<div id="items">'+items+'</div><section class="close">'+pn(prev,'« Semana anterior')+pn(nextw,'Semana siguiente »')+(o.art.querySelector('.support')?o.art.querySelector('.support').outerHTML:'')+'</section>';
 var fw=document.getElementById('filters');
 if(fw)['todas','info','carto','graf','ilus','port','foto'].forEach(function(t){if(!cu[t])return;var bt=document.createElement('button');bt.type='button';
  bt.setAttribute('aria-pressed',t==='todas'?'true':'false');bt.innerHTML=(t==='todas'?'Todas':ico(t)+esc(TN[t]))+' ('+cu[t]+')';
  bt.addEventListener('click',function(){[].forEach.call(fw.querySelectorAll('button'),function(z){z.setAttribute('aria-pressed','false');});bt.setAttribute('aria-pressed','true');
   [].forEach.call(document.querySelectorAll('.item'),function(z){z.hidden=!(t==='todas'||z.dataset.tipo===t);});});fw.appendChild(bt);});
 document.title='mucho más » semana '+num+' · inconsolata»';
 return lb;
}

// ---------- EXTRA!
function vX(o){
 document.body.classList.add('v-x');
 var b=o.body,id=o.id,d=o.d,cat=o.cat,ims=o.ims,n=ims.length;
 var nn=((TIT[id]||'').match(/(\d+)/)||(o.art.dataset.perm||'').match(/extra-?(\d+)/i)||[]);nn=nn[1]||'';
 var txt=b.textContent.replace(/ /g,' ');
 var pm=[].find.call(b.querySelectorAll('p'),function(p){return /destacamos|recopilaci|selecci[oó]n/i.test(p.textContent)&&!/EXTRA! es una secci/i.test(p.textContent);});
 var mm0=((pm?pm.textContent:txt)+' ').toLowerCase().match(new RegExp('\\b('+MESES.join('|')+')\\b'));var mes=mm0?mm0[1]:'';
 var pin=[].find.call(b.querySelectorAll('p'),function(p){return /EXTRA! es una secci/i.test(p.textContent);});
 var intro=pin?pin.textContent.trim():'EXTRA! es una sección mensual que recopila los mejores diseños en las páginas de la prensa nacional e internacional.';
 if(mes)intro=intro.replace(/\s*$/,'')+' Esta es la selección de '+mes+'.';
 var items=[];
 var sec=0;[].forEach.call(b.querySelectorAll('li'),function(li){var m=li.textContent.match(/^\s*\[(\d+)(?:\s*[-–]\s*(\d+))?\]/);
  if(!m){var ns=(li.textContent.match(/\((\d{1,2})\)/g)||[]).map(function(z){return +z.replace(/\D/g,'');});
   if(ns.length)m=[null,String(Math.min.apply(null,ns)),Math.max.apply(null,ns)>Math.min.apply(null,ns)?String(Math.max.apply(null,ns)):null];else{sec++;m=[null,String(sec),null];}}
  sec=+(m[2]||m[1]);
  var h=li.innerHTML.replace(/^\s*\[[^\]]*\]\s*/,''),bb=li.querySelector('b,strong'),md=bb?bb.textContent.trim():'';
  var fes=li.textContent.match(/\d{1,2}\s+de\s+[a-záéíóú]+/gi)||[],fe=(fes.length?fes[fes.length-1].match(/(\d{1,2})\s+de\s+([a-záéíóú]+)/i):[]);var fd=(li.textContent.match(/d[ií]a\s+(\d{1,2})/i)||[])[1];
  items.push({t:li.textContent.replace(/^\s*\[[^\]]*\]\s*/,'').trim(),a:+m[1],z:+(m[2]||m[1]),lab:'['+m[1]+(m[2]?'–'+m[2]:'')+']',bs:[].map.call(li.querySelectorAll('b,strong'),function(z){return z.textContent.trim();}),h:h,md:md,mo:medioPor(cat,md),fe:fe[1]&&MESES.indexOf(fe[2].toLowerCase())>=0?fe[1]+' de '+fe[2].toLowerCase():(fd&&mes?fd+' de '+mes:''),tipo:tipoDe(li.textContent,'info')});});
 var deI=function(i){return items.find(function(x){return i+1>=x.a&&i+1<=x.z;});};
 var lb=ims.map(function(im,i){var x=deI(i);return {src:im.src,txt:x?x.t:'',cap:(x?x.lab+' '+(x.mo?x.mo.n:x.md)+' · ':'')+'imagen '+(i+1)+' de '+n};});
 var fr=ims.map(function(im,i){var x=deI(i),l=x?'<span style="color:var(--accent)">'+esc(x.lab)+'</span> '+esc(x.mo?x.mo.n:x.md):'imagen '+(i+1);
  return '<button type="button" class="fr" data-lb="'+i+'" aria-label="Ampliar imagen '+(i+1)+'"><img loading="lazy" src="'+esc(im.el?srcDe(im.el,1280):im.src)+'" alt="'+esc(x?(x.mo?x.mo.n:x.md):'')+'" onerror="this.remove()"><span class="n">'+l+'</span></button>';}).join('');
 var idx=items.map(function(x){return '<li><span class="k-n'+(x.lab.length>4?' w':'')+'">'+esc(x.lab)+'</span><div><span class="md">'+(x.md?(x.mo&&x.mo.ficha?'<a href="'+fichaMedio(x.mo)+'" class="md-a">':'<span class="md-a">')+(x.mo&&x.mo.av?'<span class="av" aria-hidden="true"><img src="'+x.mo.av+'" alt=""></span>':'')+esc(x.mo?x.mo.n:x.md)+(x.mo&&x.mo.ficha?'</a>':'</span>'):'')+(x.fe?' · '+esc(x.fe):'')+'</span>'+
  '<div class="tx">'+x.h+'</div></div>'+ico(x.tipo)+'</li>';}).join('');
 var meds={};items.forEach(function(x){x.bs.forEach(function(z){if(z)meds[fold(z)]=1;});});
 // EXTRA! anteriores: los enlaces del final del post
 var pa=[].find.call(b.querySelectorAll('p'),function(p){return /EXTRA! anteriores/i.test(p.textContent);}),r1='',r2='';
 if(pa&&/EXTRA! anteriores/i.test(pa.textContent)){[].forEach.call(pa.querySelectorAll('a'),function(a){var t=a.textContent.trim(),h=a.getAttribute('href')||'',k=(h.match(/extra(\d+)/)||[])[1];
  if(/^\d{4}$/.test(t))r2+='<a class="yr" href="'+esc(h)+'">'+t+'</a>';else r1+='<a href="'+esc(h)+'">'+(k?'nº '+k+' · ':'')+esc(t)+'</a>';});}
 var sx='',srx=(!r1&&!r2)?serieDe(b,id):null;
 if(srx){var sx=srx.rows.map(function(r){return '<div class="prev-row'+(r.y?' y':'')+'">'+(r.y?'<span class="yr">'+r.y+'</span>':'')+'<span class="ls">'+r.ls.map(function(l){var k=(l.h.match(/extra-?(\d+)/i)||[])[1];return '<a href="'+esc(l.h)+'">'+(k?'nº '+k+' · ':'')+esc(l.t)+'</a>';}).join('')+'</span></div>';}).join('');}
 if(!r1){var c=id;for(var q=0;q<4;q++){c=vecino(c,/^EXTRA!/i,true);if(!c)break;r1+='<a href="/post/'+c+'">'+esc(TIT[c].replace(/^EXTRA!\s*/i,''))+'</a>';}}
 var x=nuevoTop('mm-top');
 x.top.innerHTML=(d<LANZAMIENTO?'<div class="wrap">'+LEG+'</div>':'')+'<section class="xhero"><div class="wrap inner"><div class="l">'+
  '<div class="crumbs caps" style="padding:0"><a href="/" style="color:#fff">Portada</a><i style="color:var(--yellow)">»</i><a href="/tagged/EXTRA!" style="color:#fff">EXTRA!</a></div>'+
  '<h1 class="xw" aria-label="EXTRA! número '+nn+'"><span aria-hidden="true">E</span><span aria-hidden="true">x</span><span aria-hidden="true">t</span><span aria-hidden="true">r</span><span aria-hidden="true">a</span><span aria-hidden="true">!</span></h1></div>'+
  '<div class="r"><span class="xnum">nº '+nn+'</span><p>'+esc(intro)+'</p><div class="meta">'+(mes?'<span>'+mes[0].toUpperCase()+mes.slice(1)+' de '+anioDe(mes,d)+'</span>':'<span>'+fecha(d)+'</span>')+(items.length?'<span>'+n+' piezas</span><span>'+Object.keys(meds).length+' medios</span>':'<span>'+n+' imágenes</span>')+'</div></div></div></section>';
 x.main.innerHTML='<section class="gal"><div class="gal-head"><span class="caps">Las páginas · '+n+'</span><span style="font-size:13px;font-weight:600">Pulsa para ampliar »</span></div><div class="masonry">'+fr+'</div></section>'+
  (idx?'<section class="idx"><div class="caps" style="margin-bottom:14px">En este EXTRA! »</div><ol>'+idx+'</ol></section>':'')+
  (sx?'<section class="prev"><div class="caps" style="border-top:2px solid var(--ink);padding-top:12px">EXTRA! anteriores »</div><div class="prev-row"><a class="cur" href="#">nº '+nn+(mes?' · '+mes:'')+'</a></div>'+sx+'</section>':'')+(!sx&&(r1||r2)?'<section class="prev"><div class="caps" style="border-top:2px solid var(--ink);padding-top:12px">EXTRA! anteriores »</div><div class="prev-row"><a class="cur" href="#">nº '+nn+(mes?' · '+mes:'')+'</a>'+r1+'</div>'+(r2?'<div class="prev-row">'+r2+'</div>':'')+'</section>':'')+
  finRow(o.art);
 document.title='EXTRA! nº '+nn+' · inconsolata»';
 return lb;
}

// ---------- metablog (posts de texto largos)
function vB(o){
 document.body.classList.add('v-b');
 var art=o.art,b=o.body,d=o.d,t=o.t;
 var tags=(art.dataset.tags||'').split('|').map(function(x){return x.trim().toLowerCase();});
 var badges=['metablog','offtopic','detallitos'].filter(function(x){return tags.indexOf(x)>=0;});if(!badges.length&&SECN[o.s])badges=[SECN[o.s]];
 // limpieza del cuerpo
 [].forEach.call(b.querySelectorAll('h1'),function(h){h.remove();});
 o.ims.forEach(function(im){if(!im.el)b.insertAdjacentHTML('afterbegin','<figure><img src="'+esc(im.src)+'" alt=""></figure>');});
 [].forEach.call(b.querySelectorAll('p'),function(p){if(!p.textContent.trim()&&!p.querySelector('img,iframe,video'))p.remove();});
 var srb=serieDe(b,o.id);
 var words=b.textContent.trim().split(/\s+/).length,mins=Math.max(1,Math.round(words/200));
 var lb=[],k=0,hero='',col=document.createElement('div');col.className='col';
 var shot=function(im){var i=k++;lb.push({src:srcDe(im,99999),cap:t+' · imagen '+(i+1)});return '<button type="button" class="fshot" data-lb="'+i+'" aria-label="Ampliar imagen '+(i+1)+'"><img loading="lazy" src="'+esc(srcDe(im,1280))+'" alt="" onerror="this.remove()"></button>';};
 var lead=false,cap=false,alt=0,heads=[];
 [].slice.call(b.childNodes).forEach(function(nd){
  if(nd.nodeType!==1){if(nd.nodeType===3&&nd.textContent.trim())col.insertAdjacentHTML('beforeend','<p>'+esc(nd.textContent)+'</p>');return;}
  var tg=nd.tagName,imgs=[].slice.call(nd.querySelectorAll('img'));
  if((nd.classList.contains('npf_row')||tg==='FIGURE'||(tg==='P'&&imgs.length&&!nd.textContent.trim()))&&imgs.length){
   if(!hero&&!lead){hero='<figure class="hero-one">'+shot(imgs[0])+'</figure>';imgs=imgs.slice(1);if(!imgs.length)return;}
   if(imgs.length>1){col.insertAdjacentHTML('beforeend','<figure class="pair" style="--n:'+Math.min(imgs.length,3)+'">'+imgs.map(shot).join('')+'</figure>');return;}
   col.insertAdjacentHTML('beforeend','<figure class="'+(alt++%2?'side-fig':'wide')+'">'+shot(imgs[0])+'</figure>');return;}
  if(tg==='BLOCKQUOTE'){if(/buymeacoffee|aportación/i.test(nd.textContent+nd.innerHTML))return;
   if(nd.classList.contains('npf_indented')){col.insertAdjacentHTML('beforeend','<aside class="note"><b>Nota al margen</b>'+nd.innerHTML+'</aside>');return;}
   col.insertAdjacentHTML('beforeend','<div class="pull"><p>'+esc(nd.textContent.trim())+'</p></div>');return;}
  if(/^H[2-6]$/.test(tg)){var a=nd.querySelector('a[href]');
   if(a&&/^\s*»/.test(nd.textContent)){var h=a.getAttribute('href');col.insertAdjacentHTML('beforeend','<a class="cta" href="'+esc(h)+'" target="_blank" rel="noopener"><b>'+esc(a.textContent.trim())+' »</b><span>Entrar</span></a>');return;}
   var hid='s-'+(heads.length+1);heads.push({id:hid,t:nd.textContent.replace(/^\s*»\s*/,'').trim()});
   col.insertAdjacentHTML('beforeend','<h2 id="'+hid+'"><i>»</i>'+esc(heads[heads.length-1].t)+'</h2>');return;}
  if(tg==='UL'){nd.className='ul';col.appendChild(nd);return;}
  if(tg==='P'){
   [].forEach.call(nd.querySelectorAll('b,strong'),function(x){if(x.textContent.trim()==='⩔'){var sp=x.closest('span')||x,br=sp.nextElementSibling;sp.remove();if(br&&br.tagName==='BR')br.remove();}});
   if(!nd.textContent.trim()&&!imgs.length)return;
   if(!lead&&nd.textContent.trim().length>40){nd.className='lead';lead=true;col.appendChild(nd);return;}
   if(lead&&!cap&&nd.textContent.trim().length>80){var w=document.createTreeWalker(nd,NodeFilter.SHOW_TEXT),x;while((x=w.nextNode())&&!x.nodeValue.trim());
    if(x){var v=x.nodeValue.replace(/^\s+/,'');var sp=document.createElement('span');sp.className='cap';sp.textContent=v[0];x.nodeValue=v.slice(1);x.parentNode.insertBefore(sp,x);cap=true;}}
  }
  col.appendChild(nd);
 });
 [].forEach.call(col.querySelectorAll('b'),function(x){if(!x.closest('a,.note,.cta,h2'))x.outerHTML='<strong>'+x.innerHTML+'</strong>';});
 if(srb)col.insertAdjacentHTML('beforeend',serieHTML(srb));
 if(o.tm)col.insertAdjacentHTML('beforeend','<div style="margin-top:30px">'+o.tm+'</div>');
 col.insertAdjacentHTML('beforeend','<div class="sign">'+ESPIRAL+'<div><span class="s">Saúl Castillo</span><small>inconsolata» · <a href="https://saulcastillo.es">saulcastillo.es</a></small></div></div>');
 var toc=heads.length>=2?'<aside class="toc" aria-label="En este post"><nav><span class="caps" style="margin-bottom:6px">En este post</span>'+heads.map(function(h){return '<a href="#'+h.id+'"><i>»</i>'+esc(h.t)+'</a>';}).join('')+'</nav></aside>':'';
 var leg=art.querySelector('.legacy'),endr=finRow(art);
 art.innerHTML=(d<LANZAMIENTO?'<div style="padding-top:20px">'+LEG+'</div>':'')+
  '<div class="crumbs caps"><a href="/">Portada</a><i>»</i><a href="/tagged/'+encodeURIComponent(badges[0]||'metablog')+'">'+esc(badges[0]||'metablog')+'</a></div>'+
  '<header class="mhead"><div class="badges">'+badges.map(function(x){return '<span class="badge">'+esc(x)+'</span>';}).join('')+'</div><h1 class="soft'+(t.length>60?' long':'')+'">'+destaca(t)+'</h1>'+
  '<div class="byline"><span>por Saúl Castillo</span><span>'+fecha(d)+'</span><span>'+mins+' minuto'+(mins>1?'s':'')+' de lectura</span></div></header>'+hero+
  '<article class="art">'+toc+'</article>'+endr;
 art.querySelector('.art').appendChild(col);
 if(!toc)col.style.margin='0 auto';
 var pnv=document.querySelector('nav.pn');if(pnv)pnv.remove();
 document.title=quita(t)+' · inconsolata»';
 return lb;
}
