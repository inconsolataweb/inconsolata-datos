"""Páginas de temas especiales: solo los posts con la etiqueta del especial.
Uso: python3 -I gen/especial.py <scratchpad>
"""
import os, sys, json, html, re
from collections import Counter, OrderedDict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from posts import CSS, OUT
from common import symbols, head_interior, HEAD_CSS, MINI_CSS, MINI_JS, TIPOS
from temas_iconos import slug as tslug, tema_symbols

S = sys.argv[1]
e = html.escape
SD = json.load(open(os.path.join(S, 'data', 'search.json')))
ES = json.load(open(os.path.join(S, 'data', 'especiales.json')))
byid = {p['i']: p for p in SD['posts']}
tidx = {t['n']: i for i, t in enumerate(SD['temas'])}
MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
SECN = {'m': 'Mucho más', 'x': 'EXTRA!', 'd': 'Detallitos', 'b': 'Metablog', 'o': 'Offtopic'}

def fdate(d, year=True):
    return f"{int(d[8:10])} de {MESES[int(d[5:7]) - 1]}" + (f" de {d[:4]}" if year else '')

def rango(a, b):
    if a == b:
        return fdate(a)
    if a[:4] == b[:4]:
        return f"del {fdate(a, False)} al {fdate(b)}"
    return f"del {fdate(a)} al {fdate(b)}"

def card(p):
    head = p['t'] or p['b'] or 'Entrada sin texto'
    meds = ' · '.join(SD['medios'][i]['n'] for i in p['m'][:2])
    auts = [SD['autores'][i]['n'] for i in p['a'][:3]]
    ico = ''.join(f'<span title="{TIPOS[k][0]}"><svg viewBox="0 0 64 64" aria-hidden="true" style="overflow:visible"><use href="#i-{k}"/></svg></span>' for k in p['k'][:3])
    return (f'<a class="ec" href="https://inconsolata.com/post/{e(p["u"])}" data-d="{p["d"]}"><div class="ph">'
            + (f'<img loading="lazy" src="{e(p["im"])}" alt="" onerror="this.remove()">' if p['im'] else '')
            + (f'<span class="sec">{SECN[p["s"]]}</span>' if p['s'] else '')
            + f'<span class="ico">{ico}</span></div>'
            f'<span class="meta"><b>{int(p["d"][8:10])} {MESES[int(p["d"][5:7]) - 1][:3]}</b>{" · " + e(meds) if meds else ""}</span>'
            f'<span class="tt">{e(head)}</span>' + (f'<span class="by">por {e(", ".join(auts))}</span>' if auts else '') + '</a>')

ECSS = """
.eh{background:var(--accent);color:#fff;position:relative;overflow:hidden}
.eh .in{display:grid;grid-template-columns:minmax(0,1fr) 260px;gap:30px;padding:40px 24px 46px;align-items:end}
.eh .kick{display:inline-block;background:var(--ink);color:var(--yellow);font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;padding:7px 11px}
.eh h1{margin:16px 0 12px;font-size:clamp(54px,8.6vw,132px);line-height:.88;letter-spacing:-.03em}
.eh .meta{display:flex;flex-wrap:wrap;gap:6px 22px;font-size:14px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;border-top:1px solid rgba(255,255,255,.6);padding-top:12px}
.eh .meta a{color:#fff;border-bottom:2px solid var(--yellow)}
.eh .meta a:hover{color:var(--yellow)}
.eh .big{width:230px;height:230px;justify-self:end;overflow:visible}
.eh .big .k{color:#fff}.eh .big .m{color:var(--ink);mix-blend-mode:normal;opacity:.85}
.etext{position:relative;border:2px dashed var(--ink);background:rgba(255,255,255,.55);padding:26px 24px 22px;font-family:'Fraunces',serif;font-size:21px;line-height:1.5;max-width:860px;margin:44px 0 0}
.etext .lbl{position:absolute;top:-13px;left:18px;background:var(--accent);color:#fff;font-family:'Archivo',sans-serif;font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;padding:4px 8px}
.who{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,380px),1fr));gap:20px 48px;margin-top:40px}
.who h2{margin:0 0 10px;font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;border-bottom:2px solid var(--ink);padding-bottom:6px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips a{border:2px solid var(--ink);border-radius:999px;padding:5px 13px;font-family:'Fraunces',serif;font-style:italic;font-weight:700;font-size:16px;min-height:38px;display:inline-flex;align-items:center;gap:7px;background:#fff}
.chips a small{font-family:'Archivo',sans-serif;font-style:normal;font-size:11px;font-weight:800;color:var(--accent)}
.chips a:hover{background:var(--yellow);color:var(--ink)}
.tl-bar{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:12px;margin:56px 0 10px;border-bottom:3px solid var(--ink);padding-bottom:12px}
.tl-bar h2{margin:0;font-size:clamp(38px,5vw,64px);line-height:.9}
.tl-bar h2 em{color:var(--accent)}
.tl-bar button{border:2px solid var(--ink);background:transparent;font-family:'Archivo',sans-serif;font-size:12px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;min-height:42px;padding:0 14px;cursor:pointer;color:var(--ink)}
.tl-bar button:hover{background:var(--ink);color:var(--paper)}
.tl{display:flex;flex-direction:column}
.mo{display:grid;grid-template-columns:150px minmax(0,1fr);gap:24px;padding:26px 0;border-bottom:1px solid #CFC8B8}
.mo h3{margin:0;font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-size:30px;line-height:1;position:sticky;top:76px;align-self:start}
.mo h3 small{display:block;font-family:'Archivo',sans-serif;font-style:normal;font-size:12px;font-weight:800;letter-spacing:1.5px;color:var(--accent);margin-top:6px}
.mo .g{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:26px 20px}
.ec{display:flex;flex-direction:column;gap:7px;color:var(--ink)}
.ec .ph{position:relative;aspect-ratio:4/3;border:2px solid var(--ink);overflow:hidden;background:#fff radial-gradient(#16140F 1px,transparent 1.2px) 0 0/7px 7px;transition:transform .2s,box-shadow .2s}
.ec .ph img{width:100%;height:100%;object-fit:cover;object-position:top;display:block;background:#fff}
.ec:hover .ph{transform:translate(-3px,-3px);box-shadow:6px 6px 0 var(--accent)}
.ec .sec{position:absolute;top:8px;left:8px;background:var(--ink);color:var(--yellow);font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;padding:5px 8px}
.ec .ico{position:absolute;left:8px;bottom:8px;display:flex;gap:4px}
.ec .ico span{width:32px;height:32px;background:var(--paper);border:2px solid var(--ink);display:flex;align-items:center;justify-content:center}
.ec .ico svg{width:20px;height:20px}
.ec .meta{font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--muted)}
.ec .meta b{color:var(--ink)}
.ec .tt{font-family:'Fraunces',serif;font-weight:600;font-size:17px;line-height:1.25;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.ec .by{font-size:13px;color:var(--muted)}
.others{margin:70px 0 0}
.others h2{margin:0 0 14px;font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;border-bottom:2px solid var(--ink);padding-bottom:6px}
.others .chips a svg{width:22px;height:22px;overflow:visible}
footer{background:var(--ink);color:var(--paper);margin-top:80px}
.cmyk-bar{display:flex;height:10px}.cmyk-bar span{flex:1}
.foot{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:12px;padding:26px 24px;font-size:13px}
@media (max-width:760px){.eh .in{grid-template-columns:1fr}.eh .big{width:120px;height:120px;justify-self:start;grid-row:1}.mo{grid-template-columns:1fr;gap:12px}.mo h3{position:static}.mo .g{grid-template-columns:repeat(auto-fill,minmax(150px,1fr))}}
"""

JS = """<script>
document.getElementById('order').addEventListener('click',function(){
 var tl=document.getElementById('tl'),b=this,rev=b.getAttribute('aria-pressed')!=='true';
 [].slice.call(tl.children).reverse().forEach(function(m){tl.appendChild(m);var g=m.querySelector('.g');[].slice.call(g.children).reverse().forEach(function(c){g.appendChild(c);});});
 b.setAttribute('aria-pressed',rev);b.textContent=rev?'Ver en orden cronológico »':'Ver lo más reciente primero »';});
</script>"""

def page(x, all_es):
    ps = [byid[i] for i in x['posts']]
    ti = tidx.get(x['tema'])
    ic = tslug(x['tema'])
    groups = OrderedDict()
    for p in ps:
        groups.setdefault(p['d'][:7], []).append(p)
    tl = ''.join(f'<section class="mo"><h3>{MESES[int(k[5:7]) - 1].capitalize()}<small>{k[:4]} · {len(v)} {"entrada" if len(v) == 1 else "entradas"}</small></h3>'
                 f'<div class="g">{"".join(card(p) for p in v)}</div></section>' for k, v in groups.items())
    cm = Counter(m for p in ps for m in p['m'])
    ca = Counter(a for p in ps for a in p['a'])
    chip = lambda arr, key, c: ''.join(f'<a href="inconsolata-buscador.html#{key}={i}">{e(arr[i]["n"])}<small>{n}</small></a>' for i, n in c.most_common(12))
    hermanos = [y for y in all_es if y['tema'] == x['tema'] and y is not x]
    others = ''.join(f'<a href="especial-{y["slug"]}.html"><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#{tslug(y["tema"])}"/></svg>{e(y["titulo"])}<small>{len(y["posts"])}</small></a>' for y in hermanos)
    n = len(ps)
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(x['titulo'])} · especial · inconsolata»</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1;1,9..144,100..900,0..100,0..1&display=swap">
<style>{CSS}{HEAD_CSS}{MINI_CSS}{ECSS}</style></head>
<body>{symbols()}{tema_symbols()}
<div class="page">
{head_interior()}
<main>
<section class="eh"><div class="wrap in">
<div><span class="kick">Especial »</span>
<h1 class="soft">{e(x['titulo'])}</h1>
<div class="meta"><span>{n} {'entrada' if n == 1 else 'entradas'}</span><span>{rango(x['desde'], x['hasta'])}</span>
<span>Dentro de: <a href="inconsolata-buscador.html#h={ti}">{e(x['tema'])} »</a></span></div></div>
<svg class="big" viewBox="0 0 64 64" aria-hidden="true"><use href="#{ic}" class="k"/><use href="#{ic}" class="m" x="3" y="2.5"/></svg>
</div></section>
<div class="wrap">
<div class="etext"><span class="lbl">Tu texto</span>[Aquí va, si quieres, una entradilla sobre el especial: qué pasó, qué cobertura gráfica destacarías…]</div>
<div class="who"><div><h2>Medios</h2><div class="chips">{chip(SD['medios'], 'm', cm)}</div></div>
<div><h2>Autores</h2><div class="chips">{chip(SD['autores'], 'a', ca) or '<span style="font-size:14px;color:var(--muted)">Sin autores identificados</span>'}</div></div></div>
<div class="tl-bar"><h2 class="soft">La cobertura, <em>mes a mes</em></h2><button type="button" id="order" aria-pressed="false">Ver lo más reciente primero »</button></div>
<div class="tl" id="tl">{tl}</div>
{f'<section class="others"><h2>Otros especiales de {e(x["tema"])}</h2><div class="chips">{others}</div></section>' if others else ''}
</div>
</main>
<footer>
<div class="cmyk-bar" aria-hidden="true"><span style="background:#00A0DC"></span><span style="background:#66C6EA"></span><span style="background:#E5007E"></span><span style="background:#EF66B2"></span><span style="background:#FFD400"></span><span style="background:#FFE566"></span><span style="background:#16140F"></span><span style="background:#7A766C"></span></div>
<div class="wrap foot"><span class="soft" style="font-size:56px;line-height:1">inc<span style="color:#EF66B2">»</span></span><span>© inconsolata» 2011–2026 · un blog de Saúl Castillo</span></div>
</footer></div>
{JS}{MINI_JS}
</body></html>"""

os.makedirs(os.path.join(OUT, 'especiales'), exist_ok=True)
for x in ES:
    open(os.path.join(OUT, 'especiales', f"especial-{x['slug']}.html"), 'w').write(page(x, ES).replace('href="inconsolata-', 'href="../inconsolata-').replace('href="ficha-', 'href="../ficha-'))
print(len(ES), 'especiales')
