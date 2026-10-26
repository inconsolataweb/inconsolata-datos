import os, sys, json, html
sys.path.insert(0, os.path.dirname(__file__))
from posts import CSS, OUT, T
from common import head_interior, HEAD_CSS, icon, MINI_CSS, MINI_JS, TEMAS_CSS, ESPIRAL_COLOR, I18N_CSS, I18N_JS, LEGACY, LEGACY_CSS
from lightbox import LB_CSS, LB_HTML, LB_JS
e = html.escape

IMGS = ['019dd6d5f646d96915f9ecd84f2c1508/eccad2effd90fb88-99/s1280x1920/7cd945d0e148e5bcd0a2fbe680cf54b944f449dd.png',
        '046ad99cfe7742aa6946c87bc01736af/eccad2effd90fb88-80/s1280x1920/6febbe27c0caba6a82e19c0c361b105250c6b2f1.png',
        'b50b7602db8e286655dfa2da84759635/eccad2effd90fb88-b8/s1280x1920/34c7da1923f4bc148670d161f349ac8c874fafa3.png',
        '351f88bc364563f9d85b2a89e1d819f0/eccad2effd90fb88-04/s1280x1920/0e6fd87c2b10a5f7a6647f230967a252a42679b6.png',
        'a714445a273a71822b23ea16335a696f/eccad2effd90fb88-fc/s2048x3072/346ad1ac7870ae5de2f1dfd8e973fb6db130f7a0.png',
        '114bc49ae57d0f54f41cef6e703c4b42/eccad2effd90fb88-c9/s2048x3072/50b3c927f36e836ff76c43e3907a8784997eb231.png',
        '52904ba33be4eb70193c0dbd5cf0ad70/eccad2effd90fb88-1e/s2048x3072/ace42c490f2c717350d3d24ed054bdad17737d16.png']
IMGS = [T + u for u in IMGS]

ITEMS = [
 ('1', 'ilus', 'Folhinha · Folha de S.Paulo', '29 de agosto', 'Doble página del suplemento infantil dedicada a las plagas urbanas (murciélagos, ratas y cucarachas), con dibujos de {a}.', ['Marcelo Delamanha']),
 ('2', 'graf', 'The Wall Street Journal', '19 de agosto', '{a} analiza cómo el calor extremo y la sequía afectan a las economías europeas: energía, logística y agricultura.', ['Daniel Kiss']),
 ('3', 'info', 'El País', '20 de agosto', 'Un artículo de opinión con consejos para abrazarse más, acompañado de una infografía de {a}.', ['Mercè Sellarés']),
 ('4', 'info', 'Público (Portugal)', '6 de agosto', 'Infografía a doble página sobre el puente 25 de Abril de Lisboa, en el 60.º aniversario de su inauguración sobre el Tajo.', []),
 ('5', 'info', 'USA Today', '20 de agosto', '{a} reconstruyen la búsqueda del avión perdido de Amelia Earhart.', ['Janet Loehrke', 'George Petras']),
 ('6', 'ilus', 'The New York Times', '22 de agosto', 'Ilustraciones de {a} sobre cómo ha crecido en altura el skyline de Miami.', ['Leo Dominguez']),
 ('7', 'port', 'The Boston Globe', '20 de agosto', 'Portada de la sección de libros con recomendaciones literarias para el otoño, con dibujo de {a}.', ['Andrew Rae']),
]

XCSS = """
.xhero{background:var(--accent);color:#fff;position:relative;overflow:hidden}
.xhero::before{content:"";position:absolute;left:-25%;top:-120%;width:150%;aspect-ratio:1;background:repeating-conic-gradient(rgba(255,212,0,.17) 0 5deg,transparent 5deg 15deg);animation:rays 90s linear infinite;pointer-events:none}
.xhero .inner{position:relative}
@keyframes rays{to{transform:rotate(360deg)}}
.xw span{display:inline-block;animation:xdrop .75s cubic-bezier(.2,1.5,.4,1) both,xwob 7s ease-in-out infinite}
.xw span:nth-child(1){animation-delay:0.00s,2.20s}
.xw span:nth-child(2){animation-delay:0.10s,2.29s}
.xw span:nth-child(3){animation-delay:0.20s,2.38s}
.xw span:nth-child(4){animation-delay:0.30s,2.47s}
.xw span:nth-child(5){animation-delay:0.40s,2.56s}
.xw span:nth-child(6){animation-delay:0.50s,2.65s}
@keyframes xdrop{from{transform:translateY(-130%) rotate(-14deg) scale(1.5);opacity:0}to{transform:none;opacity:1}}
@keyframes xwob{0%,84%,100%{transform:none}88%{transform:translateY(-18px) rotate(-5deg)}92%{transform:translateY(5px) rotate(2deg)}96%{transform:translateY(-3px)}}
.xnum{animation:xpop .6s cubic-bezier(.2,1.6,.4,1) .8s both}
@keyframes xpop{from{transform:scale(2.2) rotate(-10deg);opacity:0}to{transform:none;opacity:1}}
@media (prefers-reduced-motion:reduce){.xhero::before,.xw span,.xnum{animation:none}}

.xhero .inner{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:32px;padding:48px 24px 64px;align-items:end}
.xhero .l{grid-column:1/13;display:flex;flex-direction:column;gap:18px}
.xhero .r{grid-column:1/13;display:grid;grid-template-columns:auto minmax(0,1fr);gap:16px 40px;align-items:end;padding-top:8px}
.xhero .r .meta{grid-column:2}
.xw{font-weight:900;font-stretch:62%;font-size:clamp(120px,19vw,300px);line-height:.78;text-transform:uppercase;color:var(--ink);transform:skew(-6deg) rotate(-3deg);text-shadow:8px 8px 0 var(--yellow);white-space:nowrap;margin:10px 0 0 -6px}
.xnum{font-family:'Fraunces',serif;font-weight:900;font-variation-settings:'opsz' 144;font-size:clamp(70px,9vw,140px);line-height:.8;color:transparent;-webkit-text-stroke:2.5px #fff}
.xhero p{margin:0;font-family:'Fraunces',serif;font-size:22px;line-height:1.45}
.xhero .meta{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:13px;font-weight:800;letter-spacing:2px;text-transform:uppercase;border-top:1px solid #fff;padding-top:12px}
.gal{padding:64px 0 24px}
.gal-head{display:flex;justify-content:space-between;align-items:baseline;border-top:2px solid var(--ink);padding-top:12px;margin-bottom:28px}
.masonry{columns:4 240px;column-gap:22px}
.masonry .fr{min-height:200px;break-inside:avoid;margin:0 0 22px;background:#fff;padding:8px;box-shadow:6px 6px 0 var(--ink);display:block;width:100%;border:0;cursor:zoom-in;font:inherit;text-align:left;transition:transform .2s,box-shadow .2s}
.masonry .fr:nth-child(odd){transform:rotate(-1deg)}.masonry .fr:nth-child(even){transform:rotate(1deg)}
.masonry .fr:hover{transform:rotate(0) translateY(-3px);box-shadow:6px 6px 0 var(--accent)}
.masonry img{display:block;width:100%;height:auto;min-height:160px;background:#DAD4C6 radial-gradient(#16140F 1.1px,transparent 1.3px) 0 0/7px 7px}
.masonry .n{display:block;padding-top:8px;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase}
.idx{padding:40px 0 72px}
.idx ol{list-style:none;margin:0;padding:0;border-top:2px solid var(--ink)}
.idx li{display:grid;grid-template-columns:110px minmax(0,1fr) 84px;gap:24px;align-items:center;padding:26px 0;border-bottom:1px solid #C9C4B8}
.idx .k-n{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-size:64px;line-height:1;color:var(--accent)}
.idx .md{font-size:13px;font-weight:800;letter-spacing:2px;text-transform:uppercase;display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.idx .md-a{display:inline-flex;align-items:center;gap:9px}
.idx .md .av{width:36px;height:36px;flex-shrink:0;outline:1px dashed #B9B2A3;display:inline-flex;align-items:center;justify-content:center;font-size:8px;letter-spacing:0;color:var(--muted)}
.idx .md .av img{width:100%;height:100%;object-fit:contain}
.idx .md .av:has(img){outline:0}
.idx .md a{border-bottom:2px solid var(--accent)}
.idx .tx{font-family:'Fraunces',serif;font-size:22px;line-height:1.45;margin-top:6px}
.idx .tx a{font-style:italic;border-bottom:1px solid var(--accent)}
.idx svg{width:72px;height:72px}
.prev{padding:0 0 72px}
.prev-row{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px}
.prev-row a{border:2px solid var(--ink);padding:10px 14px;font-size:14px;font-weight:700;min-height:44px;display:inline-flex;align-items:center}
.prev-row a.cur{background:var(--accent);border-color:var(--accent);color:#fff}
.prev-row a.yr{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-size:20px}
.endrow{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:36px;padding:0 0 96px}
@media (max-width:860px){
.xhero .inner{display:flex;flex-direction:column;align-items:stretch}
.xhero .r{grid-template-columns:1fr}.xhero .r .meta{grid-column:1}
.idx li{grid-template-columns:64px minmax(0,1fr);}
.idx li svg{display:none}
.idx .k-n{font-size:44px}
}
"""

from medios_assets import avatar as m_avatar

def item_html(n, tipo, medio, fecha, txt, autores):
    a = ' y '.join(f'<a href="#">{e(x)}</a>' for x in autores)
    t = e(txt).replace('{a}', a)
    return (f'<li><span class="k-n">[{n}]</span><div><span class="md"><a href="#" class="md-a">{(f'<span class="av" aria-hidden="true"><img src="{m_avatar(medio)}" alt=""></span>' if m_avatar(medio) else '')}{e(medio)}</a> · {e(fecha)}</span>'
            f'<div class="tx">{t}</div></div>{icon(tipo)}</li>')

def page():
    IMG_ITEM = [0, 1, 2, 3, 4, 5, 6]
    def plain(it):
        n, tipo, medio, fecha, txt, autores = it
        return txt.replace('{a}', ' y '.join(autores))
    frames = ''.join(f'<button type="button" class="fr" data-lb="{i}" aria-label="Ampliar: [{ITEMS[IMG_ITEM[i]][0]}] {e(ITEMS[IMG_ITEM[i]][2])}"><img loading="lazy" src="{u}" alt="[{ITEMS[IMG_ITEM[i]][0]}] {e(ITEMS[IMG_ITEM[i]][2])}" onerror="this.remove()"><span class="n"><span style="color:var(--accent)">[{ITEMS[IMG_ITEM[i]][0]}]</span> {e(ITEMS[IMG_ITEM[i]][2])}</span></button>' for i, u in enumerate(IMGS))
    lb = json.dumps([{'src': u, 'cap': f"[{ITEMS[IMG_ITEM[i]][0]}] {ITEMS[IMG_ITEM[i]][2]} · {ITEMS[IMG_ITEM[i]][3]} · imagen {i+1} de {len(IMGS)}", 'txt': plain(ITEMS[IMG_ITEM[i]])} for i, u in enumerate(IMGS)], ensure_ascii=False)
    years = ''.join(f'<a class="yr" href="#">{y}</a>' for y in range(2025, 2014, -1))
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EXTRA! nº 131 · inconsolata» (maqueta)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1;1,9..144,100..900,0..100,0..1&display=swap">
<style>{CSS}{HEAD_CSS}{MINI_CSS}{TEMAS_CSS}{I18N_CSS}{LEGACY_CSS}{XCSS}{LB_CSS}</style>
</head>
<body>
<div class="page">
{head_interior()}
<div class="wrap" style="padding-top:16px;padding-bottom:16px">{LEGACY}</div>
<section class="xhero"><div class="wrap inner">
<div class="l">
<div class="crumbs caps" style="padding:0"><a href="inconsolata-portada.html" style="color:#fff">Portada</a><i style="color:var(--yellow)">»</i><a href="#" style="color:#fff">EXTRA!</a></div>
<h1 class="xw" aria-label="EXTRA! número 131"><span aria-hidden="true">E</span><span aria-hidden="true">x</span><span aria-hidden="true">t</span><span aria-hidden="true">r</span><span aria-hidden="true">a</span><span aria-hidden="true">!</span></h1>
</div>
<div class="r">
<span class="xnum">nº 131</span>
<p>EXTRA! es una sección mensual que recopila los mejores diseños en las páginas de la prensa nacional e internacional que no han pasado antes por el blog. Esta es la selección de agosto.</p>
<div class="meta"><span>Agosto de 2026</span><span>7 piezas</span><span>7 medios</span></div>
</div>
</div></section>
<main class="wrap">
<section class="gal">
<div class="gal-head"><span class="caps">Las páginas · {len(IMGS)}</span><span style="font-size:13px;font-weight:600">Pulsa para ampliar »</span></div>
<div class="masonry">{frames}</div>
</section>
<section class="idx">
<div class="caps" style="margin-bottom:14px">En este EXTRA! »</div>
<ol>{''.join(item_html(*it) for it in ITEMS)}</ol>
</section>
<section class="prev">
<div class="caps" style="border-top:2px solid var(--ink);padding-top:12px">EXTRA! anteriores »</div>
<div class="prev-row"><a class="cur" href="#">nº 131 · agosto</a><a href="#">nº 130 · julio</a><a href="#">nº 129 · junio</a><a href="#">nº 128 · mayo</a><a href="#">[…]</a></div>
<div class="prev-row">{years}</div>
</section>
<div class="endrow">
<div style="display:flex;flex-direction:column;gap:10px"><span class="caps">Compartir</span>
<div class="share"><a href="#">Bluesky</a><a href="#">X</a><a href="#">Reblog</a><button type="button">Copiar enlace</button></div></div>
<a href="https://buymeacoffee.com/saulcastillo" class="support"><span class="soft" style="font-size:30px;line-height:1">¿Te gusta lo que hago?</span><span style="font-size:15px;line-height:1.4">Si quieres ayudarme, puedes hacerlo con una aportación.</span><span class="caps">Apóyanos »</span></a>
</div>
</main>
<footer>
<div class="cmyk-bar" aria-hidden="true"><span style="background:#00A0DC"></span><span style="background:#66C6EA"></span><span style="background:#E5007E"></span><span style="background:#EF66B2"></span><span style="background:#FFD400"></span><span style="background:#FFE566"></span><span style="background:#16140F"></span><span style="background:#7A766C"></span></div>
<div class="wrap foot"><span class="soft" style="font-size:56px;line-height:1">inc<span style="color:#D1006F">»</span></span><span>© inconsolata» 2011–2026 · un blog de Saúl Castillo</span></div>
</footer>
</div>
{LB_HTML}
<script>{LB_JS}
initLB({lb});
</script>
{MINI_JS}
{I18N_JS}
</body>
</html>
"""

with open(os.path.join(OUT, 'post-extra.html'), 'w') as f:
    f.write(page())
print('ok')
