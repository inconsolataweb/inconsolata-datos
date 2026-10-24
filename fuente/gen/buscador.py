"""Buscador de inconsolata» con los datos reales del archivo.
Uso: python3 -I gen/buscador.py <scratchpad>
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from posts import CSS, OUT
from common import symbols, head_interior, HEAD_CSS, MINI_CSS, MINI_JS, TIPOS
from temas_iconos import slug, tema_symbols

S = sys.argv[1]
DATA = open(os.path.join(S, 'data', 'search.json')).read().replace('</', '<\\/')
TIPO_NAMES = json.dumps({k: v[0] for k, v in TIPOS.items()}, ensure_ascii=False)

BCSS = """
.hero{padding:34px 0 26px;border-bottom:2px solid var(--ink)}
.hero h1{margin:0 0 18px;font-size:clamp(46px,7vw,104px);line-height:.9;letter-spacing:-.03em}
.hero h1 em{color:var(--accent)}
.qbox{position:relative;max-width:980px}
.qrow{display:flex;align-items:center;border:3px solid var(--ink);background:#fff;box-shadow:8px 8px 0 var(--ink)}
.qrow svg{flex-shrink:0;margin:0 6px 0 18px}
#q{flex:1;min-width:0;border:0;background:transparent;font-family:'Fraunces',serif;font-style:italic;font-weight:700;font-size:clamp(22px,3vw,34px);padding:16px 10px;color:var(--ink);outline:none}
#q::placeholder{color:#8A857A}
#q::-webkit-search-cancel-button{-webkit-appearance:none;appearance:none}
.qrow:focus-within{outline:3px solid var(--accent);outline-offset:3px}
#qclear{border:0;background:transparent;font-size:28px;width:52px;height:52px;cursor:pointer;color:var(--muted)}
#qclear:hover{color:var(--accent)}
.sug{position:absolute;left:0;right:0;top:calc(100% + 12px);background:#fff;border:3px solid var(--ink);z-index:20;box-shadow:8px 8px 0 var(--accent);max-height:70vh;overflow:auto}
.sug h3{margin:0;padding:10px 16px 4px;font-size:11px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--muted)}
.sug button{display:flex;width:100%;align-items:baseline;gap:10px;border:0;background:transparent;text-align:left;padding:9px 16px;font:inherit;cursor:pointer;min-height:44px}
.sug button .nm{font-family:'Fraunces',serif;font-style:italic;font-weight:700;font-size:20px}
.sug button .ex{font-size:12px;color:var(--muted)}
.sug button .ct{margin-left:auto;font-size:12px;font-weight:800}
.sug button[aria-selected=true],.sug button:hover{background:var(--yellow)}
.sug .txt{border-top:2px solid var(--ink)}
.try{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:22px}
.try a,.chip{border:2px solid var(--ink);border-radius:999px;padding:6px 14px;font-family:'Fraunces',serif;font-style:italic;font-weight:700;font-size:16px;min-height:38px;display:inline-flex;align-items:center;gap:8px;background:var(--paper);cursor:pointer}
.try a:hover{background:var(--yellow);color:var(--ink)}

.body{display:grid;grid-template-columns:280px minmax(0,1fr);gap:40px;padding:30px 24px 70px}
.facets{display:flex;flex-direction:column;gap:28px;align-self:start;position:sticky;top:70px;max-height:calc(100vh - 80px);overflow:auto;padding-right:6px}
.fg h2{margin:0 0 10px;font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;border-bottom:2px solid var(--ink);padding-bottom:6px}
.fl{display:flex;flex-direction:column}
.fl button{display:flex;align-items:center;gap:8px;border:0;background:transparent;font:inherit;font-size:14px;font-weight:600;padding:5px 4px;min-height:34px;text-align:left;cursor:pointer;color:var(--ink)}
.fl button .ct{margin-left:auto;font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums}
.fl button:hover{background:rgba(255,212,0,.45)}
.fl button[aria-pressed=true]{background:var(--ink);color:var(--paper)}
.fl button[aria-pressed=true] .ct{color:var(--yellow)}
.fl button svg{width:26px;height:26px;flex-shrink:0}
.fl .vmore{font-size:12px;font-weight:800;color:var(--accent);letter-spacing:1px;text-transform:uppercase}
.years{display:flex;align-items:flex-end;gap:2px;height:90px}
.years button{flex:1;border:0;padding:0;background:var(--ink);cursor:pointer;min-width:0;position:relative}
.years button:hover{background:var(--accent)}
.years button[aria-pressed=true]{background:var(--accent)}
.years.has-sel button[aria-pressed=false]{opacity:.3}
.yl{display:flex;justify-content:space-between;font-size:11px;font-weight:700;margin-top:4px;color:var(--muted)}

.rhead{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;justify-content:space-between;margin-bottom:16px}
.count{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-size:34px;line-height:1}
.count small{font-family:'Archivo',sans-serif;font-style:normal;font-weight:700;font-size:13px;letter-spacing:1.5px;text-transform:uppercase;margin-left:6px}
.rhead select{min-height:40px;border:2px solid var(--ink);background:#fff;font:inherit;font-weight:700;padding:0 10px}
.active{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:18px}
.chip{background:var(--ink);color:var(--paper);border-color:var(--ink);font-size:15px}
.chip i{font-style:normal;font-family:'Archivo',sans-serif;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--yellow)}
.chip b{font-size:18px;line-height:1;color:var(--yellow)}
.chip:hover{background:var(--accent);border-color:var(--accent)}
.clearall{border:0;background:transparent;font:inherit;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--accent);cursor:pointer;min-height:38px}

.fx{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:24px;background:var(--ink);color:var(--paper);padding:24px 26px;margin-bottom:26px;box-shadow:8px 8px 0 var(--accent)}
.fx .kind{font-size:11px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--yellow)}
.fx h2{margin:6px 0 10px;font-size:clamp(36px,4.6vw,64px);line-height:.92;letter-spacing:-.02em}
.fx p{margin:0 0 6px;font-size:15px;line-height:1.5}
.fx p b{color:var(--yellow)}
.fx .rel{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.fx .rel button{border:2px solid var(--paper);background:transparent;color:var(--paper);border-radius:999px;padding:4px 12px;font-family:'Fraunces',serif;font-style:italic;font-size:15px;min-height:34px;cursor:pointer}
.fx .rel button:hover{background:var(--paper);color:var(--ink)}
.fx .go{display:inline-block;margin-top:14px;font-size:12px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--yellow);border-bottom:2px solid var(--yellow)}
.spark{display:flex;align-items:flex-end;gap:2px;height:110px;align-self:end}
.spark span{flex:1;background:var(--yellow);min-height:2px}
.spark-l{display:flex;justify-content:space-between;font-size:11px;font-weight:700;color:#BDB7AA;margin-top:4px}

.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:30px 24px}
.rc{display:flex;flex-direction:column;gap:8px;color:var(--ink);position:relative}
.rc .ph{position:relative;aspect-ratio:4/3;background:#fff radial-gradient(#16140F 1px,transparent 1.2px) 0 0/7px 7px;border:2px solid var(--ink);overflow:hidden;transition:transform .2s,box-shadow .2s}
.rc .ph img{width:100%;height:100%;object-fit:cover;object-position:top;display:block;background:#fff}
.rc:hover .ph{transform:translate(-3px,-3px);box-shadow:6px 6px 0 var(--accent)}
.rc .ico{position:absolute;left:8px;bottom:8px;display:flex;gap:4px}
.rc .ico span{width:34px;height:34px;background:var(--paper);border:2px solid var(--ink);display:flex;align-items:center;justify-content:center}
.rc .ico svg{width:22px;height:22px}
.rc .sec{position:absolute;top:8px;left:8px;background:var(--ink);color:var(--yellow);font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;padding:5px 8px}
.rc .sec.x{background:var(--accent);color:#fff}
.rc .n{position:absolute;top:8px;right:8px;background:rgba(22,20,15,.85);color:#fff;font-size:11px;font-weight:800;padding:4px 7px}
.rc .meta{font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--muted)}
.rc .meta b{color:var(--ink)}
.rc .tt{font-family:'Fraunces',serif;font-weight:600;font-size:18px;line-height:1.25;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.rc .by{font-size:13px;color:var(--muted);display:-webkit-box;-webkit-line-clamp:1;-webkit-box-orient:vertical;overflow:hidden}
.rc mark{background:var(--yellow);color:inherit}
.loadmore{display:block;margin:40px auto 0;border:3px solid var(--ink);background:var(--yellow);font:inherit;font-weight:800;font-size:14px;letter-spacing:1.5px;text-transform:uppercase;padding:14px 26px;min-height:48px;cursor:pointer;box-shadow:5px 5px 0 var(--ink)}
.loadmore:hover{background:var(--ink);color:var(--yellow)}
.empty{border:3px dashed var(--ink);padding:40px;text-align:center;font-family:'Fraunces',serif;font-style:italic;font-size:22px}
.ftoggle{display:none}
footer{background:var(--ink);color:var(--paper)}
.cmyk-bar{display:flex;height:10px}.cmyk-bar span{flex:1}
.foot{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:12px;padding:26px 24px;font-size:13px}
@media (max-width:900px){
 .body{grid-template-columns:1fr;gap:18px}
 .facets{position:static;max-height:none;display:none;border:2px solid var(--ink);padding:16px;background:#fff}
 .facets.open{display:flex}
 .ftoggle{display:inline-flex;align-items:center;border:2px solid var(--ink);background:#fff;font:inherit;font-weight:800;font-size:13px;letter-spacing:1px;text-transform:uppercase;padding:0 14px;min-height:42px;cursor:pointer}
 .fx{grid-template-columns:1fr}
 .grid{grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:22px 14px}
 .rc .tt{font-size:16px}
}
"""

JS = r"""
var D = __DATA__, TN = __TIPOS__, TS = __TS__;
var SECN = {m: 'Mucho más', x: 'EXTRA!', d: 'Detallitos', b: 'Metablog', o: 'Offtopic'};
var MESES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'];
function nz(s) { return String(s).toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '').replace(/ñ/g, 'n').replace(/[^a-z0-9ñ]+/g, ' ').trim(); }
function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]; }); }
var P = D.posts, Y0 = 2011, Y1 = 2026;
// pajar de búsqueda de cada post
D.autores.forEach(function (a) { a.k = nz([a.n].concat(a.v).join(' | ')); });
D.medios.forEach(function (m) { m.k = nz([m.n].concat(m.v).join(' | ')); });
D.temas.forEach(function (t) { t.k = nz(t.n); });
P.forEach(function (p) {
  p.y = +p.d.slice(0, 4);
  p.hay = ' ' + p.x + ' ' + p.m.map(function (i) { return D.medios[i].k; }).join(' ') + ' ' +
    p.a.map(function (i) { return D.autores[i].k; }).join(' ') + ' ' + p.h.map(function (i) { return D.temas[i].k; }).join(' ') + ' ' +
    p.k.map(function (k) { return nz(TN[k]); }).join(' ') + ' ' + (p.s ? nz(SECN[p.s]) : '') + ' ' + p.g.join(' ') + ' ';
});
var st = {q: '', k: [], s: [], y: [], m: [], a: [], h: [], o: 'new'}, shown = 36, res = [];

function readHash() {
  var h = location.hash.slice(1); if (!h) return;
  h.split('&').forEach(function (kv) {
    var i = kv.indexOf('='), k = kv.slice(0, i), v = decodeURIComponent(kv.slice(i + 1));
    if (k === 'q' || k === 'o') st[k] = v;
    else if (st[k]) st[k] = v.split('|').map(function (x) { return /^[amhy]$/.test(k) ? +x : x; });
  });
}
function writeHash() {
  var out = [];
  if (st.q) out.push('q=' + encodeURIComponent(st.q));
  ['k', 's', 'y', 'm', 'a', 'h'].forEach(function (k) { if (st[k].length) out.push(k + '=' + encodeURIComponent(st[k].join('|'))); });
  if (st.o !== 'new') out.push('o=' + st.o);
  history.replaceState(null, '', out.length ? '#' + out.join('&') : location.pathname);
}
function has(arr, v) { return arr.indexOf(v) >= 0; }
function match(p, skip) {
  if (skip !== 'k' && st.k.length && !st.k.some(function (k) { return has(p.k, k); })) return false;
  if (skip !== 's' && st.s.length && !st.s.some(function (s) { return s === 'n' ? !p.s : (p.s === s || has(p.g, s)); })) return false;
  if (skip !== 'y' && st.y.length && !has(st.y, p.y)) return false;
  if (skip !== 'm' && st.m.length && !st.m.some(function (i) { return has(p.m, i); })) return false;
  if (skip !== 'a' && st.a.length && !st.a.every(function (i) { return has(p.a, i); })) return false;
  if (skip !== 'h' && st.h.length && !st.h.every(function (i) { return has(p.h, i); })) return false;
  return true;
}
function toks() { return nz(st.q).split(' ').filter(function (t) { return t.length > 0; }); }
function textOk(p, T) { for (var i = 0; i < T.length; i++) if (p.hay.indexOf(T[i].length < 4 ? ' ' + T[i] : T[i]) < 0) return false; return true; }
function score(p, T) {
  var s = 0; T.forEach(function (t) { if ((' ' + nz(p.t + ' ' + p.b) + ' ').indexOf(' ' + t) >= 0) s += 3; if (p.hay.indexOf(' ' + t + ' ') >= 0) s += 1; }); return s;
}
function run() {
  var T = toks(), base = T.length ? P.filter(function (p) { return textOk(p, T); }) : P;
  res = base.filter(function (p) { return match(p); });
  if (st.o === 'old') res = res.slice().reverse();
  else if (st.o === 'rel' && T.length) res = res.map(function (p) { return [score(p, T), p]; }).sort(function (a, b) { return b[0] - a[0] || (a[1].d < b[1].d ? 1 : -1); }).map(function (x) { return x[1]; });
  shown = 36;
  facets(base, T); actives(); ficha(); render(); writeHash();
}
function cnt(base, key, getter) {
  var c = {}; base.forEach(function (p) { if (!match(p, key)) return; getter(p).forEach(function (v) { c[v] = (c[v] || 0) + 1; }); }); return c;
}
var openF = {};
function list(id, key, c, label, icon, limit) {
  var keys = Object.keys(c).sort(function (a, b) { return c[b] - c[a]; });
  st[key].forEach(function (v) { if (!(String(v) in c)) { c[v] = 0; keys.unshift(String(v)); } });
  var lim = openF[key] ? 60 : limit, el = document.getElementById(id);
  el.innerHTML = keys.slice(0, lim).map(function (v) {
    var vv = /^[amhy]$/.test(key) ? +v : v;
    return '<button type="button" data-k="' + key + '" data-v="' + esc(v) + '" aria-pressed="' + has(st[key], vv) + '">' + (icon ? icon(v) : '') + '<span>' + esc(label(v)) + '</span><span class="ct">' + c[v] + '</span></button>';
  }).join('') + (keys.length > limit ? '<button type="button" class="vmore" data-more="' + key + '">' + (openF[key] ? 'Ver menos' : 'Ver más (' + keys.length + ')') + '</button>' : '');
}
function ico(k) { return '<svg viewBox="0 0 64 64" aria-hidden="true" style="overflow:visible"><use href="#i-' + k + '"/></svg>'; }
function facets(base, T) {
  list('f-k', 'k', cnt(base, 'k', function (p) { return p.k; }), function (v) { return TN[v]; }, ico, 9);
  list('f-h', 'h', cnt(base, 'h', function (p) { return p.h; }), function (v) { return D.temas[v].n; }, function (v) { return '<svg viewBox="0 0 64 64" aria-hidden="true" style="overflow:visible"><use href="#' + TS[v] + '"/></svg>'; }, 10);
  list('f-m', 'm', cnt(base, 'm', function (p) { return p.m; }), function (v) { return D.medios[v].n; }, null, 10);
  list('f-a', 'a', cnt(base, 'a', function (p) { return p.a; }), function (v) { return D.autores[v].n; }, null, 10);
  var cy = cnt(base, 'y', function (p) { return [p.y]; }), mx = 1, h = '';
  for (var y = Y0; y <= Y1; y++) mx = Math.max(mx, cy[y] || 0);
  for (y = Y0; y <= Y1; y++) h += '<button type="button" data-k="y" data-v="' + y + '" aria-pressed="' + has(st.y, y) + '" title="' + y + ': ' + (cy[y] || 0) + ' entradas" aria-label="' + y + ', ' + (cy[y] || 0) + ' entradas" style="height:' + Math.max(3, (cy[y] || 0) / mx * 100) + '%"></button>';
  var ys = document.getElementById('f-y'); ys.innerHTML = h; ys.classList.toggle('has-sel', st.y.length > 0);
}
function nameOf(k, v) { return k === 'm' ? D.medios[v].n : k === 'a' ? D.autores[v].n : k === 'h' ? D.temas[v].n : k === 'k' ? TN[v] : k === 's' ? (SECN[v] || (v === 'n' ? 'Posts normales' : v)) : String(v); }
var KN = {k: 'Tipo', s: 'Sección', y: 'Año', m: 'Medio', a: 'Autor', h: 'Tema'};
function actives() {
  var h = '';
  if (st.q) h += '<button type="button" class="chip" data-rm="q"><i>Texto</i>«' + esc(st.q) + '» <b>×</b></button>';
  ['a', 'm', 'h', 'k', 's', 'y'].forEach(function (k) { st[k].forEach(function (v) { h += '<button type="button" class="chip" data-rm="' + k + '" data-v="' + esc(v) + '"><i>' + KN[k] + '</i>' + esc(nameOf(k, v)) + ' <b>×</b></button>'; }); });
  if (h) h += '<button type="button" class="clearall" data-rm="all">Borrar todo</button>';
  document.getElementById('active').innerHTML = h;
  var n = res.length;
  document.getElementById('count').innerHTML = n.toLocaleString('es-ES') + '<small>' + (n === 1 ? 'entrada' : 'entradas') + '</small>';
}
function yearsOf(list) { var c = {}; list.forEach(function (p) { c[p.y] = (c[p.y] || 0) + 1; }); return c; }
function spark(list) {
  var c = yearsOf(list), mx = 1, h = '';
  for (var y = Y0; y <= Y1; y++) mx = Math.max(mx, c[y] || 0);
  for (y = Y0; y <= Y1; y++) h += '<span title="' + y + ': ' + (c[y] || 0) + '" style="height:' + ((c[y] || 0) / mx * 100) + '%"></span>';
  return '<div><div class="spark">' + h + '</div><div class="spark-l"><span>' + Y0 + '</span><span>' + Y1 + '</span></div></div>';
}
function topRel(list, key, excl, n) {
  var c = {}; list.forEach(function (p) { p[key].forEach(function (v) { if (v !== excl) c[v] = (c[v] || 0) + 1; }); });
  return Object.keys(c).sort(function (a, b) { return c[b] - c[a]; }).slice(0, n).map(Number);
}
function relBtns(key, ids) { return ids.map(function (i) { return '<button type="button" data-add="' + key + '" data-v="' + i + '">' + esc(nameOf(key, i)) + '</button>'; }).join(''); }
function ficha() {
  var el = document.getElementById('ficha'), one = null;
  if (st.a.length === 1) one = ['a', st.a[0]]; else if (st.m.length === 1) one = ['m', st.m[0]]; else if (st.h.length === 1) one = ['h', st.h[0]];
  if (!one) { el.hidden = true; return; }
  var k = one[0], v = one[1], all = P.filter(function (p) { return has(p[k], v); }), html = '';
  var ys = all.map(function (p) { return p.y; }), y0 = Math.min.apply(null, ys), y1 = Math.max.apply(null, ys);
  if (k === 'a') {
    var a = D.autores[v];
    html = '<div><span class="kind">Autor</span><h2 class="soft">' + esc(a.n) + '</h2><p><b>' + all.length + '</b> entradas en inconsolata» · de ' + y0 + ' a ' + y1 + '</p>' +
      (a.m.length ? '<p>Trabaja en <b>' + a.m.map(esc).join(', ') + '</b></p>' : '') +
      (a.v.length ? '<p style="opacity:.7;font-size:13px">También aparece como: ' + a.v.map(esc).join(' · ') + '</p>' : '') +
      '<div class="rel">' + relBtns('h', topRel(all, 'h', -1, 5)) + '</div><a class="go" href="#">Ver ficha completa »</a></div>';
  } else if (k === 'm') {
    var m = D.medios[v];
    html = '<div><span class="kind">Medio' + (m.r ? ' · ' + esc(m.r) : '') + (m.x ? ' · ya no existe' : '') + '</span><h2 class="soft">' + esc(m.n) + '</h2><p><b>' + all.length + '</b> entradas en inconsolata» · de ' + y0 + ' a ' + y1 + '</p>' +
      '<p>Autores más presentes:</p><div class="rel">' + relBtns('a', topRel(all, 'a', -1, 6)) + '</div><a class="go" href="#">Ver ficha completa »</a></div>';
  } else {
    var t = D.temas[v];
    html = '<div><span class="kind">Tema · ' + esc(t.b) + '</span><h2 class="soft">' + esc(t.n) + '</h2><p><b>' + all.length + '</b> entradas en inconsolata» · de ' + y0 + ' a ' + y1 + '</p>' +
      '<p>Medios que más lo han tratado:</p><div class="rel">' + relBtns('m', topRel(all, 'm', -1, 6)) + '</div></div>';
  }
  el.innerHTML = html + spark(all); el.hidden = false;
}
function fdate(d) { return +d.slice(8, 10) + ' ' + MESES[+d.slice(5, 7) - 1] + ' ' + d.slice(0, 4); }
function hl(s, T) {
  s = esc(s); if (!T.length) return s;
  T.filter(function (t) { return t.length > 2; }).forEach(function (t) {
    var re = new RegExp('(' + t.split('').map(function (c) { return c.replace(/[a-z]/, function (l) { var m = {a: '[aáàä]', e: '[eéèë]', i: '[iíìï]', o: '[oóòö]', u: '[uúùü]', n: '[nñ]', c: '[cç]'}; return m[l] || l; }); }).join('') + ')', 'gi');
    s = s.replace(re, '<mark>$1</mark>');
  });
  return s;
}
function card(p, T) {
  var head = p.t || p.b || 'Entrada sin texto';
  var meds = p.m.slice(0, 2).map(function (i) { return D.medios[i].n; }).join(' · ');
  var auts = p.a.slice(0, 3).map(function (i) { return D.autores[i].n; });
  return '<a class="rc" href="https://inconsolata.com/post/' + esc(p.u) + '" target="_blank" rel="noopener"><div class="ph">' +
    (p.im ? '<img loading="lazy" src="' + esc(p.im) + '" alt="" onerror="this.remove()">' : '') +
    (p.s ? '<span class="sec ' + p.s + '">' + SECN[p.s] + '</span>' : '') + (p.n > 1 ? '<span class="n">' + p.n + ' imágenes</span>' : '') +
    '<span class="ico">' + p.k.slice(0, 3).map(function (k) { return '<span title="' + TN[k] + '">' + ico(k) + '</span>'; }).join('') + '</span></div>' +
    '<span class="meta"><b>' + fdate(p.d) + '</b>' + (meds ? ' · ' + esc(meds) : '') + '</span>' +
    '<span class="tt">' + hl(head, T) + '</span>' + (auts.length ? '<span class="by">por ' + esc(auts.join(', ')) + (p.a.length > 3 ? ' y ' + (p.a.length - 3) + ' más' : '') + '</span>' : '') + '</a>';
}
function render() {
  var T = toks(), g = document.getElementById('grid');
  if (!res.length) {
    g.innerHTML = '<div class="empty" style="grid-column:1/-1">No hay entradas con esa combinación. Prueba a quitar algún filtro.</div>';
  } else g.innerHTML = res.slice(0, shown).map(function (p) { return card(p, T); }).join('');
  document.getElementById('more').hidden = res.length <= shown;
}
document.getElementById('more').addEventListener('click', function () {
  var T = toks(), g = document.getElementById('grid');
  g.insertAdjacentHTML('beforeend', res.slice(shown, shown + 36).map(function (p) { return card(p, T); }).join(''));
  shown += 36; document.getElementById('more').hidden = res.length <= shown;
});
function toggle(k, v) { var i = st[k].indexOf(v); if (i >= 0) st[k].splice(i, 1); else st[k].push(v); run(); }
document.addEventListener('click', function (e) {
  var b = e.target.closest('button'); if (!b) return;
  if (b.dataset.more) { openF[b.dataset.more] = !openF[b.dataset.more]; run(); return; }
  if (b.dataset.k) { var k = b.dataset.k, v = b.dataset.v; toggle(k, /^[amhy]$/.test(k) ? +v : v); return; }
  if (b.dataset.add) { var k2 = b.dataset.add, v2 = +b.dataset.v; if (!has(st[k2], v2)) st[k2].push(v2); run(); return; }
  if (b.dataset.rm) {
    var r = b.dataset.rm;
    if (r === 'all') { st.q = ''; ['k', 's', 'y', 'm', 'a', 'h'].forEach(function (k) { st[k] = []; }); q.value = ''; }
    else if (r === 'q') { st.q = ''; q.value = ''; }
    else { var vv = /^[amhy]$/.test(r) ? +b.dataset.v : b.dataset.v; st[r] = st[r].filter(function (x) { return x !== vv; }); }
    run();
  }
});
document.getElementById('sort').addEventListener('change', function (e) { st.o = e.target.value; run(); });
document.getElementById('ftoggle').addEventListener('click', function () {
  var f = document.getElementById('facets'), o = f.classList.toggle('open'); this.setAttribute('aria-expanded', o);
});

// sugerencias mientras se escribe
var q = document.getElementById('q'), sug = document.getElementById('sug'), sel = -1, opts = [];
function suggest() {
  var t = nz(q.value); opts = []; sel = -1;
  if (t.length < 2) { sug.hidden = true; q.setAttribute('aria-expanded', 'false'); return; }
  function find(arr, key, n) {
    var out = [];
    for (var i = 0; i < arr.length && out.length < n; i++) {
      var k = arr[i].k, pos = k.indexOf(t);
      if (pos === 0 || (pos > 0 && /[ |]/.test(k[pos - 1]))) out.push([key, i]);
    }
    return out;
  }
  var groups = [['Autores', find(D.autores, 'a', 5)], ['Medios', find(D.medios, 'm', 4)], ['Temas', find(D.temas, 'h', 4)]];
  var h = '';
  groups.forEach(function (g) {
    if (!g[1].length) return;
    h += '<h3>' + g[0] + '</h3>';
    g[1].forEach(function (o) {
      var it = o[0] === 'a' ? D.autores[o[1]] : o[0] === 'm' ? D.medios[o[1]] : D.temas[o[1]];
      var alt = it.v && nz(it.n).indexOf(t) < 0 ? it.v.filter(function (v) { return nz(v).indexOf(t) >= 0; })[0] : '';
      var ex = o[0] === 'a' ? (it.m || []).slice(0, 2).join(', ') : o[0] === 'h' ? it.b : (it.r || '');
      h += '<button type="button" role="option" id="o' + opts.length + '" data-o="' + opts.length + '"><span class="nm">' + esc(it.n) + '</span><span class="ex">' + esc(alt ? 'como «' + alt + '»' : ex) + '</span><span class="ct">' + it.p + '</span></button>';
      opts.push(o);
    });
  });
  h += '<button type="button" class="txt" role="option" id="o' + opts.length + '" data-o="' + opts.length + '"><span class="nm">Buscar «' + esc(q.value.trim()) + '» en todo el texto</span></button>';
  opts.push(['q', q.value.trim()]);
  sug.innerHTML = h; sug.hidden = false; q.setAttribute('aria-expanded', 'true');
}
function pick(i) {
  var o = opts[i]; if (!o) return;
  if (o[0] === 'q') st.q = o[1]; else { st.q = ''; if (!has(st[o[0]], o[1])) st[o[0]].push(o[1]); }
  q.value = o[0] === 'q' ? o[1] : ''; sug.hidden = true; q.setAttribute('aria-expanded', 'false'); run();
}
function mark() { [].forEach.call(sug.querySelectorAll('button'), function (b, i) { b.setAttribute('aria-selected', i === sel); }); if (sel >= 0) q.setAttribute('aria-activedescendant', 'o' + sel); }
q.addEventListener('input', suggest);
q.addEventListener('keydown', function (e) {
  if (e.key === 'ArrowDown') { sel = Math.min(opts.length - 1, sel + 1); mark(); e.preventDefault(); }
  else if (e.key === 'ArrowUp') { sel = Math.max(0, sel - 1); mark(); e.preventDefault(); }
  else if (e.key === 'Escape') { sug.hidden = true; }
  else if (e.key === 'Enter') {
    e.preventDefault();
    if (sel >= 0) return pick(sel);
    var t = nz(q.value);
    var ex = opts.filter(function (o) { return o[0] !== 'q' && nz((o[0] === 'a' ? D.autores : o[0] === 'm' ? D.medios : D.temas)[o[1]].n) === t; })[0];
    if (ex) pick(opts.indexOf(ex)); else { st.q = q.value.trim(); sug.hidden = true; run(); }
  }
});
sug.addEventListener('click', function (e) { var b = e.target.closest('button[data-o]'); if (b) { e.stopPropagation(); pick(+b.dataset.o); } });
document.addEventListener('click', function (e) { if (!e.target.closest('.qbox')) sug.hidden = true; });
document.getElementById('qclear').addEventListener('click', function () { q.value = ''; st.q = ''; sug.hidden = true; run(); q.focus(); });
// buscador pequeño de la cabecera: manda aquí
[].forEach.call(document.querySelectorAll('.srch'), function (f) {
  f.addEventListener('submit', function () { var v = f.querySelector('input').value.trim(); if (v) { q.value = v; st.q = v; run(); scrollTo(0, 0); } });
});
document.getElementById('try').addEventListener('click', function (e) {
  var a = e.target.closest('a[data-t]'); if (!a) return; e.preventDefault();
  var k = a.dataset.t, v = a.dataset.v;
  if (k === 'q') st.q = v; else { var arr = k === 'a' ? D.autores : k === 'm' ? D.medios : D.temas; var i = arr.findIndex(function (x) { return x.n === v; }); if (i >= 0 && !has(st[k], i)) st[k].push(i); }
  run();
});
readHash(); q.value = st.q; document.getElementById('sort').value = st.o; run();
"""

TRY = [('a', 'Josemi Benítez'), ('h', 'Guerra en Ucrania'), ('m', 'Le Monde'), ('q', 'mapa del metro'), ('a', 'Francesca Fattori'),
       ('h', 'Juegos Olímpicos'), ('m', 'La Voz de Galicia'), ('q', 'tipografía')]
try_html = ''.join(f'<a href="#" data-t="{k}" data-v="{v}">{v}</a>' for k, v in TRY)

page = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Buscador · inconsolata»</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1;1,9..144,100..900,0..100,0..1&display=swap">
<style>{CSS}{HEAD_CSS}{MINI_CSS}{BCSS}</style>
</head>
<body>
{symbols()}{tema_symbols()}
<div class="page">
{head_interior()}
<main>
<section class="hero"><div class="wrap">
<h1 class="soft">Quince años de <em>periodismo visual</em>, a un clic</h1>
<div class="qbox">
<div class="qrow">
<svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2.6" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>
<label for="q" class="sr">Buscar en el archivo de inconsolata»</label>
<input id="q" type="search" placeholder="Autor, medio, tema o lo que recuerdes…" autocomplete="off" role="combobox" aria-expanded="false" aria-controls="sug" aria-autocomplete="list">
<button type="button" id="qclear" aria-label="Borrar búsqueda">×</button>
</div>
<div class="sug" id="sug" role="listbox" hidden></div>
</div>
<div class="try" id="try"><span class="caps" style="margin-right:4px">Prueba »</span>{try_html}</div>
</div></section>
<div class="wrap body">
<aside class="facets" id="facets" aria-label="Filtros">
<div class="fg"><h2>Años</h2><div class="years" id="f-y"></div><div class="yl"><span>2011</span><span>2026</span></div></div>
<div class="fg"><h2>Tipo de pieza</h2><div class="fl" id="f-k"></div></div>
<div class="fg"><h2>Temas</h2><div class="fl" id="f-h"></div></div>
<div class="fg"><h2>Medios</h2><div class="fl" id="f-m"></div></div>
<div class="fg"><h2>Autores</h2><div class="fl" id="f-a"></div></div>
</aside>
<section aria-live="polite">
<div class="rhead"><div class="count" id="count"></div>
<div style="display:flex;gap:10px;align-items:center"><button type="button" class="ftoggle" id="ftoggle" aria-expanded="false" aria-controls="facets">Filtros</button>
<label class="sr" for="sort">Ordenar</label><select id="sort"><option value="new">Más recientes</option><option value="old">Más antiguas</option><option value="rel">Más relevantes</option></select></div></div>
<div class="active" id="active"></div>
<div class="fx" id="ficha" hidden></div>
<div class="grid" id="grid"></div>
<button type="button" class="loadmore" id="more">Cargar más »</button>
</section>
</div>
</main>
<footer>
<div class="cmyk-bar" aria-hidden="true"><span style="background:#00A0DC"></span><span style="background:#66C6EA"></span><span style="background:#E5007E"></span><span style="background:#EF66B2"></span><span style="background:#FFD400"></span><span style="background:#FFE566"></span><span style="background:#16140F"></span><span style="background:#7A766C"></span></div>
<div class="wrap foot"><span class="soft" style="font-size:56px;line-height:1">inc<span style="color:#EF66B2">»</span></span><span>© inconsolata» 2011–2026 · un blog de Saúl Castillo</span></div>
</footer>
</div>
<script>{JS.replace('__DATA__', DATA).replace('__TIPOS__', TIPO_NAMES).replace('__TS__', json.dumps([slug(t['n']) for t in json.loads(DATA.replace('<\\/', '</'))['temas']]))}</script>
{MINI_JS}
</body>
</html>
"""
open(os.path.join(OUT, 'inconsolata-buscador.html'), 'w').write(page)
print('ok', round(len(page.encode()) / 1e6, 2), 'MB')
