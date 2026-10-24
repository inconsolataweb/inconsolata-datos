"""Parte el tema (ya en ASCII) en tres: tema.html (lo mínimo que se pega en Tumblr), tema.css y tema.js (viven en el
repositorio y se cargan desde jsDelivr fijados al último commit, así los cambios no obligan a volver a pegar el tema).
Uso: python3 scripts/partir_tema.py tema-ascii.html carpeta_salida"""
import re, sys, os
src, out = sys.argv[1:3]
s = open(src, encoding='ascii').read()
css = '\n'.join(re.findall(r'<style>(.*?)</style>', s, re.S))
s = re.sub(r'<style>.*?</style>', '', s, flags=re.S)
# scripts grandes (sin etiquetas de Tumblr): se van al archivo; los pequeños de detección se quedan
js = []
def saca(m):
    body = m.group(1)
    if len(body) < 400:
        return m.group(0)
    js.append(body); return ''
s = re.sub(r'<script>(.*?)</script>', saca, s, flags=re.S)
assert not re.search(r'\{(?:block:|[A-Z][A-Za-z0-9-]*\})', ''.join(js) + css), 'etiquetas de Tumblr en el código externo'
tema_js = ('(function(){function arranca(){\n' + '\n'.join(js) + '\nwindow.initLB=window.initLB||(typeof initLB!=="undefined"?initLB:null);\n}'
           'if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",arranca);else arranca();})();\n')
LOADER = """<style>html.cargando body{opacity:0}</style><script>
(function(){var H=document.documentElement;H.classList.add('cargando');function ve(){H.classList.remove('cargando');}var R='https://cdn.jsdelivr.net/gh/inconsolataweb/inconsolata-datos@',K='inc-commit',v=null;
try{var c=JSON.parse(localStorage.getItem(K)||'null');if(c&&Date.now()-c.t<6e5)v=c.v;}catch(e){}
function go(v){window.INC_BASE=R+v+'/';var l=document.createElement('link');l.rel='stylesheet';l.href=INC_BASE+'tema/tema.css';
l.onload=ve;l.onerror=ve;document.head.appendChild(l);var x=document.createElement('script');x.src=INC_BASE+'tema/tema.js';document.head.appendChild(x);
setTimeout(ve,4000);}
if(v)go(v);else{var t=setTimeout(function(){t=0;go('main');},2500);
fetch('https://api.github.com/repos/inconsolataweb/inconsolata-datos/commits/main',{headers:{Accept:'application/vnd.github.sha'}}).then(function(r){if(!r.ok)throw 0;return r.text();})
.then(function(h){if(!t)return;clearTimeout(t);h=h.trim();try{localStorage.setItem(K,JSON.stringify({v:h,t:Date.now()}));}catch(e){}go(h);}).catch(function(){if(t){clearTimeout(t);go('main');}});}
})();
</script>"""
s = s.replace('</head>', LOADER + '\n</head>', 1)
os.makedirs(out, exist_ok=True)
open(os.path.join(out, 'tema.html'), 'w', encoding='ascii').write(s)
open(os.path.join(out, 'tema.css'), 'w', encoding='ascii').write(css)
open(os.path.join(out, 'tema.js'), 'w', encoding='ascii').write(tema_js)
print('tema.html', len(s) // 1024, 'KB · tema.css', len(css) // 1024, 'KB · tema.js', len(tema_js) // 1024, 'KB')
