import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from posts import CSS, OUT
from common import head_interior, HEAD_CSS, MINI_CSS, MINI_JS, TEMAS_CSS, ESPIRAL_COLOR, I18N_CSS, I18N_JS
from lightbox import LB_CSS, LB_HTML, LB_JS
import json

MCSS = """
.mhead{padding:10px 0 40px;border-bottom:2px solid var(--ink)}
.badge{display:inline-block;background:var(--ink);color:var(--yellow);padding:6px 10px;font-size:13px;font-weight:800;letter-spacing:2px;text-transform:uppercase}
.mhead h1{margin:22px 0 26px;font-size:clamp(64px,10.5vw,170px);line-height:.86;letter-spacing:-.035em}
.mhead h1 .inc{color:var(--ink)}
.mhead h1 .inc span{color:var(--accent)}
.byline{display:flex;flex-wrap:wrap;gap:8px 22px;align-items:center;font-size:14px;font-weight:700;letter-spacing:1px;text-transform:uppercase}
.byline .who{display:flex;align-items:center;gap:10px}
.byline .who svg{width:40px;height:40px}
.art{position:relative;padding:56px 0 40px}
.toc{position:absolute;left:0;top:56px;width:230px;height:calc(100% - 96px)}
.toc nav{position:sticky;top:24px;display:flex;flex-direction:column;gap:2px;border-top:2px solid var(--ink);padding-top:12px}
.toc a{font-family:'Fraunces',serif;font-size:17px;padding:6px 0;display:flex;gap:8px}
.toc a i{font-style:normal;color:var(--accent);font-family:'Archivo',sans-serif;font-weight:800}
.col{max-width:720px;margin:0 0 0 320px;font-family:'Fraunces',serif;font-variation-settings:'opsz' 24;font-size:22px;line-height:1.6}
.col p{margin:0 0 26px}
.lead{font-size:31px;line-height:1.35;font-style:italic;font-variation-settings:'opsz' 72;margin-bottom:40px!important}
.lead::first-letter{font-style:normal}
.col .cap{float:left;font-weight:900;font-style:italic;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-size:118px;line-height:.78;padding:8px 12px 0 0;color:var(--accent)}
.col h2{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-size:46px;line-height:1;margin:64px 0 22px;scroll-margin-top:24px}
.col h2 i{font-style:normal;color:var(--accent);margin-right:8px}
.col a{border-bottom:2px solid var(--accent);font-weight:600}
.col strong{font-weight:800;background:linear-gradient(transparent 62%,rgba(255,212,0,.75) 0)}
.note{float:left;clear:left;width:240px;margin:6px 0 20px -320px;background:var(--yellow);padding:16px 16px 18px;font-family:'Archivo',sans-serif;font-size:15px;line-height:1.45;transform:rotate(-1.5deg);box-shadow:4px 4px 0 var(--ink)}
.note b{display:block;font-size:12px;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:6px}
.pull{margin:56px 0 56px -320px;width:calc(100% + 320px + 120px);background:var(--accent);color:#fff;padding:44px 48px;transform:rotate(-1deg);box-shadow:10px 10px 0 var(--ink)}
.pull p{margin:0!important;font-style:italic;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-size:clamp(36px,4.4vw,64px);line-height:1.02;letter-spacing:-.01em}
.pull span{display:block;margin-top:16px;font-family:'Archivo',sans-serif;font-size:13px;font-weight:800;letter-spacing:2px;text-transform:uppercase}
.nums{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:2px;background:var(--ink);border:2px solid var(--ink);margin:40px 0 44px}
.nums div{background:var(--paper);padding:20px 16px;display:flex;flex-direction:column;gap:6px}
.nums b{font-style:italic;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-size:52px;line-height:1;color:var(--accent)}
.nums span{font-family:'Archivo',sans-serif;font-size:12px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase}
.secs{list-style:none;padding:0;margin:8px 0 34px;display:flex;flex-direction:column;border-top:2px solid var(--ink)}
.secs li{display:grid;grid-template-columns:200px minmax(0,1fr);gap:18px;padding:16px 0;border-bottom:1px solid #C9C4B8;align-items:baseline}
.secs .n{font-style:italic;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-size:30px;line-height:1}
.secs .d{font-size:19px;line-height:1.45}
.secs .when{display:block;font-family:'Archivo',sans-serif;font-size:12px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--accent);margin-top:4px}
.ul{margin:0 0 30px;padding:0;list-style:none}
.ul li{padding-left:34px;position:relative;margin-bottom:12px}
.ul li::before{content:"»";position:absolute;left:0;top:-2px;color:var(--accent);font-weight:900;font-size:26px}
.sign{display:flex;align-items:center;gap:18px;margin:48px 0 0;padding-top:28px;border-top:2px solid var(--ink)}
.sign .s{font-style:italic;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-size:56px;line-height:1}
.sign small{display:block;font-family:'Archivo',sans-serif;font-size:13px;font-weight:700;letter-spacing:1px;text-transform:uppercase;margin-top:6px}
.endrow{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:36px;margin:56px 0 96px 320px;max-width:860px}
.draft{background:var(--ink);color:var(--paper);font-size:13px;font-weight:700;letter-spacing:.5px;padding:10px 24px;text-align:center}
.fshot{display:block;width:100%;padding:0;border:0;background:#fff radial-gradient(#16140F 1.1px,transparent 1.3px) 0 0/7px 7px;cursor:zoom-in;font:inherit}
.fshot img{display:block;width:100%;height:100%;object-fit:cover;object-position:top}
figure{margin:0}
figcaption{font-family:'Archivo',sans-serif;font-size:14px;font-weight:600;line-height:1.45;margin-top:14px;color:var(--ink)}
figcaption i{font-style:normal;color:var(--accent);font-weight:900}
.hero-fig{padding:56px 0 8px}
.desk{position:relative;height:clamp(300px,36vw,520px)}
.desk .fshot{position:absolute;height:88%;border:8px solid #fff;box-shadow:8px 8px 0 var(--ink);transition:transform .2s}
.desk .fshot:hover{z-index:5}
.pair{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;margin:36px 0 40px}
.pair .fshot{height:360px;border:8px solid #fff;box-shadow:6px 6px 0 var(--ink)}
.pair .fshot:first-child{transform:rotate(-1.5deg)}.pair .fshot:nth-child(2){transform:rotate(1.5deg)}
.pair figcaption{grid-column:1/-1}
.wide{margin:48px -120px 40px 0}
.wide .fshot{min-height:320px;height:auto;border:10px solid #fff;box-shadow:10px 10px 0 var(--ink)}
.wide .fshot img{height:auto}
.side-fig{float:right;width:250px;margin:0 -140px 20px 30px;transform:rotate(2deg)}
.side-fig .fshot{height:320px;border:7px solid #fff;box-shadow:6px 6px 0 var(--ink)}
@media (max-width:1100px){.wide{margin:40px 0}.side-fig{float:none;width:auto;margin:20px 0;transform:none}.side-fig .fshot{height:360px}}
@media (max-width:700px){.desk .fshot{border-width:4px}.pair .fshot{height:220px}}

@media (max-width:1100px){
.toc{display:none}
.col{margin:0 auto}
.note{float:none;width:auto;margin:10px 0 26px;transform:none}
.pull{margin:44px -8px;width:auto;transform:none}
.endrow{margin:48px auto 80px}
}
@media (max-width:700px){
.col{font-size:20px}
.lead{font-size:25px}
.nums{grid-template-columns:repeat(2,minmax(0,1fr))}
.secs li{grid-template-columns:1fr;gap:6px}
}
"""

LBLIST = '[{"src": "https://64.media.tumblr.com/093da2d5a18de7d40895b9ad174fe7ed/dfb73906028a5e2a-ea/s1280x1920/a1ccf50f328829da941a6c0a54c285506f0887c7.jpg", "cap": "Libération"}, {"src": "https://64.media.tumblr.com/d45665cf3bf8a089b877c8659c6b1f92/e00400f802d09bd6-18/s2048x3072/7be4cfc1dad9659582edb25ba488264d5e446f79.jpg", "cap": "The Observer"}, {"src": "https://64.media.tumblr.com/f8c5b539d68801d029de510e9e0cac9d/a9aec96b22ed4747-26/s2048x3072/8c314d152908f71319d9455520387cb70d54dae9.jpg", "cap": "The Boston Globe"}, {"src": "https://64.media.tumblr.com/94a4148f19d00aae057d05648da9129b/b61ba2d1d5d93a7d-7b/s1280x1920/9db7f5a9603f595c8fb5b13ce8f64f70ac97d016.png", "cap": "La Razón"}, {"src": "https://64.media.tumblr.com/093da2d5a18de7d40895b9ad174fe7ed/dfb73906028a5e2a-ea/s1280x1920/a1ccf50f328829da941a6c0a54c285506f0887c7.jpg", "cap": "Libération"}, {"src": "https://64.media.tumblr.com/1cca87a25ea2e74463f11df61a404519/7302b4dec07e85a6-f5/s1280x1920/5b35b7bbcc9a36f269ace91534ef2739a4e66c8d.png", "cap": "The Economist"}, {"src": "https://64.media.tumblr.com/60492347ef3173ed38fbb11a59f54995/0a4967b287ac3b00-2a/s1280x1920/93bde935c18cb437ad45ce95977d01ee23b6492b.jpg", "cap": "The Observer, en «mucho más» DCCLXXXI"}, {"src": "https://64.media.tumblr.com/019dd6d5f646d96915f9ecd84f2c1508/eccad2effd90fb88-99/s1280x1920/7cd945d0e148e5bcd0a2fbe680cf54b944f449dd.png", "cap": "EXTRA! nº 131"}]'

def page():
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bienvenido al nuevo inc» · metablog · inconsolata» (maqueta)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1;1,9..144,100..900,0..100,0..1&display=swap">
<style>{CSS}{HEAD_CSS}{MINI_CSS}{TEMAS_CSS}{I18N_CSS}{MCSS}{LB_CSS}</style>
</head>
<body>
<div class="page">
<div class="draft">Maqueta · texto de ejemplo escrito para enseñar el formato, no definitivo</div>
{head_interior()}
<main class="wrap">
<div class="crumbs caps"><a href="inconsolata-portada.html">Portada</a><i>»</i><a href="post-metablog.html">metablog</a></div>
<header class="mhead">
<span class="badge">metablog</span>
<h1 class="soft">Bienvenido al nuevo <span class="inc">inc<span>»</span></span></h1>
<div class="byline">
<span>por Saúl Castillo</span>
<span>23 de octubre de 2026</span>
<span>5 minutos de lectura</span>
</div>
</header>

<figure class="hero-fig"><div class="desk"><button type="button" class="fshot" data-lb="0" aria-label="Ampliar: Libération" style="left:0;top:30px;width:30%;transform:rotate(-4deg)"><img loading="lazy" src="https://64.media.tumblr.com/093da2d5a18de7d40895b9ad174fe7ed/dfb73906028a5e2a-ea/s1280x1920/a1ccf50f328829da941a6c0a54c285506f0887c7.jpg" alt="Libération" onerror="this.remove()"></button><button type="button" class="fshot" data-lb="1" aria-label="Ampliar: The Observer" style="left:24%;top:0;width:28%;transform:rotate(3deg);z-index:2"><img loading="lazy" src="https://64.media.tumblr.com/d45665cf3bf8a089b877c8659c6b1f92/e00400f802d09bd6-18/s2048x3072/7be4cfc1dad9659582edb25ba488264d5e446f79.jpg" alt="The Observer" onerror="this.remove()"></button><button type="button" class="fshot" data-lb="2" aria-label="Ampliar: The Boston Globe" style="left:49%;top:46px;width:27%;transform:rotate(-2deg)"><img loading="lazy" src="https://64.media.tumblr.com/f8c5b539d68801d029de510e9e0cac9d/a9aec96b22ed4747-26/s2048x3072/8c314d152908f71319d9455520387cb70d54dae9.jpg" alt="The Boston Globe" onerror="this.remove()"></button><button type="button" class="fshot" data-lb="3" aria-label="Ampliar: La Razón" style="left:72%;top:10px;width:27%;transform:rotate(5deg);z-index:2"><img loading="lazy" src="https://64.media.tumblr.com/94a4148f19d00aae057d05648da9129b/b61ba2d1d5d93a7d-7b/s1280x1920/9db7f5a9603f595c8fb5b13ce8f64f70ac97d016.png" alt="La Razón" onerror="this.remove()"></button></div><figcaption><i>»</i> Algunas de las páginas que han pasado por aquí este otoño.</figcaption></figure>

<article class="art">
<aside class="toc" aria-label="En este post">
<nav>
<span class="caps" style="margin-bottom:6px">En este post</span>
<a href="#porque"><i>»</i>Por qué ahora</a>
<a href="#cambia"><i>»</i>Qué cambia</a>
<a href="#secciones"><i>»</i>Las secciones</a>
<a href="#igual"><i>»</i>Lo que no cambia</a>
<a href="#tu"><i>»</i>Y ahora, tú</a>
</nav>
</aside>

<div class="col">
<p class="lead">Quince años después de aquel primer post, inconsolata» estrena casa. Misma dirección, mismo Tumblr y las mismas ganas de enseñarte las mejores páginas de la prensa de todo el mundo, pero con otra forma de mirarlas.</p>

<h2 id="porque"><i>»</i>Por qué ahora</h2>
<p><span class="cap">E</span>l tema que vestía esta web llevaba conmigo casi desde el principio. Le tengo cariño, pero se le notaban los años: botones para compartir en redes que ya no existen, textos en inglés que nunca traduje y, sobre todo, una manera de enseñar las cosas que no hacía justicia a lo que publicamos aquí. Un post detrás de otro, en una columna infinita, como si una portada de Libération y un minigráfico de The Economist pesaran lo mismo.</p>
<aside class="note"><b>Nota al margen</b>Esta es una nota al margen: sirve para aclaraciones, enlaces o chascarrillos sin cortar el texto.</aside>
<figure class="pair"><button type="button" class="fshot" data-lb="4" aria-label="Ampliar: Libération"><img loading="lazy" src="https://64.media.tumblr.com/093da2d5a18de7d40895b9ad174fe7ed/dfb73906028a5e2a-ea/s1280x1920/a1ccf50f328829da941a6c0a54c285506f0887c7.jpg" alt="Libération" onerror="this.remove()"></button><button type="button" class="fshot" data-lb="5" aria-label="Ampliar: The Economist"><img loading="lazy" src="https://64.media.tumblr.com/1cca87a25ea2e74463f11df61a404519/7302b4dec07e85a6-f5/s1280x1920/5b35b7bbcc9a36f269ace91534ef2739a4e66c8d.png" alt="The Economist" onerror="this.remove()"></button><figcaption><i>»</i> ¿Pesan lo mismo una portada de Libération y un minigráfico de The Economist? En el diseño antiguo, sí.</figcaption></figure>
<p>Y luego está el archivo. Quince años dan para <strong>miles de entradas</strong>, cientos de medios y muchísimos nombres propios de infografistas, ilustradores y diseñadores que merecen que se les pueda encontrar.</p>

<div class="nums" role="list">
<div role="listitem"><b>XVI</b><span>años en marcha</span></div>
<div role="listitem"><b>[n]</b><span>entradas</span></div>
<div role="listitem"><b>[n]</b><span>medios</span></div>
<div role="listitem"><b>[n]</b><span>autores</span></div>
</div>

<h2 id="cambia"><i>»</i>Qué cambia</h2>
<p>La portada ahora se parece más a una mesa de redacción que a un tablón: recortes, hojas sueltas y una apertura grande para lo que más merece la pena de cada semana. Además:</p>
<ul class="ul">
<li>Cada pieza lleva un <strong>icono según su tipo</strong>: infografía, cartografía, portada, gráfico, ilustración, fotografía, vídeo, publicidad u online.</li>
<li>Los medios y los autores tienen ahora su <strong>propia ficha</strong>, con todo lo que han aparecido por aquí.</li>
<li>Hay un <strong>buscador</strong> de verdad, para encontrar cualquier autor, tema o medio de estos quince años.</li>
<li>Las imágenes se amplían en un visor propio, para leer hasta la letra más pequeña de las infografías.</li>
</ul>

<figure class="wide"><button type="button" class="fshot" data-lb="6" aria-label="Ampliar: The Observer, en «mucho más» DCCLXXXI"><img loading="lazy" src="https://64.media.tumblr.com/60492347ef3173ed38fbb11a59f54995/0a4967b287ac3b00-2a/s1280x1920/93bde935c18cb437ad45ce95977d01ee23b6492b.jpg" alt="The Observer, en «mucho más» DCCLXXXI" onerror="this.remove()"></button><figcaption><i>»</i> Una de las quince piezas del último «mucho más»: las infraestructuras clave del Reino Unido, en The Observer.</figcaption></figure>

<div class="pull"><p>«Quince años de archivo merecían algo más que un scroll infinito.»</p><span>— el que suscribe</span></div>

<h2 id="secciones"><i>»</i>Las secciones de siempre (y alguna más)</h2>
<figure class="side-fig"><button type="button" class="fshot" data-lb="7" aria-label="Ampliar: EXTRA! nº 131"><img loading="lazy" src="https://64.media.tumblr.com/019dd6d5f646d96915f9ecd84f2c1508/eccad2effd90fb88-99/s1280x1920/7cd945d0e148e5bcd0a2fbe680cf54b944f449dd.png" alt="EXTRA! nº 131" onerror="this.remove()"></button><figcaption><i>»</i> EXTRA! nº 131, lo mejor de agosto.</figcaption></figure>
<ul class="secs">
<li><span class="n">mucho más</span><span class="d">El repaso a las mejores infografías de la semana en la prensa nacional e internacional.<span class="when">Cada domingo</span></span></li>
<li><span class="n">EXTRA!</span><span class="d">Una sección mensual que recopila los mejores diseños en las páginas de la prensa nacional e internacional que no han pasado antes por el blog.<span class="when">Una vez al mes</span></span></li>
<li><span class="n">detallitos</span><span class="d">Recortes de prensa pequeños, de esos que se escapan si no miras con atención.</span></li>
<li><span class="n">metablog</span><span class="d">Lo que pasa entre bambalinas de inconsolata», como este mismo post.</span></li>
<li><span class="n">offtopic</span><span class="d">Todo lo que no cabe en las demás.</span></li>
</ul>

<h2 id="igual"><i>»</i>Lo que no cambia</h2>
<p>Todo lo demás. Las direcciones de los posts de siempre siguen funcionando, así que ningún enlace que hayas guardado en estos años se rompe. Y yo sigo publicando igual que siempre: elegir, escanear, contarlo.</p>

<h2 id="tu"><i>»</i>Y ahora, tú</h2>
<p>Una renovación así nunca está terminada. Si algo no se ve bien, si echas de menos algo o si tienes una idea, <a href="mailto:inconsolataweb@gmail.com">escríbeme</a> o búscame en <a href="https://x.com/inconsolata">X</a>. Y si te gusta lo que hago, puedes ayudarme a que esto siga otros quince años.</p>

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
{LB_HTML}<script>{LB_JS}
initLB({LBLIST});</script>
{MINI_JS}
{I18N_JS}
</body>
</html>
"""

with open(os.path.join(OUT, 'post-metablog.html'), 'w') as f:
    f.write(page())
print('ok')
