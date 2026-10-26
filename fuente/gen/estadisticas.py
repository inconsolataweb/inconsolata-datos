"""Página de estadísticas del archivo (totales y por año).
Uso: python3 -I gen/estadisticas.py <scratchpad>
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from posts import CSS, OUT
from common import symbols, head_interior, HEAD_CSS, MINI_CSS, MINI_JS, TIPOS

S = sys.argv[1]
ST = open(os.path.join(S, 'data', 'stats.json')).read()
TN = json.dumps({k: v[0] for k, v in TIPOS.items()}, ensure_ascii=False)

SCSS = """
.hero{padding:30px 24px 22px}
.hero h1{margin:0;font-size:clamp(56px,9vw,140px);line-height:.88;letter-spacing:-.03em}
.hero h1 em{color:var(--accent)}
.hero p{font-family:'Fraunces',serif;font-style:italic;font-size:22px;margin:14px 0 0;max-width:760px}
.ybar{position:sticky;top:0;z-index:30;background:var(--paper);border-top:2px solid var(--ink);border-bottom:2px solid var(--ink);padding:10px 0}
.ybar .in{display:flex;gap:6px;overflow-x:auto;scrollbar-width:thin;padding-bottom:2px}
.ybar button{flex-shrink:0;border:2px solid var(--ink);background:transparent;font-family:'Fraunces',serif;font-style:italic;font-weight:700;font-size:17px;min-height:40px;padding:0 12px;cursor:pointer;color:var(--ink)}
.ybar button:hover{background:var(--yellow)}
.ybar button[aria-pressed=true]{background:var(--ink);color:var(--yellow)}
.kpis{background:var(--ink);color:var(--paper)}
.kpis .in{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));gap:26px;padding:34px 24px}
.kpi b{display:block;font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-size:clamp(48px,6vw,76px);line-height:1;color:var(--yellow)}
.kpi span{font-size:13px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase}
.kpi small{display:block;margin-top:4px;font-size:13px;color:#BDB7AA}
.blk{padding:48px 0 0}
.blk h2{margin:0 0 18px;font-size:clamp(34px,4vw,54px);line-height:.95;letter-spacing:-.02em;border-bottom:3px solid var(--ink);padding-bottom:10px}
.blk h2 em{color:var(--accent)}
.blk h2 small{font-family:'Archivo',sans-serif;font-style:normal;font-weight:700;font-size:13px;letter-spacing:1.5px;text-transform:uppercase;margin-left:10px;color:var(--muted)}
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,440px),1fr));gap:20px 56px}
.vbars{display:flex;align-items:flex-end;gap:6px;height:240px;padding-top:26px}
.vbars button{flex:1;position:relative;border:0;padding:0;background:var(--ink);border-radius:4px 4px 0 0;cursor:pointer;min-width:0}
.vbars button:hover{background:#4A463D}
.vbars button[aria-pressed=true]{background:var(--accent)}
.vbars button .v{position:absolute;bottom:100%;left:50%;transform:translateX(-50%);font-size:13px;font-weight:800;padding-bottom:4px;white-space:nowrap;display:none}
.vbars button[aria-pressed=true] .v{display:block;color:var(--accent)}
.vax{display:flex;gap:6px;border-top:2px solid var(--ink);padding-top:6px}
.vax span{flex:1;text-align:center;font-size:12px;font-weight:700;color:var(--muted)}
.hb{display:grid;grid-template-columns:minmax(0,190px) minmax(0,1fr) 46px;align-items:center;gap:4px 12px}
.hb a{font-family:'Fraunces',serif;font-weight:600;font-size:17px;line-height:1.2;padding:5px 0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.hb .tr{height:16px;position:relative}
.hb .tr i{position:absolute;left:0;top:0;bottom:0;background:var(--ink);border-radius:0 4px 4px 0;min-width:3px}
.hb .rw:hover i{background:var(--accent)}
.hb .rw{display:contents}
.hb .n{font-size:13px;font-weight:800;text-align:right;font-variant-numeric:tabular-nums}
.tipos-row{display:flex;gap:10px;overflow-x:auto;padding-bottom:6px}
.tp{flex:1 0 118px;border:2px solid var(--ink);background:#fff;padding:12px;display:flex;flex-direction:column;gap:6px}
.tp svg{width:40px;height:40px;overflow:visible}
.tp b{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-size:30px;line-height:1}
.tp span{font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase}
.tp i{display:block;height:6px;background:var(--accent);border-radius:0 3px 3px 0}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips a{border:2px solid var(--ink);border-radius:999px;padding:6px 14px;font-family:'Fraunces',serif;font-style:italic;font-weight:700;font-size:16px;min-height:38px;display:inline-flex;align-items:center;gap:8px;background:#fff}
.chips a small{font-family:'Archivo',sans-serif;font-style:normal;font-size:12px;font-weight:800;color:var(--accent)}
.chips a:hover{background:var(--yellow);color:var(--ink)}
.note{font-size:13px;color:var(--muted);margin:14px 0 0;max-width:760px;line-height:1.5}
#tip{position:fixed;pointer-events:none;background:var(--ink);color:var(--paper);font-size:13px;font-weight:700;padding:6px 10px;z-index:60;display:none;white-space:nowrap}
footer{background:var(--ink);color:var(--paper);margin-top:80px}
.cmyk-bar{display:flex;height:10px}.cmyk-bar span{flex:1}
.foot{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:12px;padding:26px 24px;font-size:13px}
@media (max-width:600px){.hb{grid-template-columns:minmax(0,130px) minmax(0,1fr) 40px}.hb a{font-size:15px}.vbars{height:180px}.vax span{font-size:10px}}
"""

JS = r"""
var ST = __ST__, TN = __TN__, Y = 'all';
var BUS = 'inconsolata-buscador.html#';
function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
function fmt(n) { return Number(n).toLocaleString('es-ES'); }
function ico(k) { return '<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#i-' + k + '" class="k"/></svg>'; }
var yb = '<button type="button" data-y="all">Todo el archivo</button>';
for (var y = 2026; y >= 2011; y--) yb += '<button type="button" data-y="' + y + '">' + y + '</button>';
document.getElementById('ybar').innerHTML = yb;
function hbars(id, rows, key) {
  var mx = rows.length ? rows[0][1] : 1;
  document.getElementById(id).innerHTML = rows.map(function (r) {
    var href = BUS + key + '=' + r[2] + (Y !== 'all' ? '&y=' + Y : '');
    return '<div class="rw" data-tip="' + esc(r[0]) + ': ' + fmt(r[1]) + ' entradas"><a href="' + href + '" title="' + esc(r[0]) + '">' + esc(r[0]) + '</a><div class="tr"><i style="width:' + (r[1] / mx * 100) + '%"></i></div><span class="n">' + fmt(r[1]) + '</span></div>';
  }).join('');
}
function chips(id, rows, key, unit) {
  document.getElementById(id).innerHTML = rows.map(function (r) {
    return '<a href="' + BUS + key + '=' + r[2] + '">' + esc(r[0]) + ' <small>' + r[1] + ' ' + unit + '</small></a>';
  }).join('') || '<p class="note">Ningún medio se estrenó ese año.</p>';
}
function render() {
  var d = Y === 'all' ? ST.total : ST.years[Y], T = ST.total;
  [].forEach.call(document.querySelectorAll('#ybar button'), function (b) { b.setAttribute('aria-pressed', b.dataset.y === String(Y)); });
  var lbl = Y === 'all' ? 'en 15 años de archivo' : 'en ' + Y + (Y === 2026 ? ' (hasta hoy)' : '');
  var prev = Y !== 'all' && ST.years[Y - 1] ? ST.years[Y - 1] : null;
  function diff(a, b) { if (!b) return ''; var x = a - b; return '<small>' + (x >= 0 ? '+' : '−') + fmt(Math.abs(x)) + ' respecto a ' + (Y - 1) + '</small>'; }
  document.getElementById('kpis').innerHTML =
    '<div class="kpi"><b>' + fmt(d.posts) + '</b><span>entradas ' + lbl + '</span>' + diff(d.posts, prev && prev.posts) + '</div>' +
    '<div class="kpi"><b>' + fmt(d.imgs) + '</b><span>imágenes</span>' + diff(d.imgs, prev && prev.imgs) + '</div>' +
    '<div class="kpi"><b>' + fmt(d.n_medios) + '</b><span>medios distintos</span>' + diff(d.n_medios, prev && prev.n_medios) + '</div>' +
    '<div class="kpi"><b>' + fmt(d.n_autores) + '</b><span>autores citados</span>' + diff(d.n_autores, prev && prev.n_autores) + '</div>';
  var h = '', ax = '', mx = Math.max.apply(null, Object.values(T.per_year));
  Object.keys(T.per_year).forEach(function (y) {
    var v = T.per_year[y];
    h += '<button type="button" data-y="' + y + '" aria-pressed="' + (String(Y) === y) + '" aria-label="' + y + ': ' + v + ' entradas" data-tip="' + y + ': ' + fmt(v) + ' entradas · ' + T.medios_year[y] + ' medios" style="height:' + (v / mx * 100) + '%"><span class="v">' + v + '</span></button>';
    ax += '<span>' + "'" + y.slice(2) + '</span>';
  });
  document.getElementById('vb').innerHTML = h; document.getElementById('vax').innerHTML = ax;
  document.querySelectorAll('.ylbl').forEach(function (e) { e.textContent = Y === 'all' ? 'todo el archivo' : Y; });
  hbars('hm', d.medios.slice(0, 20), 'm');
  hbars('ha', d.autores.slice(0, 15), 'a');
  hbars('ht', d.temas.slice(0, 12), 'h');
  var tmx = Math.max.apply(null, Object.values(d.tipos).concat([1]));
  document.getElementById('tp').innerHTML = ['info', 'carto', 'ilus', 'port', 'foto', 'publi', 'video', 'graf', 'online'].map(function (k) {
    var v = d.tipos[k] || 0;
    return '<a class="tp" href="' + BUS + 'k=' + k + (Y !== 'all' ? '&y=' + Y : '') + '">' + ico(k) + '<b>' + fmt(v) + '</b><span>' + TN[k] + '</span><i style="width:' + (v / tmx * 100) + '%"></i></a>';
  }).join('');
  var nv = document.getElementById('nv'), fi = document.getElementById('fi');
  if (Y === 'all') { nv.hidden = true; fi.hidden = false; chips('fic', T.fieles, 'm', 'años'); }
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
"""

page = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Estadísticas · inconsolata»</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1;1,9..144,100..900,0..100,0..1&display=swap">
<style>{CSS}{HEAD_CSS}{MINI_CSS}{SCSS}</style>
</head>
<body>
{symbols()}
<div class="page">
{head_interior()}
<main>
<section class="wrap hero">
<div class="crumbs caps" style="padding:0 0 14px"><a href="inconsolata-portada.html">Portada</a><i>»</i><a href="#">Medios</a><i>»</i><span>Estadísticas</span></div>
<h1 class="soft">Los <em>números</em> del archivo</h1>
<p>Qué medios, autores y temas han pasado por inconsolata» cada año desde 2011. Pulsa un año para ver solo ese año.</p>
</section>
<nav class="ybar" aria-label="Elegir año"><div class="wrap in" id="ybar"></div></nav>
<section class="kpis" aria-live="polite"><div class="wrap in" id="kpis"></div></section>
<div class="wrap">
<section class="blk"><h2 class="soft">Entradas <em>por año</em><small>pulsa una barra</small></h2>
<div class="vbars" id="vb"></div><div class="vax" id="vax"></div></section>
<div class="cols">
<section class="blk"><h2 class="soft">Medios <em>más presentes</em><small class="ylbl"></small></h2><div class="hb" id="hm"></div>
<p class="note">Número de entradas en las que aparece el medio. Un «mucho más» o un EXTRA! cuenta una vez por cada medio que incluye.</p></section>
<section class="blk"><h2 class="soft">Autores <em>más citados</em><small class="ylbl"></small></h2><div class="hb" id="ha"></div></section>
</div>
<section class="blk"><h2 class="soft">Tipos <em>de pieza</em><small class="ylbl"></small></h2><div class="tipos-row" id="tp"></div>
<p class="note">Gráfico y Online solo se cuentan en los posts publicados con el nuevo diseño.</p></section>
<div class="cols">
<section class="blk"><h2 class="soft">Temas<small class="ylbl"></small></h2><div class="hb" id="ht"></div></section>
<section class="blk" id="nv"><h2 class="soft">Se <em>estrenan</em><small>medios que aparecen por primera vez</small></h2><div class="chips" id="nvc"></div></section>
<section class="blk" id="fi"><h2 class="soft">Los <em>fieles</em><small>medios presentes más años</small></h2><div class="chips" id="fic"></div></section>
</div>
</div>
</main>
<footer>
<div class="cmyk-bar" aria-hidden="true"><span style="background:#00A0DC"></span><span style="background:#66C6EA"></span><span style="background:#E5007E"></span><span style="background:#EF66B2"></span><span style="background:#FFD400"></span><span style="background:#FFE566"></span><span style="background:#16140F"></span><span style="background:#7A766C"></span></div>
<div class="wrap foot"><span class="soft" style="font-size:56px;line-height:1">inc<span style="color:#D1006F">»</span></span><span>© inconsolata» 2011–2026 · un blog de Saúl Castillo</span></div>
</footer>
</div>
<div id="tip" role="presentation"></div>
<script>{JS.replace('__ST__', ST).replace('__TN__', TN)}</script>
{MINI_JS}
</body>
</html>
"""
open(os.path.join(OUT, 'inconsolata-estadisticas.html'), 'w').write(page)
print('ok', round(len(page.encode()) / 1e3), 'KB')
