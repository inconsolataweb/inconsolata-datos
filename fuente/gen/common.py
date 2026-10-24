# ------------------------------------------------------------------
# Bilingüe ES/EN: cada texto traducible lleva su versión inglesa en data-en
import html as _html
def en(txt):
    """Atributo data-en con la versión inglesa (admite HTML sencillo)."""
    return f' data-en="{_html.escape(txt, quote=True)}"'

TIPOS_EN = {'info': 'Infographic', 'carto': 'Cartography', 'port': 'Front page', 'graf': 'Chart', 'ilus': 'Illustration',
            'foto': 'Photography', 'video': 'Video', 'publi': 'Advertising', 'online': 'Online'}
PAISES_EN = {'España': 'Spain', 'Francia': 'France', 'Reino Unido': 'United Kingdom', 'Estados Unidos': 'United States', 'México': 'Mexico', 'Portugal': 'Portugal'}
TEMAS_EN = {'deporte': 'sport', 'fútbol': 'football', 'literatura': 'literature', 'cultura': 'culture', 'ocio': 'leisure', 'pasatiempos': 'puzzles',
            'geopolítica': 'geopolitics', 'economía': 'economy', 'gastronomía': 'food', 'ciencia': 'science', 'premios Nobel': 'Nobel Prizes',
            'política': 'politics', 'elecciones': 'elections', 'vivienda': 'housing', 'historia del periodismo': 'history of journalism',
            'aniversarios': 'anniversaries', 'publicidad': 'advertising', 'terremotos': 'earthquakes', 'datos': 'data', 'proyectos': 'projects'}
_MESES = {'enero': 'January', 'febrero': 'February', 'marzo': 'March', 'abril': 'April', 'mayo': 'May', 'junio': 'June', 'julio': 'July',
          'agosto': 'August', 'septiembre': 'September', 'octubre': 'October', 'noviembre': 'November', 'diciembre': 'December'}
def fecha_en(s):
    out = s.replace(' de ', ' ').replace(' y ', ' and ')
    for k, v in _MESES.items():
        out = out.replace(k, v)
    return out

LANG = ('<div class="lang" role="group" aria-label="Idioma / Language">'
        '<button type="button" data-setlang="es" aria-pressed="true" title="Español">ES</button>'
        '<button type="button" data-setlang="en" aria-pressed="false" title="English">EN</button></div>')
I18N_CSS = """
.lang{display:inline-flex;border:2px solid var(--ink);margin-left:8px}
.lang button{font-family:'Archivo',sans-serif;font-size:12px;font-weight:800;letter-spacing:1px;background:transparent;color:var(--ink);border:0;padding:6px 9px;min-height:32px;min-width:36px;cursor:pointer}
.lang button[aria-pressed="true"]{background:var(--ink);color:var(--paper)}
html[lang="es"] .only-en{display:none!important}
html[lang="en"] .only-es{display:none!important}
.tr-note{font-family:'Archivo',sans-serif;font-size:14px;font-weight:700;background:var(--yellow);padding:10px 14px;margin:0}
.hd-row2{display:flex;align-items:center;gap:4px}
"""
I18N_JS = """<script>
(function(){var K='inc-lang';
function get(){try{return localStorage.getItem(K)||'es'}catch(e){return 'es'}}
function save(l){try{localStorage.setItem(K,l)}catch(e){}}
function apply(l){document.documentElement.lang=l;
document.querySelectorAll('[data-en]').forEach(function(el){if(el.dataset.es===undefined)el.dataset.es=el.innerHTML;el.innerHTML=(l==='en')?el.dataset.en:el.dataset.es;});
document.querySelectorAll('[data-en-ph]').forEach(function(el){if(el.dataset.esPh===undefined)el.dataset.esPh=el.placeholder;el.placeholder=(l==='en')?el.dataset.enPh:el.dataset.esPh;});
document.querySelectorAll('[data-setlang]').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-setlang')===l?'true':'false');});
document.dispatchEvent(new CustomEvent('inc-lang',{detail:l}));}
document.addEventListener('click',function(e){var b=e.target.closest('[data-setlang]');if(!b)return;save(b.getAttribute('data-setlang'));apply(b.getAttribute('data-setlang'));});
apply(get());})();
</script>"""

LANG_MINI = LANG.replace('class="lang"', 'class="lang lang-mini"')
# Traducción aparcada: el botón y su script se desactivan; las versiones en inglés siguen guardadas en data-en
LANG = ''
LANG_MINI = ''
I18N_JS = ''

S4 = 'stroke="currentColor" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"'

# Tipos de pieza: clave -> (nombre, dibujo 64x64)
TIPOS = {
 'info': ('Infografía', f'<g {S4}><path d="M26 16 A18 18 0 1 0 44 34 H26 Z" fill="none"/><path d="M32 10 A18 18 0 0 1 50 28 H32 Z" fill="currentColor"/></g>'),
 'carto': ('Cartografía', f'<g {S4} fill="none"><path d="M8 14 L24 8 L40 14 L56 8 V50 L40 56 L24 50 L8 56 Z"/><path d="M24 8 V50 M40 14 V56"/><circle cx="47" cy="27" r="4" fill="currentColor"/></g>'),
 'port': ('Portada', f'<g {S4} fill="none"><rect x="10" y="8" width="44" height="50"/><path d="M16 17 H48" stroke-width="6"/><path d="M16 28 H30 M16 35 H30 M16 42 H30 M16 49 H30"/><rect x="35" y="26" width="13" height="24" fill="currentColor"/></g>'),
 'graf': ('Gráfico', f'<g {S4} fill="currentColor"><path d="M6 56 H58" fill="none"/><rect x="11" y="36" width="10" height="20"/><rect x="27" y="22" width="10" height="34"/><rect x="43" y="10" width="10" height="46"/></g>'),
 'ilus': ('Ilustración', f'<g {S4} fill="none"><path d="M32 4 L48 30 L32 60 L16 30 Z"/><path d="M32 60 V36"/><circle cx="32" cy="30" r="4" fill="currentColor"/></g>'),
 'foto': ('Fotografía', f'<g {S4} fill="none"><rect x="6" y="18" width="52" height="36" rx="4"/><path d="M22 18 L26 10 H38 L42 18"/><circle cx="32" cy="36" r="11"/><circle cx="32" cy="36" r="4" fill="currentColor"/></g>'),
 'video': ('Vídeo', f'<g {S4} fill="none"><rect x="6" y="10" width="52" height="36" rx="4"/><path d="M27 20 L41 28 L27 36 Z" fill="currentColor"/><path d="M8 56 H56"/><circle cx="22" cy="56" r="4" fill="currentColor"/></g>'),
 'publi': ('Publicidad', f'<g {S4} fill="none"><path d="M8 24 V40 H18 L42 52 V12 L18 24 Z"/><path d="M18 40 L22 54 H30 L27 41"/><path d="M50 22 L57 17 M50 32 H59 M50 42 L57 47"/></g>'),
 'online': ('Online', f'<g {S4} fill="none"><rect x="6" y="8" width="52" height="44" rx="3"/><path d="M6 19 H58"/><path d="M28 26 L28 47 L33 42 L37 51 L42 49 L38 40 L45 40 Z" fill="currentColor"/></g>'),
}
URNA = f'<g {S4} fill="none"><path d="M22 30 V6 H42 V30"/><path d="M27 16 L31 21 L38 12"/><path d="M4 30 H60"/><path d="M8 30 V58 H56 V30"/><path d="M20 30 H44" stroke-width="7"/><rect x="22" y="40" width="20" height="9" fill="currentColor"/></g>'

def symbols():
    out = ''.join(f'<symbol id="i-{k}" viewBox="0 0 64 64">{g}</symbol>' for k, (_, g) in TIPOS.items())
    out += f'<symbol id="i-urna" viewBox="0 0 64 64">{URNA}</symbol>'
    return f'<svg width="0" height="0" style="position:absolute" aria-hidden="true">{out}</svg>'

def icon(t, cls='', size=None):
    name, g = TIPOS[t]
    sz = f' width="{size}" height="{size}"' if size else ''
    return (f'<svg class="{cls}"{sz} viewBox="0 0 64 64" role="img" aria-label="{name}" style="overflow:visible"><title>{name}</title>'
            f'<g class="k">{g}</g><g class="m" transform="translate(3 2.5)">{g}</g></svg>')

# Menú superior
SEARCH = ('<form class="srch" role="search" action="#" onsubmit="return false">'
          '<label for="q-top" class="sr" data-en="Search inconsolata»">Buscar en inconsolata»</label>'
          '<input id="q-top" type="search" placeholder="Temas, medios, periodistas…" data-en-ph="Topics, outlets, journalists…" autocomplete="off">'
          '<button type="submit" aria-label="Buscar"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg></button></form>')
NAV_LINKS = ('<a href="#" data-en="About me">Sobre mí</a><a href="#" data-en="Infographics">Infografía</a><a href="#" data-en="Outlets">Medios</a><a href="https://inconsolata.com/archive" data-en="Archive">Archivo</a>' + SEARCH)
NAV = f'<nav aria-label="Secciones">{NAV_LINKS}<a href="https://buymeacoffee.com/saulcastillo" class="btn-ink" data-en="Support us »">Apóyanos »</a></nav>'

X_URL = 'https://x.com/inconsolata'
WEB_URL = 'https://saulcastillo.es'
MAIL_URL = 'mailto:inconsolataweb@gmail.com'
# Logo de X: icono publicado por Simple Icons (pensado para enlaces a redes)
X_ICON = 'https://cdn.jsdelivr.net/npm/simple-icons@11.0.0/icons/x.svg'
# Espiral de saulcastillo.es (archivo facilitado por Saúl)
ESPIRAL = '<svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true"><path d="M9.3 13.2a2.9 2.9 0 0 1 5.8 0a5.8 5.8 0 0 1-11.6 0a8.7 8.7 0 0 1 17.4 0a8.7 8.7 0 0 1-5.6 8.1" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round"/></svg>'
# La espiral en su color original, para la firma de los posts de texto
ESPIRAL_COLOR = '<svg viewBox="0 0 24 24" width="48" height="48" aria-hidden="true"><path d="M9.3 13.2a2.9 2.9 0 0 1 5.8 0a5.8 5.8 0 0 1-11.6 0a8.7 8.7 0 0 1 17.4 0a8.7 8.7 0 0 1-5.6 8.1" fill="none" stroke="#A862C8" stroke-width="2.8" stroke-linecap="round"/></svg>'
ICO_MAIL = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="5" width="18" height="14"/><path d="M3 6 L12 13 L21 6"/></svg>'

SOCIAL = (f'<div class="soc">'
          f'<a class="soc-b" href="{X_URL}" aria-label="inconsolata» en X" title="X"><img src="{X_ICON}" alt="" width="19" height="19" onerror="this.replaceWith(\'X\')"></a>'
          f'<a class="soc-b" href="{MAIL_URL}" aria-label="Escríbeme un correo" title="Correo">{ICO_MAIL}</a>'
          f'<a class="soc-b web" href="{WEB_URL}" aria-label="saulcastillo.es" title="saulcastillo.es">{ESPIRAL}</a>'
          f'</div>')

HEAD_CSS = """
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.srch{display:inline-flex;align-items:center;border-bottom:2px solid var(--ink);min-height:40px}
.srch input{border:0;background:transparent;font-family:'Archivo',sans-serif;font-size:14px;font-weight:600;color:var(--ink);width:210px;padding:8px 4px;outline-offset:2px}
.srch input{text-transform:none;letter-spacing:0}
.srch input::placeholder{color:#6E695E;text-transform:none;letter-spacing:0}
.srch button{border:0;background:transparent;color:var(--ink);width:40px;height:40px;display:inline-flex;align-items:center;justify-content:center;cursor:pointer}
.srch button:hover{color:var(--accent)}
.soc{display:flex;align-items:center;gap:2px}
.soc-b{width:42px;height:42px;display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:16px;opacity:.8;transition:opacity .2s,transform .2s}
.soc-b:hover{opacity:1;transform:translateY(-2px)}
.soc-b img,.soc-b svg{display:block}
.soc-b.web svg{width:24px;height:24px}
@media (max-width:700px){.srch input{width:150px}}
"""

def head_interior():
    return (f'<header class="head">'
            f'<a href="inconsolata-portada.html" class="brand soft" aria-label="inconsolata», ir a la portada">inc<span>»</span></a>'
            f'<div class="hd-right">{NAV}<div class="hd-row2">{SOCIAL}{LANG}</div></div></header>' + MINI_HEAD)

# Cabecera pequeña que aparece al bajar por cualquier página
MINI_HEAD = ('<div class="mini-head" id="mini-head"><div class="mh-in">'
             '<a class="mh-brand soft" href="inconsolata-portada.html" aria-label="inconsolata», ir a la portada">inc<span>»</span></a>'
             '<nav class="mh-nav" aria-label="Secciones"><a href="#" data-en="Infographics">Infografía</a><a href="#" data-en="Outlets">Medios</a><a href="https://inconsolata.com/archive" data-en="Archive">Archivo</a></nav>'
             + SEARCH.replace('q-top', 'q-mini') +
             LANG_MINI + '<a class="mh-apoya" href="https://buymeacoffee.com/saulcastillo" data-en="Support us »">Apóyanos »</a></div>'
             '<div class="mh-prog" aria-hidden="true"><span id="mh-bar"></span></div></div>')
MINI_CSS = """
.hd-right{display:flex;flex-direction:column;align-items:flex-end;gap:2px}
.hd-right nav{display:flex;flex-wrap:wrap;gap:6px 20px;align-items:center;justify-content:flex-end}
.mini-head{position:fixed;top:0;left:0;right:0;z-index:50;background:var(--paper);border-bottom:2px solid var(--ink);transform:translateY(-110%);visibility:hidden;transition:transform .3s,visibility .3s}
.mini-head.on{transform:none;visibility:visible}
.mh-in{max-width:1360px;margin:0 auto;padding:6px 24px;display:flex;align-items:center;gap:22px}
.mh-brand{font-size:38px;line-height:1;letter-spacing:0}
.mh-brand span{color:var(--accent)}
.mh-nav{display:flex;gap:18px;margin-left:auto;font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase}
.mini-head .srch{min-height:36px}
.mini-head .srch input{width:200px;font-size:13px}
.mh-apoya{font-size:12px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;background:var(--ink);color:var(--paper);padding:10px 12px}
.mh-apoya:hover{color:var(--yellow)}
.mh-prog{height:3px}
.mh-prog span{display:block;height:100%;width:0;background:var(--accent)}
@media (max-width:820px){.mh-nav{display:none}.mini-head .srch{margin-left:auto}.mini-head .srch input{width:110px}.mh-apoya{display:none}.hd-right{align-items:flex-start}.hd-right nav{justify-content:flex-start}}
@media (prefers-reduced-motion:reduce){.mini-head{transition:none}}
"""
MINI_JS = """<script>
(function(){var h=document.getElementById('mini-head'),b=document.getElementById('mh-bar');if(!h)return;
function u(){var y=window.scrollY||0;h.classList.toggle('on',y>320);var d=document.documentElement.scrollHeight-innerHeight;b.style.width=(d>0?Math.min(100,y/d*100):0)+'%';}
addEventListener('scroll',u,{passive:true});u();})();
</script>"""

# Temas: lista cerrada de temas visibles para el lector (las etiquetas técnicas quedan ocultas)
def temas_html(temas):
    if not temas:
        return ''
    return ('<div class="temas"><span class="caps" data-en="Topics »">Temas »</span>'
            + ''.join(f'<a href="#" data-en="{TEMAS_EN.get(t, t)}">{t}</a>' for t in temas) + '</div>')
TEMAS_CSS = """
.temas{display:flex;flex-wrap:wrap;align-items:center;gap:8px}
.temas .caps{margin-right:4px}
.temas a{background:var(--paper);border:2px solid var(--ink);border-radius:999px;padding:6px 14px;font-family:'Fraunces',serif;font-style:italic;font-weight:700;font-size:16px;min-height:38px;display:inline-flex;align-items:center}
.temas a:hover{background:var(--yellow);color:var(--ink)}
"""


# Aviso para los posts publicados antes del rediseño (el tema lo muestra comparando la fecha del post con la del lanzamiento)
LEGACY = ('<div class="legacy" role="note"><span class="lg-i" aria-hidden="true">»</span>'
          '<p><b>Post del archivo.</b> Se publicó originalmente en una versión anterior de inconsolata» '
          'y puede que algún elemento no se vea como debería. '
          '<a href="mailto:inconsolataweb@gmail.com?subject=Algo%20roto%20en%20un%20post">¿Ves algo roto? Avísame »</a></p></div>')
LEGACY_CSS = """
.legacy{display:flex;align-items:center;gap:14px;background:var(--yellow);padding:12px 18px;margin:4px 0 6px;box-shadow:4px 4px 0 var(--ink)}
.legacy .lg-i{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-size:34px;line-height:1;color:var(--accent)}
.legacy p{margin:0;font-family:'Archivo',sans-serif;font-size:15px;line-height:1.45}
.legacy a{font-weight:800;border-bottom:2px solid var(--ink);white-space:nowrap}
"""
