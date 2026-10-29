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
.hm-avs{display:inline-flex;align-items:center;gap:4px;flex-wrap:wrap}
.hm-avs a{display:inline-grid;place-items:center;width:30px;height:30px;border-radius:50%;background:rgba(255,255,255,.14);font-weight:800}
.hm-avs .k-av{width:24px!important;height:24px!important;margin:0!important;vertical-align:0}
.hm-n{font-family:'Archivo',sans-serif;font-weight:800}
.muchos .k-av{margin-right:.15em}
.hero-meta span{font-family:'Archivo',sans-serif;font-size:14px;font-weight:700;letter-spacing:1px;line-height:1.6em}
.masthead.choca .prueba{position:relative;left:auto;right:auto;top:auto;bottom:auto;width:auto;max-width:460px;margin:10px 0 34px}
.masthead.choca{flex-wrap:wrap}
.rbtn.new.visto svg{animation:none}
@media (max-width:820px){.masthead{min-height:0}.topbar .hd-right nav a:not(.btn-ink){display:none}}
"""

PCSS = ambito(_p + _x + EXTRA, '.v-home') + '\n' + ambito(_av, '.v-home') + """
.es-portada .page>.head,.es-portada main.wrap{display:none}
"""
PJS = open(os.path.join(D, 'tema_portada.js')).read()
