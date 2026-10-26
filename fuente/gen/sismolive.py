import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from posts import CSS, OUT, T
from common import head_interior, HEAD_CSS, MINI_CSS, MINI_JS, TEMAS_CSS, ESPIRAL_COLOR, temas_html, I18N_CSS, I18N_JS, LEGACY, LEGACY_CSS
from lightbox import LB_CSS, LB_HTML, LB_JS
import metablog  # reutiliza los estilos del post de texto (MCSS)
MCSS = metablog.MCSS

IM = [
 ('347064713ce39bc8f64fb6d78fe035f4/039e04832269dcd6-b8/s1280x1920/39c0be6a2669b9cde1527ba6c603feb6e1032f73.jpg', 'SISMOLIVE: el mapa de la portada'),
 ('3842924c4d079eb8b1783cee46d662ce/039e04832269dcd6-b4/s1280x1920/a7c0204271f6d148cea34e8103083225f1182ca5.jpg', 'La página de un evento sísmico'),
 ('5f28c684db5bc32829592720316afad7/039e04832269dcd6-87/s1280x1920/1571551251da1057b4048288562eaac23ff47918.jpg', 'Los datos de USGS y EMSC'),
 ('d834c021cdd011472cabcbc1466c9d2d/039e04832269dcd6-21/s1280x1920/bb6ac43b9855536c3d9e5b7933305c4069d848a7.jpg', 'El sismógrafo'),
 ('a08595e95c3498fe58fbad1e20640b90/039e04832269dcd6-0d/s1280x1920/be918cf5f5448f3c8c5b61036532bd2591f52d0b.jpg', 'Estadísticas y comparativas'),
 ('cf188dbae0fefed13b114dc7dcf1472b/039e04832269dcd6-98/s1280x1920/370c499f46e393df1fad089851263877e1131135.jpg', 'Tierrita™'),
 ('65f02e94c11ead650f56b0f0a4489c2f/039e04832269dcd6-26/s1280x1920/1e455e8e59ad65d9035ed2112b1d74be66943206.jpg', 'Tierrita™ explica las magnitudes'),
]
IM = [(T + u, c) for u, c in IM]

def shot(i):
    u, c = IM[i]
    return f'<button type="button" class="fshot" data-lb="{i}" aria-label="Ampliar: {c}"><img loading="lazy" src="{u}" alt="{c}" onerror="this.remove()"></button>'

SCSS = """
.hero-one{padding:52px 0 10px}
.hero-one .fshot{height:auto;width:100%;border:12px solid #fff;box-shadow:12px 12px 0 var(--ink);transform:rotate(-.6deg);min-height:340px}
.hero-one .fshot img{height:auto}
.cta{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px;background:var(--ink);color:var(--paper);padding:26px 28px;margin:10px 0 36px;box-shadow:8px 8px 0 var(--accent);font-family:'Archivo',sans-serif}
.cta:hover{color:var(--yellow)}
.cta b{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-size:40px;line-height:1}
.cta span{font-size:13px;font-weight:800;letter-spacing:2px;text-transform:uppercase}
.badges{display:flex;gap:8px}
"""

def page():
    lb = json.dumps([{'src': u, 'cap': c} for u, c in IM], ensure_ascii=False)
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Presentamos SISMOLIVE · inconsolata» (maqueta)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1;1,9..144,100..900,0..100,0..1&display=swap">
<style>{CSS}{HEAD_CSS}{MINI_CSS}{TEMAS_CSS}{I18N_CSS}{LEGACY_CSS}{MCSS}{SCSS}{LB_CSS}</style>
</head>
<body>
<div class="page">
<div class="draft">Maqueta · textos resumidos a partir del post original, no definitivos</div>
{head_interior()}
<main class="wrap">
<div style="padding-top:20px">{LEGACY}</div>
<div class="crumbs caps"><a href="inconsolata-portada.html">Portada</a><i>»</i><a href="#">metablog</a></div>
<header class="mhead">
<div class="badges"><span class="badge">metablog</span><span class="badge">offtopic</span></div>
<h1 class="soft">Presentamos <span style="color:var(--accent)">SISMOLIVE</span></h1>
<div class="byline"><span>por Saúl Castillo</span><span>Octubre de 2026</span><span>4 minutos de lectura</span></div>
</header>

<figure class="hero-one">{shot(0)}<figcaption><i>»</i> La portada de SISMOLIVE: todos los terremotos del planeta, en directo.</figcaption></figure>

<article class="art">
<aside class="toc" aria-label="En este post">
<nav>
<span class="caps" style="margin-bottom:6px">En este post</span>
<a href="#mapa"><i>»</i>El mapa</a>
<a href="#eventos"><i>»</i>Cada terremoto, su página</a>
<a href="#datos"><i>»</i>De dónde salen los datos</a>
<a href="#dentro"><i>»</i>Todo lo que hay dentro</a>
<a href="#tierrita"><i>»</i>Tierrita™</a>
<a href="#ademas"><i>»</i>Y además</a>
</nav>
</aside>

<div class="col">
<p class="lead">Aprovecho el puente para presentarte SISMOLIVE, una de mis últimas locurillas: una herramienta web que visualiza en directo todos los terremotos que suceden en el planeta, recogiendo la información de agencias de fuente abierta.</p>

<a class="cta" href="https://sismolive.saulcastillo.es/" target="_blank" rel="noopener"><b>Entra en SISMOLIVE »</b><span>sismolive.saulcastillo.es</span></a>

<h2 id="mapa"><i>»</i>El mapa</h2>
<p><span class="cap">L</span>a portada es un mapa con los terremotos más recientes, acompañado de una barra lateral para ir recorriéndolos uno a uno. Pero es mucho más que un simple visualizador: es una plataforma llena de datos, detalles y frikadas.</p>

<h2 id="eventos"><i>»</i>Cada terremoto, su página</h2>
<p>Los sismos de magnitud 4 o superior se convierten en <strong>eventos</strong> con página propia, donde se reúne toda la información disponible sobre cada uno.</p>
<figure class="wide">{shot(1)}<figcaption><i>»</i> La página de un evento.</figcaption></figure>

<h2 id="datos"><i>»</i>De dónde salen los datos</h2>
<figure class="side-fig">{shot(2)}<figcaption><i>»</i> Las fuentes, siempre a la vista.</figcaption></figure>
<p>La información llega del <strong>USGS</strong> estadounidense y del <strong>EMSC</strong>, el Centro Sismológico Euromediterráneo. Todo se guarda en un archivo continuo que alimenta las estadísticas de la web.</p>
<aside class="note"><b>Nota al margen</b>Dos fuentes abiertas y un archivo que no para de crecer.</aside>

<div class="nums" role="list">
<div role="listitem"><b>M4+</b><span>eventos con página</span></div>
<div role="listitem"><b>2</b><span>fuentes abiertas</span></div>
<div role="listitem"><b>200+</b><span>terremotos históricos</span></div>
<div role="listitem"><b>ES·EN</b><span>idiomas</span></div>
</div>

<h2 id="dentro"><i>»</i>Todo lo que hay dentro</h2>
<ul class="ul">
<li>Seguimiento de los <strong>grandes terremotos</strong>.</li>
<li>Fichas de <strong>placas tectónicas</strong> y de países.</li>
<li>Un archivo de <strong>más de 200 terremotos históricos</strong>.</li>
<li>Informes diarios, un sismógrafo y comparativas por país y por año.</li>
</ul>
<figure class="pair">{shot(3)}{shot(4)}<figcaption><i>»</i> El sismógrafo y las comparativas.</figcaption></figure>

<div class="pull"><p>«Mucho más que un simple visualizador: una plataforma llena de datos, detalles y frikadas.»</p><span>— el que suscribe</span></div>

<h2 id="tierrita"><i>»</i>Tierrita™</h2>
<p>Y como toda web que se precie necesita una mascota, SISMOLIVE tiene la suya: <strong>Tierrita™</strong>, que se encarga de explicar qué significan las magnitudes.</p>
<figure class="pair">{shot(5)}{shot(6)}<figcaption><i>»</i> Tierrita™ en acción.</figcaption></figure>

<h2 id="ademas"><i>»</i>Y además</h2>
<ul class="ul">
<li>Una versión ligera para el móvil: <strong>SISMOLIVE LITE</strong>.</li>
<li>Un diseño especial cuando hay un terremoto de magnitud 6 o superior.</li>
<li>Interfaz en español y en inglés.</li>
<li>Y es gratis.</li>
</ul>
<p>Si tienes ideas o encuentras algún fallo, <a href="mailto:inconsolataweb@gmail.com">escríbeme</a> o búscame en <a href="https://x.com/saulcastillo">X</a>. Y si quieres apoyar el proyecto, puedes hacerlo <a href="https://buymeacoffee.com/saulcastillo">con una aportación</a>.</p>

<div style="margin-top:30px">{temas_html(['ciencia', 'terremotos', 'datos', 'proyectos'])}</div>

<div class="sign">{ESPIRAL_COLOR}<div><span class="s">Saúl Castillo</span><small>inconsolata» · <a href="https://saulcastillo.es">saulcastillo.es</a></small></div></div>
</div>
</article>

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

with open(os.path.join(OUT, 'post-sismolive.html'), 'w') as f:
    f.write(page())
print('ok')
