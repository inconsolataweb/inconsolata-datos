(function(){function arranca(){

function initLB(list){
 var lb=document.getElementById('lb'), img=lb.querySelector('.lb-img'), st=lb.querySelector('.lb-stage'),
     cnt=lb.querySelector('.lb-count'), cap=lb.querySelector('.lb-cap'), cur=0, last=null, tx=null;
 function big(u){return u.replace(/\/s\d+x\d+\//,'/s2048x3072/');}
 function show(i){
  cur=(i+list.length)%list.length; lb.classList.remove('zoomed');
  
  img.setAttribute('s'+'rc',list[cur].src); img.alt=list[cur].cap;
  cnt.textContent=(cur+1)+' / '+list.length; cap.textContent=list[cur].cap; lb.querySelector('.lb-txt').textContent=list[cur].txt||'';
  lb.querySelectorAll('.lb-prev,.lb-next').forEach(function(b){b.hidden=list.length<2;});
 }
 function open(i){last=document.activeElement; show(i); lb.hidden=false; document.body.style.overflow='hidden'; lb.querySelector('.lb-close').focus();}
 function close(){lb.hidden=true; document.body.style.overflow=''; if(last) last.focus();}
 document.querySelectorAll('[data-lb]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault(); open(+b.getAttribute('data-lb'));});});
 lb.querySelector('.lb-close').addEventListener('click',close);
 lb.querySelectorAll('.lb-prev').forEach(function(b){b.addEventListener('click',function(){show(cur-1);});});
 lb.querySelectorAll('.lb-next').forEach(function(b){b.addEventListener('click',function(){show(cur+1);});});
 img.addEventListener('click',function(e){
  e.stopPropagation();
  if(lb.classList.contains('zoomed')){lb.classList.remove('zoomed');return;}
  var r=img.getBoundingClientRect();
  if(img.naturalWidth<=r.width*1.05 && img.naturalHeight<=r.height*1.05) return;
  var fx=(e.clientX-r.left)/r.width, fy=(e.clientY-r.top)/r.height;
  lb.classList.add('zoomed');
  requestAnimationFrame(function(){st.scrollLeft=fx*img.naturalWidth-st.clientWidth/2; st.scrollTop=fy*img.naturalHeight-st.clientHeight/2;});
 });
 st.addEventListener('click',function(e){if(e.target===st && !lb.classList.contains('zoomed')) close();});
 document.addEventListener('keydown',function(e){
  if(lb.hidden) return;
  if(e.key==='Escape') close();
  else if(e.key==='ArrowRight') show(cur+1);
  else if(e.key==='ArrowLeft') show(cur-1);
 });
 st.addEventListener('touchstart',function(e){tx=e.touches.length===1?e.touches[0].clientX:null;},{passive:true});
 st.addEventListener('touchend',function(e){
  if(tx===null || lb.classList.contains('zoomed')) return;
  var dx=e.changedTouches[0].clientX-tx; if(Math.abs(dx)>50) show(cur+(dx<0?1:-1)); tx=null;
 });
}


(function(){
// iconos: los del c\u00f3digo mandan sobre los que lleve pegados el tema (as\u00ed un icono nuevo no obliga a volver a pegarlo)
(function(){var d=document.createElement('div');d.innerHTML="<svg width=\"0\" height=\"0\" style=\"position:absolute\" aria-hidden=\"true\"><symbol id=\"i-info\" viewBox=\"0 0 64 64\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\"><path d=\"M26 16 A18 18 0 1 0 44 34 H26 Z\" fill=\"none\"/><path d=\"M32 10 A18 18 0 0 1 50 28 H32 Z\" fill=\"currentColor\"/></g></symbol><symbol id=\"i-carto\" viewBox=\"0 0 64 64\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M8 14 L24 8 L40 14 L56 8 V50 L40 56 L24 50 L8 56 Z\"/><path d=\"M24 8 V50 M40 14 V56\"/><circle cx=\"47\" cy=\"27\" r=\"4\" fill=\"currentColor\"/></g></symbol><symbol id=\"i-port\" viewBox=\"0 0 64 64\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><rect x=\"10\" y=\"8\" width=\"44\" height=\"50\"/><path d=\"M16 17 H48\" stroke-width=\"6\"/><path d=\"M16 28 H30 M16 35 H30 M16 42 H30 M16 49 H30\"/><rect x=\"35\" y=\"26\" width=\"13\" height=\"24\" fill=\"currentColor\"/></g></symbol><symbol id=\"i-graf\" viewBox=\"0 0 64 64\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"currentColor\"><path d=\"M6 56 H58\" fill=\"none\"/><rect x=\"11\" y=\"36\" width=\"10\" height=\"20\"/><rect x=\"27\" y=\"22\" width=\"10\" height=\"34\"/><rect x=\"43\" y=\"10\" width=\"10\" height=\"46\"/></g></symbol><symbol id=\"i-ilus\" viewBox=\"0 0 64 64\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M32 4 L48 30 L32 60 L16 30 Z\"/><path d=\"M32 60 V36\"/><circle cx=\"32\" cy=\"30\" r=\"4\" fill=\"currentColor\"/></g></symbol><symbol id=\"i-foto\" viewBox=\"0 0 64 64\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><rect x=\"6\" y=\"18\" width=\"52\" height=\"36\" rx=\"4\"/><path d=\"M22 18 L26 10 H38 L42 18\"/><circle cx=\"32\" cy=\"36\" r=\"11\"/><circle cx=\"32\" cy=\"36\" r=\"4\" fill=\"currentColor\"/></g></symbol><symbol id=\"i-video\" viewBox=\"0 0 64 64\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><rect x=\"6\" y=\"10\" width=\"52\" height=\"36\" rx=\"4\"/><path d=\"M27 20 L41 28 L27 36 Z\" fill=\"currentColor\"/><path d=\"M8 56 H56\"/><circle cx=\"22\" cy=\"56\" r=\"4\" fill=\"currentColor\"/></g></symbol><symbol id=\"i-publi\" viewBox=\"0 0 64 64\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M8 24 V40 H18 L42 52 V12 L18 24 Z\"/><path d=\"M18 40 L22 54 H30 L27 41\"/><path d=\"M50 22 L57 17 M50 32 H59 M50 42 L57 47\"/></g></symbol><symbol id=\"i-online\" viewBox=\"0 0 64 64\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><rect x=\"6\" y=\"8\" width=\"52\" height=\"44\" rx=\"3\"/><path d=\"M6 19 H58\"/><path d=\"M28 26 L28 47 L33 42 L37 51 L42 49 L38 40 L45 40 Z\" fill=\"currentColor\"/></g></symbol><symbol id=\"i-urna\" viewBox=\"0 0 64 64\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M22 30 V6 H42 V30\"/><path d=\"M27 16 L31 21 L38 12\"/><path d=\"M4 30 H60\"/><path d=\"M8 30 V58 H56 V30\"/><path d=\"M20 30 H44\" stroke-width=\"7\"/><rect x=\"22\" y=\"40\" width=\"20\" height=\"9\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-elecciones\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M22 30 V6 H42 V30\"/><path d=\"M27 16 L31 21 L38 12\"/><path d=\"M4 30 H60\"/><path d=\"M8 30 V58 H56 V30\"/><path d=\"M20 30 H44\" stroke-width=\"7\"/><rect x=\"22\" y=\"40\" width=\"20\" height=\"9\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-elecciones-en-eeuu\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M10 60 V6\"/><path d=\"M10 8 H54 V38 H10\"/><rect x=\"10\" y=\"8\" width=\"18\" height=\"15\" fill=\"currentColor\"/><path d=\"M28 16 H54 M28 24 H54 M10 31 H54\"/></g></symbol><symbol id=\"t-guerras-y-conflictos\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M14 14 L50 50 M50 14 L14 50\"/><path d=\"M38 54 L54 38 M10 38 L26 54\"/><circle cx=\"14\" cy=\"14\" r=\"4\" fill=\"currentColor\"/><circle cx=\"50\" cy=\"14\" r=\"4\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-guerra-en-ucrania\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><circle cx=\"32\" cy=\"24\" r=\"8\" fill=\"currentColor\"/><path d=\"M32 6 V10 M32 38 V42 M14 24 H18 M46 24 H50 M19 11 L22 14 M45 11 L42 14 M19 37 L22 34 M45 37 L42 34\"/><path d=\"M32 42 V60\"/><path d=\"M32 54 C24 52 20 48 18 44 C26 44 30 48 32 54\"/></g></symbol><symbol id=\"t-conflicto-palestino-israeli\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M10 56 C26 46 38 30 54 10\"/><path d=\"M22 47 C16 44 14 38 16 34 C21 37 23 42 22 47 Z\" fill=\"currentColor\"/><path d=\"M33 36 C34 30 39 26 44 26 C42 31 38 35 33 36 Z\" fill=\"currentColor\"/><path d=\"M40 26 C36 22 36 16 38 12 C42 16 42 21 40 26 Z\"/><path d=\"M27 41 C30 36 36 34 40 36 C36 40 31 42 27 41 Z\"/></g></symbol><symbol id=\"t-guerra-en-siria\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M8 58 H56\"/><path d=\"M14 58 V22 L22 16 L26 24 L32 14 L36 22 L42 18 L50 26 V58\"/><rect x=\"21\" y=\"32\" width=\"7\" height=\"8\" fill=\"currentColor\"/><rect x=\"36\" y=\"32\" width=\"7\" height=\"8\"/><path d=\"M28 58 V48 H36 V58\"/></g></symbol><symbol id=\"t-guerra-en-iran\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M32 4 C40 12 42 24 42 34 V46 H22 V34 C22 24 24 12 32 4 Z\"/><path d=\"M22 38 L12 50 V54 H22 M42 38 L52 50 V54 H42\"/><path d=\"M26 50 L32 60 L38 50 Z\" fill=\"currentColor\"/><circle cx=\"32\" cy=\"24\" r=\"4\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-terrorismo-y-atentados\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M32 4 L37 22 L54 14 L44 30 L60 36 L42 40 L48 58 L32 46 L16 58 L22 40 L4 36 L20 30 L10 14 L27 22 Z\"/><circle cx=\"32\" cy=\"32\" r=\"6\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-catastrofes-y-accidentes\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M4 34 H16 L22 14 L30 54 L38 20 L44 34 H60\"/><path d=\"M8 58 H56\" stroke-dasharray=\"2 8\"/></g></symbol><symbol id=\"t-covid-19\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><circle cx=\"32\" cy=\"32\" r=\"14\"/><circle cx=\"27\" cy=\"29\" r=\"3.5\" fill=\"currentColor\"/><circle cx=\"37\" cy=\"36\" r=\"3\" fill=\"currentColor\"/><path d=\"M32 18 V8 M32 46 V56 M18 32 H8 M46 32 H56 M22 22 L15 15 M42 42 L49 49 M42 22 L49 15 M22 42 L15 49\"/><circle cx=\"32\" cy=\"6\" r=\"3\" fill=\"currentColor\"/><circle cx=\"32\" cy=\"58\" r=\"3\" fill=\"currentColor\"/><circle cx=\"6\" cy=\"32\" r=\"3\" fill=\"currentColor\"/><circle cx=\"58\" cy=\"32\" r=\"3\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-salud\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M24 8 H40 V24 H56 V40 H40 V56 H24 V40 H8 V24 H24 Z\"/><path d=\"M14 32 H24 L28 24 L34 40 L38 32 H50\"/></g></symbol><symbol id=\"t-economia\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><circle cx=\"32\" cy=\"32\" r=\"24\"/><path d=\"M42 20 C38 16 34 15 30 16 C22 18 18 25 18 32 C18 39 22 46 30 48 C34 49 38 48 42 44\"/><path d=\"M12 28 H34 M12 36 H34\" stroke-width=\"5\"/></g></symbol><symbol id=\"t-europa\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><circle cx=\"47.3\" cy=\"42.0\" r=\"3.4\" fill=\"currentColor\"/><circle cx=\"40.0\" cy=\"49.3\" r=\"3.4\" fill=\"currentColor\"/><circle cx=\"30.0\" cy=\"52.0\" r=\"3.4\" fill=\"currentColor\"/><circle cx=\"20.0\" cy=\"49.3\" r=\"3.4\" fill=\"currentColor\"/><circle cx=\"12.7\" cy=\"42.0\" r=\"3.4\" fill=\"currentColor\"/><circle cx=\"10.0\" cy=\"32.0\" r=\"3.4\" fill=\"currentColor\"/><circle cx=\"12.7\" cy=\"22.0\" r=\"3.4\" fill=\"currentColor\"/><circle cx=\"20.0\" cy=\"14.7\" r=\"3.4\" fill=\"currentColor\"/><circle cx=\"30.0\" cy=\"12.0\" r=\"3.4\" fill=\"currentColor\"/><circle cx=\"40.0\" cy=\"14.7\" r=\"3.4\" fill=\"currentColor\"/><circle cx=\"47.3\" cy=\"22.0\" r=\"3.4\" fill=\"currentColor\"/><circle cx=\"58\" cy=\"30\" r=\"3.4\"/><path d=\"M48 32 H52\" stroke-width=\"2.5\"/></g></symbol><symbol id=\"t-politica-espanola\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M6 46 A26 26 0 0 1 58 46\"/><path d=\"M18 46 A14 14 0 0 1 46 46\"/><path d=\"M4 46 H60\"/><circle cx=\"12.0\" cy=\"46.0\" r=\"2.6\" fill=\"currentColor\"/><circle cx=\"14.7\" cy=\"36.0\" r=\"2.6\" fill=\"currentColor\"/><circle cx=\"22.0\" cy=\"28.7\" r=\"2.6\" fill=\"currentColor\"/><circle cx=\"32.0\" cy=\"26.0\" r=\"2.6\" fill=\"currentColor\"/><circle cx=\"42.0\" cy=\"28.7\" r=\"2.6\" fill=\"currentColor\"/><circle cx=\"49.3\" cy=\"36.0\" r=\"2.6\" fill=\"currentColor\"/><circle cx=\"52.0\" cy=\"46.0\" r=\"2.6\" fill=\"currentColor\"/><rect x=\"26\" y=\"50\" width=\"12\" height=\"9\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-monarquia-y-realeza\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M8 46 L6 18 L20 30 L32 10 L44 30 L58 18 L56 46 Z\"/><path d=\"M8 54 H56\"/><circle cx=\"32\" cy=\"34\" r=\"5\" fill=\"currentColor\"/><circle cx=\"6\" cy=\"16\" r=\"3\" fill=\"currentColor\"/><circle cx=\"58\" cy=\"16\" r=\"3\" fill=\"currentColor\"/><circle cx=\"32\" cy=\"8\" r=\"3\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-el-papa-y-el-vaticano\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M16 58 V30 C16 18 24 10 32 4 C40 10 48 18 48 30 V58 Z\"/><path d=\"M32 22 V44 M24 30 H40\" stroke-width=\"5\"/><path d=\"M16 50 H48\"/></g></symbol><symbol id=\"t-cataluna-y-el-proces\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><rect x=\"8\" y=\"10\" width=\"48\" height=\"44\"/><rect x=\"8\" y=\"16\" width=\"48\" height=\"5\" fill=\"currentColor\"/><rect x=\"8\" y=\"26\" width=\"48\" height=\"5\" fill=\"currentColor\"/><rect x=\"8\" y=\"36\" width=\"48\" height=\"5\" fill=\"currentColor\"/><rect x=\"8\" y=\"46\" width=\"48\" height=\"5\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-necrologicas\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><rect x=\"22\" y=\"30\" width=\"20\" height=\"28\"/><path d=\"M32 30 V24\"/><path d=\"M32 4 C38 12 40 16 38 20 C36 24 28 24 26 20 C24 16 26 12 32 4 Z\" fill=\"currentColor\"/><path d=\"M14 58 H50\"/></g></symbol><symbol id=\"t-historia\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M14 6 H50 M14 58 H50\"/><path d=\"M18 6 C18 22 30 26 30 32 C30 38 18 42 18 58 M46 6 C46 22 34 26 34 32 C34 38 46 42 46 58\"/><path d=\"M24 52 C26 46 30 44 32 44 C34 44 38 46 40 52 Z\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-resumenes-del-ano\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><rect x=\"8\" y=\"12\" width=\"48\" height=\"44\"/><path d=\"M8 24 H56\" stroke-width=\"7\"/><path d=\"M20 6 V16 M44 6 V16\"/><path d=\"M18 38 L23 34 V50\"/><path d=\"M32 38 C32 33 44 33 44 38 C44 42 33 45 32 50 H45\"/></g></symbol><symbol id=\"t-ciencia-y-espacio\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><circle cx=\"32\" cy=\"32\" r=\"14\" fill=\"currentColor\"/><ellipse cx=\"32\" cy=\"32\" rx=\"28\" ry=\"9\" transform=\"rotate(-20 32 32)\"/><circle cx=\"54\" cy=\"10\" r=\"2.5\" fill=\"currentColor\"/><circle cx=\"8\" cy=\"54\" r=\"2\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-clima-y-medio-ambiente\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M26 40 V10 C26 6 34 6 34 10 V40\"/><circle cx=\"30\" cy=\"48\" r=\"9\"/><circle cx=\"30\" cy=\"48\" r=\"5\" fill=\"currentColor\"/><path d=\"M30 44 V22\"/><path d=\"M42 14 H50 M42 22 H48 M42 30 H50\"/></g></symbol><symbol id=\"t-biodiversidad\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M12 52 C10 30 24 12 54 10 C54 38 38 54 12 52 Z\"/><path d=\"M12 52 L40 24 M22 42 H34 M30 34 V22\"/><circle cx=\"12\" cy=\"52\" r=\"3\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-viajes\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M30 6 C34 6 35 10 35 14 V26 L56 38 V44 L35 38 V50 L42 56 V60 L32 57 L22 60 V56 L29 50 V38 L8 44 V38 L29 26 V14 C29 10 30 6 30 6 Z\"/></g></symbol><symbol id=\"t-tecnologia\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><rect x=\"16\" y=\"16\" width=\"32\" height=\"32\"/><rect x=\"24\" y=\"24\" width=\"16\" height=\"16\" fill=\"currentColor\"/><path d=\"M24 16 V8 M32 16 V8 M40 16 V8 M24 48 V56 M32 48 V56 M40 48 V56 M16 24 H8 M16 32 H8 M16 40 H8 M48 24 H56 M48 32 H56 M48 40 H56\"/></g></symbol><symbol id=\"t-otros-deportes\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M18 8 H46 V22 C46 32 40 38 32 38 C24 38 18 32 18 22 Z\"/><path d=\"M18 14 H8 C8 24 12 28 18 28 M46 14 H56 C56 24 52 28 46 28\"/><path d=\"M32 38 V48\"/><rect x=\"20\" y=\"48\" width=\"24\" height=\"10\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-futbol\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><circle cx=\"32\" cy=\"32\" r=\"25\"/><path d=\"M32 22 L41 29 L38 40 H26 L23 29 Z\" fill=\"currentColor\"/><path d=\"M32 22 V8 M41 29 L55 25 M38 40 L46 52 M26 40 L18 52 M23 29 L9 25\"/></g></symbol><symbol id=\"t-juegos-olimpicos\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M22 22 H42 L36 58 H28 Z\"/><path d=\"M18 22 H46\"/><path d=\"M32 4 C40 10 40 16 36 20 H28 C24 16 24 10 32 4 Z\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-mundiales-y-eurocopas\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M6 54 V14 H58 V54\"/><path d=\"M6 14 L14 24 H50 L58 14 M14 24 V54 M50 24 V54\"/><path d=\"M14 34 H50 M14 44 H50 M26 24 V54 M38 24 V54\" stroke-width=\"2\"/><path d=\"M2 54 H62\"/></g></symbol><symbol id=\"t-motor-y-ciclismo\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M12 60 V6\"/><path d=\"M12 8 H54 V38 H12\"/><rect x=\"12\" y=\"8\" width=\"10.5\" height=\"7.5\" fill=\"currentColor\"/><rect x=\"33\" y=\"8\" width=\"10.5\" height=\"7.5\" fill=\"currentColor\"/><rect x=\"22.5\" y=\"15.5\" width=\"10.5\" height=\"7.5\" fill=\"currentColor\"/><rect x=\"43.5\" y=\"15.5\" width=\"10.5\" height=\"7.5\" fill=\"currentColor\"/><rect x=\"12\" y=\"23\" width=\"10.5\" height=\"7.5\" fill=\"currentColor\"/><rect x=\"33\" y=\"23\" width=\"10.5\" height=\"7.5\" fill=\"currentColor\"/><rect x=\"22.5\" y=\"30.5\" width=\"10.5\" height=\"7.5\" fill=\"currentColor\"/><rect x=\"43.5\" y=\"30.5\" width=\"10.5\" height=\"7.5\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-tenis\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><ellipse cx=\"26\" cy=\"24\" rx=\"16\" ry=\"18\" transform=\"rotate(-35 26 24)\"/><path d=\"M16 14 L36 34 M12 24 L28 40 M22 8 L40 26 M14 32 L36 12 M20 38 L40 18\" stroke-width=\"2\"/><path d=\"M36 38 L54 58\"/><circle cx=\"52\" cy=\"14\" r=\"6\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-cine\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M8 26 H56 V56 H8 Z\"/><path d=\"M8 26 L6 14 L54 6 L56 18 Z\"/><path d=\"M18 12 L24 22 M30 10 L36 20 M42 8 L48 18\" stroke-width=\"3.5\"/><path d=\"M20 38 H44 M20 46 H36\"/></g></symbol><symbol id=\"t-musica\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M24 48 V12 L54 6 V40\"/><path d=\"M24 20 L54 14\"/><ellipse cx=\"16\" cy=\"48\" rx=\"9\" ry=\"7\" fill=\"currentColor\"/><ellipse cx=\"46\" cy=\"40\" rx=\"9\" ry=\"7\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-television-y-series\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><rect x=\"6\" y=\"20\" width=\"52\" height=\"36\" rx=\"4\"/><path d=\"M22 6 L32 18 L44 4\"/><rect x=\"14\" y=\"28\" width=\"28\" height=\"20\" fill=\"currentColor\"/><circle cx=\"50\" cy=\"32\" r=\"2.5\" fill=\"currentColor\"/><circle cx=\"50\" cy=\"42\" r=\"2.5\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-libros-y-literatura\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M32 16 C24 10 14 10 6 12 V54 C14 52 24 52 32 58 C40 52 50 52 58 54 V12 C50 10 40 10 32 16 Z\"/><path d=\"M32 16 V58\"/><path d=\"M38 24 C44 22 48 22 52 23 M38 32 C44 30 48 30 52 31\" stroke-width=\"3\"/><path d=\"M12 20 C18 19 22 19 26 21 L26 40 C22 38 18 38 12 39 Z\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-arte-y-arquitectura\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M6 16 L32 4 L58 16 Z\" fill=\"currentColor\"/><path d=\"M8 16 H56 M8 56 H56 M4 60 H60\"/><path d=\"M14 22 V50 M26 22 V50 M38 22 V50 M50 22 V50\"/></g></symbol><symbol id=\"t-gastronomia\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M16 6 V22 C16 28 26 28 26 22 V6 M21 6 V60\"/><path d=\"M44 60 V6 C52 10 54 22 52 34 H44\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-redisenos\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M44 6 L58 20 L22 56 L6 58 L8 42 Z\"/><path d=\"M38 12 L52 26\"/><path d=\"M8 42 L22 56\" stroke-width=\"3\"/><path d=\"M6 58 L14 50\" stroke-width=\"6\"/><rect x=\"34\" y=\"44\" width=\"22\" height=\"14\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-tipografia\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M4 56 L20 10 H24 L40 56\"/><path d=\"M10 40 H34\"/><path d=\"M0 56 H12 M32 56 H44\"/><circle cx=\"51\" cy=\"47\" r=\"8\" fill=\"currentColor\"/><path d=\"M59 34 V56\"/></g></symbol><symbol id=\"t-humor-grafico\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M8 10 H56 V42 H30 L16 56 V42 H8 Z\"/><circle cx=\"22\" cy=\"26\" r=\"3.5\" fill=\"currentColor\"/><circle cx=\"32\" cy=\"26\" r=\"3.5\" fill=\"currentColor\"/><circle cx=\"42\" cy=\"26\" r=\"3.5\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-titulares\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><rect x=\"6\" y=\"8\" width=\"52\" height=\"48\"/><rect x=\"12\" y=\"14\" width=\"40\" height=\"12\" fill=\"currentColor\"/><path d=\"M12 34 H52 M12 42 H52 M12 50 H36\" stroke-width=\"3\"/></g></symbol><symbol id=\"t-industria-y-crisis-de-medios\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M6 12 H46 V56 H12 C8 56 6 54 6 50 Z\"/><path d=\"M46 22 H56 V50 C56 54 54 56 50 56 H46\"/><path d=\"M12 20 H40\" stroke-width=\"6\"/><path d=\"M14 32 L22 40 L30 34 L38 46\"/><path d=\"M32 46 H38 V40\" fill=\"currentColor\"/></g></symbol><symbol id=\"t-datos-y-visualizacion\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M8 6 V56 H58\"/><circle cx=\"18\" cy=\"44\" r=\"4\" fill=\"currentColor\"/><circle cx=\"28\" cy=\"34\" r=\"4\" fill=\"currentColor\"/><circle cx=\"38\" cy=\"38\" r=\"4\" fill=\"currentColor\"/><circle cx=\"48\" cy=\"18\" r=\"4\" fill=\"currentColor\"/><path d=\"M14 50 L56 12\" stroke-width=\"2.5\" stroke-dasharray=\"4 5\"/></g></symbol><symbol id=\"t-urna\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><path d=\"M22 30 V6 H42 V30\"/><path d=\"M27 16 L31 21 L38 12\"/><path d=\"M4 30 H60\"/><path d=\"M8 30 V58 H56 V30\"/><path d=\"M20 30 H44\" stroke-width=\"7\"/></g></symbol><symbol id=\"t-tren\" viewBox=\"0 0 64 64\" overflow=\"visible\"><g stroke=\"currentColor\" stroke-width=\"4\" stroke-linejoin=\"round\" stroke-linecap=\"round\" fill=\"none\"><rect x=\"15\" y=\"5\" width=\"34\" height=\"40\" rx=\"9\"/><rect x=\"21\" y=\"12\" width=\"22\" height=\"12\" rx=\"2\" fill=\"currentColor\"/><circle cx=\"23\" cy=\"35\" r=\"3\" fill=\"currentColor\"/><circle cx=\"41\" cy=\"35\" r=\"3\" fill=\"currentColor\"/><path d=\"M22 45 L15 57 M42 45 L49 57\"/><path d=\"M6 57 H58\"/><path d=\"M18 51 H46\" stroke-width=\"3\"/></g></symbol></svg>";var sv=d.querySelector('svg');if(!sv)return;[].forEach.call(sv.querySelectorAll('symbol'),function(x){var o=document.getElementById(x.id);if(o)o.remove();});(document.body||document.documentElement).insertBefore(sv,(document.body||document.documentElement).firstChild);})();
(function(){var B=(window.INC_BASE||'https://cdn.jsdelivr.net/gh/inconsolataweb/inconsolata-datos@main/')+'assets/marca/';if(!document.querySelector('link[href*="assets/marca/"]')){[].forEach.call(document.querySelectorAll('link[rel~="icon"],link[rel="apple-touch-icon"]'),function(l){l.remove();});document.head.insertAdjacentHTML('beforeend','<link rel="icon" href="'+B+'favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="'+B+'favicon-32.png"><link rel="apple-touch-icon" href="'+B+'apple-touch-icon.png">');}})();
(function(){if(!document.querySelector('link[href*="Instrument+Sans"]'))document.head.insertAdjacentHTML('beforeend','<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&display=swap">');})();
(function(){var y=document.getElementById('y-now');if(y)y.textContent=new Date().getFullYear();})();
var CDN=(window.INC_BASE||'https://cdn.jsdelivr.net/gh/inconsolataweb/inconsolata-datos@main/')+'datos/';
var LANZAMIENTO='2026-10-27';
var TN={"info": "Infograf\u00eda", "carto": "Cartograf\u00eda", "port": "Portada", "graf": "Gr\u00e1fico", "ilus": "Ilustraci\u00f3n", "foto": "Fotograf\u00eda", "video": "V\u00eddeo", "publi": "Publicidad", "online": "Online"}, TS=["t-elecciones", "t-elecciones-en-eeuu", "t-guerras-y-conflictos", "t-guerra-en-ucrania", "t-conflicto-palestino-israeli", "t-guerra-en-siria", "t-guerra-en-iran", "t-terrorismo-y-atentados", "t-catastrofes-y-accidentes", "t-covid-19", "t-salud", "t-economia", "t-europa", "t-monarquia-y-realeza", "t-el-papa-y-el-vaticano", "t-cataluna-y-el-proces", "t-necrologicas", "t-historia", "t-resumenes-del-ano", "t-ciencia-y-espacio", "t-clima-y-medio-ambiente", "t-biodiversidad", "t-viajes", "t-tecnologia", "t-otros-deportes", "t-futbol", "t-juegos-olimpicos", "t-mundiales-y-eurocopas", "t-motor-y-ciclismo", "t-tenis", "t-cine", "t-musica", "t-television-y-series", "t-libros-y-literatura", "t-arte-y-arquitectura", "t-gastronomia", "t-redisenos", "t-tipografia", "t-humor-grafico", "t-titulares", "t-industria-y-crisis-de-medios", "t-datos-y-visualizacion", "t-politica-espanola"], SECN={m:'mucho m\u00e1s',x:'EXTRA!',d:'detallitos',b:'metablog',o:'offtopic'};
var MESES=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'];
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function get(f){var k='inc-'+f;try{var c=JSON.parse(sessionStorage.getItem(k)||'null');if(c)return Promise.resolve(c);}catch(e){}
 return fetch(CDN+f+'.json').then(function(r){return r.json();}).then(function(j){try{sessionStorage.setItem(k,JSON.stringify(j));}catch(e){}return j;});}
function fecha(d){return +d.slice(8,10)+' de '+MESES[+d.slice(5,7)-1]+' de '+d.slice(0,4);}
function ico(k,cls){return '<svg class="'+(cls||'')+'" viewBox="0 0 64 64" role="img" aria-label="'+esc(TN[k])+'" style="overflow:visible"><title>'+esc(TN[k])+'</title><use href="#i-'+k+'" class="k"/><use href="#i-'+k+'" class="m" x="3" y="2.5"/></svg>';}
var TIT={},AJ={};
// ------------------------------------------------------------------ vistas especiales (mucho m\u00e1s, EXTRA!, metablog)
var MES3=['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'];
var STOP=' a al ante bajo con contra de del desde durante el en entre hacia hasta la las lo los para por que qu\u00e9 se seg\u00fan sin sobre su sus tras un una unos unas y o e u ni como c\u00f3mo cuando d\u00f3nde donde es son est\u00e1 est\u00e1n m\u00e1s muy the of and to in for on with ';
function fold(s){return String(s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/^the\s+/,'').replace(/[^a-z0-9]+/g,' ').trim();}
function medioPor(cat,n){var f=fold(n);if(!f)return null;return cat.medios.find(function(m){return fold(m.n)===f;})||cat.medios.find(function(m){var g=fold(m.n);return g.length>3&&(f.indexOf(g)===0||g.indexOf(f)===0);})||null;}
// T\u00edtulo con la palabra destacada en magenta: *palabra* manda; si no, una palabra en may\u00fasculas o la m\u00e1s larga
function destaca(t){
 if(/\*[^*]+\*/.test(t))return esc(t).replace(/\*([^*]+)\*/,'<em>$1</em>').replace(/\*/g,'');
 var ws=t.split(/(\s+)/),best=-1,bl=0;
 ws.forEach(function(w,i){var c=w.replace(/[\u00ab\u00bb"\u201c\u201d.,:;!?\u00bf\u00a1()]/g,'');if(c.length>=4&&c===c.toUpperCase()&&/[A-Z\u00c1\u00c9\u00cd\u00d3\u00da\u00d1]/.test(c)&&!/^[IVXLCDM]+$/.test(c)&&best<0)best=i;});
 if(best<0)ws.forEach(function(w,i){var c=w.replace(/[\u00ab\u00bb"\u201c\u201d.,:;!?\u00bf\u00a1()]/g,'');if(c.length>bl&&c.length>=5&&STOP.indexOf(' '+c.toLowerCase()+' ')<0&&!/^[A-Z\u00c1\u00c9\u00cd\u00d3\u00da\u00d1]/.test(c)){bl=c.length;best=i;}});
 return ws.map(function(w,i){if(i!==best)return esc(w);var m=w.match(/^([\u00ab"\u201c(\u00bf\u00a1]*)(.*?)([\u00bb"\u201d.,:;!?)]*)$/);return esc(m[1])+'<em>'+esc(m[2])+'</em>'+esc(m[3]);}).join('');
}
function quita(t){return String(t||'').replace(/\*/g,'');}
function rango(d){var b=new Date(d+'T12:00:00');b=new Date(b.getTime()-b.getDay()*864e5);var a=new Date(b.getTime()-6*864e5); // la semana acaba el domingo anterior o igual a la fecha
 return a.getMonth()===b.getMonth()?a.getDate()+'\u2013'+b.getDate()+' '+MES3[b.getMonth()]+' '+b.getFullYear():a.getDate()+' '+MES3[a.getMonth()]+'\u2013'+b.getDate()+' '+MES3[b.getMonth()]+' '+b.getFullYear();}
function anioDe(mes,d){var i=MESES.indexOf(String(mes).toLowerCase());var y=+d.slice(0,4);return (i>=0&&i+1>+d.slice(5,7))?y-1:y;}
function tipoDe(t,def){t=t.toLowerCase();
 if(/portad/.test(t))return 'port';if(/\bmapas?\b|cartogr|\brutas?\b|\bd\u00f3nde\b|territori/.test(t))return 'carto';
 if(/ilustra|dibuj|vi\u00f1eta|c\u00f3mic/.test(t))return 'ilus';if(/gr\u00e1fic|datos|evoluci|cifras|aumento|subida|precios|encuesta|ranking/.test(t))return 'graf';
 if(/fotogra/.test(t))return 'foto';return def||'info';}
// tipo indicado a mano en la pieza: \u00abTipo: cartograf\u00eda\u00bb
function tipoExpl(t){var m=String(t||'').match(/\bTipo\s*:\s*([^|\n;]+)/i);if(!m)return '';var w=m[1].toLowerCase().trim();
 var L=[['info',/^infograf/],['carto',/^cartograf|^mapa/],['graf',/^gr[a\u00e1]fic/],['port',/^portad/],['ilus',/^ilustraci/],['foto',/^fotograf/],['video',/^v[i\u00ed]deo/],['publi',/^publicidad/],['online',/^(online|interactiv)/]];
 for(var i=0;i<L.length;i++)if(L[i][1].test(w))return L[i][0];return '';}
// subrayador blanco: <palabras> en el texto de los posts nuevos
function subraya(root){var w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT),L=[],x;while((x=w.nextNode())){if(/<[^<>\s][^<>]{0,118}>/.test(x.nodeValue)&&!x.parentNode.closest('a,code,pre,.fuente'))L.push(x);}
 L.forEach(function(n){var f=document.createDocumentFragment(),t=n.nodeValue,re=/<([^<>\s][^<>]{0,118})>/g,i=0,m;
  while((m=re.exec(t))){if(m.index>i)f.appendChild(document.createTextNode(t.slice(i,m.index)));var k=document.createElement('mark');k.className='subr';k.textContent=m[1];f.appendChild(k);i=m.index+m[0].length;}
  if(i<t.length)f.appendChild(document.createTextNode(t.slice(i)));n.parentNode.replaceChild(f,n);});}
function bloque(el){return el.closest('.npf_row')||(el.closest('p')&&el.closest('.body')!==el.closest('p')?el.closest('p'):null)||el.closest('figure')||el;}
function textoDe(el){var t=document.createElement('div');t.innerHTML=el.innerHTML.replace(/<br\s*\/?>/gi,' | ');return t.textContent.replace(/\u00a0/g,' ');}
function nuevoTop(cls){var main=document.querySelector('main.wrap'),top=document.createElement('div');top.className=cls;main.parentNode.insertBefore(top,main);return {main:main,top:top};}
var LEG='<div class="legacy" role="note"><span class="lg-i" aria-hidden="true">\u00bb</span><p><b>Post del archivo.</b> Se public\u00f3 originalmente en una versi\u00f3n anterior de inconsolata\u00bb y puede que alg\u00fan elemento no se vea como deber\u00eda. <a href="mailto:inconsolataweb@gmail.com?subject=Algo%20roto%20en%20un%20post">\u00bfVes algo roto? Av\u00edsame \u00bb</a></p></div>';
function idMenor(a,b){return a.length<b.length||(a.length===b.length&&a<b);}
function vecino(id,re,antes){var r=null;Object.keys(TIT).forEach(function(k){if(!re.test(TIT[k]))return;
 if(antes?idMenor(k,id)&&(!r||idMenor(r,k)):idMenor(id,k)&&(!r||idMenor(k,r)))r=k;});return r;}
function finRow(art){var sh=art.querySelector('.share'),sp=art.querySelector('.support');
 return '<div class="endrow"><div style="display:flex;flex-direction:column;gap:10px"><span class="caps">Compartir</span>'+(sh?sh.outerHTML:'')+'</div>'+(sp?sp.outerHTML:'')+'</div>';}


// ---------- \u00abretah\u00edla\u00bb final de enlaces a entregas anteriores de una serie \u2192 bloque de botones como el del EXTRA!
function esPost(a){return /inconsolata\.com\/post\/|^\/post\/|tumblr\.com\/post\//.test(a.getAttribute('href')||'');}
function serieDe(b,id){
 var ps=[].filter.call(b.querySelectorAll('p,div'),function(p){return !p.querySelector('img')&&[].filter.call(p.querySelectorAll('a[href]'),esPost).length>=3&&!p.closest('.fuente');});
 var p=ps[ps.length-1];if(!p)return null;
 var ls=[],h=p.innerHTML.replace(/<a\b[^>]*href="([^"]*)"[^>]*>([\s\S]*?)<\/a>/gi,function(m0,hr,tx){var d=document.createElement('div');d.innerHTML=tx;ls.push({h:hr.replace(/&amp;/g,'&'),t:d.textContent.replace(/\s+/g,' ').trim()});return '\u0001'+(ls.length-1)+'\u0002';});
 h=h.replace(/<br\s*\/?>/gi,'|');var d0=document.createElement('div');d0.innerHTML=h;var tx=d0.textContent.replace(/\u00a0/g,' ');
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
 label=label.replace(/[\u2026\.]+/g,' ').replace(/\s+de\s*$/,'').replace(/[:\u00b7\s]+$/,'').replace(/^\s*[\u00bb\u00b7\s]+/,'').trim()||'Entregas anteriores';
 // quita tambi\u00e9n un separador \u00ab\u2026\u00bb suelto justo antes
 var pr=p.previousElementSibling;if(pr&&pr.tagName==='P'&&/^[\s\u2026\.]*$/.test(pr.textContent)&&!pr.querySelector('img'))pr.remove();
 p.remove();
 return {label:label,rows:rows};
}
function serieHTML(sr){
 return '<section class="serie"><div class="caps">'+esc(sr.label)+' \u00bb</div>'+sr.rows.map(function(r){return '<div class="prev-row'+(r.y?' y':'')+'">'+(r.y?'<span class="yr">'+r.y+'</span>':'')+
  '<span class="ls">'+r.ls.map(function(l){return '<a href="'+esc(l.h)+'"'+(l.cur?' class="cur"':'')+'>'+esc(l.t)+'</a>';}).join('')+'</span></div>';}).join('')+'</section>';
}

// ---------- mucho m\u00e1s
function vMM(o){
 document.body.classList.add('v-mm');
 var b=o.body,id=o.id,d=o.d,cat=o.cat,ims=o.ims,n=ims.length;
 var num=((TIT[id]||'')+' '+b.textContent).replace(/\u00a0/g,' ').match(/semana\s+([IVXLCDM]+)/i);num=num?num[1].toUpperCase():'';
 var p1=[].find.call(b.querySelectorAll('p'),function(p){var t=p.textContent.trim();return t.length>60&&!/Trabajo\s*:/.test(t)&&!/^[\u2026\.]+$/.test(t);});
 var intro=p1?p1.textContent.replace(/\u00a0/g,' ').trim().replace(/\s*[^.!?]*(tras el salto|salto de rigor)[^.!?]*[.!?:]?\s*$/i,'').trim():'';
 var def=o.tipos.length===1?o.tipos[0]:'info';
 var it=ims.map(function(im,i){
  var r={im:im,tr:'',au:[],md:'',fe:'',mo:null};
  if(im.el){var bl=bloque(im.el),nx=bl.nextElementSibling,k=0;
   // el pie es el siguiente p\u00e1rrafo con texto (saltando separadores de puntos y vac\u00edos)
   while(nx&&k<4&&(nx.tagName!=='P'||!nx.textContent.replace(/[\s\u2026\.\u00a0]/g,''))&&!nx.querySelector('img')){nx=nx.nextElementSibling;k++;}
   if(nx&&nx.tagName==='P'&&!nx.querySelector('img')&&nx.textContent.replace(/[\s\u2026\.\u00a0]/g,'')){
    var tx=textoDe(nx),bb=nx.querySelector('b,strong');
    if(/Trabajo\s*:|Medio\s*:/.test(tx)){
     tx.split('|').forEach(function(f){var m=f.match(/^\s*(Trabajo|Autor(?:a|es|as)?|Medio|Tipo)\s*:\s*(.*)$/i);if(!m)return;
      if(/^Tipo/i.test(m[1])){r.tp=tipoExpl('Tipo: '+m[2]);return;}
      if(/^Trabajo/i.test(m[1]))r.tr=m[2].trim().replace(/\.$/,'');
      else if(/^Autor/i.test(m[1]))r.au=m[2].split(/\s+y\s+|,\s*/).map(function(a){return a.trim().replace(/\.$/,'');}).filter(Boolean);
      else{r.md=(bb?bb.textContent:m[2].split(',')[0]).trim();}});
    } else {
     // formato antiguo: una frase libre con el medio en negrita
     r.md=bb?bb.textContent.trim():'';var t0=tx.trim();
     var c0=t0.match(/^(.{8,140}?),\s+(el|del|durante|en)\s/);
     if(c0&&t0.length<220)r.tr=c0[1];else r.desc=nx.innerHTML;
    }
    var fm=tx.match(/(\d{1,2})\s+de\s+([a-z\u00e1\u00e9\u00ed\u00f3\u00fa]+)/i);if(fm&&MESES.indexOf(fm[2].toLowerCase())>=0)r.fe=fm[1]+' de '+fm[2].toLowerCase();
   }}
  r.mo=medioPor(cat,r.md);r.tipo=r.tp||tipoDe(r.tr||r.desc||'',def);return r;});
 var lb=it.map(function(r,i){return {src:r.im.src,cap:(r.md?r.md+' \u00b7 ':'')+(r.tr||'imagen '+(i+1))+' \u00b7 '+(i+1)+' de '+n};});
 var cover=n?[it[0],it[Math.floor(n/3)],it[n-1]].filter(function(x,i,a){return a.indexOf(x)===i;}):[];
 var hero='<section class="mm-hero"><div class="wrap inner"><div class="txt"><span class="caps" style="font-size:15px;letter-spacing:3px">La semana en infograf\u00edas \u00b7 '+rango(d)+'</span>'+
  '<h1 class="soft">mucho m\u00e1s \u00bb</h1><span class="num">semana '+num+'</span>'+(intro?'<p>'+esc(intro)+'</p>':'')+'</div>'+
  '<div class="cover-fan" aria-hidden="true">'+cover.map(function(r){return '<div class="cf"><img src="'+esc(r.im.el?srcDe(r.im.el,700):r.im.src)+'" alt="" onerror="this.remove()"></div>';}).join('')+'</div></div></section>';
 var th='<nav class="index" aria-label="Las '+n+' infograf\u00edas de la semana"><div class="perf"></div><div class="thumbs" style="grid-template-columns:repeat('+Math.max(n,8)+',minmax(0,1fr))">'+
  it.map(function(r,i){return '<a href="#mm-'+(i+1)+'"><div class="t"><img loading="lazy" src="'+esc(r.im.el?srcDe(r.im.el,250):r.im.src)+'" alt="" onerror="this.remove()"></div><span>'+esc(r.md||('n\u00ba '+(i+1)))+'</span></a>';}).join('')+'</div><div class="perf"></div></nav>';
 var items=it.map(function(r,i){
  var al=(TN[r.tipo]||'Imagen')+(r.md?' de '+r.md:'')+(r.tr?': '+r.tr:'');
  var y=r.fe?anioDe(r.fe.split(' de ')[1],d):'';
  return '<article class="item'+(i%2?' alt':'')+'" id="mm-'+(i+1)+'" data-tipo="'+r.tipo+'"><button type="button" class="img" data-lb="'+i+'" aria-label="Ampliar: '+esc(r.tr||('imagen '+(i+1)))+'"><span class="tape" aria-hidden="true"></span><img loading="lazy" src="'+esc(r.im.src)+'" alt="'+esc(al)+'" onerror="this.remove()"><span class="zoom">Ampliar \u00bb</span></button>'+
   '<div class="txt">'+ico(r.tipo,'ico')+(r.md?(r.mo&&r.mo.ficha?'<a href="'+fichaMedio(r.mo)+'" class="medio">':'<span class="medio">')+(r.mo&&r.mo.av?'<span class="av" aria-hidden="true"><img src="'+r.mo.av+'" alt=""></span>':'')+esc(r.mo?r.mo.n:r.md)+(r.mo&&r.mo.ficha?'</a>':'</span>'):'')+
   (r.tr?'<h2>'+esc(r.tr)+'</h2>':'')+(r.desc?'<p class="desc">'+r.desc+'</p>':'')+(r.au.length?'<span class="by">por '+r.au.map(function(a){return '<a href="'+fichaAutor(a)+'">'+esc(a)+'</a>';}).join(' y ')+'</span>':'')+
   (r.fe?'<span class="when">'+esc(r.fe)+' de '+y+'</span>':'')+'</div></article>';}).join('');
 var cu={todas:n};it.forEach(function(r){cu[r.tipo]=(cu[r.tipo]||0)+1;});
 var prev=vecino(id,/^Mucho m\u00e1s/i,true),nextw=vecino(id,/^Mucho m\u00e1s/i,false);
 var pn=function(k,lab){if(!k)return '';var t=(TIT[k].match(/semana\s+([IVXLCDM]+)/i)||[])[1]||'';return '<a href="/post/'+k+'" class="pn"><span class="caps">'+lab+'</span><span class="big soft">'+t+'</span></a>';};
 var x=nuevoTop('mm-top');
 x.top.innerHTML=(d<LANZAMIENTO?'<div class="wrap">'+LEG+'</div>':'')+hero+(n?th:'')+(Object.keys(cu).length>2?'<div class="filters"><div class="wrap" id="filters"><span class="caps" style="margin-right:6px">Ver \u00bb</span></div></div>':'');
 x.main.innerHTML='<div id="items">'+items+'</div><section class="close">'+pn(prev,'\u00ab Semana anterior')+pn(nextw,'Semana siguiente \u00bb')+(o.art.querySelector('.support')?o.art.querySelector('.support').outerHTML:'')+'</section>';
 var fw=document.getElementById('filters');
 if(fw)['todas','info','carto','graf','ilus','port','foto'].forEach(function(t){if(!cu[t])return;var bt=document.createElement('button');bt.type='button';
  bt.setAttribute('aria-pressed',t==='todas'?'true':'false');bt.innerHTML=(t==='todas'?'Todas':ico(t)+esc(TN[t]))+' ('+cu[t]+')';
  bt.addEventListener('click',function(){[].forEach.call(fw.querySelectorAll('button'),function(z){z.setAttribute('aria-pressed','false');});bt.setAttribute('aria-pressed','true');
   [].forEach.call(document.querySelectorAll('.item'),function(z){z.hidden=!(t==='todas'||z.dataset.tipo===t);});});fw.appendChild(bt);});
 document.title='mucho m\u00e1s \u00bb semana '+num+' \u00b7 inconsolata\u00bb';
 return lb;
}

// ---------- EXTRA!
function vX(o){
 document.body.classList.add('v-x');
 var b=o.body,id=o.id,d=o.d,cat=o.cat,ims=o.ims,n=ims.length;
 var nn=((TIT[id]||'').match(/(\d+)/)||(o.art.dataset.perm||'').match(/extra-?(\d+)/i)||[]);nn=nn[1]||'';
 var txt=b.textContent.replace(/\u00a0/g,' ');
 var pm=[].find.call(b.querySelectorAll('p'),function(p){return /destacamos|recopilaci|selecci[o\u00f3]n/i.test(p.textContent)&&!/EXTRA! es una secci/i.test(p.textContent);});
 var mm0=((pm?pm.textContent:txt)+' ').toLowerCase().match(new RegExp('\\b('+MESES.join('|')+')\\b'));var mes=mm0?mm0[1]:'';
 var pin=[].find.call(b.querySelectorAll('p'),function(p){return /EXTRA! es una secci/i.test(p.textContent);});
 var intro=pin?pin.textContent.trim():'EXTRA! es una secci\u00f3n mensual que recopila los mejores dise\u00f1os en las p\u00e1ginas de la prensa nacional e internacional.';
 if(mes)intro=intro.replace(/\s*$/,'')+' Esta es la selecci\u00f3n de '+mes+'.';
 var items=[];
 var sec=0;[].forEach.call(b.querySelectorAll('li'),function(li){var m=li.textContent.match(/^\s*\[(\d+)(?:\s*[-\u2013]\s*(\d+))?\]/);
  if(!m){var ns=(li.textContent.match(/\((\d{1,2})\)/g)||[]).map(function(z){return +z.replace(/\D/g,'');});
   if(ns.length)m=[null,String(Math.min.apply(null,ns)),Math.max.apply(null,ns)>Math.min.apply(null,ns)?String(Math.max.apply(null,ns)):null];else{sec++;m=[null,String(sec),null];}}
  sec=+(m[2]||m[1]);
  var h=li.innerHTML.replace(/^\s*\[[^\]]*\]\s*/,'').replace(/\s*\|?\s*(<(i|em)>\s*)?Tipo(\s*<\/(i|em)>)?\s*:\s*[^|<]+/i,''),bb=li.querySelector('b,strong'),md=bb?bb.textContent.trim():'';
  var fes=li.textContent.match(/\d{1,2}\s+de\s+[a-z\u00e1\u00e9\u00ed\u00f3\u00fa]+/gi)||[],fe=(fes.length?fes[fes.length-1].match(/(\d{1,2})\s+de\s+([a-z\u00e1\u00e9\u00ed\u00f3\u00fa]+)/i):[]);var fd=(li.textContent.match(/d[i\u00ed]a\s+(\d{1,2})/i)||[])[1];
  items.push({t:li.textContent.replace(/^\s*\[[^\]]*\]\s*/,'').trim(),a:+m[1],z:+(m[2]||m[1]),lab:'['+m[1]+(m[2]?'\u2013'+m[2]:'')+']',bs:[].map.call(li.querySelectorAll('b,strong'),function(z){return z.textContent.trim();}),h:h,md:md,mo:medioPor(cat,md),fe:fe[1]&&MESES.indexOf(fe[2].toLowerCase())>=0?fe[1]+' de '+fe[2].toLowerCase():(fd&&mes?fd+' de '+mes:''),tipo:tipoExpl(li.textContent)||tipoDe(li.textContent,'info')});});
 var deI=function(i){return items.find(function(x){return i+1>=x.a&&i+1<=x.z;});};
 var lb=ims.map(function(im,i){var x=deI(i);return {src:im.src,txt:x?x.t:'',cap:(x?x.lab+' '+(x.mo?x.mo.n:x.md)+' \u00b7 ':'')+'imagen '+(i+1)+' de '+n};});
 var fr=ims.map(function(im,i){var x=deI(i),l=x?'<span style="color:var(--accent)">'+esc(x.lab)+'</span> '+esc(x.mo?x.mo.n:x.md):'imagen '+(i+1);
  return '<button type="button" class="fr" data-lb="'+i+'" aria-label="Ampliar imagen '+(i+1)+'"><img loading="lazy" src="'+esc(im.el?srcDe(im.el,1280):im.src)+'" alt="'+esc(x?(x.mo?x.mo.n:x.md):'')+'" onerror="this.remove()"><span class="n">'+l+'</span></button>';}).join('');
 var idx=items.map(function(x){return '<li><span class="k-n'+(x.lab.length>4?' w':'')+'">'+esc(x.lab)+'</span><div><span class="md">'+(x.md?(x.mo&&x.mo.ficha?'<a href="'+fichaMedio(x.mo)+'" class="md-a">':'<span class="md-a">')+(x.mo&&x.mo.av?'<span class="av" aria-hidden="true"><img src="'+x.mo.av+'" alt=""></span>':'')+esc(x.mo?x.mo.n:x.md)+(x.mo&&x.mo.ficha?'</a>':'</span>'):'')+(x.fe?' \u00b7 '+esc(x.fe):'')+'</span>'+
  '<div class="tx">'+x.h+'</div></div>'+ico(x.tipo)+'</li>';}).join('');
 var meds={};items.forEach(function(x){x.bs.forEach(function(z){if(z)meds[fold(z)]=1;});});
 // EXTRA! anteriores: los enlaces del final del post
 var pa=[].find.call(b.querySelectorAll('p'),function(p){return /EXTRA! anteriores/i.test(p.textContent);}),r1='',r2='';
 if(pa&&/EXTRA! anteriores/i.test(pa.textContent)){[].forEach.call(pa.querySelectorAll('a'),function(a){var t=a.textContent.trim(),h=a.getAttribute('href')||'',k=(h.match(/extra(\d+)/)||[])[1];
  if(/^\d{4}$/.test(t))r2+='<a class="yr" href="'+esc(h)+'">'+t+'</a>';else r1+='<a href="'+esc(h)+'">'+(k?'n\u00ba '+k+' \u00b7 ':'')+esc(t)+'</a>';});}
 var sx='',srx=(!r1&&!r2)?serieDe(b,id):null;
 if(srx){var sx=srx.rows.map(function(r){return '<div class="prev-row'+(r.y?' y':'')+'">'+(r.y?'<span class="yr">'+r.y+'</span>':'')+'<span class="ls">'+r.ls.map(function(l){var k=(l.h.match(/extra-?(\d+)/i)||[])[1];return '<a href="'+esc(l.h)+'">'+(k?'n\u00ba '+k+' \u00b7 ':'')+esc(l.t)+'</a>';}).join('')+'</span></div>';}).join('');}
 if(!r1){var c=id;for(var q=0;q<4;q++){c=vecino(c,/^EXTRA!/i,true);if(!c)break;r1+='<a href="/post/'+c+'">'+esc(TIT[c].replace(/^EXTRA!\s*/i,''))+'</a>';}}
 var x=nuevoTop('mm-top');
 x.top.innerHTML=(d<LANZAMIENTO?'<div class="wrap">'+LEG+'</div>':'')+'<section class="xhero"><div class="wrap inner"><div class="l">'+
  '<div class="crumbs caps" style="padding:0"><a href="/" style="color:#fff">inconsolata</a><i style="color:var(--yellow)">\u00bb</i><a href="/tagged/EXTRA!" style="color:#fff">EXTRA!</a></div>'+
  '<h1 class="xw" aria-label="EXTRA! n\u00famero '+nn+'"><span aria-hidden="true">E</span><span aria-hidden="true">x</span><span aria-hidden="true">t</span><span aria-hidden="true">r</span><span aria-hidden="true">a</span><span aria-hidden="true">!</span></h1></div>'+
  '<div class="r"><span class="xnum">n\u00ba '+nn+'</span><p>'+esc(intro)+'</p><div class="meta">'+(mes?'<span>'+mes[0].toUpperCase()+mes.slice(1)+' de '+anioDe(mes,d)+'</span>':'<span>'+fecha(d)+'</span>')+(items.length?'<span>'+n+' piezas</span><span>'+Object.keys(meds).length+' medios</span>':'<span>'+n+' im\u00e1genes</span>')+'</div></div></div></section>';
 x.main.innerHTML='<section class="gal"><div class="gal-head"><span class="caps">Las p\u00e1ginas \u00b7 '+n+'</span><span style="font-size:13px;font-weight:600">Pulsa para ampliar \u00bb</span></div><div class="masonry">'+fr+'</div></section>'+
  (idx?'<section class="idx"><div class="caps" style="margin-bottom:14px">En este EXTRA! \u00bb</div><ol>'+idx+'</ol></section>':'')+
  (sx?'<section class="prev"><div class="caps" style="border-top:2px solid var(--ink);padding-top:12px">EXTRA! anteriores \u00bb</div><div class="prev-row"><a class="cur" href="#">n\u00ba '+nn+(mes?' \u00b7 '+mes:'')+'</a></div>'+sx+'</section>':'')+(!sx&&(r1||r2)?'<section class="prev"><div class="caps" style="border-top:2px solid var(--ink);padding-top:12px">EXTRA! anteriores \u00bb</div><div class="prev-row"><a class="cur" href="#">n\u00ba '+nn+(mes?' \u00b7 '+mes:'')+'</a>'+r1+'</div>'+(r2?'<div class="prev-row">'+r2+'</div>':'')+'</section>':'')+
  finRow(o.art);
 document.title='EXTRA! n\u00ba '+nn+' \u00b7 inconsolata\u00bb';
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
 var shot=function(im){var i=k++;lb.push({src:srcDe(im,99999),cap:t+' \u00b7 imagen '+(i+1)});return '<button type="button" class="fshot" data-lb="'+i+'" aria-label="Ampliar imagen '+(i+1)+'"><img loading="lazy" src="'+esc(srcDe(im,1280))+'" alt="" onerror="this.remove()"></button>';};
 var lead=false,cap=false,alt=0,heads=[];
 [].slice.call(b.childNodes).forEach(function(nd){
  if(nd.nodeType!==1){if(nd.nodeType===3&&nd.textContent.trim())col.insertAdjacentHTML('beforeend','<p>'+esc(nd.textContent)+'</p>');return;}
  var tg=nd.tagName,imgs=[].slice.call(nd.querySelectorAll('img'));
  if((nd.classList.contains('npf_row')||tg==='FIGURE'||(tg==='P'&&imgs.length&&!nd.textContent.trim()))&&imgs.length){
   if(!hero&&!lead){hero='<figure class="hero-one">'+shot(imgs[0])+'</figure>';imgs=imgs.slice(1);if(!imgs.length)return;}
   if(imgs.length>1){col.insertAdjacentHTML('beforeend','<figure class="pair" style="--n:'+Math.min(imgs.length,3)+'">'+imgs.map(shot).join('')+'</figure>');return;}
   col.insertAdjacentHTML('beforeend','<figure class="'+(alt++%2?'side-fig':'wide')+'">'+shot(imgs[0])+'</figure>');return;}
  if(tg==='BLOCKQUOTE'){if(/buymeacoffee|aportaci\u00f3n/i.test(nd.textContent+nd.innerHTML))return;
   if(nd.classList.contains('npf_indented')){col.insertAdjacentHTML('beforeend','<aside class="note"><b>Nota al margen</b>'+nd.innerHTML+'</aside>');return;}
   col.insertAdjacentHTML('beforeend','<div class="pull"><p>'+esc(nd.textContent.trim())+'</p></div>');return;}
  if(/^H[2-6]$/.test(tg)){var a=nd.querySelector('a[href]');
   if(a&&/^\s*\u00bb/.test(nd.textContent)){var h=a.getAttribute('href');col.insertAdjacentHTML('beforeend','<a class="cta" href="'+esc(h)+'" target="_blank" rel="noopener"><b>'+esc(a.textContent.trim())+' \u00bb</b><span>Entrar</span></a>');return;}
   var hid='s-'+(heads.length+1);heads.push({id:hid,t:nd.textContent.replace(/^\s*\u00bb\s*/,'').trim()});
   col.insertAdjacentHTML('beforeend','<h2 id="'+hid+'"><i>\u00bb</i>'+esc(heads[heads.length-1].t)+'</h2>');return;}
  if(tg==='UL'){nd.className='ul';col.appendChild(nd);return;}
  if(tg==='P'){
   [].forEach.call(nd.querySelectorAll('b,strong'),function(x){if(x.textContent.trim()==='\u2a54'){var sp=x.closest('span')||x,br=sp.nextElementSibling;sp.remove();if(br&&br.tagName==='BR')br.remove();}});
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
 col.insertAdjacentHTML('beforeend','<div class="sign">'+"<svg viewBox=\"0 0 24 24\" width=\"48\" height=\"48\" aria-hidden=\"true\"><path d=\"M9.3 13.2a2.9 2.9 0 0 1 5.8 0a5.8 5.8 0 0 1-11.6 0a8.7 8.7 0 0 1 17.4 0a8.7 8.7 0 0 1-5.6 8.1\" fill=\"none\" stroke=\"#A862C8\" stroke-width=\"2.8\" stroke-linecap=\"round\"/></svg>"+'<div><span class="s">Sa\u00fal Castillo</span><small>inconsolata\u00bb \u00b7 <a href="https://saulcastillo.es">saulcastillo.es</a></small></div></div>');
 var toc=heads.length>=2?'<aside class="toc" aria-label="En este post"><nav><span class="caps" style="margin-bottom:6px">En este post</span>'+heads.map(function(h){return '<a href="#'+h.id+'"><i>\u00bb</i>'+esc(h.t)+'</a>';}).join('')+'</nav></aside>':'';
 var leg=art.querySelector('.legacy'),endr=finRow(art);
 art.innerHTML=(d<LANZAMIENTO?'<div style="padding-top:20px">'+LEG+'</div>':'')+
  '<div class="crumbs caps"><a href="/">inconsolata</a><i>\u00bb</i><a href="/tagged/'+encodeURIComponent(badges[0]||'metablog')+'">'+esc(badges[0]||'metablog')+'</a></div>'+
  '<header class="mhead"><div class="badges">'+badges.map(function(x){return '<span class="badge">'+esc(x)+'</span>';}).join('')+'</div><h1 class="soft'+(t.length>60?' long':'')+'">'+destaca(t)+'</h1>'+
  '<div class="byline"><span>por Sa\u00fal Castillo</span><span>'+fecha(d)+'</span><span>'+mins+' minuto'+(mins>1?'s':'')+' de lectura</span></div></header>'+hero+
  '<article class="art">'+toc+'</article>'+endr;
 art.querySelector('.art').appendChild(col);
 if(!toc)col.style.margin='0 auto';
 var pnv=document.querySelector('nav.pn');if(pnv)pnv.remove();
 document.title=quita(t)+' \u00b7 inconsolata\u00bb';
 return lb;
}

// ------------------------------------------------------------------ portada
// La primera p\u00e1gina del blog se convierte en la portada: los posts que pone Tumblr (los m\u00e1s frescos) se completan
// con los datos ligeros del repositorio (portada.json, efem\u00e9rides, avisos).
var DIAS=['domingo','lunes','martes','mi\u00e9rcoles','jueves','viernes','s\u00e1bado'];
var PROY={k:'Proyectos \u00bb',t:'SISMOLIVE',p:'Todos los terremotos del planeta, en directo y con datos abiertos.',u:'/post/830276402210291712/sismolive',
 im:'https://64.media.tumblr.com/347064713ce39bc8f64fb6d78fe035f4/039e04832269dcd6-b8/s1280x1920/39c0be6a2669b9cde1527ba6c603feb6e1032f73.jpg'};
var TINTAS=['ht-c','ht-k','ht-y','ht-m'];
function hoyISO(){var d=new Date();return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2);}
function romano(n){var x='',m=[[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],[50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']];m.forEach(function(q){while(n>=q[0]){x+=q[1];n-=q[0];}});return x;}
function ddmm(d){return d.slice(8,10)+'.'+d.slice(5,7);}
function primeras(t,n){t=(t||'').replace(/<([^<>]{1,120})>/g,'$1').replace(/^[\s\u2a54]+/,'').replace(/\s+/g,' ').trim();var re=/[^.!?]+[.!?]+(?=\s|$)/g,r='',m;
 while((m=re.exec(t))){var x=m[0].trim();if(!r){r=x;if(r.length>=70)break;}else if((r+' '+x).length<=n){r+=' '+x;break;}else break;}
 r=r||t;if(r.length>n){r=r.slice(0,n).replace(/\s+\S*$/,'').replace(/[,;:\s]+$/,'')+'\u2026';}return r;}
function img(u,alt,cls){return u?'<img loading="lazy" src="'+esc(u)+'" alt="'+esc(alt||'')+'"'+(cls?' class="'+cls+'"':'')+' onerror="this.remove()">':'';}
function medioN(cat,n){return cat.medios.find(function(m){return m.n===n;})||{n:n};}
function deco(s){var t=document.createElement('textarea');t.innerHTML=s;return t.value;}
function ls(k,v){try{if(v===undefined)return JSON.parse(localStorage.getItem(k)||'null');localStorage.setItem(k,JSON.stringify(v));}catch(e){return null;}}

function deTarjeta(c,meta,cat){
 var id=rid(c),mt=meta[id],tags=(c.dataset.tags||'').toLowerCase().split('|').filter(Boolean);
 var tg=function(r){return tags.some(function(t){return r.test(t);});};
 var s=mt?mt[0]:tg(/^mucho ?m[a\u00e1]s$/)?'m':tg(/^extra!?$/)?'x':tg(/^detallitos$/)?'d':tg(/^metablog$/)?'b':'';
 var d=c.dataset.date||'';
 var ims=[],hr=(c.dataset.hr||'').trim().split(/\s+/).filter(Boolean),sm=(c.dataset.img||'').trim().split(/\s+/).filter(Boolean);
 hr.forEach(function(u,i){ims.push({big:u,sm:sm[i]||u});});
 var tp=c.querySelector('template.lb-body'),body=null;
 if(tp){body=document.createElement('div');body.innerHTML=tp.innerHTML;unwrap(body);
  [].forEach.call(body.querySelectorAll('img'),function(i){if(i.closest('blockquote'))return;
   ims.push({big:srcDe(i,1280),sm:srcDe(i,640),w:+(i.getAttribute('data-orig-width')||0),h:+(i.getAttribute('data-orig-height')||0)});});}
 ims=ims.filter(function(im,k){return !esPortadilla(s,k,im,d||'2099');});
 var t=(c.querySelector('.tt')||{}).textContent||'',bh=body&&body.querySelector('h1');t=t.trim()||TIT[id]||(bh?bh.textContent.trim():'');
 var txt=deco(c.dataset.txt||'').replace(/^[\s\u2a54]+/,'');if(c.dataset.root)txt=txt.replace(/^[\w.-]+:\s*/,'').replace(/^[\s\u2a54]+/,'');
 if(bh&&txt.indexOf(bh.textContent.trim())===0)txt=txt.slice(bh.textContent.trim().length).replace(/^[\s\u2a54]+/,'');
 if(!t)t=primeras(txt,110);
 return {id:id,tags:tags,u:c.getAttribute('href'),d:d,s:s,k:mt?mt[1]:[],meds:mt?mt[2].map(function(i){return cat.medios[i];}).filter(Boolean):[],
  auts:mt?mt[3].map(function(i){return cat.autores[i];}):[],ims:ims,t:t,txt:txt,body:body};
}
function deDato(r,cat){return {id:r[0],u:'/post/'+r[1],d:r[2],s:r[3],k:r[4],meds:r[7].map(function(n){return medioN(cat,n);}),auts:[],
 ims:r[8]?[{big:r[8],sm:r[8]}]:[],t:r[5],txt:r[6],body:null};}

var META0={};
function espDe(p){var sl=(META0[p.id]||[])[5];return sl&&cat0&&cat0.esp&&cat0.esp[sl]?{slug:sl,n:cat0.esp[sl]}:null;}
function espK(p,cls){var e=espDe(p);return e?'<span class="'+(cls||'k-esp')+'">'+esc(e.n)+' \u00bb</span>':'';}
function tituloDe(p){return p.s==='m'?'mucho m\u00e1s':p.t;}
function kicker(p,cls){return '<span class="'+(cls||'kicker')+(p.meds.length>1?' muchos':'')+'">'+(p.meds.length?medsK(p.meds)+' \u00b7 ':'\u00bb ')+ddmm(p.d)+'</span>';}

// ---------- piezas
function hero(p){var im=p.ims[0];
 var ki=p.s==='b'?'metablog \u00bb':p.s==='o'?'offtopic \u00bb':p.k[0]?esc(TN[p.k[0]])+' \u00bb':'Lo \u00faltimo \u00bb';
 return '<section class="hero">'+(im?'<a href="'+esc(p.u)+'" class="hero-img"><div class="ph ht-k">'+img(im.big,(TN[p.k[0]]||'Imagen')+(p.meds[0]?' de '+p.meds[0].n:''))+'</div></a>':'')+
  '<div class="hero-card'+(im?'':' solo')+(p.col?' c-'+p.col:'')+'"><span class="caps" style="letter-spacing:3px">'+ki+(espDe(p)?' <a class="k-esp" href="/especiales#'+esc(espDe(p).slug)+'">'+esc(espDe(p).n)+' \u00bb</a>':'')+'</span><h1 class="soft"><a href="'+esc(p.u)+'">'+destaca(p.t)+'</a></h1>'+
  (p.txt?'<p>'+esc(primeras(p.txt.indexOf(quita(p.t))===0?p.txt.slice(quita(p.t).length):p.txt,230))+'</p>':'')+
  '<div class="hero-meta">'+(p.meds.length?'<span class="hm-avs">'+p.meds.map(function(m){return '<a href="'+fichaMedio(m)+'" title="'+esc(m.n)+'" aria-label="Ficha de '+esc(m.n)+'">'+(m.avw?'<img class="k-av" src="'+esc(m.avw)+'" alt="" onerror="this.parentNode.textContent=\''+esc(m.n.charAt(0))+'\'">':esc(m.n.charAt(0)))+'</a>';}).join('')+'</span><span class="hm-n">\u00bb '+(p.meds.length>3?p.meds.length+' medios':p.meds.map(function(m){return '<a href="'+fichaMedio(m)+'">'+esc(m.n)+'</a>';}).join(', ').replace(/, (<a [^>]*>[^<]*<\/a>)$/,' y $1'))+'</span>':'')+'<span>'+p.d.split('-').reverse().join('.')+'</span></div></div></section>';}

// versi\u00f3n lite: \u00ablo \u00faltimo\u00bb como lista sencilla (miniatura, medio y t\u00edtulo)
function liteFila(p){var im=p.ims[0],t=p.s==='m'?'mucho m\u00e1s \u00bb '+quita(p.t).replace(/^mucho m[a\u00e1]s\s*[\u00bb\u00b7]?\s*/i,''):p.s==='x'?(p.mes?'EXTRA! \u00b7 lo mejor de '+p.mes:quita(p.t)):p.t;
 return '<a class="lf'+(p.s?' s-'+p.s:'')+'" href="'+esc(p.u)+'"><span class="lf-ph">'+(im?img(im.sm):'')+'</span><span class="lf-tx">'+(p.s&&SECN[p.s]?'<span class="lf-s">'+SECN[p.s]+' \u00bb</span>':espK(p,'lf-s'))+kicker(p,'lf-k')+'<span class="lf-t">'+(p.s==='m'||p.s==='x'?esc(t):destaca(t))+'</span></span></a>';}
function hoja(p,i,pos){
 var st=' style="grid-column:'+pos.c+';margin-top:'+pos.mt+'px;transform:rotate('+pos.r+'deg)"',tape='<span class="tape" aria-hidden="true"></span>';
 var a='<a href="'+esc(p.u)+'" ';
 if(p.s==='d'){return a+'class="clip"'+st+'><svg class="pc" viewBox="0 0 22 58" aria-hidden="true"><path d="M6 4 V42 a5 5 0 0 0 10 0 V10 a3.5 3.5 0 0 0 -7 0 V40" fill="none" stroke="#7A766C" stroke-width="2.4" stroke-linecap="round"/></svg><span class="clip-sec">detallitos</span>'+
  '<div class="clip-g'+(p.ims.length>1?' two':'')+'">'+p.ims.slice(0,2).map(function(im){return '<div class="ph ht-k" style="height:170px">'+img(im.sm)+'</div>';}).join('')+'</div>'+kicker(p,'clip-cap')+'<span class="clip-t">'+esc(quita(p.t))+'</span></a>';}
 if(p.s==='x'){return a+'class="xsheet"'+st+'>'+tape+'<div class="xs-top"><span class="xword" aria-label="EXTRA!">Extra!</span><span class="caps xs-n">'+(p.num?'N\u00ba '+p.num+'<br>':'')+(p.mes?'lo mejor de '+esc(p.mes):'')+'</span></div>'+
  '<div class="xfan" aria-hidden="true">'+p.ims.slice(0,3).map(function(im){return '<div class="ph ht-k">'+img(im.sm)+'</div>';}).join('')+'</div>'+
  '<span class="tt">'+(p.mes?'Lo mejor del dise\u00f1o de prensa de '+esc(p.mes):esc(quita(p.t)))+'</span>'+(p.meds.length?'<span class="xs-m">'+esc(p.meds.map(function(m){return m.n;}).join(', '))+'.</span>':'')+'</a>';}
 if(p.s==='b'||p.s==='o'){return a+'class="tsheet"'+st+'>'+tape+'<div class="ts-t"><span class="caps">'+SECN[p.s]+' \u00bb</span><h3 class="soft'+(quita(p.t).length>60?' largo':'')+'">'+destaca(p.t)+'</h3>'+(p.txt?'<p>'+esc(primeras(p.txt,170))+'</p>':'')+'<span class="caps" style="color:var(--accent)">Seguir leyendo \u00bb</span></div>'+
  (p.ims.length?'<div class="tcoll" aria-hidden="true">'+p.ims.slice(0,3).map(function(im){return '<div class="ph ht-k">'+img(im.sm)+'</div>';}).join('')+'</div>':'')+'</a>';}
 var dark=p.k.indexOf('port')>=0&&p.k.length===1;
 if(p.col==='negro')dark=true;return a+'class="sheet'+(dark?' dark':'')+(p.col&&p.col!=='negro'?' c-'+p.col:'')+'"'+st+'>'+tape+icoP(p.id,p.k[0],'ico '+(i%2?'tl':'tr'))+
  (p.ims[0]?'<div class="ph '+TINTAS[i%4]+'" style="height:'+pos.h+'px">'+img(p.ims[0].sm,(TN[p.k[0]]||'Imagen')+(p.meds[0]?' de '+p.meds[0].n:''))+'</div>':'')+
  espK(p)+kicker(p)+'<span class="tt">'+esc(quita(p.t))+'</span>'+(p.auts.length?'<span class="by">por '+esc(p.auts.slice(0,3).join(', ').replace(/, ([^,]*)$/,' y $1'))+'</span>':'')+'</a>';}

// colocaci\u00f3n en la rejilla de 12 columnas: piezas alternas a izquierda y derecha, con giros y desniveles
function colocar(L){var out=[],R=[-1.5,1,-2.5,.6,1.4,-2,-1,2,-.8],H=[400,320,360,300,380,340],MA=[0,30,10,40,0,20],MB=[110,60,140,80,120,50];
 var peso=function(p){return p.tam==='grande'?8:p.tam==='mediana'?6:p.tam==='peque\u00f1a'?4:p.s==='d'?3:p.s==='b'||p.s==='o'?7:p.s==='x'?7:5;};
 for(var i=0,f=0;i<L.length;i+=2,f++){var a=L[i],b=L[i+1],h=function(p,k){return p.tam==='grande'?480:p.tam==='peque\u00f1a'?260:H[k%H.length];};
  if(!b){out.push({c:'3/11',mt:MA[f%6],r:R[i%9],h:h(a,i)});break;}
  var pa=peso(a),pb=peso(b),wa=Math.max(3,Math.min(8,Math.round(11*pa/(pa+pb))));
  if(f%2&&pa===pb)wa=11-wa;   // alterna el lado ancho en las filas de piezas iguales
  out.push({c:'1/'+(1+wa),mt:MA[f%6],r:R[i%9],h:h(a,i)});out.push({c:(2+wa)+'/13',mt:MB[f%6],r:R[(i+1)%9],h:h(b,i+1)});}
 return out;}

function mmSec(m,top){var fr=m.fr||[],num=(m.t.match(/semana\s+([IVXLCDM]+)/i)||[])[1]||'';
 var lab=top?(m.d===hoyISO()?'Hoy, '+DIAS[new Date().getDay()]+' \u00bb':'Reci\u00e9n salido \u00bb'):'';
 return '<section class="mm"'+(top?' style="margin-top:44px"':'')+'><div class="wrap inner"><div class="mm-top"><div style="display:flex;flex-direction:column;gap:4px">'+
  (lab?'<span class="caps mm-hoy">'+lab+'</span>':'')+'<span class="caps" style="font-size:15px;letter-spacing:3px">La semana en infograf\u00edas</span><span class="mm-title soft">mucho m\u00e1s \u00bb</span></div>'+
  '<a href="'+esc(m.u)+'" class="btn-yellow">Ver '+(fr.length>1?'las '+(m.n&&m.n>fr.length?fr.length:fr.length):'el post')+' \u00bb</a></div>'+
  (num?'<div class="mm-num" aria-hidden="true">'+num.toUpperCase()+'</div>':'')+
  '<div class="film"><div class="perf"></div><div class="frames">'+fr.slice(0,7).map(function(f,i){return '<a class="frame" href="'+esc(m.u)+'#mm-'+(i+1)+'"><div class="ph">'+img(f[0])+'</div><span>'+esc(f[1]||'')+(f[1]?' \u25b8':'')+'</span></a>';}).join('')+'</div><div class="perf"></div></div></div></section>';}

function xdaySec(x){return '<section class="xday"><div class="in"><a href="'+esc(x.u)+'" class="xd-a"><span class="caps xd-k">'+(x.d===hoyISO()?'Hoy sale el EXTRA! \u00bb':'Reci\u00e9n salido \u00bb')+'</span>'+
 '<div class="w" aria-label="EXTRA!">Extra!</div><div class="t">'+(x.num?'N\u00ba '+x.num+' \u00b7 ':'')+'lo mejor del dise\u00f1o de prensa'+(x.mes?' de '+esc(x.mes):'')+'</div>'+
 (x.meds.length?'<p>'+esc(x.meds.length)+' medios en esta entrega: '+esc(x.meds.map(function(m){return m.n;}).join(', '))+'.</p>':'')+'<span class="go">Abrir el EXTRA! \u00bb</span></a>'+
 '<a href="'+esc(x.u)+'" class="fan" aria-hidden="true" tabindex="-1">'+x.ims.slice(0,5).map(function(im){return '<span class="xf">'+img(im.sm)+'</span>';}).join('')+'</a></div></section>';}

function mesDe(p){var t=(p.txt||'')+' ',re=new RegExp('(destacamos|recopilaci|selecci[o\u00f3]n)[^.]*?\\b('+MESES.join('|')+')\\b','i'),m=t.match(re);
 if(m)return m[2].toLowerCase();var d=new Date(p.d);d.setMonth(d.getMonth()-1);return MESES[d.getMonth()];}

function hoySec(ef){var y=new Date().getFullYear();
 var rows=(ef||[]).filter(function(r){return +r[0]<y;}).slice(0,3);
 if(!rows.length)return '';
 return '<div class="hoy"><h2 class="serif">tal d\u00eda <em class="soft">como hoy</em></h2>'+rows.map(function(r,i){
  return '<a href="/post/'+esc(r[1])+'" class="hoy-row"><span class="hoy-year">'+r[0]+'</span><span class="hoy-txt">'+esc(quita(r[2]))+(r[3][0]?'<small>\u00bb '+esc(r[3][0])+'</small>':'')+'</span><span class="hoy-thumb ph '+['ht-m','ht-c','ht-y'][i]+'" aria-hidden="true">'+img(r[4])+'</span></a>';}).join('')+'</div>';}

function temasSec(P,cat,esp){
 var PT=P.temas.filter(function(t){return !t[5];}),V=PT.filter(function(t){return t[2]>=8&&t[4].length;}),COL=['t-ink','t-yel','t-cya','t-pap','t-mag'];
 var fijo=esp?{n:esp.t,c:esp.n,b:'Especial',u:'/especiales#'+esp.slug,im:esp.im,ic:esp.ic}:null;
 if(!fijo){var tp=V.slice().sort(function(a,b){return b[2]-a[2];})[0];fijo={n:tp[1],c:tp[2],b:tp[3],u:'/buscador#h='+tp[0],im:tp[4][0],ic:TS[tp[0]]};}
 var tile=function(t,cl,big){return '<a href="'+esc(t.u)+'" class="tema '+cl+(big?' big vit-fix':'')+'"><div class="tm-ph">'+img(t.im)+'</div>'+
  (t.ic?'<svg class="tm-ico'+(big?'':' tm-ico-s')+'" viewBox="0 0 64 64" aria-hidden="true"><use href="#'+t.ic+'" class="k"/><use href="#'+t.ic+'" class="m" x="3" y="2.5"/></svg>':'')+
  (big?'<span class="tm-k">'+esc(t.b)+'</span>':'<span class="tm-b">'+esc(t.b)+'</span>')+'<span class="tm-n soft">'+esc(t.n)+'</span><span class="tm-c">'+t.c+(t.c===1?' post':' posts')+'</span></a>';};
 var bloques={};PT.forEach(function(t){(bloques[t[3]]=bloques[t[3]]||[]).push(t);});
 var dlg='<dialog class="tdl" id="tm-dlg" aria-labelledby="tdl-h"><div class="tdl-top"><h2 id="tdl-h" class="soft">Todos los <em>temas</em></h2><button type="button" class="tdl-x" data-close aria-label="Cerrar">\u00d7</button></div>'+
  '<p class="tdl-sub">'+PT.length+' temas en '+(new Date().getFullYear()-(+P.anios))+' a\u00f1os de archivo. Pulsa uno para ver todas sus entradas.</p>'+
  (P.esp.length?'<div class="tdl-b tdl-esp"><h3>Especiales <span>\u00b7 acontecimientos e historias concretas, cada uno dentro de su tema</span></h3><div class="tdl-c">'+P.esp.filter(function(e){return !e[6];}).sort(function(a,b){return (b[4]||'').localeCompare(a[4]||'');}).map(function(e){var ti=cat.temas.findIndex(function(t){return t.n===e[2];});
   return '<a href="/especiales#'+esc(e[1])+'">'+(ti>=0?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+TS[ti]+'"/></svg>':'')+esc(e[0])+'<small>'+e[3]+'</small></a>';}).join('')+'</div></div>':'')+
  Object.keys(bloques).map(function(b){return '<div class="tdl-b"><h3>'+esc(b)+'</h3><div class="tdl-c">'+bloques[b].map(function(t){return '<a href="/buscador#h='+t[0]+'"><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+TS[t[0]]+'"/></svg>'+esc(t[1])+'<small>'+t[2]+'</small></a>';}).join('')+'</div></div>';}).join('')+'</dialog>';
 var EG={};P.esp.filter(function(e){return !e[6];}).forEach(function(e){(EG[e[5]]=EG[e[5]]||[]).push(e);});
 var nCap=function(sl){return P.esp.filter(function(e){return e[6]===sl;}).length;};
 dlg+='<dialog class="tdl" id="es-dlg" aria-labelledby="esd-h"><div class="tdl-top"><h2 id="esd-h" class="soft">Todos los <em>especiales</em></h2><button type="button" class="tdl-x" data-close aria-label="Cerrar">\u00d7</button></div>'+
  '<p class="tdl-sub">Acontecimientos e historias con p\u00e1gina propia, cada uno dentro de su tema. <a href="/especiales" style="border-bottom:2px solid var(--accent)">Ver la p\u00e1gina de especiales \u00bb</a></p>'+
  cat.temas.map(function(t){return t.n;}).filter(function(n){return EG[n];}).map(function(n){return '<div class="tdl-b"><h3>'+esc(n)+'</h3><div class="tdl-c">'+EG[n].sort(function(a,b){return (b[4]||'').localeCompare(a[4]||'');}).map(function(e){var ti=cat.temas.findIndex(function(t){return t.n===e[2];});var nc=nCap(e[1]);
   return '<a href="/especiales#'+esc(e[1])+'">'+(ti>=0?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+TS[ti]+'"/></svg>':'')+esc(e[0])+'<small>'+e[3]+(nc?' \u00b7 '+nc+' cap.':'')+'</small></a>';}).join('')+'</div></div>';}).join('')+'</dialog>';
 return {html:'<section class="temas-sec" aria-labelledby="tm-h"><div class="sec-head tm-head"><h2 id="tm-h" class="serif"><em class="soft">temas</em></h2><div class="tm-btns"><button type="button" class="tm-allbtn" data-open="tm-dlg" aria-haspopup="dialog">Todos los temas <b>'+PT.length+'</b> \u00bb</button><button type="button" class="tm-allbtn" data-open="es-dlg" aria-haspopup="dialog">Todos los especiales <b>'+P.esp.filter(function(e){return !e[6];}).length+'</b> \u00bb</button></div></div>'+
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
 var run=y+' <i>\u00bb</i> <b>'+L.length+'</b> medios <i>\u00bb</i> <b>'+M.posts+'</b> entradas <i>\u00bb</i> '+top.map(function(r){return esc(r[0])+' <b>'+r[1]+'</b>';}).join(' <i>\u00bb</i> ')+' <i>\u00bb</i> ';
 var todos=M.l.map(function(r){return {m:medioN(cat,r[0]),y:r[1],t:r[2]};}).filter(function(o){return o.m.ficha;});
 return '<section class="medios" aria-labelledby="md-h"><div class="sec-head md-head"><h2 id="md-h" class="serif"><em class="soft">medios</em></h2>'+
  '<a class="cinta" href="/estadisticas#'+y+'" aria-label="Estad\u00edsticas de medios de '+y+': '+L.length+' medios, '+M.posts+' entradas. Ver todas las estad\u00edsticas"><span class="ci-k"><b>'+y+'</b> en cifras</span><span class="ci-bars" aria-hidden="true">'+
  top.map(function(r){return '<span class="cb" style="height:'+Math.max(12,Math.round(r[1]/mx*100))+'%" title="'+esc(r[0])+': '+r[1]+'"></span>';}).join('')+'</span><span class="ci-tk" aria-hidden="true"><span class="ci-run">'+run+run+'</span></span><span class="ci-go">Ver \u00bb</span></a></div>'+
  '<div class="logos">'+logos.map(function(o){return '<a href="'+fichaMedio(o.m)+'" aria-label="Ficha de '+esc(o.m.n)+'" class="logo-a"><div class="logo-slot logo-img"><img src="'+esc(o.m.logo)+'" alt="'+esc(o.m.n)+'" onerror="this.replaceWith(this.alt)"></div></a>';}).join('')+
  '<button type="button" class="logo-more" data-open="md-dlg" aria-haspopup="dialog"><span class="logo-slot">Todos los medios \u00bb</span></button></div>'+
  '<dialog class="tdl mdl" id="md-dlg" aria-labelledby="mdl-h"><div class="tdl-top"><h2 id="mdl-h" class="soft">Todos los <em>medios</em></h2><button type="button" class="tdl-x" data-close aria-label="Cerrar">\u00d7</button></div>'+
  '<div class="mdl-tools"><p class="tdl-sub">'+todos.length+' medios con ficha, ordenados por entradas en '+y+'. Pulsa uno para ir a su ficha.</p><label class="sr" for="md-q">Buscar medio</label><input id="md-q" type="search" placeholder="Buscar medio\u2026" autocomplete="off"></div>'+
  '<div class="mdl-grid" id="md-grid">'+todos.map(function(o){return '<a class="mdc" href="'+fichaMedio(o.m)+'" data-n="'+esc(fold(o.m.n))+'">'+(o.m.av?'<span class="mdc-av" aria-hidden="true"><img src="'+esc(o.m.av)+'" alt=""></span>':'')+'<span class="mdc-n">'+esc(o.m.n)+'</span><span class="mdc-c">'+(o.y?'<b>'+o.y+'</b> en '+y+' \u00b7 ':'')+o.t+' en total</span></a>';}).join('')+'</div></dialog></section>';}

// ---------- avisos: prueba de imprenta (grandes) y marca de registro (ligeros)
var BAR=['#00A0DC','#E5007E','#FFD400','#16140F','#7FCFED','#F27FBF','#FFE97F','#8B8A87','#16140F','#D1006F'];
function avisoId(a){return a.id||a.u||a.t;}
// icono que no es de un tema (p. ej. \u00abTren\u00bb): su s\u00edmbolo se llama t-<nombre>
function symN(n){if(!n)return '';if(/^t-/.test(n))return n;var id='t-'+fold(n).replace(/\s+/g,'-');return document.getElementById(id)?id:n;}
function avMedia(a){
 if(a.ico){var ti=cat0.temas.findIndex(function(t){return t.n===a.ico||TS[cat0.temas.indexOf(t)]===a.ico;}),sy=ti>=0?TS[ti]:symN(a.ico);
  return '<span class="pv-md ico">'+['#00A0DC','#E5007E','#FFD400','#16140F'].map(function(c){return '<span style="color:'+c+'"><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+esc(sy)+'"/></svg></span>';}).join('')+'</span>';}
 if(a.imgs&&a.imgs.length)return '<span class="pv-md trio">'+a.imgs.slice(0,3).map(function(u){return '<span>'+img(u)+'</span>';}).join('')+'</span>';
 if(a.img)return '<span class="pv-md">'+img(a.img)+'</span>';
 return '';}
var cat0=null;
// la prueba de imprenta se coloca a la derecha del logo medido de verdad (letras ya cargadas y animaci\u00f3n acabada);
// si aun as\u00ed no cabe, baja debajo del logo
function colocaPrueba(){var mh=document.querySelector('.v-home .masthead');if(!mh)return;var m=mh.querySelector('.mast');if(!m)return;
 var r0=mh.getBoundingClientRect(),rg=document.createRange();rg.selectNodeContents(m);var rt=rg.getBoundingClientRect();if(!rt.width)rt=m.getBoundingClientRect();
 mh.style.setProperty('--mw',Math.round(rt.right-r0.left)+'px');mh.classList.remove('choca');
 var pr=document.getElementById('prueba');if(pr&&!pr.hidden){var pb=pr.getBoundingClientRect();if(pb.left<rt.right+12&&pb.top<rt.bottom-8&&pb.bottom>rt.top)mh.classList.add('choca');}}
function avisos(A){var hoy=hoyISO(),vig=function(a){return (!a.desde||a.desde<=hoy)&&(!a.hasta||a.hasta>=hoy);};
 var cerr=ls('inc-avisos-cerrados')||[],G=(A.grandes||[]).filter(function(a){return vig(a)&&cerr.indexOf(avisoId(a))<0;}),cur=0;
 var box=document.getElementById('prueba');
 function pinta(anim){if(!G.length){box.hidden=true;return;}var a=G[cur];
  box.innerHTML='<i class="crop c1"></i><i class="crop c1b"></i><i class="crop c2"></i><i class="crop c2b"></i><i class="crop c3"></i><i class="crop c3b"></i><i class="crop c4"></i><i class="crop c4b"></i>'+
   '<a class="pr" href="'+esc(a.u||'#')+'" aria-label="'+esc((a.k||'Aviso')+': '+quita(a.t))+'"><span class="slug"><span class="k">'+esc(a.k||'Aviso')+'</span><span>prueba '+(cur+1)+'/'+G.length+'</span><span>'+hoy.slice(8)+'\u00b7'+hoy.slice(5,7)+'\u00b7'+hoy.slice(2,4)+'</span></span>'+
   '<span class="row">'+avMedia(a)+'<span class="t soft">'+destaca(a.t)+'</span></span><span class="bar" aria-hidden="true">'+BAR.map(function(c,i){return '<i style="background:'+c+';--i:'+i+'"></i>';}).join('')+'</span></a>'+
   '<div class="ctrl">'+(G.length>1?'<button data-prev aria-label="Aviso anterior">\u2039</button><span class="n">'+(cur+1)+'/'+G.length+'</span><button data-next aria-label="Aviso siguiente">\u203a</button>':'')+'<button class="x" data-cerrar aria-label="Cerrar aviso">\u00d7</button></div>';
  box.hidden=false;var mh=document.querySelector('.v-home .masthead');colocaPrueba();
  if(anim){mh.classList.remove('go');void mh.offsetWidth;mh.classList.add('go');}}
 box.addEventListener('click',function(e){
  if(e.target.closest('[data-cerrar]')){cerr.push(avisoId(G[cur]));ls('inc-avisos-cerrados',cerr.slice(-40));G.splice(cur,1);cur=0;pinta(false);}
  if(e.target.closest('[data-next]')){cur=(cur+1)%G.length;pinta(false);}
  if(e.target.closest('[data-prev]')){cur=(cur+G.length-1)%G.length;pinta(false);}});
 // la prueba sale cuando la cabecera ya se ha plegado en inc\u00bb
 setTimeout(function(){pinta(true);},matchMedia('(prefers-reduced-motion: reduce)').matches?0:3300);
 addEventListener('resize',colocaPrueba);
 var mst=document.querySelector('.v-home .mast');if(mst){mst.addEventListener('animationend',colocaPrueba);if(window.ResizeObserver)new ResizeObserver(colocaPrueba).observe(mst);}
 if(document.fonts&&document.fonts.ready)document.fonts.ready.then(colocaPrueba);
 // ligeros
 var Lg=(A.ligeros||[]).filter(function(a){return !a.desde||a.desde<=hoy;}).sort(function(a,b){return (b.f||'').localeCompare(a.f||'');});
 // una novedad sigue marcada durante una semana desde su fecha; abrir la lista solo para la animaci\u00f3n
 var lim=new Date(Date.now()-7*864e5).toISOString().slice(0,10),visto=ls('inc-novedades-visto')||'',nuevos=Lg.filter(function(a){return (a.f||'')>=lim;}).length;
 var b=document.getElementById('rbtn'),pn=document.getElementById('panel');if(!b)return;
 var lbn=document.getElementById('lb-n');if(lbn&&nuevos){lbn.textContent=nuevos;lbn.hidden=false;}
 if(!Lg.length){b.closest('.reg-w').classList.add('vacio');return;}
 function lista(){pn.querySelector('ul').innerHTML=Lg.slice(0,Math.max(5,nuevos)).map(function(a,i){var ti=a.ico?cat0.temas.findIndex(function(t){return t.n===a.ico;}):-1,sy=ti>=0?TS[ti]:symN(a.ico);
  var inn='<span class="ic'+(sy?'':' bl soft')+'">'+(sy?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+esc(sy)+'"/></svg>':'\u00bb')+'</span><span><span class="fe">'+(a.f?+a.f.slice(8)+' '+MESES[+a.f.slice(5,7)-1].slice(0,3):'')+'</span><span class="tx">'+esc(a.t)+'</span></span>';
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
  esc(t.charAt(0).toUpperCase()+t.slice(1))+'&nbsp;\u00b7&nbsp;A\u00f1o '+romano(n)+'</span><div class="hd-slot"></div></div>'+
  '<div class="wrap"><header class="masthead"><a href="/" class="mast soft" aria-label="inconsolata\u00bb, ir a la portada">inc'+fold+'<span class="reg q">\u00bb<span class="reg-y" aria-hidden="true">\u00bb</span><span class="reg-c" aria-hidden="true">\u00bb</span></span></a>'+
  '<aside class="prueba" id="prueba" aria-label="Aviso" hidden></aside>'+
  '<div class="side"><div class="side-top"><div class="reg-w"><button class="rbtn" id="rbtn" aria-expanded="false" aria-controls="panel"><span class="sr">Novedades de la web</span><svg viewBox="0 0 64 64" fill="none" stroke-width="1.6" aria-hidden="true"><circle cx="32" cy="32" r="16"/><circle cx="32" cy="32" r="8"/><path d="M32 4v56M4 32h56"/></svg><span class="dot" aria-hidden="true"></span></button>'+
  '<div class="panel" id="panel" hidden><h3><span>Novedades de la web</span><span class="cmyk" aria-hidden="true"><span style="background:#00A0DC"></span><span style="background:#E5007E"></span><span style="background:#FFD400"></span><span style="background:#16140F"></span></span></h3><ul></ul><a class="all" href="/novedades">Todas las novedades \u00bb</a></div></div></div>'+
  '<span class="mini soft">inconsolata<span style="color:var(--accent)">\u00bb</span></span><span class="tagline">la web del dise\u00f1o period\u00edstico</span></div></header></div>';}

function faldon(f,cat){if(!f||!f.t||(f.hasta&&f.hasta<hoyISO()))return '';
 var ti=f.ico?cat.temas.findIndex(function(t){return t.n===f.ico;}):-1,sy=ti>=0?TS[ti]:symN(f.ico);
 var run=esc(f.t).replace(/\s*\u00bb\s*/g,' <i>\u00bb</i> ')+' <i>\u00bb</i> ';run=run+run;
 return '<a href="'+esc(f.u||'#')+'" class="faldon" aria-label="'+esc(f.t.replace(/\u00bb/g,'\u00b7'))+'">'+(sy?'<span class="f-icon" aria-hidden="true"><svg viewBox="0 0 64 64"><use href="#'+esc(sy)+'" class="k"/><use href="#'+esc(sy)+'" class="m" x="3" y="2.5"/></svg></span>':'')+
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
  // completa con los datos lo que falte en los posts de la p\u00e1gina (fotogramas de mucho m\u00e1s y EXTRA!, n\u00famero\u2026)
  L.forEach(function(p){
   if(p.s==='x'){p.mes=mesDe(p);if(P.x&&P.x.i===p.id){p.num=P.x.num;if(p.ims.length<3)p.ims=P.x.fr.map(function(f){return {sm:f[0],big:f[0]};});}}});
  // elecci\u00f3n manual: etiqueta #apertura en Tumblr o el archivo portada_manual.json
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
  var resto=L.filter(function(p){return !usados[p.id];});
  var h=aper||resto.find(function(p){return p.s!=='d'&&p.s!=='x'&&p.ims.length;})||resto[0];
  if(h)usados[h.id]=1;
  fx=fx.filter(function(p){return !usados[p.id];});fx.forEach(function(p){usados[p.id]=1;});
  var ult=fx.concat(L.filter(function(p){return !usados[p.id]&&p.s!=='m';})).slice(0,Math.max(9,fx.length));
  var de=obj(M.destacado),dd=PROY;
  if(vig(de)){var dp=de.id?porId(de.id):null;dd={k:de.k||(dp&&dp.s==='b'?'metablog \u00bb':'Destacado \u00bb'),t:de.t||(dp?quita(dp.t):''),p:de.p||(dp?primeras(dp.txt,150):''),u:de.u||(dp?dp.u:'#'),im:de.img||(dp&&dp.ims[0]?dp.ims[0].big:'')};}
  var pos=colocar(ult);
  // especial destacado: el del fald\u00f3n, si lo hay
  var esp=null,f=A.faldon;
  if(f&&f.especial){var e=P.esp.find(function(x){return x[1]===f.especial;});if(e){var ti=cat.temas.findIndex(function(t){return t.n===e[2];});
   var tt=ti>=0?P.temas.find(function(t){return t[0]===ti;}):null;esp={t:e[0],slug:e[1],n:e[3],im:f.img||(tt&&tt[4][0])||'',ic:ti>=0?TS[ti]:''};}}
  var tm=temasSec(P,cat,esp);
  home.innerHTML='<div class="v-home">'+cabecera()+faldon(f,cat)+arriba+'<div class="wrap">'+(h?hero(h):'')+
   '<section><div class="sec-head"><h2 class="serif">lo <em class="soft">\u00faltimo</em></h2><a href="/archive" class="underline">Todo el archivo \u00bb</a></div>'+
   (document.documentElement.classList.contains('lite')?'<div class="lite-lista">'+ult.map(liteFila).join('')+'</div>':'<div class="scatter">'+ult.map(function(p,i){return hoja(p,i,pos[i]);}).join('')+'</div>')+'<div class="mas"><a href="/page/2" class="btn-ink">M\u00e1s entradas \u00bb</a></div></section></div>'+
   (mm&&!mm.arriba?mmSec(mm,false):'')+
   '<div class="wrap"><section class="duo"><a href="'+esc(dd.u)+'" class="proj"><div class="ph">'+img(dd.im,dd.t)+'</div><div class="txt"><span class="caps" style="font-size:14px;letter-spacing:3px">'+esc(dd.k)+'</span><h3 class="soft'+(dd.t.length>14?' largo':'')+'">'+esc(dd.t)+'</h3><p>'+esc(dd.p)+'</p></div></a>'+
   hoySec(EF[hoyISO().slice(8)])+'</section>'+tm.html+mediosSec(P,cat)+'</div></div>';
  // el men\u00fa de siempre pasa a la barra superior
  var hr=document.querySelector('.page>.head .hd-right');if(hr)home.querySelector('.hd-slot').appendChild(hr);
  tm.init();avisos(A);
  home.addEventListener('click',function(e){var o=e.target.closest('[data-open]');if(o){var d=document.getElementById(o.dataset.open);if(d.showModal)d.showModal();else d.setAttribute('open','');}
   var c=e.target.closest('[data-close]');if(c){var dl=c.closest('dialog');dl.close?dl.close():dl.removeAttribute('open');}
   if(e.target.tagName==='DIALOG')e.target.close();});
  var q=document.getElementById('md-q');if(q)q.addEventListener('input',function(){var v=fold(this.value.trim());[].forEach.call(document.querySelectorAll('#md-grid .mdc'),function(c){c.hidden=v&&c.dataset.n.indexOf(v)<0;});});
 }).catch(function(e){console.error('inconsolata\u00bb: portada',e);document.body.classList.remove('es-portada');listado(meta,cat);});
}

// ------------------------------------------------------------------ p\u00e1ginas propias
// /buscador, /medios(#slug), /autores(#nombre), /estadisticas(#a\u00f1o), /especiales(#slug), /novedades, /cronologia(#a\u00f1o)
var RUTA=(location.pathname.match(/\/(buscador|medios|autores|estadisticas|especiales|novedades|cronologia)(?:\.html)?\/?$/)||[])[1]||'';
var Y1=new Date().getFullYear(),TIPOS_ORD=['info','carto','port','ilus','foto','video','publi','online'];
var MES3=['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'];
function fcorta(d){return +d.slice(8,10)+' '+MES3[+d.slice(5,7)-1]+' '+d.slice(0,4);}
function crumbs(a){return '<div class="crumbs caps"><a href="/">inconsolata</a>'+a.map(function(x){return '<i>\u00bb</i>'+(x[1]?'<a href="'+x[1]+'">'+esc(x[0])+'</a>':'<span>'+esc(x[0])+'</span>');}).join('')+'</div>';}
function tituloP(p){return quita(TIT[p.i]||p.t||'')||'Entrada sin t\u00edtulo';}
function contar(ps,f){var c={};ps.forEach(function(p){f(p).forEach(function(v){c[v]=(c[v]||0)+1;});});return Object.keys(c).sort(function(a,b){return c[b]-c[a];}).map(function(k){return [k,c[k]];});}
function cartaP(A,p,i){var auts=p.a.slice(0,3).map(function(j){return A.autores[j].n;});
 return '<a href="/post/'+esc(p.u)+'" class="card" data-k="'+p.k.join(' ')+'"><span class="tape" aria-hidden="true"></span>'+icoP(p.i,p.k[0],'ico')+
  '<div class="ph">'+(p.im?'<img loading="lazy" src="'+esc(p.im)+'" alt="" onerror="this.remove()">':'')+'</div><span class="caps">'+(p.m.length?medsI(p.m):'\u00bb '+esc(SECN[p.s]||''))+' \u00b7 '+fcorta(p.d)+'</span>'+
  '<span class="tt">'+esc(tituloP(p))+'</span>'+(auts.length?'<span class="by">por '+esc(auts.join(', '))+(p.a.length>3?' y '+(p.a.length-3)+' m\u00e1s':'')+'</span>':'')+'</a>';}
function barrasAnios(ps){var c={},mx=1,h='',ax='';ps.forEach(function(p){var y=+p.d.slice(0,4);c[y]=(c[y]||0)+1;});
 for(var y=2011;y<=Y1;y++)mx=Math.max(mx,c[y]||0);var n=Y1-2010;
 for(y=2011;y<=Y1;y++){h+='<div class="bar real" style="height:'+Math.max(2,(c[y]||0)/mx*100)+'%" title="'+y+': '+(c[y]||0)+' entradas"><span>'+(c[y]||'')+'</span></div>';ax+='<span>'+String(y).slice(2)+'</span>';}
 return '<section class="years"><div class="caps" style="margin-bottom:14px">Entradas por a\u00f1o \u00bb</div><div class="chart" style="grid-template-columns:repeat('+n+',minmax(0,1fr))">'+h+'</div><div class="yax" style="grid-template-columns:repeat('+n+',minmax(0,1fr))">'+ax+'</div></section>';}
function entradas(A,ps){var ks=contar(ps,function(p){return p.k;}).slice(0,6);
 return '<section class="entries"><div class="fbar"><span class="caps" style="margin-right:6px">Todas las entradas \u00bb</span><button type="button" aria-pressed="true" data-f="">Todas \u00b7 '+ps.length+'</button>'+
  ks.map(function(k){return '<button type="button" aria-pressed="false" data-f="'+k[0]+'">'+esc(TN[k[0]])+' \u00b7 '+k[1]+'</button>';}).join('')+'</div><div class="grid" id="e-grid"></div><button type="button" class="more-btn" id="e-more">Cargar m\u00e1s \u00bb</button></section>';}
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
 return '<div class="fl-dates"><span>Primera entrada en inconsolata\u00bb: <a href="/post/'+esc(a.u)+'">'+fcorta(a.d)+'</a></span><span>\u00daltima: <a href="/post/'+esc(b.u)+'">'+fcorta(b.d)+'</a></span></div>';}
function inicial(n){return '<span class="mdc-av ini" aria-hidden="true">'+esc((n||'?').replace(/^(the|el|la|le|les|los|las|il|die|der)\s+/i,'').charAt(0).toUpperCase())+'</span>';}

// ---------- medios
function medioIdx(A,cat){
 var y=String(Y1),L=A.medios.map(function(m,i){return {i:i,n:m.n,p:m.p,c:cat.medios[i]||{},y:0};});
 A.posts.forEach(function(p){if(p.d.slice(0,4)===y)p.m.forEach(function(i){L[i].y++;});});
 L=L.filter(function(o){return o.p>0;});
 var html=crumbs([['Medios']])+'<div class="idx-top"><div><h1 class="soft">Todos los <em>medios</em></h1><p>'+L.length+' medios han pasado por inconsolata\u00bb desde 2011. Los que tienen ficha llevan su logo; el resto te lleva a sus entradas en el buscador.</p></div>'+
  '<div class="idx-tools"><label class="sr" for="mq">Buscar medio</label><input id="mq" type="search" placeholder="Buscar medio\u2026" autocomplete="off"><label class="sr" for="mo">Ordenar</label><select id="mo"><option value="p">M\u00e1s entradas</option><option value="y">M\u00e1s entradas en '+y+'</option><option value="n">A\u2013Z</option></select>'+
  '<a class="btn-ink" href="/estadisticas">Estad\u00edsticas \u00bb</a></div></div><div class="mgrid" id="mgrid"></div>';
 return {html:'<div class="wrap">'+html+'</div>',init:function(){
  function pinta(){var q=fold(document.getElementById('mq').value.trim()),o=document.getElementById('mo').value;
   var R=L.filter(function(x){return !q||fold(x.n).indexOf(q)>=0;}).sort(function(a,b){return o==='n'?a.n.localeCompare(b.n,'es'):o==='y'?(b.y-a.y||b.p-a.p):b.p-a.p;});
   document.getElementById('mgrid').innerHTML=R.map(function(x){var f=x.c.ficha;return '<a class="mdc'+(f?'':' off')+'" href="'+(f?fichaMedio(x.c):'/buscador#m='+x.i)+'">'+(x.c.av?'<span class="mdc-av" aria-hidden="true"><img src="'+esc(x.c.av)+'" alt="" loading="lazy"></span>':inicial(x.n))+
    '<span class="mdc-n">'+esc(x.n)+'</span><span class="mdc-c"><b>'+x.p+'</b> entradas'+(x.y?' \u00b7 '+x.y+' en '+y:'')+'</span></a>';}).join('');}
  document.getElementById('mq').addEventListener('input',pinta);document.getElementById('mo').addEventListener('change',pinta);pinta();}};}

// ---------- autores
function autorIdx(A){var L=A.autores.map(function(a,i){return {i:i,n:a.n,p:a.p,m:a.m||[],y:a.y||[]};}).filter(function(a){return a.p>0;});
 var html=crumbs([['Autores']])+'<div class="idx-top"><div><h1 class="soft">Los <em>autores</em></h1><p>'+L.length.toLocaleString('es-ES')+' periodistas, infografistas e ilustradores citados en el archivo. Busca por nombre o mira los m\u00e1s presentes.</p></div>'+
  '<div class="idx-tools"><label class="sr" for="aq">Buscar autor</label><input id="aq" type="search" placeholder="Buscar autor\u2026" autocomplete="off"></div></div><div class="mgrid" id="agrid"></div>';
 return {html:'<div class="wrap">'+html+'</div>',init:function(){function pinta(){var q=fold(document.getElementById('aq').value.trim());
   var R=L.filter(function(a){return !q||fold(a.n).indexOf(q)>=0;}).sort(function(a,b){return b.p-a.p;}).slice(0,q?200:120);
   document.getElementById('agrid').innerHTML=R.map(function(a){return '<a class="mdc" href="'+fichaAutor(a.n)+'">'+inicial(a.n)+'<span class="mdc-n">'+esc(a.n)+'</span><span class="mdc-c"><b>'+a.p+'</b> entradas'+(a.m[0]?' \u00b7 '+esc(a.m[0]):'')+'</span></a>';}).join('')||'<div class="vacio" style="grid-column:1/-1">No hay ning\u00fan autor con ese nombre.</div>';}
  document.getElementById('aq').addEventListener('input',pinta);pinta();}};}
// datos de Wikidata (en espa\u00f1ol) y resumen de la Wikipedia en espa\u00f1ol
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
function corto(t,n){var s=(t||'').match(/[^.]+\.(\s|$)/g)||[t||''],r='';for(var i=0;i<s.length;i++){if(r&&(r+s[i]).length>n)break;r+=s[i];}r=r.trim();return r.length>n+60?r.slice(0,n).replace(/\s+\S*$/,'')+'\u2026':r;}
var TIPO_ES={Q11032:'peri\u00f3dico',Q1110794:'diario',Q41298:'revista',Q1153191:'peri\u00f3dico digital',Q1002697:'peri\u00f3dico',Q2305295:'revista semanal',Q35127:'web',Q1047113:'revista especializada',Q685935:'revista'};
function bandera(cc){return cc?'<img class="flag" src="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/flags/4x3/'+esc(cc.toLowerCase())+'.svg" alt="" width="24" height="18">':'';}
// iconos de los enlaces de las fichas
var ICR={x:'<path fill="currentColor" d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"/>',
 bsky:'<path fill="currentColor" d="M12 10.8c-1.087-2.114-4.046-6.053-6.798-7.995C2.566.944 1.561 1.266.902 1.565.139 1.908 0 3.08 0 3.768c0 .69.378 5.65.624 6.479.815 2.736 3.713 3.66 6.383 3.364-3.912.58-7.387 2.005-2.83 7.078 5.013 5.19 6.87-1.113 7.823-4.308.953 3.195 2.05 9.271 7.733 4.308 4.267-4.308 1.172-6.498-2.74-7.078 2.67.297 5.568-.628 6.383-3.364.246-.828.624-5.79.624-6.478 0-.69-.139-1.861-.902-2.206-.659-.298-1.664-.62-4.3 1.24C16.046 4.748 13.087 8.687 12 10.8Z"/>',
 ig:'<rect x="2.5" y="2.5" width="19" height="19" rx="5.5" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="12" cy="12" r="4.4" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="17.6" cy="6.4" r="1.4" fill="currentColor"/>',
 li:'<rect x="2" y="2" width="20" height="20" rx="3" fill="currentColor"/><path fill="#fff" d="M6.2 9.6h2.6V18H6.2zM7.5 5.6a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3zM10.4 9.6h2.5v1.2c.4-.7 1.3-1.4 2.6-1.4 2.7 0 3.2 1.8 3.2 4.1V18h-2.6v-4c0-1 0-2.2-1.3-2.2s-1.6 1-1.6 2.1V18h-2.6z"/>',
 wiki:'<text x="12" y="17.5" text-anchor="middle" font-family="Georgia,serif" font-size="17" font-weight="700" fill="currentColor">W</text>',
 be:'<text x="12" y="17" text-anchor="middle" font-family="Archivo,Arial,sans-serif" font-size="13" font-weight="900" fill="currentColor">B\u0113</text>',
 web:'<circle cx="12" cy="12" r="9.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M2.5 12h19M12 2.5c3 3.2 3 15.8 0 19M12 2.5c-3 3.2-3 15.8 0 19" fill="none" stroke="currentColor" stroke-width="1.8"/>',
 bus:'<circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2.6"/><path d="M15.5 15.5l5.5 5.5" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/>',
 link:'<path d="M10 14a4.5 4.5 0 0 0 6.4 0l3.2-3.2a4.5 4.5 0 0 0-6.4-6.4L11.6 6M14 10a4.5 4.5 0 0 0-6.4 0l-3.2 3.2a4.5 4.5 0 0 0 6.4 6.4l1.6-1.6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>'};
function oficioG(t,g){t=t||'';if(g!=='autor'&&g!=='autora')return t;return t.replace(/([^\s\/]+?)(o)?\/a\b/g,function(m,a,o){return g==='autora'?a+'a':a+(o||'');});}
function boton(l,u){var k=l==='X'?'x':l==='Bluesky'?'bsky':l==='Instagram'?'ig':l==='LinkedIn'||/linkedin\./.test(u)?'li':l==='Wikipedia'?'wiki':/behance\./.test(u)?'be':l==='En el buscador'?'bus':l==='Web'?'web':'link';
 if(k==='be')l='Behance';if(k==='li')l='LinkedIn';var ext=/^https?:/.test(u);
 return '<a href="'+esc(u)+'"'+(ext?' target="_blank" rel="noopener"':'')+' class="red"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">'+ICR[k]+'</svg>'+esc(l)+'</a>';}
function redes(o){var L=[];(o.otros||'').split(/\n+/).forEach(function(u){u=u.trim();if(/^https?:/.test(u))L.push([u.replace(/^https?:\/\/(www\.)?/,'').split('/')[0],u]);});if(o.web)L.push(['Web',o.web]);if(o.x)L.push(['X','https://x.com/'+o.x.replace(/^@/,'')]);if(o.bsky)L.push(['Bluesky','https://bsky.app/profile/'+o.bsky.replace(/^@/,'')]);
 if(o.ig)L.push(['Instagram','https://instagram.com/'+o.ig.replace(/^@/,'')]);if(o.linkedin)L.push(['LinkedIn',o.linkedin]);return L;}

// ---------- extras de la ficha de medio: propiedad en \u00e1rbol, formato dibujado y coronas
var PAISES_CC={'Espa\u00f1a':'es','Estados Unidos':'us','EEUU':'us','EE. UU.':'us','Reino Unido':'gb','Francia':'fr','Italia':'it','Alemania':'de','M\u00e9xico':'mx','Argentina':'ar','Chile':'cl','Brasil':'br','China':'cn','Portugal':'pt','B\u00e9lgica':'be','Canad\u00e1':'ca','Om\u00e1n':'om','Uruguay':'uy','Ciudad del Vaticano':'va','Vaticano':'va','Ecuador':'ec','Colombia':'co','Per\u00fa':'pe','Venezuela':'ve','Suiza':'ch','Pa\u00edses Bajos':'nl','Holanda':'nl','Austria':'at','Suecia':'se','Noruega':'no','Dinamarca':'dk','Finlandia':'fi','Irlanda':'ie','Polonia':'pl','Grecia':'gr','Rusia':'ru','Ucrania':'ua','Jap\u00f3n':'jp','Corea del Sur':'kr','India':'in','Australia':'au','Nueva Zelanda':'nz','Sud\u00e1frica':'za','Israel':'il','Turqu\u00eda':'tr','Catar':'qa','Qatar':'qa','Emiratos \u00c1rabes Unidos':'ae','Hong Kong':'hk','Singapur':'sg','Cuba':'cu','Luxemburgo':'lu','Hungr\u00eda':'hu','Rep\u00fablica Checa':'cz','Egipto':'eg','Marruecos':'ma','Taiw\u00e1n':'tw','Arabia Saud\u00ed':'sa','Mongolia':'mn','Andorra':'ad'};
// \u00abPRISA (Espa\u00f1a)\u00bb y debajo, con guion o con %, los que la controlan: \u00ab- Amber Capital (Reino Unido, 29,9%)\u00bb
function arbolProp(t){
 var L=[];String(t||'').split(/\n+/).forEach(function(l){if(!l.trim())return;
  var nv=(l.match(/^\s*(-+|\u00b7+|>+)/)||[''])[0].replace(/\s/g,'').length;l=l.replace(/^\s*[-\u00b7>]+\s*/,'');
  // varias en una l\u00ednea: \u00abA (Espa\u00f1a), B (Francia, 20%)\u00bb
  (l.match(/[^,(]+(\([^)]*\))?/g)||[]).forEach(function(x){x=x.trim();if(x)L.push([nv,x]);});});
 var raiz=-1;L=L.map(function(it){var m=it[1].match(/^(.*?)\s*\(([^)]*)\)\s*$/),n=m?m[1]:it[1],dentro=m?m[2]:'',pm=dentro.match(/(\d+(?:[.,]\d+)?)\s*%/),pct=pm?pm[1]+'%':'',pais=dentro.replace(/(\d+(?:[.,]\d+)?)\s*%/,'').replace(/^[\s,;]+|[\s,;]+$/g,'');
  var nv=it[0];if(!nv&&pct&&raiz>=0)nv=1;if(!nv)raiz=1;return {n:n,pais:pais,pct:pct,nv:nv};});
 if(!L.length)return '';
 return '<ul class="prop">'+L.map(function(o){var cc=PAISES_CC[o.pais];return '<li class="nv'+Math.min(o.nv,3)+'">'+(o.nv?'<span class="rama" aria-hidden="true"></span>':'')+
  '<span class="pnom">'+(cc?bandera(cc):'')+esc(o.n)+(o.pais&&!cc?' <small>('+esc(o.pais)+')</small>':'')+'</span>'+
  (o.pct?'<span class="pct"><i style="width:'+Math.min(100,parseFloat(o.pct.replace(',','.'))||0)+'%"></i><b>'+esc(o.pct)+'</b></span>':'')+'</li>';}).join('')+'</ul>';}
// tama\u00f1os de p\u00e1gina habituales (mm, ancho \u00d7 alto)
var FORMATOS=[['s\u00e1bana',380,600,/s[a\u00e1]bana|broadsheet|gran formato/i],['berlin\u00e9s',315,470,/berlin/i],['tabloide',280,430,/tabloid|compact/i],['revista (A4)',210,297,/revista|a4|magazine/i]];
function formatoSVG(t,nom){t=t||'';var k=FORMATOS.findIndex(function(f){return f[3].test(t);}),m=t.match(/(\d+(?:[.,]\d+)?)\s*[x\u00d7]\s*(\d+(?:[.,]\d+)?)/i),dim=null;
 if(m){var a=parseFloat(m[1].replace(',','.')),b=parseFloat(m[2].replace(',','.'));if(a<100&&b<100){a*=10;b*=10;}dim=[Math.round(Math.min(a,b)),Math.round(Math.max(a,b))];}
 if(k<0&&!dim)return '';var S=.2,W=Math.max(FORMATOS[0][1],dim?dim[0]:0)*S+20,H=Math.max(FORMATOS[0][2],dim?dim[1]:0)*S+20,h='';
 FORMATOS.slice().reverse().forEach(function(f,i){var w=f[1]*S,hh=f[2]*S;h+='<rect x="10" y="'+(H-10-hh)+'" width="'+w+'" height="'+hh+'"/>';});
 var sel=dim||[FORMATOS[k][1],FORMATOS[k][2]];h+='<rect class="on" x="10" y="'+(H-10-sel[1]*S)+'" width="'+sel[0]*S+'" height="'+sel[1]*S+'"/>';
 return '<span class="fmt"><svg viewBox="0 0 '+W+' '+H+'" width="'+W+'" height="'+H+'" role="img" aria-label="P\u00e1gina de '+sel[0]+' por '+sel[1]+' mil\u00edmetros comparada con otros formatos">'+h+'</svg><small>'+(nom?'<em>'+esc(nom)+'</em>':'')+'<b>'+(sel[0]/10)+' \u00d7 '+(sel[1]/10)+' cm'+'</b><br>'+FORMATOS.map(function(f,i){return '<i class="'+(i===k?'on':'')+'">'+f[0]+'</i>';}).join('<span class="sep"> \u00b7 </span>')+'</small></span>';}
// coronas: a\u00f1os en que el medio fue el 1.\u00ba, 2.\u00ba o 3.\u00ba m\u00e1s presente
function coronas(ST,n){if(!ST||!ST.years)return '';var y1=String(new Date().getFullYear()),out=[];
 Object.keys(ST.years).sort().forEach(function(y){var L=ST.years[y].medios||[];for(var i=0;i<3&&i<L.length;i++)if(L[i][0]===n)out.push([y,i]);});
 if(!out.length)return '';var C=['oro','plata','bronce'],T=['1.\u00ba','2.\u00ba','3.\u00ba'];
 return '<div class="coronas">'+out.map(function(o){var tx=T[o[1]]+' medio m\u00e1s presente en inconsolata\u00bb en '+o[0]+(o[0]===y1?' (provisional: el a\u00f1o no ha terminado)':'');return '<span class="cor '+C[o[1]]+(o[0]===y1?' prov':'')+'" tabindex="0" aria-label="'+tx+'" data-tip="'+tx+'"><svg viewBox="0 0 64 44" aria-hidden="true"><path d="M4 40 L2 8 L18 22 L32 2 L46 22 L62 8 L60 40 Z"/></svg><b>'+o[0]+'</b></span>';}).join('')+'</div>';}

function medioFicha(A,cat,FM,mi,ST){
 var m=A.medios[mi],c=cat.medios[mi]||{},f=FM[m.n]||{},ps=A.posts.filter(function(p){return p.m.indexOf(mi)>=0;});
 document.title=m.n+' \u00b7 inconsolata\u00bb';
 var auts=contar(ps,function(p){return p.a.filter(function(a){return (A.autores[a].m||[]).indexOf(m.n)>=0;});}).slice(0,8);
 var fund=+f.fundacion||0,cierre=+f.cierre||0;
 var tieneFmt=!!(f.formato),vis=(c.logo||tieneFmt)?'<div class="fvis">'+(c.logo?'<div class="logo-big logo-wk"><img src="'+esc(c.logo)+'" alt="Logo de '+esc(m.n)+'" onerror="var v=this.closest(\'.fvis\');this.closest(\'.logo-big\').remove();if(!v.querySelector(\'.fmt-box *\')){v.closest(\'.fhero\').classList.add(\'novis\');v.remove();}"></div>':'')+'<div class="fmt-box" id="m-fmt"></div></div>':'';
 var big2=fund?'<div class="stat"><b>'+((cierre||Y1)-fund)+'</b><span>'+(cierre?'a\u00f1os public\u00e1ndose \u00b7 de '+fund+' a '+cierre:'a\u00f1os public\u00e1ndose \u00b7 desde '+fund)+'</span></div>':
  '<div class="stat"><b>'+(new Set(ps.map(function(p){return p.d.slice(0,4);})).size)+'</b><span>a\u00f1os apareciendo en inconsolata\u00bb</span></div>';
 var html=crumbs([['Medios','/medios'],[m.n]])+'<section class="fhero'+(vis?'':' novis')+'">'+vis+'<div class="finfo"><span class="caps ante" style="color:var(--accent)">Medio \u00bb '+bandera(f.cc)+esc(f.pais||'')+'<span id="m-tipo"></span>'+(f.desaparecido||cierre?' \u00b7 ya no se publica':'')+'</span>'+
  '<h1 class="soft">'+esc(m.n)+'</h1>'+
  '<div class="wk" id="wk"><div class="wk-h"><span class="caps">Datos \u00bb</span><a class="wk-src" id="wk-src" href="'+esc(f.wikipedia||'#')+'" target="_blank" rel="noopener"'+(f.wikipedia?'':' hidden')+'>Fuente: Wikidata y Wikipedia \u00b7 CC BY-SA \u00bb</a></div>'+
  '<div class="wk-top">'+(c.av?'<span class="av-slot" aria-hidden="true"><img src="'+esc(c.av)+'" alt=""></span>':'')+'<p class="wk-r'+(f.nota?' propio':'')+'" id="wk-r"'+(f.nota?'':' hidden')+'>'+esc(f.nota||'')+'</p></div><dl id="wk-dl"></dl></div>'+
  '<div class="flinks" id="m-links"></div></div></section>';
 function datos(o){o=o||{};var lab=function(ids){return (ids||[]).map(function(i){return (o.l||{})[i];}).filter(Boolean);};
  var tipo=f.tipo||(o.tipo||[]).map(function(i){return TIPO_ES[i]||(o.l||{})[i];}).filter(Boolean)[0]||'';if(tipo)document.getElementById('m-tipo').textContent=' \u00b7 '+tipo;
  var d=[],anio=f.fundacion||o.anio,fin=f.cierre||o.fin;
  if(anio)d.push(['Fundaci\u00f3n',anio+(fin?' \u00b7 cierre en '+fin:'')]);var fu=f.fundador?[f.fundador]:lab(o.fund);if(fu.length)d.push([fu.length>1?'Fundadores':'Fundador',fu.slice(0,3).join(', ')]);
  var se=f.sede?[f.sede]:lab(o.sede);if(se.length)d.push(['Sede',se[0]]);var pr=f.propietario?[f.propietario]:lab(o.prop);if(pr.length)d.push(['Propietario',f.propietario?arbolProp(f.propietario):esc(pr.join(', ')),1]);if(f.director)d.push(['Direcci\u00f3n',esc(f.director)+(f.director_desde?' <small class="dd">'+esc(f.director_desde)+'</small>':''),1]);
  var fo=f.formato?[f.formato]:lab(o.formato);var fb=document.getElementById('m-fmt');if(fo.length){var fn=fo[0].replace(/\s*\([^)]*\)/g,'').trim();if(fb)fb.innerHTML='<span class="caps">Formato \u00bb</span>'+(formatoSVG(fo[0],fn)||'<b>'+esc(fn)+'</b>');else d.push(['Formato',esc(fn)+formatoSVG(fo[0]),1]);}var id=f.idioma?[f.idioma]:lab(o.idioma);if(id.length)d.push(['Idioma',id.join(', ')]);
  if(f.pais)d.push(['Pa\u00eds',f.pais]);if(o.issn)d.push(['ISSN',o.issn]);
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
  '<div class="stat"><b>'+ps.length+'</b><span>entradas en inconsolata\u00bb</span>'+coronas(ST,m.n)+'</div>'+big2+
  (auts.length?'<div class="stat"><span>Autores m\u00e1s citados</span><ol class="tops">'+auts.map(function(a){return '<li><a href="'+fichaAutor(A.autores[a[0]].n)+'">'+esc(A.autores[a[0]].n)+'<small>'+a[1]+'</small></a></li>';}).join('')+'</ol></div>':'')+
  '<div class="stat" style="grid-column:1/-1"><span>Tipos de pieza</span>'+tiposBanda(ps,'m='+mi)+fechasBanda(ps)+'</div></div></section>'+
  '<div class="wrap">'+barrasAnios(ps)+entradas(A,ps)+'</div>',
  init:function(){activaEntradas(A,ps);datos(null);if(f.qid)wikidata(f.qid).then(datos).catch(function(){});}};}

function chipMedio(cat,n){var c=cat.medios.find(function(x){return x.n===n;}),i=cat.medios.indexOf(c);
 return '<a class="ch-av" href="'+(c&&c.ficha?fichaMedio(c):'/buscador#m='+i)+'">'+(c&&c.avw?'<img src="'+esc(c.avw)+'" alt="">':'')+esc(n)+'</a>';}
function autorFicha(A,cat,FM,AX,ai){var a=A.autores[ai],ps=A.posts.filter(function(p){return p.a.indexOf(ai)>=0;}),x=AX[a.n]||{};
 document.title=a.n+' \u00b7 inconsolata\u00bb';
 var md=x.medio||(a.m||[])[0],mc=md?cat.medios.find(function(m){return m.n===md;}):null,fm=FM[md]||{};
 var pais=x.pais||fm.pais||'',cc=x.cc||fm.cc||'';
 var otros=md?A.autores.map(function(o,i){return {i:i,n:o.n,p:o.p,m:o.m||[]};}).filter(function(o){return o.i!==ai&&o.m.indexOf(md)>=0&&o.p>0;}).sort(function(p,q){return q.p-p.p;}).slice(0,8):[];
 var ys=ps.map(function(p){return +p.d.slice(0,4);}),y0=Math.min.apply(null,ys),y1=Math.max.apply(null,ys),ny=new Set(ys).size;
 var W=ps.filter(function(p){return p.im&&p.a.length<=6;}).slice().reverse();
 var vis=W.length?'<div class="fvis"><figure class="work"><span class="tape" aria-hidden="true"></span><a class="wph" id="work-a" href="#" aria-label="Abrir esta pieza en inconsolata\u00bb"><img id="work-img" alt="" src=""></a>'+
  (W.length>1?'<button type="button" class="wnext" id="work-next" aria-label="Ver otra pieza al azar"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M4 7h11l-3-3M20 17H9l3 3M15 4l3 3-3 3M9 20l-3-3 3-3" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg><span>otra</span></button>':'')+
  '<figcaption><span class="wn">Pieza <b id="work-n"></b> de <b>'+W.length+'</b> en el archivo</span><span class="wm" id="work-m"></span></figcaption></figure></div>':'';
 var L=redes(x);
 var html='<div class="wrap">'+crumbs([['Autores','/autores'],[a.n]])+'<section class="fhero'+(vis?'':' novis')+'">'+vis+'<div class="finfo"><span class="caps ante" style="color:var(--accent)">'+(x.genero==='autora'?'Autora':x.genero==='autor'?'Autor':'Periodista')+(a.m&&a.m.length?' \u00bb '+esc(a.m.slice(0,3).join(' \u00b7 ')):'')+'</span>'+
  '<div class="name-row"><h1 class="soft autor">'+esc(a.n)+'</h1>'+(mc?'<a class="av-medio" href="'+fichaMedio(mc)+'" aria-label="Trabaja en '+esc(md)+'">'+(mc.av?'<span class="av-slot" aria-hidden="true"><img src="'+esc(mc.av)+'" alt=""></span>':'')+'<span>'+esc(md)+' \u00bb</span></a>':'')+'</div>'+(pais||x.oficio?'<p class="nac">'+bandera(cc)+'<span>'+esc(pais)+(pais&&x.oficio?' \u00b7 ':'')+esc(oficioG(x.oficio,x.genero))+'</span></p>':'')+
  (x.texto?'<div class="ftext">'+esc(x.texto)+'</div>':'')+
  '<div class="flinks">'+L.map(function(l){return boton(l[0],l[1]);}).join('')+boton('En el buscador','/buscador#a='+ai)+'</div></div></section></div>'+
  '<section class="band"><div class="wrap in"><div class="stat"><b>'+ps.length+'</b><span>entradas en inconsolata\u00bb</span></div>'+
  '<div class="stat"><b>'+ny+'</b><span>a\u00f1os apareciendo en inconsolata\u00bb \u00b7 de '+y0+' a '+y1+'</span></div>'+
  (a.m&&a.m.length?'<div class="stat"><span>Medios</span><div class="chips">'+a.m.map(function(n){return chipMedio(cat,n);}).join('')+'</div></div>':'')+
  (otros.length?'<div class="stat"><span>Otros autores de '+esc(md)+'</span><ol class="tops">'+otros.map(function(o){return '<li><a href="'+fichaAutor(o.n)+'">'+esc(o.n)+'<small>'+o.p+'</small></a></li>';}).join('')+'</ol></div>':'')+
  '<div class="stat" style="grid-column:1/-1"><span>Tipos de pieza</span>'+tiposBanda(ps,'a='+ai)+fechasBanda(ps)+'</div></div></section>'+
  '<div class="wrap">'+barrasAnios(ps)+entradas(A,ps)+'</div>';
 return {html:html,init:function(){activaEntradas(A,ps);if(!W.length)return;var i=Math.floor(Math.random()*W.length);
  function show(){var w=W[i%W.length];document.getElementById('work-a').href='/post/'+w.u;document.getElementById('work-img').setAttribute('s'+'rc',w.im);
   document.getElementById('work-n').textContent=(i%W.length)+1;document.getElementById('work-m').innerHTML=medsI(w.m)+' \u00b7 '+fcorta(w.d);}
  show();var nb=document.getElementById('work-next');if(nb)nb.addEventListener('click',function(){i+=1+Math.floor(Math.random()*(W.length-1));show();});}};}

// ---------- especiales
function rangoE(a,b){var f=function(d,y){return +d.slice(8,10)+' de '+MESES[+d.slice(5,7)-1]+(y?' de '+d.slice(0,4):'');};
 return a===b?f(a,1):a.slice(0,4)===b.slice(0,4)?'del '+f(a,0)+' al '+f(b,1):'del '+f(a,1)+' al '+f(b,1);}
function icoE(cat,e){if(ESPI[e.slug])return ESPI[e.slug];var ti=cat.temas.findIndex(function(t){return t.n===e.tema;});if(ti<0)ti=cat.temas.findIndex(function(t){return t.n===e.padre;});return ti>=0?TS[ti]:'';}
function espIdx(ES,cat){
 var top=ES.filter(function(e){return !e.cap_de;}),by={};ES.forEach(function(e){by[e.slug]=e;});
 var g={};top.forEach(function(e){(g[e.padre]=g[e.padre]||[]).push(e);});
 var orden=cat.temas.map(function(t){return t.n;}).filter(function(n){return g[n];});
 var html=crumbs([['Especiales']])+'<div class="idx-top"><div><h1 class="soft">Los <em>especiales</em></h1><p>'+top.length+' acontecimientos e historias con p\u00e1gina propia, cada uno dentro de su tema. Algunos se dividen en cap\u00edtulos.</p></div></div><div class="esp-idx">'+
  orden.map(function(t){var ti=cat.temas.findIndex(function(x){return x.n===t;});return '<div class="esp-g"><h2><a href="/buscador#h='+ti+'">'+esc(t)+' \u00bb</a></h2><div class="esp-l">'+g[t].sort(function(a,b){return (b.hasta||'').localeCompare(a.hasta||'');}).map(function(e){var ic=icoE(cat,e);
   return '<div class="esp-i"><a class="esp-a" href="/especiales#'+esc(e.slug)+'">'+(ic?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+ic+'"/></svg>':'')+'<span>'+esc(e.titulo)+'</span><small>'+e.posts.length+'</small></a>'+
    ((e.capitulos||[]).length?'<span class="esp-caps">'+e.capitulos.map(function(c){return by[c];}).filter(Boolean).sort(function(a,b){return (a.desde||'').localeCompare(b.desde||'');}).map(function(c){return '<a href="/especiales#'+esc(c.slug)+'">'+esc(c.titulo)+'</a>';}).join('')+'</span>':'')+'</div>';}).join('')+'</div></div>';}).join('')+'</div>';
 return {html:'<div class="wrap">'+html+'</div>',init:function(){}};}
function espPag(A,cat,ES,x){var byId={},by={};A.posts.forEach(function(p){byId[p.i]=p;});ES.forEach(function(e){by[e.slug]=e;});
 var ps=x.posts.map(function(i){return byId[i];}).filter(Boolean).sort(function(a,b){return b.d.localeCompare(a.d);});
 document.title=x.titulo+' \u00b7 especial \u00b7 inconsolata\u00bb';
 var pi=cat.temas.findIndex(function(t){return t.n===x.padre;}),ic=icoE(cat,x),madre=x.cap_de?by[x.cap_de]:null;
 var carta=function(p){var ie=icoEsp(espSl(p.i),'',false),auts=p.a.slice(0,3).map(function(i){return A.autores[i].n;});
  return '<a class="ec" href="/post/'+esc(p.u)+'"><div class="ph">'+(p.im?'<img loading="lazy" src="'+esc(p.im)+'" alt="" onerror="this.remove()">':'')+(p.s?'<span class="sec">'+esc(SECN[p.s])+'</span>':'')+
   '<span class="ico">'+(ie?'<span>'+ie+'</span>':p.k.slice(0,3).map(function(k){return '<span title="'+esc(TN[k])+'"><svg viewBox="0 0 64 64" aria-hidden="true" style="overflow:visible"><use href="#i-'+k+'"/></svg></span>';}).join(''))+'</span></div>'+
   '<span class="meta"><b>'+(+p.d.slice(8,10))+' '+MES3[+p.d.slice(5,7)-1]+'</b>'+(p.m.length?' \u00b7 '+medsI(p.m):'')+'</span><span class="tt">'+esc(tituloP(p))+'</span>'+(auts.length?'<span class="by">por '+esc(auts.join(', '))+'</span>':'')+'</a>';};
 var meses=function(L){var gr={};L.forEach(function(p){(gr[p.d.slice(0,7)]=gr[p.d.slice(0,7)]||[]).push(p);});
  return Object.keys(gr).map(function(k){var v=gr[k];return '<section class="mo"><h3>'+MESES[+k.slice(5,7)-1].replace(/^./,function(c){return c.toUpperCase();})+'<small>'+k.slice(0,4)+' \u00b7 '+v.length+' '+(v.length===1?'entrada':'entradas')+'</small></h3><div class="g">'+v.map(carta).join('')+'</div></section>';}).join('');};
 var caps=(x.capitulos||[]).map(function(c){return by[c];}).filter(Boolean).sort(function(a,b){return (b.hasta||'').localeCompare(a.hasta||'');}),tl='';
 if(caps.length){var usados={};
  tl=caps.map(function(c){var L=c.posts.map(function(i){return byId[i];}).filter(Boolean).sort(function(a,b){return b.d.localeCompare(a.d);});L.forEach(function(p){usados[p.i]=1;});
   return '<div class="cap"><div class="cap-h"><h2 class="soft"><a href="/especiales#'+esc(c.slug)+'">'+esc(c.titulo)+'</a></h2><span>'+L.length+' '+(L.length===1?'entrada':'entradas')+(c.desde?' \u00b7 '+rangoE(c.desde,c.hasta||c.desde):'')+'</span></div>'+meses(L)+'</div>';}).join('');
  var resto=ps.filter(function(p){return !usados[p.i];});
  if(resto.length)tl+='<div class="cap"><div class="cap-h"><h2 class="soft">Otras entradas</h2><span>'+resto.length+' '+(resto.length===1?'entrada':'entradas')+'</span></div>'+meses(resto)+'</div>';}
 else tl=meses(ps);
 var cm=contar(ps,function(p){return p.m;}).slice(0,12),ca=contar(ps,function(p){return p.a;}).slice(0,12);
 var her=ES.filter(function(y){return !y.cap_de&&y.padre===x.padre&&y!==x&&y!==madre;});
 var cr=[['Especiales','/especiales']];if(madre)cr.push([madre.titulo,'/especiales#'+madre.slug]);cr.push([x.titulo]);
 var html='<div class="wrap">'+crumbs(cr)+'</div><section class="eh"><div class="wrap in"><div><span class="kick">'+(madre?'Cap\u00edtulo de \u00ab'+esc(madre.titulo)+'\u00bb \u00bb':'Especial \u00bb')+'</span><h1 class="soft">'+esc(x.titulo)+'</h1><div class="meta"><span>'+ps.length+' '+(ps.length===1?'entrada':'entradas')+'</span>'+(x.desde?'<span>'+rangoE(x.desde,x.hasta||x.desde)+'</span>':'')+
  (caps.length?'<span>'+caps.length+' cap\u00edtulos</span>':'')+(pi>=0?'<span>Dentro de: <a href="/buscador#h='+pi+'">'+esc(x.padre)+' \u00bb</a></span>':'')+'</div></div>'+(ic?'<svg class="big" viewBox="0 0 64 64" aria-hidden="true"><use href="#'+ic+'" class="k"/><use href="#'+ic+'" class="m" x="3" y="2.5"/></svg>':'')+'</div></section>'+
  '<div class="wrap">'+(x.texto?'<div class="etext">'+esc(x.texto)+'</div>':'')+
  (caps.length?'<nav class="caps-nav" aria-label="Cap\u00edtulos"><span class="caps">Cap\u00edtulos \u00bb</span>'+caps.map(function(c){return '<a href="/especiales#'+esc(c.slug)+'">'+esc(c.titulo)+'<small>'+c.posts.length+'</small></a>';}).join('')+'</nav>':'')+
  '<div class="who"><div><h2>Medios</h2><div class="chips">'+cm.map(function(c){var m=cat.medios[c[0]];return '<a href="'+(m&&m.ficha?fichaMedio(m):'/buscador#m='+c[0])+'">'+esc(A.medios[c[0]].n)+'<small>'+c[1]+'</small></a>';}).join('')+'</div></div>'+
  '<div><h2>Autores</h2><div class="chips">'+(ca.map(function(c){return '<a href="'+fichaAutor(A.autores[c[0]].n)+'">'+esc(A.autores[c[0]].n)+'<small>'+c[1]+'</small></a>';}).join('')||'<span style="font-size:14px;color:var(--muted)">Sin autores identificados</span>')+'</div></div></div>'+
  '<div class="tl-bar"><h2 class="soft">La cobertura, <em>'+(caps.length?'cap\u00edtulo a cap\u00edtulo':'mes a mes')+'</em></h2><button type="button" id="order" aria-pressed="true">Ver en orden cronol\u00f3gico \u00bb</button></div><div class="tl" id="tl">'+tl+'</div>'+
  (her.length?'<section class="others"><h2>Otros especiales de '+esc(x.padre)+'</h2><div class="chips">'+her.map(function(y){var i2=icoE(cat,y);return '<a href="/especiales#'+esc(y.slug)+'">'+(i2?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+i2+'"/></svg>':'')+esc(y.titulo)+'<small>'+y.posts.length+'</small></a>';}).join('')+'</div></section>':'')+
  '<p style="margin:56px 0 0"><a class="btn-ink todos" href="/especiales">Todos los especiales \u00bb</a></p></div>';
 return {html:html,init:function(){document.getElementById('order').addEventListener('click',function(){var tl=document.getElementById('tl'),b=this,rev=b.getAttribute('aria-pressed')!=='true';
  var rv=function(box,sel){[].slice.call(box.querySelectorAll(sel)).reverse().forEach(function(c){box.appendChild(c);});};
  rv(tl,':scope>.cap');rv(tl,':scope>.mo');[].forEach.call(tl.querySelectorAll('.cap'),function(c){rv(c,':scope>.mo');});[].forEach.call(tl.querySelectorAll('.g'),function(g){rv(g,':scope>*');});
  b.setAttribute('aria-pressed',rev);b.textContent=rev?'Ver en orden cronol\u00f3gico \u00bb':'Ver lo m\u00e1s reciente primero \u00bb';});}};}

// ---------- novedades
function novPag(A,cat){var L=((A&&A.ligeros)||[]).slice().sort(function(a,b){return (b.f||'').localeCompare(a.f||'');});
 var html='<div class="wrap">'+crumbs([['Novedades de la web']])+'<div class="nov-top"><h1 class="soft">Novedades <em>de la web</em></h1><p>Mejoras, arreglos y cosas nuevas de inconsolata\u00bb, de la m\u00e1s reciente a la m\u00e1s antigua.</p></div>'+
  '<ul class="nov-list">'+(L.map(function(a){var ti=a.ico?cat.temas.findIndex(function(t){return t.n===a.ico;}):-1,sy=ti>=0?TS[ti]:a.ico;
   return '<li><span class="f">'+(a.f?(+a.f.slice(8))+' '+MES3[+a.f.slice(5,7)-1]+'<small>'+a.f.slice(0,4)+'</small>':'')+'</span><span class="ic'+(sy?'':' bl')+'">'+(sy?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+esc(sy)+'"/></svg>':'\u00bb')+'</span>'+
    (a.u?'<a class="t" href="'+esc(a.u)+'">'+esc(a.t)+'</a>':'<span class="t">'+esc(a.t)+'</span>')+'</li>';}).join('')||'<li><span class="t">Todav\u00eda no hay novedades.</span></li>')+'</ul></div>';
 if(L[0])ls('inc-novedades-visto',L[0].f||'');
 return {html:html,init:function(){}};}

// ---------- cronolog\u00eda: una tira horizontal con 15 a\u00f1os de la web
function cronoPag(A,cat,ES,CR){
 document.title='Cronolog\u00eda \u00b7 inconsolata\u00bb';
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
  pts.push({tipo:h.tipo||'pieza',d:d,t:h.t||(p?tituloP(p):''),u:h.u||(p?'/post/'+p.u:'#'),im:h.img||(p&&p.im)||'',nota:h.nota||'',m:p?p.m.slice(0,2).map(function(i){return A.medios[i].n;}).join(' \u00b7 '):''});});
 pts.sort(function(a,b){return a.d.localeCompare(b.d);});
 // carriles: cada pieza en el primero que est\u00e9 libre
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
   '<span class="k">'+KIT[o.tipo]+' \u00bb</span><span class="f">'+fd(o.d)+'</span><span class="tt">'+destaca(o.t)+'</span>'+(o.nota?'<span class="nt">'+esc(o.nota)+'</span>':'')+'</a>'+
   (dx<-2?'<i class="ld" style="top:'+(SP-top-30)+'px;height:30px;left:'+(10+dx)+'px"></i>':'<i class="ld" style="height:'+(SP-top)+'px"></i>')+(dx<-2?'<i class="ld-h" style="left:'+(10+dx)+'px;width:'+(-dx)+'px;top:'+(SP-top-30)+'px"></i><i class="ld-v" style="top:40px;height:'+(SP-top-70)+'px"></i>':'')+'</div>';}).join('');
 var bs=barras.map(function(o){return '<a class="cr-b" href="'+esc(o.u)+'" style="left:'+o.x+'px;top:'+(yB+o.lane*36)+'px" title="'+esc(o.t)+' \u00b7 '+o.n+' entradas \u00b7 '+fd(o.a)+(o.b!==o.a?' \u2013 '+fd(o.b):'')+'"><i style="width:'+o.w+'px"></i>'+
   (o.ic?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+o.ic+'"/></svg>':'')+'<span>'+esc(o.t)+'</span></a>';}).join('');
 var hs=hilos.map(function(o){return '<a class="cr-h" href="'+esc(o.u)+'" style="left:'+o.x+'px;top:'+(yH+o.lane*26)+'px;width:'+o.w+'px" title="'+esc(o.t)+' \u00b7 '+o.n+' entradas \u00b7 '+fd(o.a)+' \u2013 '+fd(o.b)+'"><span>'+(o.ic?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+o.ic+'"/></svg>':'')+esc(o.t)+' <small>'+o.n+'</small></span></a>';}).join('');
 // minimapa
 var mm=anios.map(function(y){return '<button type="button" data-y="'+y+'" style="left:'+((X(y+'-01-01')-PAD)/(W-PAD-FIN)*100)+'%">'+String(y).slice(2)+'</button>';}).join('')+
  pts.map(function(o){return '<i class="t-'+o.tipo+'" style="left:'+((o.x-PAD)/(W-PAD-FIN)*100)+'%"></i>';}).join('');
 var cuenta=function(t){return t==='cobertura'?barras.length+hilos.length:pts.filter(function(o){return o.tipo===t;}).length;};
 var html='<div class="wrap">'+crumbs([['Archivo','/archive'],['Cronolog\u00eda']])+'<div class="cr-top"><h1 class="soft">Crono<em>log\u00eda</em></h1><p>'+(+hoy.slice(0,4)-y0)+' a\u00f1os de dise\u00f1o de noticias en una tira: las grandes coberturas, las noticias que llenaron portadas y las piezas que no hemos olvidado.</p></div>'+
  '<div class="cr-ctl"><div class="cr-f" role="group" aria-label="Mostrar">'+['noticia','pieza','cobertura','web'].map(function(t){return '<button type="button" class="t-'+t+'" data-f="'+t+'" aria-pressed="true"><i></i>'+(t==='cobertura'?'Coberturas':t==='web'?'La web':KIT[t]+'s')+' <small>'+cuenta(t)+'</small></button>';}).join('')+'</div>'+
  '<div class="cr-nav"><button type="button" data-ir="ini">\u00ab Inicio</button><button type="button" data-ir="hoy">Hoy \u00bb</button></div></div></div>'+
  '<div class="cr-sc" id="cr-sc" tabindex="0" aria-label="L\u00ednea del tiempo; despl\u00e1zate en horizontal"><div class="cr-in" style="width:'+W+'px;height:'+H+'px;--sp:'+SP+'px">'+
  '<div class="cr-intro" style="height:'+SP+'px"><span class="caps">Octubre de '+y0+'</span><p class="soft">Aqu\u00ed empieza inconsolata\u00bb.</p><span class="caps">Arrastra hacia la izquierda \u00bb</span></div>'+
  marcas+'<div class="cr-sp" style="top:'+SP+'px"></div><div class="cr-act" style="top:'+(SP+3)+'px">'+act+'</div>'+
  '<span class="cr-lab" style="top:'+(yB-24)+'px">Coberturas especiales \u00bb</span>'+bs+(hilos.length?'<span class="cr-lab" style="top:'+(yH-24)+'px">Grandes historias \u00bb</span>'+hs:'')+cartas+
  '<div class="cr-hoy" style="left:'+X(hoy)+'px;height:'+SP+'px"><span>Hoy</span></div></div></div>'+
  '<div class="wrap"><div class="cr-mm" id="cr-mm">'+mm+'<span class="vw" id="cr-vw"></span></div><p class="cr-nota">Arrastra la tira, usa la barra de abajo o pulsa un a\u00f1o. Las coberturas enlazan a su especial; el resto, al post.</p></div>';
 // mientras no se publique (cronologia.json \u00abvisible\u00bb: true), solo un adelanto borroso con \u00abPr\u00f3ximamente\u00bb
 if(!CR.visible){var i0=html.indexOf('<div class="cr-sc"'),i1=html.indexOf('<div class="wrap"><div class="cr-mm"');
  var tira=html.slice(i0,i1).replace('id="cr-sc" tabindex="0"','id="cr-sc" tabindex="-1" inert');
  var pre='<div class="wrap">'+crumbs([['Archivo','/archive'],['Cronolog\u00eda']])+'<div class="cr-top"><h1 class="soft">Crono<em>log\u00eda</em></h1><p>'+(+hoy.slice(0,4)-y0)+' a\u00f1os de dise\u00f1o de noticias en una sola tira: las grandes coberturas, las noticias que llenaron portadas y las piezas que no hemos olvidado.</p></div></div>';
  return {html:pre+'<div class="cr-pronto">'+tira+'<div class="cr-velo"><span class="caps">Pr\u00f3ximamente \u00bb</span><p class="soft">Estamos terminando de colocar quince a\u00f1os de historia.</p><a class="btn-ink" href="/archive">Mientras, el archivo \u00bb</a></div></div><div class="wrap"><p class="cr-nota" style="margin-top:18px">La cronolog\u00eda se abrir\u00e1 muy pronto.</p></div>',
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
 
var SECN = {m: 'Mucho m\u00e1s', x: 'EXTRA!', d: 'Detallitos', b: 'Metablog', o: 'Offtopic'};
var MESES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'];
function nz(s) { return String(s).toLowerCase().normalize('NFKD').replace(/[\u0300-\u036f]/g, '').replace(/\u00f1/g, 'n').replace(/[^a-z0-9\u00f1]+/g, ' ').trim(); }
function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]; }); }
var P = D.posts, Y0 = 2011, Y1 = new Date().getFullYear();
// pajar de b\u00fasqueda de cada post
D.autores.forEach(function (a) { a.k = nz([a.n].concat(a.v).join(' | ')); });
D.medios.forEach(function (m) { m.k = nz([m.n].concat(m.v).join(' | ')); });
D.temas.forEach(function (t) { t.k = nz(t.n); });
P.forEach(function (p) {
  p.y = +p.d.slice(0, 4);
  p.hay = ' ' + p.x + ' ' + (TIT[p.i] ? nz(quita(TIT[p.i])) + ' ' : '') + p.m.map(function (i) { return D.medios[i].k; }).join(' ') + ' ' +
    p.a.map(function (i) { return D.autores[i].k; }).join(' ') + ' ' + p.h.map(function (i) { return D.temas[i].k; }).join(' ') + ' ' +
    p.k.map(function (k) { return nz(TN[k]); }).join(' ') + ' ' + (p.s ? nz(SECN[p.s]) : '') + ' ' + p.g.join(' ') + ' ';
});
var st = {q: '', k: [], s: [], y: [], m: [], a: [], h: [], o: 'new'}, shown = 36, res = [];

function readHash() {
  var h = location.hash.slice(1); if (!h) return;
  h.split('&').forEach(function (kv) {
    var i = kv.indexOf('='), k = kv.slice(0, i), v = decodeURIComponent(kv.slice(i + 1));
    if (k === 'q' || k === 'o') st[k] = v;
    else if (st[k]) st[k] = v.split('|').map(function (x) { if (/^[amh]$/.test(k) && isNaN(+x)) { var arr = k === 'a' ? D.autores : k === 'm' ? D.medios : D.temas, f = nz(x); return arr.findIndex(function (o) { return nz(o.n) === f; }); } return /^[amhy]$/.test(k) ? +x : x; }).filter(function (x) { return x !== -1; });
  });
}
function writeHash() {
  var out = [];
  if (st.q) out.push('q=' + encodeURIComponent(st.q));
  ['k', 's', 'y', 'm', 'a', 'h'].forEach(function (k) { if (st[k].length) out.push(k + '=' + encodeURIComponent(st[k].join('|'))); });
  if (st.o !== 'new') out.push('o=' + st.o);
  history.replaceState(null, '', out.length ? '#' + out.join('&') : location.pathname);
}
function has(arr, v) { return arr.indexOf(v) >= 0; }
function match(p, skip) {
  if (skip !== 'k' && st.k.length && !st.k.some(function (k) { return has(p.k, k); })) return false;
  if (skip !== 's' && st.s.length && !st.s.some(function (s) { return s === 'n' ? !p.s : (p.s === s || has(p.g, s)); })) return false;
  if (skip !== 'y' && st.y.length && !has(st.y, p.y)) return false;
  if (skip !== 'm' && st.m.length && !st.m.some(function (i) { return has(p.m, i); })) return false;
  if (skip !== 'a' && st.a.length && !st.a.every(function (i) { return has(p.a, i); })) return false;
  if (skip !== 'h' && st.h.length && !st.h.every(function (i) { return has(p.h, i); })) return false;
  return true;
}
function toks() { return nz(st.q).split(' ').filter(function (t) { return t.length > 0; }); }
function textOk(p, T) { for (var i = 0; i < T.length; i++) if (p.hay.indexOf(T[i].length < 4 ? ' ' + T[i] : T[i]) < 0) return false; return true; }
function score(p, T) {
  var s = 0; T.forEach(function (t) { if ((' ' + nz(p.t + ' ' + p.b) + ' ').indexOf(' ' + t) >= 0) s += 3; if (p.hay.indexOf(' ' + t + ' ') >= 0) s += 1; }); return s;
}
function run() {
  var T = toks(), base = T.length ? P.filter(function (p) { return textOk(p, T); }) : P;
  res = base.filter(function (p) { return match(p); });
  if (st.o === 'old') res = res.slice().reverse();
  else if (st.o === 'rel' && T.length) res = res.map(function (p) { return [score(p, T), p]; }).sort(function (a, b) { return b[0] - a[0] || (a[1].d < b[1].d ? 1 : -1); }).map(function (x) { return x[1]; });
  shown = 36;
  facets(base, T); actives(); ficha(); render(); writeHash();
}
function cnt(base, key, getter) {
  var c = {}; base.forEach(function (p) { if (!match(p, key)) return; getter(p).forEach(function (v) { c[v] = (c[v] || 0) + 1; }); }); return c;
}
var openF = {};
function list(id, key, c, label, icon, limit) {
  var keys = Object.keys(c).sort(function (a, b) { return c[b] - c[a]; });
  st[key].forEach(function (v) { if (!(String(v) in c)) { c[v] = 0; keys.unshift(String(v)); } });
  var lim = openF[key] ? 60 : limit, el = document.getElementById(id);
  el.innerHTML = keys.slice(0, lim).map(function (v) {
    var vv = /^[amhy]$/.test(key) ? +v : v;
    return '<button type="button" data-k="' + key + '" data-v="' + esc(v) + '" aria-pressed="' + has(st[key], vv) + '">' + (icon ? icon(v) : '') + '<span>' + esc(label(v)) + '</span><span class="ct">' + c[v] + '</span></button>';
  }).join('') + (keys.length > limit ? '<button type="button" class="vmore" data-more="' + key + '">' + (openF[key] ? 'Ver menos' : 'Ver m\u00e1s (' + keys.length + ')') + '</button>' : '');
}
function ico(k) { return '<svg viewBox="0 0 64 64" aria-hidden="true" style="overflow:visible"><use href="#i-' + k + '"/></svg>'; }
function facets(base, T) {
  list('f-k', 'k', cnt(base, 'k', function (p) { return p.k; }), function (v) { return TN[v]; }, ico, 9);
  list('f-h', 'h', cnt(base, 'h', function (p) { return p.h.filter(function (v) { return !D.temas[v].x; }); }), function (v) { return D.temas[v].n; }, function (v) { return '<svg viewBox="0 0 64 64" aria-hidden="true" style="overflow:visible"><use href="#' + TS[v] + '"/></svg>'; }, 10);
  list('f-m', 'm', cnt(base, 'm', function (p) { return p.m; }), function (v) { return D.medios[v].n; }, null, 10);
  list('f-a', 'a', cnt(base, 'a', function (p) { return p.a; }), function (v) { return D.autores[v].n; }, null, 10);
  var cy = cnt(base, 'y', function (p) { return [p.y]; }), mx = 1, h = '';
  for (var y = Y0; y <= Y1; y++) mx = Math.max(mx, cy[y] || 0);
  for (y = Y0; y <= Y1; y++) h += '<button type="button" data-k="y" data-v="' + y + '" aria-pressed="' + has(st.y, y) + '" title="' + y + ': ' + (cy[y] || 0) + ' entradas" aria-label="' + y + ', ' + (cy[y] || 0) + ' entradas" style="height:' + Math.max(3, (cy[y] || 0) / mx * 100) + '%"></button>';
  var ys = document.getElementById('f-y'); ys.innerHTML = h; ys.classList.toggle('has-sel', st.y.length > 0);
}
function nameOf(k, v) { return k === 'm' ? D.medios[v].n : k === 'a' ? D.autores[v].n : k === 'h' ? D.temas[v].n : k === 'k' ? TN[v] : k === 's' ? (SECN[v] || (v === 'n' ? 'Posts normales' : v)) : String(v); }
var KN = {k: 'Tipo', s: 'Secci\u00f3n', y: 'A\u00f1o', m: 'Medio', a: 'Autor', h: 'Tema'};
function actives() {
  var h = '';
  if (st.q) h += '<button type="button" class="chip" data-rm="q"><i>Texto</i>\u00ab' + esc(st.q) + '\u00bb <b>\u00d7</b></button>';
  ['a', 'm', 'h', 'k', 's', 'y'].forEach(function (k) { st[k].forEach(function (v) { h += '<button type="button" class="chip" data-rm="' + k + '" data-v="' + esc(v) + '"><i>' + KN[k] + '</i>' + esc(nameOf(k, v)) + ' <b>\u00d7</b></button>'; }); });
  if (h) h += '<button type="button" class="clearall" data-rm="all">Borrar todo</button>';
  document.getElementById('active').innerHTML = h;
  var n = res.length;
  document.getElementById('count').innerHTML = n.toLocaleString('es-ES') + '<small>' + (n === 1 ? 'entrada' : 'entradas') + '</small>';
}
function yearsOf(list) { var c = {}; list.forEach(function (p) { c[p.y] = (c[p.y] || 0) + 1; }); return c; }
function spark(list) {
  var c = yearsOf(list), mx = 1, h = '';
  for (var y = Y0; y <= Y1; y++) mx = Math.max(mx, c[y] || 0);
  for (y = Y0; y <= Y1; y++) h += '<span title="' + y + ': ' + (c[y] || 0) + '" style="height:' + ((c[y] || 0) / mx * 100) + '%"></span>';
  return '<div><div class="spark">' + h + '</div><div class="spark-l"><span>' + Y0 + '</span><span>' + Y1 + '</span></div></div>';
}
function topRel(list, key, excl, n) {
  var c = {}; list.forEach(function (p) { p[key].forEach(function (v) { if (v !== excl) c[v] = (c[v] || 0) + 1; }); });
  return Object.keys(c).sort(function (a, b) { return c[b] - c[a]; }).slice(0, n).map(Number);
}
function relBtns(key, ids) { return ids.map(function (i) { return '<button type="button" data-add="' + key + '" data-v="' + i + '">' + esc(nameOf(key, i)) + '</button>'; }).join(''); }
function ficha() {
  var el = document.getElementById('ficha'), one = null;
  if (st.a.length === 1) one = ['a', st.a[0]]; else if (st.m.length === 1) one = ['m', st.m[0]]; else if (st.h.length === 1) one = ['h', st.h[0]];
  if (!one) { el.hidden = true; return; }
  var k = one[0], v = one[1], all = P.filter(function (p) { return has(p[k], v); }), html = '';
  var ys = all.map(function (p) { return p.y; }), y0 = Math.min.apply(null, ys), y1 = Math.max.apply(null, ys);
  if (k === 'a') {
    var a = D.autores[v];
    html = '<div><span class="kind">Autor</span><h2 class="soft">' + esc(a.n) + '</h2><p><b>' + all.length + '</b> entradas en inconsolata\u00bb \u00b7 de ' + y0 + ' a ' + y1 + '</p>' +
      (a.m.length ? '<p>Trabaja en <b>' + a.m.map(esc).join(', ') + '</b></p>' : '') +
      (a.v.length ? '<p style="opacity:.7;font-size:13px">Tambi\u00e9n aparece como: ' + a.v.map(esc).join(' \u00b7 ') + '</p>' : '') +
      '<div class="rel">' + relBtns('h', topRel(all, 'h', -1, 5)) + '</div><a class="go" href="/autores#' + encodeURIComponent(a.n) + '">Ver ficha completa \u00bb</a></div>';
  } else if (k === 'm') {
    var m = D.medios[v];
    html = '<div><span class="kind">Medio' + (m.r ? ' \u00b7 ' + esc(m.r) : '') + (m.x ? ' \u00b7 ya no existe' : '') + '</span><h2 class="soft">' + esc(m.n) + '</h2><p><b>' + all.length + '</b> entradas en inconsolata\u00bb \u00b7 de ' + y0 + ' a ' + y1 + '</p>' +
      '<p>Autores m\u00e1s presentes:</p><div class="rel">' + relBtns('a', topRel(all, 'a', -1, 6)) + '</div><a class="go" href="' + fichaN(m.n) + '">Ver ficha completa \u00bb</a></div>';
  } else {
    var t = D.temas[v];
    html = '<div><span class="kind">Tema \u00b7 ' + esc(t.b) + '</span><h2 class="soft">' + esc(t.n) + '</h2><p><b>' + all.length + '</b> entradas en inconsolata\u00bb \u00b7 de ' + y0 + ' a ' + y1 + '</p>' +
      '<p>Medios que m\u00e1s lo han tratado:</p><div class="rel">' + relBtns('m', topRel(all, 'm', -1, 6)) + '</div></div>';
  }
  el.innerHTML = html + spark(all); el.hidden = false;
}
function fdate(d) { return +d.slice(8, 10) + ' ' + MESES[+d.slice(5, 7) - 1] + ' ' + d.slice(0, 4); }
function hl(s, T) {
  s = esc(s); if (!T.length) return s;
  T.filter(function (t) { return t.length > 2; }).forEach(function (t) {
    var re = new RegExp('(' + t.split('').map(function (c) { return c.replace(/[a-z]/, function (l) { var m = {a: '[a\u00e1\u00e0\u00e4]', e: '[e\u00e9\u00e8\u00eb]', i: '[i\u00ed\u00ec\u00ef]', o: '[o\u00f3\u00f2\u00f6]', u: '[u\u00fa\u00f9\u00fc]', n: '[n\u00f1]', c: '[c\u00e7]'}; return m[l] || l; }); }).join('') + ')', 'gi');
    s = s.replace(re, '<mark>$1</mark>');
  });
  return s;
}
function card(p, T) {
  var head = quita(TIT[p.i] || '') || p.t || p.b || 'Entrada sin texto';
  var meds = p.m.slice(0, 2).map(function (i) { return D.medios[i].n; }).join(' \u00b7 ');
  var auts = p.a.slice(0, 3).map(function (i) { return D.autores[i].n; });
  return '<a class="rc" href="/post/' + esc(p.u) + '"><div class="ph">' +
    (p.im ? '<img loading="lazy" src="' + esc(p.im) + '" alt="" onerror="this.remove()">' : '') +
    (p.s ? '<span class="sec ' + p.s + '">' + SECN[p.s] + '</span>' : '') + (p.n > 1 ? '<span class="n">' + p.n + ' im\u00e1genes</span>' : '') +
    '<span class="ico">' + (icoEsp(espSl(p.i), '', false) ? '<span>' + icoEsp(espSl(p.i), '', false) + '</span>' : p.k.slice(0, 3).map(function (k) { return '<span title="' + TN[k] + '">' + ico(k) + '</span>'; }).join('')) + '</span></div>' +
    '<span class="meta"><b>' + fdate(p.d) + '</b>' + (p.m.length ? ' \u00b7 ' + medsI(p.m) : '') + '</span>' +
    '<span class="tt">' + hl(head, T) + '</span>' + (auts.length ? '<span class="by">por ' + esc(auts.join(', ')) + (p.a.length > 3 ? ' y ' + (p.a.length - 3) + ' m\u00e1s' : '') + '</span>' : '') + '</a>';
}
function render() {
  var T = toks(), g = document.getElementById('grid');
  if (!res.length) {
    g.innerHTML = '<div class="empty" style="grid-column:1/-1">No hay entradas con esa combinaci\u00f3n. Prueba a quitar alg\u00fan filtro.</div>';
  } else g.innerHTML = res.slice(0, shown).map(function (p) { return card(p, T); }).join('');
  document.getElementById('more').hidden = res.length <= shown;
}
document.getElementById('more').addEventListener('click', function () {
  var T = toks(), g = document.getElementById('grid');
  g.insertAdjacentHTML('beforeend', res.slice(shown, shown + 36).map(function (p) { return card(p, T); }).join(''));
  shown += 36; document.getElementById('more').hidden = res.length <= shown;
});
function toggle(k, v) { var i = st[k].indexOf(v); if (i >= 0) st[k].splice(i, 1); else st[k].push(v); run(); }
document.addEventListener('click', function (e) {
  var b = e.target.closest('button'); if (!b) return;
  if (b.dataset.more) { openF[b.dataset.more] = !openF[b.dataset.more]; run(); return; }
  if (b.dataset.k) { var k = b.dataset.k, v = b.dataset.v; toggle(k, /^[amhy]$/.test(k) ? +v : v); return; }
  if (b.dataset.add) { var k2 = b.dataset.add, v2 = +b.dataset.v; if (!has(st[k2], v2)) st[k2].push(v2); run(); return; }
  if (b.dataset.rm) {
    var r = b.dataset.rm;
    if (r === 'all') { st.q = ''; ['k', 's', 'y', 'm', 'a', 'h'].forEach(function (k) { st[k] = []; }); q.value = ''; }
    else if (r === 'q') { st.q = ''; q.value = ''; }
    else { var vv = /^[amhy]$/.test(r) ? +b.dataset.v : b.dataset.v; st[r] = st[r].filter(function (x) { return x !== vv; }); }
    run();
  }
});
document.getElementById('sort').addEventListener('change', function (e) { st.o = e.target.value; run(); });
document.getElementById('ftoggle').addEventListener('click', function () {
  var f = document.getElementById('facets'), o = f.classList.toggle('open'); this.setAttribute('aria-expanded', o);
});

// sugerencias mientras se escribe
var q = document.getElementById('q'), sug = document.getElementById('sug'), sel = -1, opts = [];
function suggest() {
  var t = nz(q.value); opts = []; sel = -1;
  if (t.length < 2) { sug.hidden = true; q.setAttribute('aria-expanded', 'false'); return; }
  function find(arr, key, n) {
    var out = [];
    for (var i = 0; i < arr.length && out.length < n; i++) {
      var k = arr[i].k, pos = k.indexOf(t);
      if (pos === 0 || (pos > 0 && /[ |]/.test(k[pos - 1]))) out.push([key, i]);
    }
    return out;
  }
  var groups = [['Autores', find(D.autores, 'a', 5)], ['Medios', find(D.medios, 'm', 4)], ['Temas', find(D.temas, 'h', 4)]];
  var h = '';
  groups.forEach(function (g) {
    if (!g[1].length) return;
    h += '<h3>' + g[0] + '</h3>';
    g[1].forEach(function (o) {
      var it = o[0] === 'a' ? D.autores[o[1]] : o[0] === 'm' ? D.medios[o[1]] : D.temas[o[1]];
      var alt = it.v && nz(it.n).indexOf(t) < 0 ? it.v.filter(function (v) { return nz(v).indexOf(t) >= 0; })[0] : '';
      var ex = o[0] === 'a' ? (it.m || []).slice(0, 2).join(', ') : o[0] === 'h' ? it.b : (it.r || '');
      h += '<button type="button" role="option" id="o' + opts.length + '" data-o="' + opts.length + '"><span class="nm">' + esc(it.n) + '</span><span class="ex">' + esc(alt ? 'como \u00ab' + alt + '\u00bb' : ex) + '</span><span class="ct">' + it.p + '</span></button>';
      opts.push(o);
    });
  });
  h += '<button type="button" class="txt" role="option" id="o' + opts.length + '" data-o="' + opts.length + '"><span class="nm">Buscar \u00ab' + esc(q.value.trim()) + '\u00bb en todo el texto</span></button>';
  opts.push(['q', q.value.trim()]);
  sug.innerHTML = h; sug.hidden = false; q.setAttribute('aria-expanded', 'true');
}
function pick(i) {
  var o = opts[i]; if (!o) return;
  if (o[0] === 'q') st.q = o[1]; else { st.q = ''; if (!has(st[o[0]], o[1])) st[o[0]].push(o[1]); }
  q.value = o[0] === 'q' ? o[1] : ''; sug.hidden = true; q.setAttribute('aria-expanded', 'false'); run();
}
function mark() { [].forEach.call(sug.querySelectorAll('button'), function (b, i) { b.setAttribute('aria-selected', i === sel); }); if (sel >= 0) q.setAttribute('aria-activedescendant', 'o' + sel); }
q.addEventListener('input', suggest);
q.addEventListener('keydown', function (e) {
  if (e.key === 'ArrowDown') { sel = Math.min(opts.length - 1, sel + 1); mark(); e.preventDefault(); }
  else if (e.key === 'ArrowUp') { sel = Math.max(0, sel - 1); mark(); e.preventDefault(); }
  else if (e.key === 'Escape') { sug.hidden = true; }
  else if (e.key === 'Enter') {
    e.preventDefault();
    if (sel >= 0) return pick(sel);
    var t = nz(q.value);
    var ex = opts.filter(function (o) { return o[0] !== 'q' && nz((o[0] === 'a' ? D.autores : o[0] === 'm' ? D.medios : D.temas)[o[1]].n) === t; })[0];
    if (ex) pick(opts.indexOf(ex)); else { st.q = q.value.trim(); sug.hidden = true; run(); }
  }
});
sug.addEventListener('click', function (e) { var b = e.target.closest('button[data-o]'); if (b) { e.stopPropagation(); pick(+b.dataset.o); } });
document.addEventListener('click', function (e) { if (!e.target.closest('.qbox')) sug.hidden = true; });
document.getElementById('qclear').addEventListener('click', function () { q.value = ''; st.q = ''; sug.hidden = true; run(); q.focus(); });
// buscador peque\u00f1o de la cabecera: manda aqu\u00ed
addEventListener('hashchange', function () { st = {q: '', k: [], s: [], y: [], m: [], a: [], h: [], o: 'new'}; readHash(); q.value = st.q; run(); scrollTo(0, 0); });
document.getElementById('try').addEventListener('click', function (e) {
  var a = e.target.closest('a[data-t]'); if (!a) return; e.preventDefault();
  var k = a.dataset.t, v = a.dataset.v;
  if (k === 'q') st.q = v; else { var arr = k === 'a' ? D.autores : k === 'm' ? D.medios : D.temas; var i = arr.findIndex(function (x) { return x.n === v; }); if (i >= 0 && !has(st[k], i)) st[k].push(i); }
  run();
});
readHash(); q.value = st.q; document.getElementById('sort').value = st.o; run();

 document.querySelector('.v-buscador .y-now').textContent=Y1;
}
function estadisticasPag(ST){
 
var Y = 'all', Y1 = new Date().getFullYear();
var BUS = '/buscador#';
function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
function fmt(n) { return Number(n).toLocaleString('es-ES'); }
function ico(k) { return '<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#i-' + k + '" class="k"/></svg>'; }
var yb = '<button type="button" data-y="all">Todo el archivo</button>';
for (var y = Y1; y >= 2011; y--) yb += '<button type="button" data-y="' + y + '">' + y + '</button>';
document.getElementById('ybar').innerHTML = yb;
function avh(key, r) { var i = key === 'm' ? r[2] : key === 'a' ? r[3] : null, c = i != null && cat0 && cat0.medios[i]; return key === 'm' || key === 'a' ? (c && c.av ? '<img class="hav" src="' + esc(c.av) + '" alt="">' : '<span class="hav"></span>') : ''; }
function hbars(id, rows, key) {
  var mx = rows.length ? rows[0][1] : 1;
  document.getElementById(id).innerHTML = rows.map(function (r) {
    var href = BUS + key + '=' + r[2] + (Y !== 'all' ? '&y=' + Y : '');
    return '<div class="rw" data-tip="' + esc(r[0]) + ': ' + fmt(r[1]) + ' entradas"><a href="' + href + '" title="' + esc(r[0]) + '">' + avh(key, r) + esc(r[0]) + '</a><div class="tr"><i style="width:' + (r[1] / mx * 100) + '%"></i></div><span class="n">' + fmt(r[1]) + '</span></div>';
  }).join('');
}
function chips(id, rows, key, unit) {
  document.getElementById(id).innerHTML = rows.map(function (r) {
    return '<a href="' + BUS + key + '=' + r[2] + '">' + esc(r[0]) + ' <small>' + r[1] + ' ' + unit + '</small></a>';
  }).join('') || '<p class="note">Ning\u00fan medio se estren\u00f3 ese a\u00f1o.</p>';
}
function render() {
  var d = Y === 'all' ? ST.total : ST.years[Y], T = ST.total;
  [].forEach.call(document.querySelectorAll('#ybar button'), function (b) { b.setAttribute('aria-pressed', b.dataset.y === String(Y)); });
  var lbl = Y === 'all' ? 'en ' + (Y1 - 2011) + ' a\u00f1os de archivo' : 'en ' + Y + (Y === Y1 ? ' (hasta hoy)' : '');
  var prev = Y !== 'all' && ST.years[Y - 1] ? ST.years[Y - 1] : null;
  function diff(a, b) { if (!b) return ''; var x = a - b; return '<small>' + (x >= 0 ? '+' : '\u2212') + fmt(Math.abs(x)) + ' respecto a ' + (Y - 1) + '</small>'; }
  document.getElementById('kpis').innerHTML =
    '<div class="kpi"><b>' + fmt(d.posts) + '</b><span>entradas ' + lbl + '</span>' + diff(d.posts, prev && prev.posts) + '</div>' +
    '<div class="kpi"><b>' + fmt(d.imgs) + '</b><span>im\u00e1genes</span>' + diff(d.imgs, prev && prev.imgs) + '</div>' +
    '<div class="kpi"><b>' + fmt(d.n_medios) + '</b><span>medios distintos</span>' + diff(d.n_medios, prev && prev.n_medios) + '</div>' +
    '<div class="kpi"><b>' + fmt(d.n_autores) + '</b><span>autores citados</span>' + diff(d.n_autores, prev && prev.n_autores) + '</div>';
  var h = '', ax = '', mx = Math.max.apply(null, Object.values(T.per_year)), MS = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'];
  var vh = document.getElementById('vb-h');
  if (Y !== 'all' && d.meses) {
    var mm = Math.max.apply(null, d.meses.concat([1]));
    d.meses.forEach(function (v, i) { h += '<span class="mb" data-tip="' + MS[i] + ' de ' + Y + ': ' + fmt(v) + ' entradas" style="height:' + (v / mm * 100) + '%"><span class="v">' + v + '</span></span>'; ax += '<span>' + MS[i].slice(0, 3) + '</span>'; });
    vh.innerHTML = 'Entradas <em>por mes</em><small>' + Y + '</small><button type="button" class="vb-back" data-y="all">\u00ab Todos los a\u00f1os</button>';
    document.getElementById('vb').innerHTML = h; document.getElementById('vax').innerHTML = ax; T = { per_year: {} };
  } else vh.innerHTML = 'Entradas <em>por a\u00f1o</em><small>pulsa una barra</small>';
  Object.keys(T.per_year).forEach(function (y) {
    var v = T.per_year[y];
    h += '<button type="button" data-y="' + y + '" aria-pressed="' + (String(Y) === y) + '" aria-label="' + y + ': ' + v + ' entradas" data-tip="' + y + ': ' + fmt(v) + ' entradas \u00b7 ' + T.medios_year[y] + ' medios" style="height:' + (v / mx * 100) + '%"><span class="v">' + v + '</span></button>';
    ax += '<span>' + "'" + y.slice(2) + '</span>';
  });
  document.getElementById('vb').innerHTML = h; document.getElementById('vax').innerHTML = ax;
  document.querySelectorAll('.ylbl').forEach(function (e) { e.textContent = Y === 'all' ? 'todo el archivo' : Y; });
  hbars('hm', d.medios.slice(0, 20), 'm');
  hbars('ha', d.autores.slice(0, 15), 'a');
  hbars('ht', d.temas.filter(function (r) { var t = cat0 && cat0.temas[r[2]]; return !(t && t.x); }).slice(0, 12), 'h');
  var tmx = Math.max.apply(null, Object.values(d.tipos).concat([1]));
  document.getElementById('tp').innerHTML = ['info', 'carto', 'ilus', 'port', 'foto', 'publi', 'video', 'graf', 'online'].map(function (k) {
    var v = d.tipos[k] || 0;
    return '<a class="tp" href="' + BUS + 'k=' + k + (Y !== 'all' ? '&y=' + Y : '') + '">' + ico(k) + '<b>' + fmt(v) + '</b><span>' + TN[k] + '</span><i style="width:' + (v / tmx * 100) + '%"></i></a>';
  }).join('');
  var nv = document.getElementById('nv'), fi = document.getElementById('fi');
  if (Y === 'all') { nv.hidden = true; fi.hidden = false; chips('fic', T.fieles, 'm', 'a\u00f1os'); }
  else { nv.hidden = false; fi.hidden = true; chips('nvc', d.nuevos, 'm', 'entr.'); }
  try { history.replaceState(null, '', Y === 'all' ? location.pathname : '#' + Y); } catch (e) {}
}
document.addEventListener('click', function (e) {
  var b = e.target.closest('button[data-y]'); if (!b) return;
  Y = b.dataset.y === 'all' ? 'all' : +b.dataset.y; render();
});
var tip = document.getElementById('tip');
document.addEventListener('mousemove', function (e) {
  var t = e.target.closest('[data-tip]');
  if (!t) { tip.style.display = 'none'; return; }
  tip.textContent = t.dataset.tip; tip.style.display = 'block';
  tip.style.left = Math.min(innerWidth - tip.offsetWidth - 8, e.clientX + 14) + 'px'; tip.style.top = (e.clientY + 16) + 'px';
});
var hy = +location.hash.slice(1); if (ST.years[hy]) Y = hy;
render();

}
function pagina(meta,cat){
 cat0=cat;var home=document.getElementById('home');
 home.innerHTML='<div class="v-pag v-'+RUTA+'"><div class="wrap"><p class="cargando-pag" style="padding:60px 0;font-family:Fraunces,serif;font-style:italic;font-size:22px">Cargando\u2026</p></div></div>';
 var box=home.firstChild,hash=function(){return decodeURIComponent(location.hash.slice(1));};
 var pon=function(r,cls){box.className='v-pag v-'+RUTA+(cls?' '+cls:'');box.innerHTML=r.html;r.init();};
 var falla=function(e){console.error('inconsolata\u00bb: p\u00e1gina',e);box.innerHTML='<div class="wrap"><p style="padding:60px 0">No se han podido cargar los datos. Prueba a recargar la p\u00e1gina.</p></div>';};
 if(RUTA==='buscador'){document.title='Buscador \u00b7 inconsolata\u00bb';get('indice').then(function(D){box.innerHTML="<section class=\"hero\"><div class=\"wrap\"><h1 class=\"soft\">Quince a\u00f1os de <em>periodismo visual</em>, a un clic</h1><div class=\"qbox\"><div class=\"qrow\"><svg viewBox=\"0 0 24 24\" width=\"30\" height=\"30\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.6\" aria-hidden=\"true\"><circle cx=\"11\" cy=\"11\" r=\"7\"/><path d=\"M20 20l-4-4\"/></svg><label for=\"q\" class=\"sr\">Buscar en el archivo de inconsolata\u00bb</label><input id=\"q\" type=\"search\" placeholder=\"Autor, medio, tema o lo que recuerdes\u2026\" autocomplete=\"off\" role=\"combobox\" aria-expanded=\"false\" aria-controls=\"sug\" aria-autocomplete=\"list\"><button type=\"button\" id=\"qclear\" aria-label=\"Borrar b\u00fasqueda\">\u00d7</button></div><div class=\"sug\" id=\"sug\" role=\"listbox\" hidden></div></div><div class=\"try\" id=\"try\"><span class=\"caps\" style=\"margin-right:4px\">Prueba \u00bb</span><a href=\"#\" data-t=\"a\" data-v=\"Josemi Ben\u00edtez\">Josemi Ben\u00edtez</a><a href=\"#\" data-t=\"h\" data-v=\"Guerra en Ucrania\">Guerra en Ucrania</a><a href=\"#\" data-t=\"m\" data-v=\"Le Monde\">Le Monde</a><a href=\"#\" data-t=\"q\" data-v=\"mapa del metro\">mapa del metro</a><a href=\"#\" data-t=\"a\" data-v=\"Francesca Fattori\">Francesca Fattori</a><a href=\"#\" data-t=\"h\" data-v=\"Juegos Ol\u00edmpicos\">Juegos Ol\u00edmpicos</a><a href=\"#\" data-t=\"m\" data-v=\"La Voz de Galicia\">La Voz de Galicia</a><a href=\"#\" data-t=\"q\" data-v=\"tipograf\u00eda\">tipograf\u00eda</a></div></div></section><div class=\"wrap bbody\"><aside class=\"facets\" id=\"facets\" aria-label=\"Filtros\"><div class=\"fg\"><h2>A\u00f1os</h2><div class=\"years\" id=\"f-y\"></div><div class=\"yl\"><span>2011</span><span class=\"y-now\"></span></div></div><div class=\"fg\"><h2>Tipo de pieza</h2><div class=\"fl\" id=\"f-k\"></div></div><div class=\"fg\"><h2>Temas</h2><div class=\"fl\" id=\"f-h\"></div></div><div class=\"fg\"><h2>Medios</h2><div class=\"fl\" id=\"f-m\"></div></div><div class=\"fg\"><h2>Autores</h2><div class=\"fl\" id=\"f-a\"></div></div></aside><section aria-live=\"polite\"><div class=\"rhead\"><div class=\"count\" id=\"count\"></div><div style=\"display:flex;gap:10px;align-items:center\"><button type=\"button\" class=\"ftoggle\" id=\"ftoggle\" aria-expanded=\"false\" aria-controls=\"facets\">Filtros</button><label class=\"sr\" for=\"sort\">Ordenar</label><select id=\"sort\"><option value=\"new\">M\u00e1s recientes</option><option value=\"old\">M\u00e1s antiguas</option><option value=\"rel\">M\u00e1s relevantes</option></select></div></div><div class=\"active\" id=\"active\"></div><div class=\"fx\" id=\"ficha\" hidden></div><div class=\"grid\" id=\"grid\"></div><button type=\"button\" class=\"loadmore\" id=\"more\">Cargar m\u00e1s \u00bb</button></section></div>";buscadorPag(D);}).catch(falla);return;}
 if(RUTA==='estadisticas'){document.title='Estad\u00edsticas \u00b7 inconsolata\u00bb';get('estadisticas').then(function(ST){box.innerHTML="<section class=\"wrap hero\"><div class=\"crumbs caps\" style=\"padding:0 0 14px\"><a href=\"/\">inconsolata</a><i>\u00bb</i><a href=\"/medios\">Medios</a><i>\u00bb</i><span>Estad\u00edsticas</span></div><h1 class=\"soft\">Los <em>n\u00fameros</em> del archivo</h1><p>Qu\u00e9 medios, autores y temas han pasado por inconsolata\u00bb cada a\u00f1o desde 2011. Pulsa un a\u00f1o para ver solo ese a\u00f1o.</p></section><nav class=\"ybar\" aria-label=\"Elegir a\u00f1o\"><div class=\"wrap in\" id=\"ybar\"></div></nav><section class=\"kpis\" aria-live=\"polite\"><div class=\"wrap in\" id=\"kpis\"></div></section><div class=\"wrap\"><section class=\"blk\"><h2 class=\"soft\" id=\"vb-h\">Entradas <em>por a\u00f1o</em><small>pulsa una barra</small></h2><div class=\"vbars\" id=\"vb\"></div><div class=\"vax\" id=\"vax\"></div></section><div class=\"cols\"><section class=\"blk\"><h2 class=\"soft\">Medios <em>m\u00e1s presentes</em><small class=\"ylbl\"></small></h2><div class=\"hb\" id=\"hm\"></div><p class=\"note\">N\u00famero de entradas en las que aparece el medio. Un \u00abmucho m\u00e1s\u00bb o un EXTRA! cuenta una vez por cada medio que incluye.</p></section><section class=\"blk\"><h2 class=\"soft\">Autores <em>m\u00e1s citados</em><small class=\"ylbl\"></small></h2><div class=\"hb\" id=\"ha\"></div></section></div><section class=\"blk\"><h2 class=\"soft\">Tipos <em>de pieza</em><small class=\"ylbl\"></small></h2><div class=\"tipos-row\" id=\"tp\"></div><p class=\"note\">Gr\u00e1fico y Online solo se cuentan en los posts publicados con el nuevo dise\u00f1o.</p></section><div class=\"cols\"><section class=\"blk\"><h2 class=\"soft\">Temas<small class=\"ylbl\"></small></h2><div class=\"hb\" id=\"ht\"></div></section><section class=\"blk\" id=\"nv\"><h2 class=\"soft\">Se <em>estrenan</em><small>medios que aparecen por primera vez</small></h2><div class=\"chips\" id=\"nvc\"></div></section><section class=\"blk\" id=\"fi\"><h2 class=\"soft\">Los <em>fieles</em><small>medios presentes m\u00e1s a\u00f1os</small></h2><div class=\"chips\" id=\"fic\"></div></section></div></div><div id=\"tip\" role=\"presentation\"></div>";estadisticasPag(ST);}).catch(falla);return;}
 if(RUTA==='cronologia'){Promise.all([get('archivo'),get('especiales'),get('cronologia')]).then(function(r){pon(cronoPag(r[0],cat,r[1],r[2]));}).catch(falla);return;}
 if(RUTA==='novedades'){document.title='Novedades \u00b7 inconsolata\u00bb';get('avisos').then(function(A){pon(novPag(A,cat));}).catch(falla);return;}
 if(RUTA==='especiales'){Promise.all([get('archivo'),get('especiales')]).then(function(r){
   function ve(){var s=hash(),x=r[1].find(function(e){return e.slug===s;});pon(x?espPag(r[0],cat,r[1],x):espIdx(r[1],cat));if(!x)document.title='Especiales \u00b7 inconsolata\u00bb';scrollTo(0,0);}
   ve();addEventListener('hashchange',ve);}).catch(falla);return;}
 if(RUTA==='medios'){Promise.all([get('archivo'),get('fichas_medios'),get('estadisticas').catch(function(){return null;})]).then(function(r){
   function ve(){var s=hash(),mi=s?cat.medios.findIndex(function(m){return m.slug===s;}):-1;if(mi<0&&s)mi=r[0].medios.findIndex(function(m){return fold(m.n)===fold(s);});
    if(mi>=0)pon(medioFicha(r[0],cat,r[1],mi,r[2]),'v-ficha');else{document.title='Medios \u00b7 inconsolata\u00bb';pon(medioIdx(r[0],cat),'v-ficha');}scrollTo(0,0);}
   ve();addEventListener('hashchange',ve);}).catch(falla);return;}
 if(RUTA==='autores'){Promise.all([get('archivo'),get('fichas_medios'),get('autores_fichas').catch(function(){return {};})]).then(function(r){var A=r[0];
   function ve(){var s=fold(hash()),ai=s?A.autores.findIndex(function(a){return fold(a.n)===s;}):-1;
    if(ai>=0)pon(autorFicha(A,cat,r[1],r[2],ai),'v-ficha');else{document.title='Autores \u00b7 inconsolata\u00bb';pon(autorIdx(A),'v-ficha');}scrollTo(0,0);}
   ve();addEventListener('hashchange',ve);}).catch(falla);return;}
}

// en el blog de pruebas los posts son reblogueos: usamos el id del post original
function rid(el){var m=(el.dataset.root||'').match(/\/post\/(\d+)/);return m?m[1]:el.dataset.id;}
function unwrap(b){var p=b.firstElementChild,q=p&&p.nextElementSibling;if(p&&q&&p.tagName==='P'&&q.tagName==='BLOCKQUOTE'&&(p.querySelector('a.tumblr_blog')||/:\s*$/.test(p.textContent))){b.innerHTML=q.innerHTML;}}
// Tumblr da un nombre de archivo distinto a cada tama\u00f1o: hay que elegirlo del srcset, no cambiar el tama\u00f1o en la URL
function srcDe(i,t){var ss=(i.getAttribute('srcset')||'').split(',').map(function(x){var p=x.trim().split(/\s+/);return {u:p[0],w:parseInt(p[1])||0};}).filter(function(x){return x.u&&x.w;}).sort(function(a,b){return a.w-b.w;});
 if(!ss.length)return i.getAttribute('src');var ok=ss.filter(function(x){return x.w>=t;});return (ok[0]||ss[ss.length-1]).u;}
function fichaMedio(m){return '/medios#'+encodeURIComponent(m.slug||m.n);}
function fichaAutor(a){return '/autores#'+encodeURIComponent(a);}
// medios de una pieza en un antet\u00edtulo: avatares de todos y \u00abN medios\u00bb si son m\u00e1s de 3, o sus nombres si son 3 o menos
function medsK(ms){ms=(ms||[]).filter(Boolean);if(!ms.length)return '';
 var av=ms.filter(function(m){return m.avw;}).map(function(m){return '<img class="k-av" src="'+esc(m.avw)+'" alt="" title="'+esc(m.n)+'" onerror="this.remove()">';}).join('');
 return (av?'<span class="k-avs">'+av+'</span>':'')+'\u00bb '+esc(ms.length>3?ms.length+' medios':ms.map(function(m){return m.n;}).join(', ').replace(/, ([^,]*)$/,' y $1'));}
function medsI(ix){var C=(typeof cat0!=='undefined'&&cat0)||window.CAT||{medios:[]};return medsK((ix||[]).map(function(i){return C.medios[i];}));}
// iconos propios de los especiales (catalogo.espi = {slug:[icono, texto]}): se montan como s\u00edmbolos #e-slug
var ESPI={},ESPI_N={},EXTRA_SYM={'t-urna':'<g stroke="currentColor" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" fill="none"><path d="M22 30 V6 H42 V30"/><path d="M27 16 L31 21 L38 12"/><path d="M4 30 H60"/><path d="M8 30 V58 H56 V30"/><path d="M20 30 H44" stroke-width="7"/></g>'};
var ESPI_LBL={'t-urna':[50.5,15,40]};
function prepEspIcos(cat){if(!cat||!cat.espi||prepEspIcos.hecho)return;prepEspIcos.hecho=1;var h='';
 Object.keys(cat.espi).forEach(function(sl){var v=cat.espi[sl],id=symN(v[0]),b=document.getElementById(id),body=b?b.innerHTML:EXTRA_SYM[id];if(!body)return;
  var t=String(v[1]||'').trim(),L=ESPI_LBL[id],lab='',fs;
  if(t&&L){fs=Math.min(L[1],L[2]/Math.max(1,t.length)*1.75);lab='<text x="32" y="'+L[0]+'" text-anchor="middle" font-family="Archivo,sans-serif" font-weight="800" font-size="'+fs.toFixed(1)+'" fill="var(--lbl,currentColor)" stroke="none">'+esc(t)+'</text>';}
  else if(t){fs=Math.min(14,50/Math.max(1,t.length)*1.75);lab='<rect x="4" y="46" width="56" height="17" rx="2" fill="var(--lbl,currentColor)" stroke="none"/><text x="32" y="59" text-anchor="middle" font-family="Archivo,sans-serif" font-weight="800" font-size="'+fs.toFixed(1)+'" fill="#fff" stroke="none">'+esc(t)+'</text>';}
  h+='<symbol id="e-'+sl+'" viewBox="0 0 64 64" overflow="visible">'+body+lab+'</symbol>';ESPI[sl]='e-'+sl;ESPI_N[sl]=(cat.esp&&cat.esp[sl])||'';});
 if(h)document.body.insertAdjacentHTML('afterbegin','<svg width="0" height="0" style="position:absolute" aria-hidden="true">'+h+'</svg>');}
function icoEsp(sl,cls,dos){var id=ESPI[sl];if(!id)return '';var n=esc(ESPI_N[sl]||'Especial');
 return '<svg class="'+(cls||'')+'" viewBox="0 0 64 64" role="img" aria-label="'+n+'" style="overflow:visible"><title>'+n+'</title><use href="#'+id+'" class="k"/>'+(dos===false?'':'<use href="#'+id+'" class="m" x="3" y="2.5"/>')+'</svg>';}
// icono de una pieza: el de su especial si lo tiene; si no, el de su tipo
function espSl(id){return (typeof META0!=='undefined'&&META0&&(META0[id]||[])[5])||'';}
function icoP(id,k,cls){var e=icoEsp(espSl(id),cls);return e||(k?ico(k,cls):'');}
function esPortadilla(s,k,im,d){if((s!=='m'&&s!=='x')||!im.w||!im.h)return false;var r=im.w/im.h;
 return (r>=4.5&&im.w>=1200&&im.w<=1400)||(s==='m'&&k===0&&r>=4.5)||(s==='m'&&k===0&&r>=2.6&&r<=2.9&&d>='2013');}

// ------------------------------------------------------------------ p\u00e1gina de post
// ajustes del panel de portada: frases subrayadas y pies de foto a\u00f1adidos sin tocar Tumblr
function ajustes(body,aj,s){if(!aj)return;
 (aj.subrayados||[]).forEach(function(f){f=String(f||'').replace(/\s+/g,' ').trim();if(!f)return;
  var w=document.createTreeWalker(body,NodeFilter.SHOW_TEXT),x;while((x=w.nextNode())){var v=x.nodeValue.replace(/\u00a0/g,' '),i=v.indexOf(f);
   if(i>=0&&!x.parentNode.closest('mark,a,.fuente')){var r=x.splitText(i);r.splitText(f.length);var m=document.createElement('mark');m.className='subr';r.parentNode.replaceChild(m,r);m.appendChild(r);break;}}});
}
function post(art,meta,cat,medido){
 var id=rid(art), d=art.dataset.date, mt=meta[id]||['',[],[],[],[]];
 var s=mt[0], tipos=mt[1], meds=mt[2].map(function(i){return cat.medios[i];}), auts=mt[3].map(function(i){return cat.autores[i];}), tems=mt[4];
 var esp=mt[5]&&cat.esp&&cat.esp[mt[5]]?{slug:mt[5],n:cat.esp[mt[5]]}:null;
 var body=art.querySelector('.body'), raw=art.querySelector('.post-raw'); unwrap(body);
 // im\u00e1genes: fotos \u00abantiguas\u00bb de Tumblr + figuras del cuerpo (formato nuevo)
 var ims=[];
 [].forEach.call(raw.querySelectorAll('img[data-hr]'),function(i){ims.push({src:i.dataset.hr,w:+i.dataset.w||0,h:+i.dataset.h||0,cap:''});});
 [].forEach.call(body.querySelectorAll('figure img, img'),function(i){
  if(i.closest('blockquote'))return;
  var w=+(i.getAttribute('data-orig-width')||i.closest('figure')&&i.closest('figure').getAttribute('data-orig-width')||0),
      h=+(i.getAttribute('data-orig-height')||i.closest('figure')&&i.closest('figure').getAttribute('data-orig-height')||0);
  w=w||+(i.getAttribute('data-mw')||0);h=h||+(i.getAttribute('data-mh')||0);
  ims.push({src:srcDe(i,99999),w:w,h:h,el:i});
 });
 // sin medidas (p. ej. en reblogueos) no se puede saber cu\u00e1l es la portadilla: se miden con una versi\u00f3n peque\u00f1ita y se vuelve a empezar
 if(!medido&&(s==='m'||s==='x')){var falta=ims.filter(function(im){return im.el&&(!im.w||!im.h);});
  if(falta.length){Promise.all(falta.map(function(im){return new Promise(function(res){var x=new Image(),ok=false;
    x.onload=function(){if(x.naturalWidth){var mx=Math.max.apply(null,(im.el.getAttribute('srcset')||'').split(',').map(function(q){return parseInt(q.trim().split(/\s+/)[1])||0;}).filter(function(v){return v>0;}).concat([x.naturalWidth]));im.el.setAttribute('data-mw',mx);im.el.setAttribute('data-mh',Math.round(mx*x.naturalHeight/x.naturalWidth));}res();};
    x.onerror=res;setTimeout(res,5000);x.setAttribute('s'+'rc',srcDe(im.el,100));});})).then(function(){post(art,meta,cat,true);});return;}}
 ims=ims.filter(function(im,k){return !esPortadilla(s,k,im,d);});
 // t\u00edtulo: el de Tumblr, o el primer H1 del cuerpo, o la primera frase
 var h1=art.querySelector('.title h1'), t=TIT[id]||h1.textContent.trim();
 var bh=body.querySelector('h1'); if(!t&&bh){t=bh.textContent.trim();}
 if(s==='m'){var mm=(t+' '+body.textContent).replace(/&nbsp;/g,' ').match(/semana\s+([IVXLCDM]+)/i);t='mucho m\u00e1s \u00bb semana '+(mm?mm[1].toUpperCase():'');}
 if(!t){var tx=body.textContent.replace(/^[\s\u2a54]+/,'').trim(),f=tx.match(/^(.{20,140}?[.!?:])(\s|$)/);t=f?f[1]:tx.slice(0,110).replace(/\s\S*$/,'\u2026');h1.classList.add('auto');}
 tems=tems.filter(function(i){var q=cat.temas[i];return q&&(!q.x||(q.x==='sub'&&q.e));});
 var tm=tems.length?'<div class="temas"><span class="caps">Temas \u00bb</span>'+tems.map(function(i){var q=cat.temas[i];return '<a href="'+(q.x==='sub'?'/especiales#'+q.e:'/buscador#h='+i)+'"'+(q.x==='sub'?' class="esp"':'')+'><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+(q.x==='sub'&&ESPI[q.e]||TS[i])+'"/></svg>'+esc(q.n)+'</a>';}).join('')+'</div>':'';
 if(d>='2026-10-01')subraya(body);
 ajustes(body,AJ[id],s);
 if(s==='m'||s==='x'||s==='b'||(s==='o'&&body.textContent.length>1500)){
  var o={art:art,body:body,ims:ims,d:d,id:id,cat:cat,tipos:tipos,s:s,t:t,tm:tm};
  var lbv=s==='m'?vMM(o):s==='x'?vX(o):vB(o); if(lbv.length&&window.initLB)initLB(lbv); return;
 }
 if(h1.classList.contains('auto'))h1.textContent=t; else h1.innerHTML=destaca(t); document.title=quita(t)+' \u00b7 inconsolata\u00bb';
 var bico=icoEsp(mt[5],'big-ico')||(tipos[0]?ico(tipos[0],'big-ico'):'');if(bico)art.querySelector('.title').insertAdjacentHTML('beforeend',bico);
 // migas
 var cr='<a href="/">inconsolata</a><i>\u00bb</i>'+(s&&s!=='m'&&s!=='x'?'<a href="/tagged/'+encodeURIComponent(SECN[s])+'">'+SECN[s]+'</a>':tipos[0]?'<a href="/buscador#k='+tipos[0]+'">'+esc(TN[tipos[0]])+'</a>':'<span>post</span>');
 if(esp)cr+='<i>\u00bb</i><a class="k-esp" href="/especiales#'+esc(esp.slug)+'">'+esc(esp.n)+'</a>';
 if(meds.length>3)cr+='<i>\u00bb</i><span>'+meds.length+' medios</span>';
 else if(meds.length)cr+='<i>\u00bb</i>'+meds.map(function(m){return '<a href="'+fichaMedio(m)+'">'+esc(m.n)+'</a>';}).join(', ').replace(/, (<a [^>]*>[^<]*<\/a>)$/,' y $1');
 art.querySelector('.crumbs').innerHTML=cr;
 if(d<LANZAMIENTO)art.querySelector('.legacy').hidden=false;
 // cuerpo: fuera el \u00ab\u2a54\u00bb inicial, letra capitular, l\u00ednea de fuente como bloque negro, fuera la caja de apoyo antigua
 [].forEach.call(body.querySelectorAll('blockquote'),function(b){if(/buymeacoffee|aportaci\u00f3n/i.test(b.textContent+b.innerHTML))b.remove();});
 [].forEach.call(body.querySelectorAll('p'),function(p){
  var b=p.querySelector('b,strong');
  if(b&&b.textContent.trim()==='\u2a54'){var sp=b.closest('span')||b;var br=sp.nextElementSibling;sp.remove();if(br&&br.tagName==='BR')br.remove();}
 });
 var sr=(s==='m'||s==='x'||s==='b')?null:serieDe(body,id);
 // l\u00ednea de fuente \u2192 bloque negro. Formato actual: \u00ab\u00bb Medio, del \u2026\u00bb; formato antiguo: \u00abMedio, del \u2026\u00bb sin el s\u00edmbolo
 // avatares de todos los medios citados (si no caben, van pasando)
 function avsDe(){return meds.map(function(m){return '<a class="f-av'+(m.avw?'':' f-av-l')+'" href="'+fichaMedio(m)+'" title="'+esc(m.n)+'" aria-label="Ficha de '+esc(m.n)+'">'+(m.avw?'<img src="'+m.avw+'" alt="">':esc(m.n.charAt(0)))+'</a>';}).join('');}
 // quita el \u00ab\u00bb\u00bb (y el guion de las listas antiguas) del principio, est\u00e9 dentro de las etiquetas que est\u00e9
 function limpia(p){var c=p.cloneNode(true),w=document.createTreeWalker(c,NodeFilter.SHOW_TEXT),x;
  while((x=w.nextNode())){var v=x.nodeValue.replace(/^[\s\xa0]+/,'');if(!v){x.nodeValue='';continue;}x.nodeValue=v.replace(/^[\u00bb\-\u2013]\s*/,'').replace(/^[\s\xa0]+/,'');if(x.nodeValue)break;}
  var h=c.innerHTML;for(var k=0;k<4;k++)h=h.replace(/^\s*<(b|strong|span|i|em)[^>]*>\s*<\/\1>\s*/,'');return h.replace(/^\s*(<br\s*\/?>\s*)+/,'');}
 function hazFuente(p){var dv=document.createElement('div');dv.className='fuente';var av=avsDe(),larga=p.textContent.replace(/\s+/g,' ').length>150||meds.length>3;
  dv.innerHTML=(larga?'<p class="f-res"><i>\u00bb</i> Autores y medios</p>':'')+'<p class="f-tx"><i>\u00bb</i> '+limpia(p)+'</p>'+(av?'<div class="f-avs"><div class="f-track">'+av+'</div></div>':'')+(larga?'<button type="button" class="f-mas" aria-expanded="false" aria-label="Ver autores y medios"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="M5 9l7 7 7-7"/></svg></button>':'');
  if(larga){dv.classList.add('plegable');dv.querySelector('.f-mas').addEventListener('click',function(){var ab=dv.classList.toggle('abierta');this.setAttribute('aria-expanded',ab?'true':'false');rueda(dv);});}
  p.replaceWith(dv);if(av)setTimeout(function(){rueda(dv);},0);}
 // si los avatares no caben en su hueco, pasan en bucle (se para al pasar el rat\u00f3n; nada si se pide menos movimiento)
 function rueda(dv){var box=dv.querySelector('.f-avs'),tr=box&&box.querySelector('.f-track');if(!tr)return;
  var dup=tr.querySelector('.f-dup');if(dup)dup.remove();tr.classList.remove('gira');tr.style.removeProperty('--dur');
  if(dv.classList.contains('abierta')||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  if(tr.scrollWidth<=box.clientWidth+2)return;
  var w=tr.scrollWidth,c=document.createElement('span');c.className='f-dup';c.setAttribute('aria-hidden','true');c.innerHTML=tr.innerHTML;
  [].forEach.call(c.querySelectorAll('a'),function(a){a.tabIndex=-1;});tr.appendChild(c);tr.style.setProperty('--dur',Math.max(8,w/40)+'s');tr.classList.add('gira');}
 var ruedaT;addEventListener('resize',function(){clearTimeout(ruedaT);ruedaT=setTimeout(function(){[].forEach.call(document.querySelectorAll('.fuente'),rueda);},200);});
 [].forEach.call(body.querySelectorAll('p'),function(p){if(/^[\s\xa0]*\u00bb/.test(p.textContent)&&!p.closest('.fuente'))hazFuente(p);});
 if(!body.querySelector('.fuente')&&s!=='m'&&s!=='x'){
  var ps=[].filter.call(body.querySelectorAll('p'),function(p){return !p.querySelector('img');});
  var cand=ps.filter(function(p){var t=p.textContent.replace(/\xa0/g,' ').trim(),f=fold(t);return t.length<400&&/,\s+(del?|el)\s+\d{1,2}(\s|,)/.test(t)&&(t.length<=160||meds.some(function(m){return f.indexOf(fold(m.n))===0;}));});
  var fp=cand[cand.length-1];
  if(fp&&(ps.length>1||fp.textContent.trim().length<160))hazFuente(fp);
 }
 var first=[].find.call(body.querySelectorAll('p'),function(p){return !p.closest('.fuente')&&p.textContent.trim().length>40;});
 if(first&&s!=='m'&&s!=='x'){var w=document.createTreeWalker(first,NodeFilter.SHOW_TEXT),n;while((n=w.nextNode())&&!n.nodeValue.trim());
  if(n){var v=n.nodeValue.replace(/^\s+/,'');var sp=document.createElement('span');sp.className='cap';sp.textContent=v[0];n.nodeValue=v.slice(1);n.parentNode.insertBefore(sp,n);}}
 // parte visual
 var vis=art.querySelector('.visual'), lay=art.querySelector('.layout'), n=ims.length;
 var alt=function(i){return (TN[tipos[0]]||'Imagen')+(meds[0]?' de '+meds[0].n:'')+', imagen '+(i+1)+' de '+n;};
 var lb=[];
 if(s==='m'||s==='x'){
  // mucho m\u00e1s / EXTRA!: cada imagen con su pieza (Trabajo | Autor | Medio)
  var html='', k=0;
  ims.forEach(function(im,i){
   var cap='',el=im.el&&(im.el.closest('.npf_row')||im.el.closest('figure'));
   var nx=el&&el.nextElementSibling;
   if(nx&&nx.tagName==='P'&&/Trabajo/.test(nx.textContent)){cap=nx.innerHTML.replace(/&nbsp;|\u00a0/g,' ');nx.remove();}
   var tr=(cap.match(/Trabajo\s*<\/i>\s*:\s*([^|]*)/)||[])[1]||'', au=(cap.match(/Autor(?:a|es|as)?\s*<\/i>\s*:\s*([^|]*)/)||[])[1]||'',
       md=(cap.match(/Medio\s*<\/i>\s*:\s*<b>([^<]*)<\/b>([^|<]*)/)||[]);
   var mdo=cat.medios.find(function(m){return md[1]&&m.n.toLowerCase()===md[1].trim().toLowerCase();});
   lb.push({src:im.src,cap:(tr?tr.replace(/<[^>]+>/g,'').trim()+' \u00b7 ':'')+(md[1]||'')+' \u00b7 imagen '+(i+1)+' de '+n});
   html+='<article class="mm-it"><button type="button" class="shot" data-lb="'+i+'" aria-label="Ampliar imagen '+(i+1)+'"><img loading="lazy" src="'+esc(im.src)+'" alt="'+esc(tr.replace(/<[^>]+>/g,''))+'"><span class="zoom">Ampliar \u00bb</span></button>'+
    '<div class="txt"><span class="mm-n">'+(i+1)+'</span>'+(md[1]?'<span class="md">'+(mdo&&mdo.av?'<img src="'+mdo.av+'" alt="">':'')+esc(md[1].trim())+'</span>':'')+
    (tr?'<h2>'+tr+'</h2>':'')+(au?'<span class="by">por '+au.split(/\s+y\s+|,\s*/).map(function(a){return '<a href="'+fichaAutor(a.replace(/<[^>]+>/g,'').trim())+'">'+a+'</a>';}).join(', ')+'</span>':'')+
    (md[2]?'<span class="caps" style="font-size:12px">'+esc(md[2].replace(/^,\s*/,''))+'</span>':'')+'</div></article>';
  });
  vis.innerHTML='<div class="mm-items">'+html+'</div>'; lay.classList.add('single');
 } else if(n){
  var PIE=(AJ[id]&&AJ[id].pies)||{},pie=function(i){return String(PIE[i+1]||'').trim();},pieH=function(i,c){return pie(i)?'<p class="'+(c||'pie-aj')+'">'+esc(pie(i))+'</p>':'';};
  ims.forEach(function(im,i){lb.push({src:im.src,cap:(pie(i)?pie(i)+' \u00b7 ':meds.length===1?meds[0].n+' \u00b7 ':'')+'imagen '+(i+1)+' de '+n});});
  alt=function(i){return pie(i)||(TN[tipos[0]]||'Imagen')+(meds.length===1?' de '+meds[0].n:'')+', imagen '+(i+1)+' de '+n;};
  if(s==='d'){
   vis.innerHTML='<div class="dclips">'+ims.map(function(im,i){return '<div class="dclip"><button type="button" class="shot" data-lb="'+i+'" aria-label="Ampliar recorte '+(i+1)+'"><img src="'+esc(im.src)+'" alt="'+esc(alt(i))+'"><span class="zoom">Ampliar \u00bb</span></button>'+pieH(i)+'</div>';}).join('')+'</div>';
   lay.classList.add('single');
  } else {
   var h='<div class="main-sheet"><span class="tape" aria-hidden="true"></span><button type="button" class="shot" data-lb="0" aria-label="Ampliar imagen 1 de '+n+'"><img src="'+esc(ims[0].src)+'" alt="'+esc(alt(0))+'"><span class="zoom">Ampliar \u00bb</span></button>'+pieH(0)+'</div>';
   if(n>1)h+='<div><div class="sheet-head"><span class="caps">Todas las im\u00e1genes \u00b7 '+n+'</span><span style="font-size:13px;font-weight:600">Pulsa para ampliar \u00bb</span></div><div class="contact'+(n<=4?' c2':'')+'">'+
     ims.slice(1).map(function(im,j){var i=j+1;return '<div class="frame"><button type="button" class="shot" data-lb="'+i+'" aria-label="Ampliar imagen '+(i+1)+' de '+n+'"><img loading="lazy" src="'+esc(im.src)+'" alt="'+esc(alt(i))+'"><span class="zoom">Ampliar \u00bb</span></button><span class="n">'+(i+1)+' / '+n+' <span style="color:var(--accent)">\u25b8</span></span>'+pieH(i,'pie-f')+'</div>';}).join('')+'</div></div>';
   vis.innerHTML=h; if(n===1)lay.classList.add('single');
  }
 } else { vis.remove(); lay.classList.add('single'); }
 ims.forEach(function(im){if(im.el){var r=im.el.closest('.npf_row')||im.el.closest('figure')||im.el;r.remove();}});
 // ficha
 var dl='';
 if(meds.length)dl+='<dt>Medio'+(meds.length>1?'s':'')+'</dt><dd>'+meds.map(function(m){return '<a href="'+fichaMedio(m)+'">'+esc(m.n)+'</a>'+(m.pais?' \u00b7 '+esc(m.pais):'');}).join('<br>')+'</dd>';
 dl+='<dt>Fecha</dt><dd>'+fecha(d)+'</dd>';
 if(tipos.length)dl+='<dt>Tipo</dt><dd>'+tipos.map(function(k){return esc(TN[k]);}).join(', ')+'</dd>';
 if(auts.length&&s!=='m'&&s!=='x')dl+='<dt>Cr\u00e9ditos</dt><dd>'+auts.map(function(a){return '<a class="credit" href="'+fichaAutor(a)+'">'+esc(a)+'</a>';}).join(', ')+'</dd>';
 var lgs=meds.filter(function(m){return m.logo;});
 var logo=lgs.length?'<div class="m-id'+(lgs.length>1?' multi':'')+(lgs.length>4?' mucho':'')+'">'+lgs.map(function(m){return '<a href="'+fichaMedio(m)+'" aria-label="Ficha de '+esc(m.n)+'"><img class="m-logo" src="'+m.logo+'" alt="Logo de '+esc(m.n)+'" onerror="var d=this.closest(\'.m-id\');this.parentNode.remove();if(d&&!d.querySelector(\'img\'))d.remove()"></a>';}).join('')+'</div>':'';
 art.querySelector('.ficha').innerHTML='<span class="tape" aria-hidden="true"></span><span class="caps">Ficha \u00bb</span>'+logo+'<dl>'+dl+'</dl>'+tm+(esp?'<div class="temas esps"><a class="esp" href="/especiales#'+esc(esp.slug)+'">'+(ESPI[esp.slug]?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+ESPI[esp.slug]+'"/></svg>':'')+esc(esp.n)+'</a></div>':'');
 if(sr)lay.insertAdjacentHTML('afterend',serieHTML(sr));
 if(lb.length&&window.initLB)initLB(lb);
}

// ------------------------------------------------------------------ listados (provisional)
function listado(meta,cat){
 [].forEach.call(document.querySelectorAll('.lc'),function(c){
  var cid=rid(c), mt=meta[cid]; if(!mt)return;
  var m=cat.medios[mt[2][0]], k=c.querySelector('.kicker');
  if(mt[0]&&SECN[mt[0]])c.insertAdjacentHTML('afterbegin','<span class="sec">'+SECN[mt[0]]+'</span>');
  if(m)k.innerHTML=medsK(mt[2].map(function(i){return cat.medios[i];}))+' \u00b7 '+k.textContent.replace(/^\u00bb\s*/,'');
  var tt=c.querySelector('.tt'),tid=TIT[cid]; if(tid&&mt[0]!=='m')tt.textContent=quita(tid); if(!tt.textContent.trim()){var tx=(c.dataset.txt||'').replace(/<([^<>]{1,120})>/g,'$1').replace(/^[\s\u2a54]+/,'');var f=tx.match(/^(.{20,120}?[.!?:])(\s|$)/);tt.textContent=f?f[1]:tx.slice(0,100)+'\u2026';}
  if(mt[0]==='m'){var mm=((tid||'')+' '+(c.dataset.txt||'')).replace(/&nbsp;/g,' ').match(/semana\s+([IVXLCDM]+)/i);tt.textContent='mucho m\u00e1s \u00bb semana '+(mm?mm[1].toUpperCase():'');}
  var ph=c.querySelector('.ph img'); if(ph&&!ph.getAttribute('src')){var u=(c.dataset.img||'').trim().split(/\s+/)[0];
   if(!u){var tp=c.querySelector('template.lb-body');if(tp){var ims=[].map.call(tp.content.querySelectorAll('img'),function(i){return {u:srcDe(i,600),w:+(i.getAttribute('data-orig-width')||0),h:+(i.getAttribute('data-orig-height')||0)};});
    var ok=ims.filter(function(im,k){return !esPortadilla(mt[0],k,im,'2099');});u=(ok[0]||ims[0]||{}).u;}}
   if(u)ph.setAttribute('s'+'rc',u);else ph.remove();}
 });
}

Promise.all([get('meta'),get('catalogo'),get('titulos').catch(function(){return {};}),get('ajustes_posts').catch(function(){return {};})]).then(function(r){
 TIT=r[2]||{};AJ=r[3]||{};
 // logos y avatares fijados al mismo commit que el c\u00f3digo (as\u00ed no se quedan versiones viejas en cach\u00e9)
 if(window.INC_BASE)r[1].medios.forEach(function(m){['av','avw','logo'].forEach(function(k){if(m[k])m[k]=m[k].replace('https://cdn.jsdelivr.net/gh/inconsolataweb/inconsolata-datos@main/',INC_BASE);});});
 autocompleta(r[1]);META0=r[0]||{};cat0=r[1];prepEspIcos(r[1]);
 var art=document.querySelector('article.post'); if(RUTA)pagina(r[0],r[1]); else if(art)post(art,r[0],r[1]); else if(document.body.classList.contains('es-portada'))portada(r[0],r[1]); else listado(r[0],r[1]);
}).catch(function(e){console.error('inconsolata\u00bb: no se pudieron cargar los datos',e);});
document.addEventListener('click',function(e){var b=e.target.closest('.share .cp');if(!b)return;var u=b.dataset.u||location.href;
 var fin=function(){b.classList.add('done');b.setAttribute('aria-label','Enlace copiado');setTimeout(function(){b.classList.remove('done');b.setAttribute('aria-label','Copiar enlace');},1800);};
 if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(u).then(fin,fin);else{var t=document.createElement('textarea');t.value=u;document.body.appendChild(t);t.select();try{document.execCommand('copy');}catch(x){}t.remove();fin();}});
// sugerencias de medios con ficha y autores mientras se escribe en el buscador de la cabecera
function autocompleta(cat){
 var M=cat.medios.map(function(m,i){return {t:'m',n:m.n,k:fold(m.n),u:m.ficha?fichaMedio(m):'/buscador#m='+i,av:m.av,f:m.ficha};}).filter(function(o){return o.f;}),
     A=cat.autores.map(function(n,i){var mi=cat.am?cat.am[i]:-1,m=mi>=0?cat.medios[mi]:null;return {t:'a',n:n,k:fold(n),u:fichaAutor(n),av:m&&m.av,md:m&&m.n};});
 function busca(q){q=fold(q.trim());if(q.length<2)return [];var ok=function(o){var i=o.k.indexOf(q);return i===0||(i>0&&/[\s(.'-]/.test(o.k[i-1]));};
  return M.filter(ok).slice(0,4).concat(A.filter(ok).slice(0,6));}
 [].forEach.call(document.querySelectorAll('.srch'),function(f){var inp=f.querySelector('input'),box=document.createElement('div'),sel=-1,L=[];
  box.className='ac';box.hidden=true;box.setAttribute('role','listbox');box.id='ac-'+inp.id;f.appendChild(box);inp.setAttribute('aria-controls',box.id);inp.setAttribute('aria-autocomplete','list');
  function pinta(){box.innerHTML=L.map(function(o,i){return '<a href="'+o.u+'" role="option" class="'+(i===sel?'on':'')+'">'+(o.av?'<img src="'+esc(o.av)+'" alt="">':'<span class="ini'+(o.t==='a'?' a':'')+'">'+esc(o.n.charAt(0))+'</span>')+'<span class="nm">'+esc(o.n)+'</span><small>'+(o.t==='m'?'medio':'autor'+(o.md?' \u00b7 '+esc(o.md):''))+'</small></a>';}).join('')+
   (inp.value.trim()?'<a href="/buscador#q='+encodeURIComponent(inp.value.trim())+'" class="todo'+(sel===L.length?' on':'')+'">Buscar \u00ab'+esc(inp.value.trim())+'\u00bb en todo el archivo \u00bb</a>':'');box.hidden=!inp.value.trim();}
  inp.addEventListener('input',function(){L=busca(inp.value);sel=-1;pinta();});
  inp.addEventListener('keydown',function(e){if(box.hidden)return;var n=L.length+1;
   if(e.key==='ArrowDown'){sel=(sel+1)%n;pinta();e.preventDefault();}else if(e.key==='ArrowUp'){sel=(sel+n-1)%n;pinta();e.preventDefault();}
   else if(e.key==='Escape'){box.hidden=true;}else if(e.key==='Enter'&&sel>=0&&sel<=L.length){e.preventDefault();e.stopImmediatePropagation();box.querySelectorAll('a')[sel].click();}});
  document.addEventListener('click',function(e){if(!f.contains(e.target))box.hidden=true;});});
}
// el buscador peque\u00f1o de la cabecera lleva al buscador
[].forEach.call(document.querySelectorAll('.srch'),function(f){f.addEventListener('submit',function(){var v=f.querySelector('input').value.trim();location.href='/buscador'+(v?'#q='+encodeURIComponent(v):'');});});
})();

(function(){var h=document.documentElement,v=null;try{v=localStorage.getItem('inc-version');}catch(e){}
 if(v==='completa')h.classList.remove('lite');else if(v==='lite')h.classList.add('lite');
 var sw=document.querySelector('.ver-sw');if(sw)sw.hidden=h.classList.contains('lite')||innerWidth>900;
 var m=document.getElementById('lite-menu'),bm=document.querySelector('[data-lite=menu]');
 function abre(o){if(!m)return;m.hidden=!o;if(bm)bm.setAttribute('aria-expanded',o?'true':'false');document.body.classList.toggle('lm-abierto',o);}
 document.addEventListener('click',function(e){var b=e.target.closest('[data-lite],[data-version]');
  if(!b){if(m&&!m.hidden&&e.target.closest('#lite-menu a'))abre(false);return;}
  if(b.dataset.version){try{localStorage.setItem('inc-version',b.dataset.version);}catch(x){}location.reload();return;}
  if(b.dataset.lite==='menu')abre(m.hidden);
  if(b.dataset.lite==='buscar'){abre(true);var q=document.getElementById('q-lite');if(q)q.focus();}});
 document.addEventListener('keydown',function(e){if(e.key==='Escape'&&m&&!m.hidden){abre(false);if(bm)bm.focus();}});})();

document.addEventListener('click',function(e){var b=e.target.closest('.dd-b');document.querySelectorAll('.dd').forEach(function(d){var bt=d.querySelector('.dd-b'),m=d.querySelector('.dd-m'),ab=b&&d.contains(b)?bt.getAttribute('aria-expanded')!=='true':false;bt.setAttribute('aria-expanded',ab?'true':'false');m.hidden=!ab;});});
document.addEventListener('keydown',function(e){if(e.key==='Escape')document.querySelectorAll('.dd-b[aria-expanded=true]').forEach(function(b){b.click();b.focus();});});

window.initLB=window.initLB||(typeof initLB!=="undefined"?initLB:null);
}if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",arranca);else arranca();})();
