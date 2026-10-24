LB_CSS = """
/* visor de imágenes propio */
.lb{position:fixed;inset:0;z-index:100;background:rgba(22,20,15,.97);display:flex;flex-direction:column;color:#ECE7DC}
.lb[hidden]{display:none}
.lb-stage{flex:1;min-height:0;overflow:auto;display:flex;align-items:center;justify-content:center;padding:24px;background-image:radial-gradient(rgba(236,231,220,.08) 1px,transparent 1.2px);background-size:8px 8px}
.lb-img{max-width:100%;max-height:100%;object-fit:contain;cursor:zoom-in;background:#fff;box-shadow:10px 10px 0 #D1006F;display:block}
.lb.zoomed .lb-stage{display:block;padding:0}
.lb.zoomed .lb-img{max-width:none;max-height:none;margin:0 auto;cursor:zoom-out;box-shadow:none}
.lb-bar{display:flex;flex-wrap:wrap;align-items:center;gap:12px 18px;padding:14px 24px;border-top:2px solid #ECE7DC;font-family:'Archivo',sans-serif}
.lb-count{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-size:34px;line-height:1;color:#FFD400}
.lb-info{flex:1;min-width:220px;display:flex;flex-direction:column;gap:4px}
.lb-cap{font-size:13px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:#FFD400}
.lb-txt{font-family:'Fraunces',serif;font-size:17px;line-height:1.45;max-width:900px}
.lb-txt:empty{display:none}
.lb-hint{font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:#A8A39A}
.lb button{font-family:'Archivo',sans-serif;font-size:15px;font-weight:800;letter-spacing:1px;text-transform:uppercase;background:transparent;color:#ECE7DC;border:2px solid #ECE7DC;min-height:44px;min-width:44px;padding:8px 14px;cursor:pointer}
.lb button:hover{background:#ECE7DC;color:#16140F}
.lb .lb-close{background:#D1006F;border-color:#D1006F;color:#fff}
.lb-side{position:absolute;top:50%;transform:translateY(-50%);font-size:40px!important;padding:6px 14px!important;background:rgba(22,20,15,.7)!important}
.lb-side.l{left:16px}.lb-side.r{right:16px}
.lb.zoomed .lb-side{display:none}
@media (max-width:700px){.lb-hint{display:none}.lb-side{display:none}}
"""

LB_HTML = """
<div class="lb" id="lb" hidden role="dialog" aria-modal="true" aria-label="Visor de imágenes">
<div class="lb-stage"><img class="lb-img" alt=""></div>
<button type="button" class="lb-side l lb-prev" aria-label="Imagen anterior">«</button>
<button type="button" class="lb-side r lb-next" aria-label="Imagen siguiente">»</button>
<div class="lb-bar">
<span class="lb-count"></span>
<div class="lb-info"><span class="lb-cap"></span><span class="lb-txt"></span></div>
<span class="lb-hint" data-en="Click the image to see it full size · ← → to browse">Pulsa la imagen para verla a tamaño real · ← → para pasar</span>
<button type="button" class="lb-close" data-en="Close ×">Cerrar ×</button>
</div>
</div>
"""

LB_JS = r"""
function initLB(list){
 var lb=document.getElementById('lb'), img=lb.querySelector('.lb-img'), st=lb.querySelector('.lb-stage'),
     cnt=lb.querySelector('.lb-count'), cap=lb.querySelector('.lb-cap'), cur=0, last=null, tx=null;
 function big(u){return u.replace(/\/s\d+x\d+\//,'/s2048x3072/');}
 function show(i){
  cur=(i+list.length)%list.length; lb.classList.remove('zoomed');
  img.onerror=function(){img.onerror=null; img.src=list[cur].src;};
  img.src=big(list[cur].src); img.alt=list[cur].cap;
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
"""
