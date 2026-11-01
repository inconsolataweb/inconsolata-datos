"""Portada del tema: estilos de la maqueta de portada (más el día de EXTRA!, el domingo de mucho más y los avisos)
encerrados en .v-home, y el código que la monta."""
import os, re
from tema_vistas import ambito
D = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(D, '..', 'html')

def _style(f):
    return re.findall(r'<style>(.*?)</style>', open(os.path.join(HTML, f)).read(), re.S)[0]

_p = _style('inconsolata-portada.html')
_p = _p[_p.index('/* tramas'):]
# fuera lo que ya pone el tema (idioma, cabecera pequeña, buscador, redes)
_p = re.sub(r'\.lang\{.*?\.hd-row2\{[^}]*\}', '', _p, flags=re.S)
_x = _style('inconsolata-portada-extra.html')
_x = '\n'.join(l for l in _x.split('\n') if l.startswith(('.xday', '@keyframes xrays', '@media (prefers-reduced-motion:reduce){.xday', '@media (max-width:820px){.xday')))

_b = _style('burbuja2.tpl.html')
_av = _b[_b.index('/* ===== aviso grande'):_b.index('/* notas de la maqueta')]
_av = (_av + _b[_b.index('@media (max-width:1180px)'):]).replace('.md', '.pv-md')
from tema_vistas import _reglas
PROPIAS = ('.prueba', '.go', '.reg-w', '.rbtn', '.panel', '.pr')
def _pref(css):
    out = []
    for r in _reglas(css):
        if r.startswith('@keyframes'):
            out.append(r); continue
        if r.startswith('@media'):
            i = r.index('{'); inner = _pref(r[i + 1:-1])
            if inner.strip():
                out.append(r[:i + 1] + inner + '}')
            continue
        sel, body = r.split('{', 1)
        sels = [x.strip() for x in sel.split(',')]
        if any(x.startswith(('.picker', '.topbar', '.masthead', '.side', '*')) for x in sels):
            continue
        out.append(','.join(x if x.startswith(PROPIAS) else '.prueba ' + x for x in sels) + '{' + body)
    return '\n'.join(out)
_av = _pref(re.sub(r'/\*.*?\*/', '', _av, flags=re.S))

EXTRA = """
.side .reg-w{display:block}
.reg-w.vacio .rbtn{pointer-events:none}
.mm-hoy{font-size:15px;letter-spacing:3px;background:var(--ink);color:var(--yellow);padding:6px 10px;display:inline-block;align-self:flex-start;margin-bottom:6px}
.xday .xd-a{color:#fff;display:block}
.xday .xd-k{font-size:14px;letter-spacing:3px;background:var(--ink);color:var(--yellow);padding:6px 10px}
.xday .w{margin-top:22px}
.xday .fan{display:block}
.hero-card.solo{grid-column:1/13;margin-top:0;transform:rotate(-.6deg)}
.clip-g{display:grid;grid-template-columns:1fr;gap:8px}.clip-g.two{grid-template-columns:1fr 1fr}
.xs-top{display:flex;justify-content:space-between;align-items:flex-end;gap:16px;flex-wrap:wrap}
.xs-n{text-align:right}
.xs-m{font-size:15px;line-height:1.45}
.ts-t{display:flex;flex-direction:column;gap:14px}
.tsheet h3{font-size:clamp(32px,3.2vw,48px);overflow-wrap:anywhere}
.tsheet h3.largo{font-size:clamp(30px,3vw,42px)}
.proj h3.largo{font-size:clamp(34px,3.6vw,52px);line-height:.95}
.mas{display:flex;justify-content:center;margin:-40px 0 110px}
.mas .btn-ink{font-family:'Archivo',sans-serif;font-size:14px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;padding:14px 22px}
.sheet .tt em,.tsheet h3 em{color:var(--accent);font-style:inherit}
.hero-card h1 em{color:var(--yellow);font-style:inherit}
.frame{border:0;padding:0;background:none;box-shadow:none}
.frame:hover{transform:none}
.topbar .hd-right{gap:2px}
.topbar .btn-ink{min-height:40px}
.masthead{min-height:300px}
.masthead{z-index:20}
.serif{font-family:'Fraunces',serif}
.sec-head h2.serif{font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144}
.rbtn .dot{color:#fff!important}
.side{z-index:30}
.tm-btns{display:flex;flex-wrap:wrap;gap:14px}
.lite-lista{display:flex;flex-direction:column;border-top:2px solid var(--ink)}
.lf{display:grid;grid-template-columns:92px minmax(0,1fr);gap:14px;align-items:start;padding:14px 0;border-bottom:1px solid #CFC8B8;color:var(--ink)}
.lf-ph{width:92px;height:92px;background:#DCD5C6;overflow:hidden;border:2px solid var(--ink)}
.lf-ph img{width:100%;height:100%;object-fit:cover;display:block}
.lf-tx{display:flex;flex-direction:column;gap:4px;min-width:0}
.lf-s{font-family:'Archivo',sans-serif;font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--accent)}
.lf-k{font-family:'Archivo',sans-serif;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--muted)}
.lf-k .k-av{width:1.3em;height:1.3em}
.lf-t{font-family:'Fraunces',serif;font-weight:700;font-size:19px;line-height:1.15}
.lf-t em{color:var(--accent);font-style:inherit}
.s-m .lf-ph{border-color:var(--yellow)}.s-x .lf-ph{border-color:var(--accent)}
.hero-meta .k-av{filter:none;width:1.6em;height:1.6em;vertical-align:-.45em}
.hero-meta a{display:inline-flex;align-items:center}
.hero-meta{align-items:center}
.k-esp{color:var(--accent);font-family:'Archivo',sans-serif;font-size:12px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;display:block;margin:2px 0 4px}
.hero-card .k-esp{display:inline;color:var(--yellow);font-size:inherit;letter-spacing:inherit;margin:0}
.sheet.dark .k-esp{color:var(--yellow)}
.hero-card.c-negro{background:var(--ink)}
.hero-card.c-amarillo{background:var(--yellow);color:var(--ink)}
.hero-card.c-amarillo h1 a,.hero-card.c-amarillo .hero-meta a{color:var(--ink)}
.hero-card.c-amarillo h1 em,.hero-card.c-amarillo .k-esp{color:var(--accent)}
.hero-card.c-amarillo .hero-meta{border-top-color:var(--ink)}
.hero-card.c-amarillo .k-av{filter:brightness(0)}
.hero-card.c-blanco{background:#fff;color:var(--ink)}
.hero-card.c-blanco h1 a,.hero-card.c-blanco .hero-meta a{color:var(--ink)}
.hero-card.c-blanco h1 em,.hero-card.c-blanco .k-esp{color:var(--accent)}
.hero-card.c-blanco .hero-meta{border-top-color:var(--ink)}
.hero-card.c-blanco .k-av{filter:brightness(0)}
.sheet.c-magenta{background:var(--accent);color:#fff}
.sheet.c-magenta .tt,.sheet.c-magenta .kicker,.sheet.c-magenta .by{color:#fff}
.sheet.c-magenta .k-esp{color:var(--yellow)}
.sheet.c-magenta .k-av{filter:none}
.sheet.c-amarillo{background:var(--yellow)}
.hm-avs{display:inline-flex;align-items:center;gap:4px;flex-wrap:wrap}
.hm-avs a{display:inline-grid;place-items:center;width:30px;height:30px;border-radius:50%;background:rgba(255,255,255,.14);font-weight:800}
.hm-avs .k-av{width:24px!important;height:24px!important;margin:0!important;vertical-align:0}
.hm-n{font-family:'Archivo',sans-serif;font-weight:800}
.muchos .k-av{margin-right:.15em}
.hero-meta span{font-family:'Archivo',sans-serif;font-size:14px;font-weight:700;letter-spacing:1px;line-height:1.6em}
.masthead.choca .prueba{position:relative;left:auto;right:auto;top:auto;bottom:auto;width:auto;max-width:460px;margin:10px 0 34px}
.masthead.choca{flex-wrap:wrap}
.rbtn.new.visto svg{animation:none}
.mm{overflow:hidden}
.film.cinta{display:block;height:auto;max-height:none;margin:6px -12px 44px;padding:0 0 4px;overflow:hidden;transform:rotate(-.6deg)}
.cn-v .frame .ph{flex-shrink:0}
.cn-v{display:flex;width:max-content}
.cn-v .cn-r{display:flex;gap:12px;padding:6px 6px 6px 12px;flex-shrink:0}
.cn-v .frame{width:200px;flex-shrink:0}
.cn-v .frame .ph{height:230px;overflow:hidden}
.cn-v .frame .ph img{width:100%;height:100%;object-fit:cover;object-position:top}
.cn-v.gira{animation:cnm var(--cn,60s) linear infinite}
.cn-v.gira:hover,.cn-v.gira:focus-within{animation-play-state:paused}
@keyframes cnm{to{transform:translateX(-50%)}}
.cn-v.quieta{width:auto;overflow-x:auto}
@media (max-width:820px){.cn-v .frame{width:150px}.cn-v .frame .ph{height:180px}}
.tdl-pl{margin-top:12px}
.tdl-pl summary{cursor:pointer;display:inline-flex;align-items:center;gap:8px;font:800 12px 'Archivo',sans-serif;letter-spacing:2px;text-transform:uppercase;border:2px solid var(--ink);padding:8px 14px;min-height:40px;background:var(--paper);list-style:none}
.tdl-pl summary::-webkit-details-marker{display:none}
.tdl-pl summary::after{content:'▾';font-size:14px}
.tdl-pl[open] summary::after{content:'▴'}
.tdl-pl summary:hover{background:var(--yellow)}
.tdl-pl[open] summary{margin-bottom:12px}
@media (max-width:820px){.masthead{min-height:0}.topbar .hd-right nav a:not(.btn-ink){display:none}}
"""

PCSS = ambito(_p + _x + EXTRA, '.v-home') + '\n' + ambito(_av, '.v-home') + """
/* ===== móvil «carrete» ===== */
html.lite body{padding-bottom:84px}
.v-home.lt{padding-bottom:10px;overflow-x:hidden}
.lt img{display:block}
.lt-kk{display:block;font:800 11px/1.3 'Archivo',sans-serif;letter-spacing:2.5px;text-transform:uppercase}
.lt-k{display:flex;flex-wrap:wrap;align-items:center;gap:4px;font:800 10px/1.35 'Archivo',sans-serif;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted)}
.lt-av{width:16px;height:16px;object-fit:contain;border-radius:2px;background:#fff}
.lt-sh{display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin:30px 16px 12px;border-top:2px solid var(--ink);padding-top:12px}
.lt-sh h2{margin:0;font:800 13px/1 'Archivo',sans-serif;letter-spacing:2.5px;text-transform:uppercase}
.lt-sh h2 em{font-style:normal;color:var(--accent)}
.lt-sh a,.lt-sh button{font:800 11px 'Archivo',sans-serif;letter-spacing:2px;text-transform:uppercase;color:var(--ink);background:none;border:0;border-bottom:2px solid var(--accent);padding:4px 0;cursor:pointer}
.lt-sw{display:flex;gap:12px;overflow-x:auto;overscroll-behavior-x:contain;scroll-snap-type:x mandatory;scroll-padding:0 16px;padding:2px 16px 8px;scrollbar-width:none;-webkit-overflow-scrolling:touch}
.lt-sw::-webkit-scrollbar{display:none}
.lt-sw>a{scroll-snap-align:start;flex-shrink:0;color:var(--ink);text-decoration:none}
.lt-car>.lt-c{flex:0 0 76%;max-width:330px;background:#fff;border:2px solid var(--ink);display:flex;flex-direction:column;box-shadow:4px 4px 0 var(--ink);margin-bottom:4px}
.lt-ph{position:relative;aspect-ratio:4/5;overflow:hidden;border-bottom:2px solid var(--ink);background:#E3DDD0}
.lt-ph img{width:100%;height:100%;object-fit:cover;object-position:top}
.lt-e{position:absolute;left:0;bottom:0;background:var(--accent);color:#fff;font:800 10px/1.2 'Archivo',sans-serif;letter-spacing:1.5px;text-transform:uppercase;padding:6px 9px;max-width:100%}
.lt-tx{display:flex;flex-direction:column;gap:6px;padding:11px 12px 13px}
.lt-t{font:700 18px/1.17 'Fraunces',serif;overflow-wrap:break-word}
.lt-t em,.lt-ht em{color:var(--accent);font-style:italic}
.lt-d{font:700 11px 'Archivo',sans-serif;color:var(--muted)}
.lt-fin{flex:0 0 40%!important;max-width:170px;background:var(--ink);color:var(--yellow)!important;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:8px;text-align:center;font:800 11px 'Archivo',sans-serif;letter-spacing:2px;text-transform:uppercase;border:2px solid var(--ink);margin-bottom:4px}
.lt-fin b{font:italic 900 44px/1 'Fraunces',serif;letter-spacing:0}
.lt-hero{position:relative;display:block;aspect-ratio:4/5;max-height:72vh;width:100%;overflow:hidden;background:var(--ink);color:#fff;border-bottom:2px solid var(--ink)}
.lt-hero img{width:100%;height:100%;object-fit:cover;object-position:top}
.lt-ov{position:absolute;left:0;right:0;bottom:0;padding:70px 16px 18px;background:linear-gradient(rgba(22,20,15,0),rgba(22,20,15,.94) 55%);display:flex;flex-direction:column;gap:8px}
.lt-ov .lt-kk{color:var(--yellow)}.lt-ov .lt-k{color:#fff}
.lt-ht{font:italic 900 30px/1.02 'Fraunces',serif;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;overflow-wrap:break-word}
.lt-web{display:flex;flex-direction:column;gap:12px;padding:22px 16px 24px;background:#fff;border-bottom:2px solid var(--ink);color:var(--ink)}
.lt-web .lt-kk{color:var(--accent)}
.lt-wf{display:block;border:2px solid var(--ink);box-shadow:5px 5px 0 var(--yellow);background:#fff}
.lt-wb{display:flex;gap:5px;padding:6px 8px;background:var(--ink)}.lt-wb i{width:7px;height:7px;border-radius:50%;background:#5E5A50}
.lt-wf img{width:100%;aspect-ratio:16/10;object-fit:cover;object-position:top}
.lt-wp{font:16px/1.45 'Fraunces',serif}
.lt-cta{align-self:flex-start;background:var(--accent);color:#fff;font:800 12px 'Archivo',sans-serif;letter-spacing:2px;text-transform:uppercase;padding:12px 16px;box-shadow:4px 4px 0 var(--ink)}
.lt-mm{background:var(--yellow);border-top:2px solid var(--ink);border-bottom:2px solid var(--ink);padding:18px 0 14px;margin-top:0}
.lt-in{padding:0 16px 12px}
.lt-mmt{display:block;color:var(--ink);margin-top:6px;font:italic 900 31px/1.05 'Fraunces',serif;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144}
.lt-mmt b{font-style:normal;font-variation-settings:'opsz' 144;letter-spacing:-.02em;white-space:nowrap}
.lt-fr>a{flex:0 0 136px}
.lt-fi{display:block;height:176px;background:#fff;border:2px solid var(--ink);overflow:hidden}
.lt-fi img{width:100%;height:100%;object-fit:cover;object-position:top}
.lt-fc{display:block;margin-top:6px;font:800 9.5px 'Archivo',sans-serif;letter-spacing:1.5px;text-transform:uppercase;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lt-fr>.lt-fin{height:180px;flex:0 0 120px!important}
.lt-esp>a{flex:0 0 62%;max-width:260px;min-height:156px;padding:14px;color:#fff!important;border:2px solid var(--ink);display:flex;flex-direction:column;justify-content:flex-end;gap:6px;box-shadow:4px 4px 0 var(--ink);margin-bottom:4px}
.lt-esp svg{width:40px;height:40px;overflow:visible;margin-bottom:auto}
.lt-esp b{font:italic 900 21px/1.05 'Fraunces',serif;overflow-wrap:break-word}
.lt-esp small{font:800 10px 'Archivo',sans-serif;letter-spacing:2px;text-transform:uppercase;opacity:.85}
.lt-esp .c-mag{background:var(--accent)}.lt-esp .c-cya{background:#00A0DC}.lt-esp .c-ink{background:var(--ink)}.lt-esp .c-yel{background:var(--yellow);color:var(--ink)!important}
.lt-tm{display:flex;flex-wrap:wrap;gap:8px;padding:0 16px}
.lt-tm a{display:inline-flex;align-items:center;gap:7px;background:var(--yellow);border:2px solid var(--ink);padding:7px 11px;font:700 14px 'Archivo',sans-serif;color:var(--ink)}
.lt-tm svg{width:18px;height:18px;overflow:visible}
.lt-hoy>a{flex:0 0 46%;max-width:200px;display:flex;flex-direction:column;gap:4px}
.lt-hoy .lt-fi{height:130px}
.lt-hoy b{font:italic 900 26px/1 'Fraunces',serif;color:var(--accent);margin-top:6px}
.lt-hoy span:last-child{font:600 14px/1.25 'Fraunces',serif}
.lt-proj{display:flex;flex-direction:column;gap:8px;margin:30px 16px 0;padding:0 0 16px;border:2px solid var(--ink);background:#fff;color:var(--ink);box-shadow:4px 4px 0 var(--ink)}
.lt-proj img{width:100%;aspect-ratio:16/9;object-fit:cover;border-bottom:2px solid var(--ink)}
.lt-proj .lt-kk,.lt-proj b,.lt-proj span{margin:0 14px}.lt-proj .lt-kk{margin-top:6px;color:var(--accent)}
.lt-proj b{font:italic 900 26px/1.05 'Fraunces',serif}.lt-proj>span:last-child{font:15px/1.45 'Fraunces',serif}
.lt-md>a{flex:0 0 84px;display:flex;flex-direction:column;align-items:center;gap:6px;text-align:center}
.lt-md img{width:64px;height:64px;object-fit:contain;background:#fff;border:2px solid var(--ink);padding:6px}
.lt-md span{font:700 11px/1.2 'Archivo',sans-serif;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.lt-ver{text-align:center;margin:34px 16px 10px}
.lt-ver button{background:none;border:2px solid var(--ink);padding:10px 14px;font:800 11px 'Archivo',sans-serif;letter-spacing:2px;text-transform:uppercase;color:var(--ink)}
html.lite .v-home.lt .faldon{height:44px;transform:none;margin:0;overflow:hidden}
html.lite .v-home.lt .faldon .f-icon{width:44px;height:44px;transform:none;margin:0;box-shadow:none}
html.lite .v-home.lt .faldon .f-icon svg{width:30px;height:30px}
html.lite .v-home.lt .faldon .f-track{font-size:15px}
html.lite .v-home.lt .tira{font-size:13px}
html.lite .v-home.lt .colav{margin:16px;max-width:none;position:relative;left:auto;right:auto;top:auto}
html.lite .tdl{width:100vw;max-width:100vw;height:100dvh;max-height:100dvh;margin:0;border:0}
html.lite .tdl h2{font-size:34px}
html.lite .tdl .tdl-c a{font-size:15px;min-height:36px;padding:5px 12px}

.es-portada .page>.head,.es-portada main.wrap{display:none}
"""
PJS = open(os.path.join(D, 'tema_portada.js')).read()
