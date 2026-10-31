"""Tema de Tumblr de inconsolata» (versión 1: páginas de post y listado provisional).
El HTML de Tumblr pone el contenido; un script lo reorganiza con el diseño nuevo y completa medio, autores,
temas y avatares leyendo los datos del repositorio inconsolata-datos (vía jsDelivr).
Uso: python3 gen/tumblr_theme.py <salida.html>
"""
import os, sys, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from posts import CSS
from common import symbols, HEAD_CSS, MINI_CSS, MINI_JS, TEMAS_CSS, LEGACY_CSS, TIPOS, SOCIAL, SEARCH, ESPIRAL
from lightbox import LB_CSS, LB_HTML, LB_JS
from temas_iconos import tema_symbols, slug as tslug
from tema_vistas import VCSS, VJS
from tema_portada import PCSS, PJS
from tema_paginas import PAG_CSS, PAG_JS
from common import ESPIRAL_COLOR

OUT = sys.argv[1]
APOYA = 'https://buymeacoffee.com/saulcastillo'

NAV = (f'<nav aria-label="Secciones"><a href="https://saulcastillo.es/#sobre-mi">Sobre mí</a><a href="/buscador#k=info">Infografía</a><a href="/medios">Medios</a>'
       f'<div class="dd"><button type="button" class="dd-b" aria-expanded="false" aria-haspopup="true">Archivo <i aria-hidden="true">▾</i></button><div class="dd-m" hidden><a href="/archive">Ver el archivo</a><a href="/estadisticas">Estadísticas</a><a href="/cronologia">Cronología</a></div></div>{SEARCH}<a href="{APOYA}" class="btn-ink">Apóyanos »</a></nav>')
LITE = (f'<div class="lite-bar"><a class="lb-brand soft" href="/" aria-label="inconsolata», ir a la portada">inc<span>»</span></a><div class="lb-acc">'
        '<a class="lb-nov" href="/novedades" aria-label="Novedades de la web"><svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="11" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="20" cy="20" r="5" fill="none" stroke="currentColor" stroke-width="2.4"/><path d="M20 3v34M3 20h34" stroke="currentColor" stroke-width="2.4"/></svg><b class="lb-n" id="lb-n" hidden></b></a>'
        '<button type="button" class="lb-btn" data-lite="buscar" aria-label="Buscar"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg></button>'
        '<button type="button" class="lb-menu" data-lite="menu" aria-expanded="false" aria-controls="lite-menu"><span class="lb-h" aria-hidden="true"><i></i><i></i><i></i></span>Menú</button></div></div>'
        '<div class="lite-menu" id="lite-menu" hidden>' + SEARCH.replace('q-top', 'q-lite') +
        '<nav class="lm-nav" aria-label="Secciones"><a href="/">Portada</a><a href="/buscador#k=info">Infografía</a><a href="/medios">Medios</a><a href="/autores">Autores</a><a href="/especiales">Especiales</a>'
        '<a href="/archive">Archivo</a><a href="/estadisticas">Estadísticas</a><a href="/cronologia">Cronología</a><a href="/novedades">Novedades</a><a href="https://saulcastillo.es/#sobre-mi">Sobre mí</a></nav>'
        f'<a class="lm-apoya" href="{APOYA}">Apóyanos »</a>{SOCIAL}<button type="button" class="lm-ver" data-version="completa">Ver la versión completa de la web</button></div>')
HEAD = (f'<header class="head"><a href="/" class="brand soft" aria-label="inconsolata», ir a la portada">inc<span>»</span></a>'
        f'<div class="hd-right">{NAV}<div class="hd-row2">{SOCIAL}</div></div></header>'
        '<div class="mini-head" id="mini-head"><div class="mh-in">'
        '<a class="mh-brand soft" href="/" aria-label="inconsolata», ir a la portada">inc<span>»</span></a>'
        '<nav class="mh-nav" aria-label="Secciones"><a href="/buscador#k=info">Infografía</a><a href="/medios">Medios</a><div class="dd"><button type="button" class="dd-b" aria-expanded="false" aria-haspopup="true">Archivo <i aria-hidden="true">▾</i></button><div class="dd-m" hidden><a href="/archive">Ver el archivo</a><a href="/estadisticas">Estadísticas</a><a href="/cronologia">Cronología</a></div></div></nav>'
        + SEARCH.replace('q-top', 'q-mini') + f'<a class="mh-apoya" href="{APOYA}">Apóyanos »</a></div>'
        '<div class="mh-prog" aria-hidden="true"><span id="mh-bar"></span></div></div>')

TCSS = """
.crumbs .k-esp{color:var(--accent)}
.ficha .esps{margin-top:14px}
.ficha dd{line-height:1.5}
.hero-card p,.ficha dd,.fuente,.fuente p{font-family:'Instrument Sans',sans-serif!important}
.ficha .esps{display:flex;justify-content:center}
/* las comillas de los logos, enteras (Safari recortaba su cola izquierda) */
.brand span,.mh-brand span,.lb-brand span{display:inline-block;padding:0 .06em 0 .14em;margin:0 -.06em 0 -.14em}
/* especial web: banda blanca de borde a borde */
.v-home .ew{background:#fff;color:var(--ink);margin:64px 0 0;padding:60px 0 0;border-top:6px solid var(--ink);border-bottom:6px solid var(--ink);position:relative;z-index:1}
.v-home .ew-in{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:56px;align-items:center}
.v-home .ew-k{color:var(--accent);font-size:13px;letter-spacing:3px}
.v-home .ew h2{font-size:clamp(56px,7.4vw,108px);line-height:.88;margin:14px 0 18px;letter-spacing:-.01em}
.v-home .ew h2 a{color:var(--ink);text-decoration:none}.v-home .ew h2 em{color:var(--accent);font-style:inherit}
.v-home .ew p{font:400 19px/1.5 'Instrument Sans',sans-serif;max-width:480px;margin:0 0 28px}
.v-home .ew-cta{display:inline-block;background:var(--accent);color:#fff;font:800 15px Archivo,sans-serif;letter-spacing:3px;text-transform:uppercase;padding:18px 26px;box-shadow:7px 7px 0 var(--ink);text-decoration:none;transition:transform .15s,box-shadow .15s}
.v-home .ew-cta:hover,.v-home .ew-cta:focus-visible{transform:translate(-3px,-3px);box-shadow:10px 10px 0 var(--ink)}
.v-home .ew-post{display:inline-block;margin-left:26px;font:800 13px Archivo,sans-serif;letter-spacing:2px;text-transform:uppercase;color:var(--ink);text-decoration:underline;text-underline-offset:5px}
.v-home .ew-nav{display:block;border-radius:12px;overflow:hidden;background:#2B2822;box-shadow:14px 14px 0 var(--yellow);transform:rotate(1.2deg);text-decoration:none}
.v-home .ew-bar{display:flex;gap:8px;align-items:center;padding:10px 14px}.v-home .ew-bar i{width:11px;height:11px;border-radius:50%;background:#5A554B}
.v-home .ew-bar span{margin-left:12px;flex:1;background:#3A362E;color:#BDB5A3;font:600 13px Archivo,sans-serif;padding:5px 12px;border-radius:6px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.v-home .ew-win{display:block;aspect-ratio:16/10;overflow:hidden;background:var(--paper)}.v-home .ew-win img{width:100%;height:100%;object-fit:cover;object-position:top;display:block}
.v-home .ew-tira{margin-top:60px;background:var(--ink);padding:18px 0 18px max(24px,calc((100% - 1312px)/2));overflow:hidden}
.v-home .ew-tr{display:flex;gap:16px;overflow-x:auto;scrollbar-width:none;-ms-overflow-style:none;scroll-snap-type:x proximity}
.v-home .ew-tr::-webkit-scrollbar{display:none}
.v-home .ew-tr a{flex:0 0 250px;background:#fff;padding:8px 8px 10px;text-decoration:none;color:var(--ink);scroll-snap-align:start;transition:transform .15s}
.v-home .ew-tr a:hover{transform:translateY(-4px)}
.v-home .ew-tr img{width:100%;height:150px;object-fit:cover;object-position:top;display:block}
.v-home .ew-tr .caps{display:block;font-size:11px;letter-spacing:2px;margin-top:8px}
.v-home .ew+.wrap>section:first-child{margin-top:72px}
@media (max-width:900px){.v-home .ew{padding-top:40px}.v-home .ew-in{grid-template-columns:1fr;gap:36px}.v-home .ew-post{display:block;margin:18px 0 0}.v-home .ew-tira{margin-top:44px}.v-home .ew-tr a{flex-basis:200px}.v-home .ew-tr img{height:120px}}
/* avisos de portada: tira bajo la cabecera (A) y columna junto al destacado (D) */
.v-home .tira{display:flex;align-items:center;gap:18px;border-bottom:1px solid var(--ink);padding:12px 0;margin:-6px 0 18px}
.v-home .tira[hidden],.v-home .colav[hidden]{display:none}
.tira .tr-k,.colav .cl-k{font:800 12px Archivo,sans-serif;letter-spacing:2.5px;text-transform:uppercase;color:var(--accent);flex-shrink:0}
.tira .x{margin-left:auto}
.tira .tr-t{flex:1;min-width:0;font-size:24px;line-height:1.1;color:var(--ink);text-decoration:none}
.tira .tr-t em,.colav .cl-t em{color:var(--accent);font-style:inherit}
.tira .tr-q{color:var(--accent)}
.tira .tr-t:hover,.colav .cl-t:hover{text-decoration:underline;text-decoration-color:var(--accent);text-decoration-thickness:2px;text-underline-offset:4px}
.cbar{display:flex;flex-shrink:0}.cbar i{display:block;width:22px;height:12px}
.tira .x,.colav .x,.colav .cl-c button{background:none;border:0;padding:4px 6px;font:700 20px Archivo,sans-serif;line-height:1;color:var(--ink);cursor:pointer;min-width:32px;min-height:32px}
.colav{position:relative;width:290px;border-top:3px solid var(--ink);padding-top:12px;margin:0 0 30px}
.colav .cl-k{display:flex;justify-content:space-between;align-items:center}
.colav .cl-c{display:flex;align-items:center;gap:2px;color:var(--ink);font-weight:700;letter-spacing:1px}
.colav .cl-k{font-size:11px;line-height:1.2}
.colav .x,.colav .cl-c button{font-size:14px;padding:0 0 0 8px;min-width:0;min-height:0;line-height:1}
.colav .cl-c button{font-size:15px}
.colav .cl-t{display:block;font-size:30px;line-height:1.02;color:var(--ink);text-decoration:none;margin:8px 0 12px}
.colav .cbar{width:100%}.colav .cbar i{flex:1;width:auto;height:8px}
.v-home .hero .colav.en-hero{grid-column:8/13;grid-row:1;justify-self:end;align-self:start;margin:-30px 30px 0 0;z-index:3}
.v-home .sec-head .colav.en-sh{margin:0 0 0 auto;align-self:flex-end}
.colav.go{animation:clIn .6s cubic-bezier(.2,.8,.2,1) both}
@keyframes clIn{from{opacity:0;transform:translateY(-14px)}}
@media (prefers-reduced-motion:reduce){.colav.go{animation:none}}
@media (max-width:700px){.v-home .tira{flex-wrap:wrap;gap:6px 14px}.tira .tr-t{flex-basis:100%;order:3;font-size:21px}.colav{width:auto}}
@media (max-width:760px){.main-sheet .shot{min-height:0}}
html.lite .main-sheet .shot{min-height:0}

.pie-aj{font-family:'Archivo',sans-serif;font-size:14px;line-height:1.45;color:var(--muted);margin:14px 0 0;padding-left:12px;border-left:3px solid var(--accent);text-align:left}
.pie-f{display:block;font-family:'Archivo',sans-serif;font-size:12px;line-height:1.35;color:var(--muted);margin-top:4px}

.fuente.plegable{position:relative;padding-right:56px!important}
.fuente .f-res{display:none}
.fuente.plegable:not(.abierta) .f-res{display:block;flex:0 0 auto;white-space:nowrap}
.fuente.plegable:not(.abierta) .f-tx{display:none}
.fuente.plegable:not(.abierta) .f-avs{flex:1 1 auto;max-width:none}
.fuente.abierta{flex-wrap:wrap}
.fuente.abierta .f-tx{flex:1 1 100%}
.fuente.abierta .f-avs{flex:1 1 100%;max-width:none;-webkit-mask-image:none;mask-image:none}
.fuente.abierta .f-track{flex-wrap:wrap;width:auto;row-gap:10px}
.f-track{display:flex;width:max-content}
.f-track .f-av{margin-right:10px}
.f-dup{display:flex}
.f-track.gira{animation:f-rueda var(--dur,20s) linear infinite}
.f-avs:hover .f-track,.f-avs:focus-within .f-track{animation-play-state:paused}
.f-avs:has(.gira){-webkit-mask-image:linear-gradient(90deg,transparent,#000 18px,#000 calc(100% - 18px),transparent);mask-image:linear-gradient(90deg,transparent,#000 18px,#000 calc(100% - 18px),transparent)}
@keyframes f-rueda{to{transform:translateX(-50%)}}
.f-av-l{border-radius:50%;background:rgba(255,255,255,.14);color:#fff;font:800 20px 'Archivo',sans-serif;text-decoration:none}
.k-av{display:inline-block;width:1.25em;height:1.25em;object-fit:contain;vertical-align:-.3em;filter:brightness(0)}
.k-avs{display:inline-flex;align-items:center;gap:.15em;margin-right:.35em;vertical-align:-.3em;flex-wrap:wrap}
.k-avs .k-av{margin:0!important;vertical-align:0}
svg .m{--lbl:transparent}
.m-id.multi.mucho{gap:12px 18px}
.m-id.multi.mucho .m-logo{max-height:28px;max-width:116px}
.f-mas{position:absolute;right:10px;top:50%;transform:translateY(-50%);width:40px;height:40px;border:2px solid var(--yellow);background:transparent;color:var(--yellow);display:grid;place-items:center;cursor:pointer;transition:transform .2s}
.fuente.abierta .f-mas{top:12px;transform:rotate(180deg)}
.f-mas:focus-visible{outline:3px solid #fff;outline-offset:2px}

.lite-bar,.lite-menu{display:none}
.ver-sw,.lm-ver{background:none;border:0;padding:6px 0;font:700 13px 'Archivo',sans-serif;letter-spacing:.5px;color:inherit;text-decoration:underline;text-underline-offset:3px;cursor:pointer;opacity:.8}
html.lite .page>.head,html.lite .mini-head,html.lite .v-home .topbar{display:none!important}
html.lite .lite-bar{display:flex;position:sticky;top:0;z-index:70;align-items:center;justify-content:space-between;gap:10px;padding:8px 16px;background:var(--paper);border-bottom:2px solid var(--ink)}
.lb-brand{font-size:34px;line-height:1;color:var(--ink);padding-bottom:4px}.lb-brand span{color:var(--accent)}
.lb-acc{display:flex;align-items:center;gap:4px}
.lb-btn,.lb-nov{min-width:44px;height:44px;display:inline-flex;align-items:center;justify-content:center;background:none;border:0;color:var(--ink);position:relative;cursor:pointer;padding:0}
.lb-nov svg{width:26px;height:26px;color:var(--accent)}
.lb-n{position:absolute;top:3px;right:1px;background:var(--accent);color:#fff;font:800 11px/18px 'Archivo',sans-serif;min-width:18px;height:18px;border-radius:9px;text-align:center;padding:0 4px}
.lb-menu{display:inline-flex;align-items:center;gap:8px;height:40px;margin-left:4px;padding:0 12px;border:2px solid var(--ink);background:var(--ink);color:var(--paper);font:800 12px 'Archivo',sans-serif;letter-spacing:1.5px;text-transform:uppercase;cursor:pointer}
.lb-menu[aria-expanded=true]{background:var(--accent);border-color:var(--accent)}
.lb-h{display:flex;flex-direction:column;gap:3px}.lb-h i{display:block;width:15px;height:2px;background:currentColor}
html.lite .lite-menu:not([hidden]){display:flex;flex-direction:column;gap:22px;position:fixed;left:0;right:0;bottom:0;top:62px;z-index:69;background:var(--paper);padding:18px 16px 40px;overflow-y:auto}
.lite-menu .srch{width:100%;min-height:48px}.lite-menu .srch input{width:100%;font-size:17px}
.lite-menu .srch .ac{width:100%}
.lm-nav{display:flex;flex-direction:column}
.lm-nav a{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-size:32px;line-height:1.1;padding:9px 0;border-bottom:1px solid #CFC8B8;color:var(--ink)}
.lm-nav a:active,.lm-nav a:hover{color:var(--accent)}
.lm-apoya{align-self:flex-start;background:var(--ink);color:var(--yellow);font:800 14px 'Archivo',sans-serif;letter-spacing:1.5px;text-transform:uppercase;padding:14px 20px}
.lite-menu .soc{display:flex;gap:10px}
html.lite body.lm-abierto{overflow:hidden}
html.lite .v-home .masthead{min-height:0;padding-top:8px}
html.lite .v-home .mast{font-size:31vw}
html.lite .v-home .side{display:none}
html.lite .v-home .prueba{position:relative;left:auto;right:auto;top:auto;bottom:auto;width:auto;max-width:100%;margin:4px 0 26px}
html.lite .v-home .faldon{margin-top:0}
html.lite .v-home .scatter{display:none}
html.lite .v-home .mas{margin:18px 0 60px}
html.lite .v-home .sec-head h2{font-size:44px}
html.lite .v-home .vit{display:flex;flex-direction:column;gap:14px}
html.lite .v-home .vit-stage{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
html.lite .v-home .medios .cinta{display:none}
html.lite .v-home .logos{grid-template-columns:repeat(3,minmax(0,1fr))}
html.lite .v-ficha .grid{display:flex!important;flex-direction:column;gap:0!important}
html.lite .v-ficha .grid .card{display:grid!important;grid-template-columns:84px minmax(0,1fr);grid-template-rows:auto auto 1fr;column-gap:12px;row-gap:4px;padding:12px 0!important;margin:0!important;border:0!important;border-bottom:1px solid #CFC8B8!important;box-shadow:none!important;transform:none!important;background:none!important}
html.lite .v-ficha .grid .card .ph{grid-row:1/4;width:84px!important;height:84px!important;aspect-ratio:auto!important;margin:0!important;border:2px solid var(--ink)}
html.lite .v-ficha .grid .card .ph img{width:100%;height:100%;object-fit:cover}
html.lite .v-ficha .grid .card .tape,html.lite .v-ficha .grid .card .ico,html.lite .v-ficha .grid .card .by{display:none!important}
html.lite .v-ficha .grid .card .tt{font-size:17px!important;line-height:1.15}
html.lite .wk-top .av-slot{display:none!important}
html.lite .v-home .mm-num{font-size:15vw;white-space:nowrap;overflow:hidden}
html.lite .v-home .film{transform:none}
html.lite .v-home .frames{display:flex!important;overflow-x:auto;scroll-snap-type:x mandatory;gap:10px}
html.lite .v-home .frames .frame{flex:0 0 42%;scroll-snap-align:start}
html.lite .v-home .proj h3{font-size:38px!important;overflow-wrap:anywhere}
html.lite .legacy{font-size:13px}


mark.subr{background:none;color:inherit;padding:.06em .24em;margin:0 -.08em;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 40' preserveAspectRatio='none'%3E%3Cpath d='M6 9C34 3 70 8 104 4s68 1 90 5c4 7 3 16 1 24-30 3-62 0-98 4S26 38 4 34C1 27 2 16 6 9z' fill='white'/%3E%3C/svg%3E");background-repeat:no-repeat;background-size:100% 96%;background-position:0 55%;-webkit-box-decoration-break:clone;box-decoration-break:clone}

.dd{position:relative;display:inline-flex}
.dd-b{font:inherit;letter-spacing:inherit;text-transform:inherit;color:inherit;background:none;border:0;padding:0;cursor:pointer;display:inline-flex;gap:5px;align-items:center}
.dd-b i{font-style:normal;font-size:.8em;transition:transform .15s}
.dd-b[aria-expanded=true] i{transform:rotate(180deg)}
.dd-m{position:absolute;top:calc(100% + 10px);right:0;z-index:60;display:flex;flex-direction:column;min-width:200px;background:var(--paper);border:2px solid var(--ink);box-shadow:6px 6px 0 var(--ink)}
.dd-m[hidden]{display:none}
.dd-m a{padding:11px 16px;white-space:nowrap;border-bottom:1px solid #CFC8B8}
.dd-m a:last-child{border-bottom:0}
.dd-m a:hover,.dd-m a:focus-visible{background:var(--ink);color:var(--paper)}
@media (max-width:820px){.topbar .hd-right nav .dd{display:none}}

.post-raw{display:none}
.title h1.auto{font-size:clamp(34px,4.2vw,64px);line-height:1.02;letter-spacing:-.015em}
.title h1 em{color:var(--accent)}
.body .npf_row,.body figure{display:none}
.body blockquote.npf_indented{display:none}
.body h1{display:none}
.mm-items{display:flex;flex-direction:column;gap:56px}
.mm-it{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:28px;align-items:center}
.mm-it .txt{display:flex;flex-direction:column;gap:8px}
.mm-it .md{display:inline-flex;align-items:center;gap:10px;font-size:13px;font-weight:800;letter-spacing:2px;text-transform:uppercase}
.mm-it .md img{width:36px;height:36px;object-fit:contain}
.mm-it h2{margin:0;font-family:'Fraunces',serif;font-weight:700;font-size:26px;line-height:1.1}
.mm-it .by{font-family:'Fraunces',serif;font-style:italic;font-size:17px}
.mm-it .by a{border-bottom:2px solid var(--accent)}
.mm-n{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-size:40px;color:var(--accent);line-height:1}
.pn a .t{font-family:'Fraunces',serif;font-weight:700;font-size:22px}
/* listado provisional */
.lst{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:44px 28px;padding:40px 0 70px}
.lc{position:relative;background:#fff;padding:12px 12px 18px;box-shadow:7px 7px 0 var(--ink);display:flex;flex-direction:column;gap:9px;transition:transform .2s}
.lc:hover{transform:translateY(-4px)}
.lc .ph{aspect-ratio:4/3;overflow:hidden;background:#DAD4C6 radial-gradient(#16140F 1.1px,transparent 1.3px) 0 0/7px 7px}
.lc .ph img{width:100%;height:100%;object-fit:cover;object-position:top;display:block}
.lc .kicker{font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;display:flex;align-items:center;gap:6px}
.lc .kicker img{width:16px;height:16px;object-fit:contain;filter:brightness(0)}
.lc .tt{font-family:'Fraunces',serif;font-weight:700;font-size:21px;line-height:1.12}
.lc .sec{position:absolute;top:22px;left:22px;background:var(--ink);color:var(--yellow);font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;padding:5px 8px}
.pag{display:flex;justify-content:space-between;gap:12px;padding:0 0 70px}
.pag a{background:var(--ink);color:var(--paper);padding:14px 20px;font-size:13px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase}
.tag-head{padding:30px 0 0}.tag-head h1{margin:0;font-size:clamp(48px,7vw,104px);line-height:.9}
.fuente{display:flex;align-items:center;gap:16px}
.fuente p{margin:0;flex:1;min-width:0}
.f-av{flex-shrink:0;width:52px;height:52px;display:flex;align-items:center;justify-content:center}
.f-av img{width:100%;height:100%;object-fit:contain}
.m-id{display:flex;justify-content:center;padding:4px 0 10px;border-bottom:1px dashed #CFC8B8}
.m-logo{display:block;max-width:100%;max-height:64px;width:auto;height:auto;object-fit:contain;margin:0 auto}
.m-id.multi{flex-wrap:wrap;align-items:center;gap:14px 22px}
.m-id.multi a{flex:0 1 auto}
.m-id.multi .m-logo{max-height:38px;max-width:150px}
.f-avs{flex:0 1 auto;min-width:0;max-width:60%;overflow:hidden}
.serie{padding:8px 0 48px}
.serie>.caps{display:block;border-top:2px solid var(--ink);padding-top:12px}
.prev-row{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px;align-items:center}
.prev-row a{border:2px solid var(--ink);padding:8px 12px;font-size:14px;font-weight:700;min-height:40px;display:inline-flex;align-items:center}
.prev-row a:hover{background:var(--ink);color:var(--paper)}
.prev-row a.cur{background:var(--accent);border-color:var(--accent);color:#fff}
.share{display:flex;gap:10px}
.share a,.share button{width:48px;height:48px;min-height:48px;padding:0;display:inline-flex;align-items:center;justify-content:center;background:var(--ink);color:var(--paper);border:2px solid var(--ink);cursor:pointer;position:relative;transition:background .15s,border-color .15s}
.share a:hover,.share button:hover,.share a:focus-visible,.share button:focus-visible{background:var(--accent);border-color:var(--accent);color:#fff}
.share .ok{display:none;position:absolute;inset:0;align-items:center;justify-content:center}
.share button.done svg:first-child{visibility:hidden}.share button.done .ok{display:flex}
.share button.done{background:var(--accent);border-color:var(--accent);color:#fff}
.prev-row.y{display:grid;grid-template-columns:76px minmax(0,1fr);align-items:start}
.prev-row .ls{display:flex;flex-wrap:wrap;gap:8px}
.prev-row .yr{line-height:40px;font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-size:22px;color:var(--accent);padding:0 6px 0 2px;min-width:64px}
.v-x .prev-row.y{display:grid;grid-template-columns:76px minmax(0,1fr);align-items:start}
.prev-row .ls{display:flex;flex-wrap:wrap;gap:8px}
.prev-row .yr{line-height:40px;color:var(--ink)}
.temas a svg{width:20px;height:20px;overflow:visible;margin-right:6px}
.srch{position:relative}
.srch .ac{position:absolute;top:calc(100% + 6px);left:0;width:max(100%,320px);background:#fff;border:2px solid var(--ink);box-shadow:6px 6px 0 var(--accent);z-index:80;text-transform:none;letter-spacing:0}
.srch .ac a{display:flex;align-items:center;gap:10px;padding:8px 12px;min-height:44px;font-weight:600;font-size:15px;color:var(--ink)}
.srch .ac a.on,.srch .ac a:hover{background:var(--yellow)}
.srch .ac img,.srch .ac .ini{width:26px;height:26px;object-fit:contain;flex-shrink:0}
.srch .ac .ini{display:grid;place-items:center;background:var(--paper);font-family:'Fraunces',serif;font-style:italic;font-weight:900}
.srch .ac .ini.a{border-radius:50%}
.srch .ac .nm{font-family:'Fraunces',serif;font-style:italic;font-weight:700;font-size:17px}
.srch .ac small{margin-left:auto;font-size:10px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted)}
.srch .ac .todo{border-top:2px solid var(--ink);font-size:13px;font-weight:800}
.temas a.esp{background:var(--ink);color:var(--paper)}.temas a.esp:hover{background:var(--accent)}
@media (max-width:860px){.mm-it{grid-template-columns:1fr}}
"""

JS = r"""
(function(){
// iconos: los del código mandan sobre los que lleve pegados el tema (así un icono nuevo no obliga a volver a pegarlo)
(function(){var d=document.createElement('div');d.innerHTML=__SYMS__;var sv=d.querySelector('svg');if(!sv)return;[].forEach.call(sv.querySelectorAll('symbol'),function(x){var o=document.getElementById(x.id);if(o)o.remove();});(document.body||document.documentElement).insertBefore(sv,(document.body||document.documentElement).firstChild);})();
(function(){var B=(window.INC_BASE||'https://cdn.jsdelivr.net/gh/inconsolataweb/inconsolata-datos@main/')+'assets/marca/';if(!document.querySelector('link[href*="assets/marca/"]')){[].forEach.call(document.querySelectorAll('link[rel~="icon"],link[rel="apple-touch-icon"]'),function(l){l.remove();});document.head.insertAdjacentHTML('beforeend','<link rel="icon" href="'+B+'favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="'+B+'favicon-32.png"><link rel="apple-touch-icon" href="'+B+'apple-touch-icon.png">');}})();
(function(){if(!document.querySelector('link[href*="Instrument+Sans"]'))document.head.insertAdjacentHTML('beforeend','<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&display=swap">');})();
(function(){var y=document.getElementById('y-now');if(y)y.textContent=new Date().getFullYear();})();
var CDN=(window.INC_BASE||'https://cdn.jsdelivr.net/gh/inconsolataweb/inconsolata-datos@main/')+'datos/';
var LANZAMIENTO='2026-11-01';
var TN=__TN__, TS=__TS__, SECN={m:'mucho más',x:'EXTRA!',d:'detallitos',b:'metablog',o:'offtopic',w:'especial web'};
var MESES=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'];
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function get(f){var k='inc-'+f;try{var c=JSON.parse(sessionStorage.getItem(k)||'null');if(c)return Promise.resolve(c);}catch(e){}
 return fetch(CDN+f+'.json').then(function(r){return r.json();}).then(function(j){try{sessionStorage.setItem(k,JSON.stringify(j));}catch(e){}return j;});}
function fecha(d){return +d.slice(8,10)+' de '+MESES[+d.slice(5,7)-1]+' de '+d.slice(0,4);}
function ico(k,cls){return '<svg class="'+(cls||'')+'" viewBox="0 0 64 64" role="img" aria-label="'+esc(TN[k])+'" style="overflow:visible"><title>'+esc(TN[k])+'</title><use href="#i-'+k+'" class="k"/><use href="#i-'+k+'" class="m" x="3" y="2.5"/></svg>';}
var TIT={},AJ={};
__VJS__
__PJS__
__PAGJS__
// en el blog de pruebas los posts son reblogueos: usamos el id del post original
function rid(el){var m=(el.dataset.root||'').match(/\/post\/(\d+)/);return m?m[1]:el.dataset.id;}
function unwrap(b){var p=b.firstElementChild,q=p&&p.nextElementSibling;if(p&&q&&p.tagName==='P'&&q.tagName==='BLOCKQUOTE'&&(p.querySelector('a.tumblr_blog')||/:\s*$/.test(p.textContent))){b.innerHTML=q.innerHTML;}}
// Tumblr da un nombre de archivo distinto a cada tamaño: hay que elegirlo del srcset, no cambiar el tamaño en la URL
function srcDe(i,t){var ss=(i.getAttribute('srcset')||'').split(',').map(function(x){var p=x.trim().split(/\s+/);return {u:p[0],w:parseInt(p[1])||0};}).filter(function(x){return x.u&&x.w;}).sort(function(a,b){return a.w-b.w;});
 if(!ss.length)return i.getAttribute('src');var ok=ss.filter(function(x){return x.w>=t;});return (ok[0]||ss[ss.length-1]).u;}
function fichaMedio(m){return '/medios#'+encodeURIComponent(m.slug||m.n);}
function fichaAutor(a){return '/autores#'+encodeURIComponent(a);}
// medios de una pieza en un antetítulo: avatares de todos y «N medios» si son más de 3, o sus nombres si son 3 o menos
function medsK(ms){ms=(ms||[]).filter(Boolean);if(!ms.length)return '';
 var av=ms.filter(function(m){return m.avw;}).map(function(m){return '<img class="k-av" src="'+esc(m.avw)+'" alt="" title="'+esc(m.n)+'" onerror="this.remove()">';}).join('');
 return (av?'<span class="k-avs">'+av+'</span>':'')+'» '+esc(ms.length>3?ms.length+' medios':ms.map(function(m){return m.n;}).join(', ').replace(/, ([^,]*)$/,' y $1'));}
function medsI(ix){var C=(typeof cat0!=='undefined'&&cat0)||window.CAT||{medios:[]};return medsK((ix||[]).map(function(i){return C.medios[i];}));}
// iconos propios de los especiales (catalogo.espi = {slug:[icono, texto]}): se montan como símbolos #e-slug
var ESPI={},ESPI_N={},EXTRA_SYM={'t-urna':'<g stroke="currentColor" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" fill="none"><path d="M22 30 V6 H42 V30"/><path d="M27 16 L31 21 L38 12"/><path d="M4 30 H60"/><path d="M8 30 V58 H56 V30"/><path d="M20 30 H44" stroke-width="7"/></g>'};
var ESPI_LBL={'t-urna':[50.5,15,40]};
function prepEspIcos(cat){if(!cat||!cat.espi||prepEspIcos.hecho)return;prepEspIcos.hecho=1;var h='';
 Object.keys(cat.espi).forEach(function(sl){var v=cat.espi[sl],id=symN(v[0]),b=document.getElementById(id),body=b?b.innerHTML:EXTRA_SYM[id];if(!body)return;
  var t=String(v[1]||'').trim(),L=ESPI_LBL[id],lab='',fs;
  if(t&&L){fs=Math.min(L[1],L[2]/Math.max(1,t.length)*1.75);lab='<text x="32" y="'+L[0]+'" text-anchor="middle" font-family="Archivo,sans-serif" font-weight="800" font-size="'+fs.toFixed(1)+'" fill="var(--lbl,currentColor)" stroke="none">'+esc(t)+'</text>';}
  else if(t){fs=Math.min(14,50/Math.max(1,t.length)*1.75);lab='<rect x="4" y="46" width="56" height="17" rx="2" fill="var(--lbl,currentColor)" stroke="none"/><text x="32" y="59" text-anchor="middle" font-family="Archivo,sans-serif" font-weight="800" font-size="'+fs.toFixed(1)+'" fill="#fff" stroke="none">'+esc(t)+'</text>';}
  h+='<symbol id="e-'+sl+'" viewBox="0 0 64 64" overflow="visible">'+body+lab+'</symbol>';ESPI[sl]='e-'+sl;ESPI_N[sl]=(cat.esp&&cat.esp[sl])||'';});
 if(h)document.body.insertAdjacentHTML('afterbegin','<svg width="0" height="0" style="position:absolute" aria-hidden="true">'+h+'</svg>');}
function icoEsp(sl,cls,dos){var id=ESPI[sl];if(!id)return '';var n=esc(ESPI_N[sl]||'Especial');
 return '<svg class="'+(cls||'')+'" viewBox="0 0 64 64" role="img" aria-label="'+n+'" style="overflow:visible"><title>'+n+'</title><use href="#'+id+'" class="k"/>'+(dos===false?'':'<use href="#'+id+'" class="m" x="3" y="2.5"/>')+'</svg>';}
// icono de una pieza: el de su especial si lo tiene; si no, el de su tipo
function espSl(id){return (typeof META0!=='undefined'&&META0&&(META0[id]||[])[5])||'';}
function icoP(id,k,cls){var e=icoEsp(espSl(id),cls);return e||(k?ico(k,cls):'');}
function esPortadilla(s,k,im,d){if((s!=='m'&&s!=='x')||!im.w||!im.h)return false;var r=im.w/im.h;
 return (r>=4.5&&im.w>=1200&&im.w<=1400)||(s==='m'&&k===0&&r>=4.5)||(s==='m'&&k===0&&r>=2.6&&r<=2.9&&d>='2013');}

// ------------------------------------------------------------------ página de post
// ajustes del panel de portada: frases subrayadas y pies de foto añadidos sin tocar Tumblr
function ajustes(body,aj,s){if(!aj)return;
 (aj.subrayados||[]).forEach(function(f){f=String(f||'').replace(/\s+/g,' ').trim();if(!f)return;
  var w=document.createTreeWalker(body,NodeFilter.SHOW_TEXT),x;while((x=w.nextNode())){var v=x.nodeValue.replace(/ /g,' '),i=v.indexOf(f);
   if(i>=0&&!x.parentNode.closest('mark,a,.fuente')){var r=x.splitText(i);r.splitText(f.length);var m=document.createElement('mark');m.className='subr';r.parentNode.replaceChild(m,r);m.appendChild(r);break;}}});
}
function post(art,meta,cat,medido){
 var id=rid(art), d=art.dataset.date, mt=meta[id]||['',[],[],[],[]];
 var s=mt[0], tipos=mt[1], meds=mt[2].map(function(i){return cat.medios[i];}), auts=mt[3].map(function(i){return cat.autores[i];}), tems=mt[4];
 var esp=mt[5]&&cat.esp&&cat.esp[mt[5]]?{slug:mt[5],n:cat.esp[mt[5]]}:null;
 var body=art.querySelector('.body'), raw=art.querySelector('.post-raw'); unwrap(body);
 // imágenes: fotos «antiguas» de Tumblr + figuras del cuerpo (formato nuevo)
 var ims=[];
 [].forEach.call(raw.querySelectorAll('img[data-hr]'),function(i){ims.push({src:i.dataset.hr,w:+i.dataset.w||0,h:+i.dataset.h||0,cap:''});});
 [].forEach.call(body.querySelectorAll('figure img, img'),function(i){
  if(i.closest('blockquote'))return;
  var w=+(i.getAttribute('data-orig-width')||i.closest('figure')&&i.closest('figure').getAttribute('data-orig-width')||0),
      h=+(i.getAttribute('data-orig-height')||i.closest('figure')&&i.closest('figure').getAttribute('data-orig-height')||0);
  w=w||+(i.getAttribute('data-mw')||0);h=h||+(i.getAttribute('data-mh')||0);
  ims.push({src:srcDe(i,99999),w:w,h:h,el:i});
 });
 // sin medidas (p. ej. en reblogueos) no se puede saber cuál es la portadilla: se miden con una versión pequeñita y se vuelve a empezar
 if(!medido&&(s==='m'||s==='x')){var falta=ims.filter(function(im){return im.el&&(!im.w||!im.h);});
  if(falta.length){Promise.all(falta.map(function(im){return new Promise(function(res){var x=new Image(),ok=false;
    x.onload=function(){if(x.naturalWidth){var mx=Math.max.apply(null,(im.el.getAttribute('srcset')||'').split(',').map(function(q){return parseInt(q.trim().split(/\s+/)[1])||0;}).filter(function(v){return v>0;}).concat([x.naturalWidth]));im.el.setAttribute('data-mw',mx);im.el.setAttribute('data-mh',Math.round(mx*x.naturalHeight/x.naturalWidth));}res();};
    x.onerror=res;setTimeout(res,5000);x.setAttribute('s'+'rc',srcDe(im.el,100));});})).then(function(){post(art,meta,cat,true);});return;}}
 ims=ims.filter(function(im,k){return !esPortadilla(s,k,im,d);});
 // título: el de Tumblr, o el primer H1 del cuerpo, o la primera frase
 var h1=art.querySelector('.title h1'), t=TIT[id]||h1.textContent.trim();
 var bh=body.querySelector('h1'); if(!t&&bh){t=bh.textContent.trim();}
 if(s==='m'){var mm=(t+' '+body.textContent).replace(/&nbsp;/g,' ').match(/semana\s+([IVXLCDM]+)/i);t='mucho más » semana '+(mm?mm[1].toUpperCase():'');}
 if(!t){var tx=body.textContent.replace(/^[\s⩔]+/,'').trim(),f=tx.match(/^(.{20,140}?[.!?:])(\s|$)/);t=f?f[1]:tx.slice(0,110).replace(/\s\S*$/,'…');h1.classList.add('auto');}
 tems=tems.filter(function(i){var q=cat.temas[i];return q&&(!q.x||(q.x==='sub'&&q.e));});
 var tm=tems.length?'<div class="temas"><span class="caps">Temas »</span>'+tems.map(function(i){var q=cat.temas[i];return '<a href="'+(q.x==='sub'?'/especiales#'+q.e:'/buscador#h='+i)+'"'+(q.x==='sub'?' class="esp"':'')+'><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+(q.x==='sub'&&ESPI[q.e]||TS[i])+'"/></svg>'+esc(q.n)+'</a>';}).join('')+'</div>':'';
 if(d>='2026-10-01')subraya(body);
 ajustes(body,AJ[id],s);
 if(s==='m'||s==='x'||s==='b'||(s==='o'&&body.textContent.length>1500)){
  var o={art:art,body:body,ims:ims,d:d,id:id,cat:cat,tipos:tipos,s:s,t:t,tm:tm};
  var lbv=s==='m'?vMM(o):s==='x'?vX(o):vB(o); if(lbv.length&&window.initLB)initLB(lbv); return;
 }
 if(h1.classList.contains('auto'))h1.textContent=t; else h1.innerHTML=destaca(t); document.title=quita(t)+' · inconsolata»';
 var bico=icoEsp(mt[5],'big-ico')||(tipos[0]?ico(tipos[0],'big-ico'):'');if(bico)art.querySelector('.title').insertAdjacentHTML('beforeend',bico);
 // migas
 var cr='<a href="/">inconsolata</a><i>»</i>'+(s&&s!=='m'&&s!=='x'?'<a href="/tagged/'+encodeURIComponent(SECN[s])+'">'+SECN[s]+'</a>':tipos[0]?'<a href="/buscador#k='+tipos[0]+'">'+esc(TN[tipos[0]])+'</a>':'<span>post</span>');
 if(esp)cr+='<i>»</i><a class="k-esp" href="/especiales#'+esc(esp.slug)+'">'+esc(esp.n)+'</a>';
 if(meds.length>3)cr+='<i>»</i><span>'+meds.length+' medios</span>';
 else if(meds.length)cr+='<i>»</i>'+meds.map(function(m){return '<a href="'+fichaMedio(m)+'">'+esc(m.n)+'</a>';}).join(', ').replace(/, (<a [^>]*>[^<]*<\/a>)$/,' y $1');
 art.querySelector('.crumbs').innerHTML=cr;
 if(d<LANZAMIENTO)art.querySelector('.legacy').hidden=false;
 // cuerpo: fuera el «⩔» inicial, letra capitular, línea de fuente como bloque negro, fuera la caja de apoyo antigua
 [].forEach.call(body.querySelectorAll('blockquote'),function(b){if(/buymeacoffee|aportación/i.test(b.textContent+b.innerHTML))b.remove();});
 [].forEach.call(body.querySelectorAll('p'),function(p){
  var b=p.querySelector('b,strong');
  if(b&&b.textContent.trim()==='⩔'){var sp=b.closest('span')||b;var br=sp.nextElementSibling;sp.remove();if(br&&br.tagName==='BR')br.remove();}
 });
 var sr=(s==='m'||s==='x'||s==='b')?null:serieDe(body,id);
 // línea de fuente → bloque negro. Formato actual: «» Medio, del …»; formato antiguo: «Medio, del …» sin el símbolo
 // avatares de todos los medios citados (si no caben, van pasando)
 function avsDe(){return meds.map(function(m){return '<a class="f-av'+(m.avw?'':' f-av-l')+'" href="'+fichaMedio(m)+'" title="'+esc(m.n)+'" aria-label="Ficha de '+esc(m.n)+'">'+(m.avw?'<img src="'+m.avw+'" alt="">':esc(m.n.charAt(0)))+'</a>';}).join('');}
 // quita el «»» (y el guion de las listas antiguas) del principio, esté dentro de las etiquetas que esté
 function limpia(p){var c=p.cloneNode(true),w=document.createTreeWalker(c,NodeFilter.SHOW_TEXT),x;
  while((x=w.nextNode())){var v=x.nodeValue.replace(/^[\s\xa0]+/,'');if(!v){x.nodeValue='';continue;}x.nodeValue=v.replace(/^[»\-–]\s*/,'').replace(/^[\s\xa0]+/,'');if(x.nodeValue)break;}
  var h=c.innerHTML;for(var k=0;k<4;k++)h=h.replace(/^\s*<(b|strong|span|i|em)[^>]*>\s*<\/\1>\s*/,'');return h.replace(/^\s*(<br\s*\/?>\s*)+/,'');}
 function hazFuente(p){var dv=document.createElement('div');dv.className='fuente';var av=avsDe(),larga=p.textContent.replace(/\s+/g,' ').length>150||meds.length>3;
  dv.innerHTML=(larga?'<p class="f-res"><i>»</i> Autores y medios</p>':'')+'<p class="f-tx"><i>»</i> '+limpia(p)+'</p>'+(av?'<div class="f-avs"><div class="f-track">'+av+'</div></div>':'')+(larga?'<button type="button" class="f-mas" aria-expanded="false" aria-label="Ver autores y medios"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="M5 9l7 7 7-7"/></svg></button>':'');
  if(larga){dv.classList.add('plegable');dv.querySelector('.f-mas').addEventListener('click',function(){var ab=dv.classList.toggle('abierta');this.setAttribute('aria-expanded',ab?'true':'false');rueda(dv);});}
  p.replaceWith(dv);if(av)setTimeout(function(){rueda(dv);},0);}
 // si los avatares no caben en su hueco, pasan en bucle (se para al pasar el ratón; nada si se pide menos movimiento)
 function rueda(dv){var box=dv.querySelector('.f-avs'),tr=box&&box.querySelector('.f-track');if(!tr)return;
  var dup=tr.querySelector('.f-dup');if(dup)dup.remove();tr.classList.remove('gira');tr.style.removeProperty('--dur');
  if(dv.classList.contains('abierta')||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  if(tr.scrollWidth<=box.clientWidth+2)return;
  var w=tr.scrollWidth,c=document.createElement('span');c.className='f-dup';c.setAttribute('aria-hidden','true');c.innerHTML=tr.innerHTML;
  [].forEach.call(c.querySelectorAll('a'),function(a){a.tabIndex=-1;});tr.appendChild(c);tr.style.setProperty('--dur',Math.max(8,w/40)+'s');tr.classList.add('gira');}
 var ruedaT;addEventListener('resize',function(){clearTimeout(ruedaT);ruedaT=setTimeout(function(){[].forEach.call(document.querySelectorAll('.fuente'),rueda);},200);});
 [].forEach.call(body.querySelectorAll('p'),function(p){if(/^[\s\xa0]*»/.test(p.textContent)&&!p.closest('.fuente'))hazFuente(p);});
 if(!body.querySelector('.fuente')&&s!=='m'&&s!=='x'){
  var ps=[].filter.call(body.querySelectorAll('p'),function(p){return !p.querySelector('img');});
  var cand=ps.filter(function(p){var t=p.textContent.replace(/\xa0/g,' ').trim(),f=fold(t);return t.length<400&&/,\s+(del?|el)\s+\d{1,2}(\s|,)/.test(t)&&(t.length<=160||meds.some(function(m){return f.indexOf(fold(m.n))===0;}));});
  var fp=cand[cand.length-1];
  if(fp&&(ps.length>1||fp.textContent.trim().length<160))hazFuente(fp);
 }
 var first=[].find.call(body.querySelectorAll('p'),function(p){return !p.closest('.fuente')&&p.textContent.trim().length>40;});
 if(first&&s!=='m'&&s!=='x'){var w=document.createTreeWalker(first,NodeFilter.SHOW_TEXT),n;while((n=w.nextNode())&&!n.nodeValue.trim());
  if(n){var v=n.nodeValue.replace(/^\s+/,'');var sp=document.createElement('span');sp.className='cap';sp.textContent=v[0];n.nodeValue=v.slice(1);n.parentNode.insertBefore(sp,n);}}
 // parte visual
 var vis=art.querySelector('.visual'), lay=art.querySelector('.layout'), n=ims.length;
 var alt=function(i){return (TN[tipos[0]]||'Imagen')+(meds[0]?' de '+meds[0].n:'')+', imagen '+(i+1)+' de '+n;};
 var lb=[];
 if(s==='m'||s==='x'){
  // mucho más / EXTRA!: cada imagen con su pieza (Trabajo | Autor | Medio)
  var html='', k=0;
  ims.forEach(function(im,i){
   var cap='',el=im.el&&(im.el.closest('.npf_row')||im.el.closest('figure'));
   var nx=el&&el.nextElementSibling;
   if(nx&&nx.tagName==='P'&&/Trabajo/.test(nx.textContent)){cap=nx.innerHTML.replace(/&nbsp;|\u00a0/g,' ');nx.remove();}
   var tr=(cap.match(/Trabajo\s*<\/i>\s*:\s*([^|]*)/)||[])[1]||'', au=(cap.match(/Autor(?:a|es|as)?\s*<\/i>\s*:\s*([^|]*)/)||[])[1]||'',
       md=(cap.match(/Medio\s*<\/i>\s*:\s*<b>([^<]*)<\/b>([^|<]*)/)||[]);
   var mdo=cat.medios.find(function(m){return md[1]&&m.n.toLowerCase()===md[1].trim().toLowerCase();});
   lb.push({src:im.src,cap:(tr?tr.replace(/<[^>]+>/g,'').trim()+' · ':'')+(md[1]||'')+' · imagen '+(i+1)+' de '+n});
   html+='<article class="mm-it"><button type="button" class="shot" data-lb="'+i+'" aria-label="Ampliar imagen '+(i+1)+'"><img loading="lazy" src="'+esc(im.src)+'" alt="'+esc(tr.replace(/<[^>]+>/g,''))+'"><span class="zoom">Ampliar »</span></button>'+
    '<div class="txt"><span class="mm-n">'+(i+1)+'</span>'+(md[1]?'<span class="md">'+(mdo&&mdo.av?'<img src="'+mdo.av+'" alt="">':'')+esc(md[1].trim())+'</span>':'')+
    (tr?'<h2>'+tr+'</h2>':'')+(au?'<span class="by">por '+au.split(/\s+y\s+|,\s*/).map(function(a){return '<a href="'+fichaAutor(a.replace(/<[^>]+>/g,'').trim())+'">'+a+'</a>';}).join(', ')+'</span>':'')+
    (md[2]?'<span class="caps" style="font-size:12px">'+esc(md[2].replace(/^,\s*/,''))+'</span>':'')+'</div></article>';
  });
  vis.innerHTML='<div class="mm-items">'+html+'</div>'; lay.classList.add('single');
 } else if(n){
  var PIE=(AJ[id]&&AJ[id].pies)||{},pie=function(i){return String(PIE[i+1]||'').trim();},pieH=function(i,c){return pie(i)?'<p class="'+(c||'pie-aj')+'">'+esc(pie(i))+'</p>':'';};
  ims.forEach(function(im,i){lb.push({src:im.src,cap:(pie(i)?pie(i)+' · ':meds.length===1?meds[0].n+' · ':'')+'imagen '+(i+1)+' de '+n});});
  alt=function(i){return pie(i)||(TN[tipos[0]]||'Imagen')+(meds.length===1?' de '+meds[0].n:'')+', imagen '+(i+1)+' de '+n;};
  if(s==='d'){
   vis.innerHTML='<div class="dclips">'+ims.map(function(im,i){return '<div class="dclip"><button type="button" class="shot" data-lb="'+i+'" aria-label="Ampliar recorte '+(i+1)+'"><img src="'+esc(im.src)+'" alt="'+esc(alt(i))+'"><span class="zoom">Ampliar »</span></button>'+pieH(i)+'</div>';}).join('')+'</div>';
   lay.classList.add('single');
  } else {
   var h='<div class="main-sheet"><span class="tape" aria-hidden="true"></span><button type="button" class="shot" data-lb="0" aria-label="Ampliar imagen 1 de '+n+'"><img src="'+esc(ims[0].src)+'" alt="'+esc(alt(0))+'"><span class="zoom">Ampliar »</span></button>'+pieH(0)+'</div>';
   if(n>1)h+='<div><div class="sheet-head"><span class="caps">Todas las imágenes · '+n+'</span><span style="font-size:13px;font-weight:600">Pulsa para ampliar »</span></div><div class="contact'+(n<=4?' c2':'')+'">'+
     ims.slice(1).map(function(im,j){var i=j+1;return '<div class="frame"><button type="button" class="shot" data-lb="'+i+'" aria-label="Ampliar imagen '+(i+1)+' de '+n+'"><img loading="lazy" src="'+esc(im.src)+'" alt="'+esc(alt(i))+'"><span class="zoom">Ampliar »</span></button><span class="n">'+(i+1)+' / '+n+' <span style="color:var(--accent)">▸</span></span>'+pieH(i,'pie-f')+'</div>';}).join('')+'</div></div>';
   vis.innerHTML=h; if(n===1)lay.classList.add('single');
  }
 } else { vis.remove(); lay.classList.add('single'); }
 ims.forEach(function(im){if(im.el){var r=im.el.closest('.npf_row')||im.el.closest('figure')||im.el;r.remove();}});
 // ficha
 var dl='';
 if(meds.length)dl+='<dt>Medio'+(meds.length>1?'s':'')+'</dt><dd>'+meds.map(function(m){return '<a href="'+fichaMedio(m)+'">'+esc(m.n)+'</a>'+(m.pais?' · '+esc(m.pais):'');}).join('<br>')+'</dd>';
 dl+='<dt>Fecha</dt><dd>'+fecha(d)+'</dd>';
 if(tipos.length)dl+='<dt>Tipo</dt><dd>'+tipos.map(function(k){return esc(TN[k]);}).join(', ')+'</dd>';
 if(auts.length&&s!=='m'&&s!=='x')dl+='<dt>Créditos</dt><dd>'+auts.map(function(a){return '<a class="credit" href="'+fichaAutor(a)+'">'+esc(a)+'</a>';}).join(', ')+'</dd>';
 var lgs=meds.filter(function(m){return m.logo;});
 var logo=lgs.length?'<div class="m-id'+(lgs.length>1?' multi':'')+(lgs.length>4?' mucho':'')+'">'+lgs.map(function(m){return '<a href="'+fichaMedio(m)+'" aria-label="Ficha de '+esc(m.n)+'"><img class="m-logo" src="'+m.logo+'" alt="Logo de '+esc(m.n)+'" onerror="var d=this.closest(\'.m-id\');this.parentNode.remove();if(d&&!d.querySelector(\'img\'))d.remove()"></a>';}).join('')+'</div>':'';
 art.querySelector('.ficha').innerHTML='<span class="tape" aria-hidden="true"></span><span class="caps">Ficha »</span>'+logo+'<dl>'+dl+'</dl>'+tm+(esp?'<div class="temas esps"><a class="esp" href="/especiales#'+esc(esp.slug)+'">'+(ESPI[esp.slug]?'<svg viewBox="0 0 64 64" aria-hidden="true"><use href="#'+ESPI[esp.slug]+'"/></svg>':'')+esc(esp.n)+'</a></div>':'');
 if(sr)lay.insertAdjacentHTML('afterend',serieHTML(sr));
 if(lb.length&&window.initLB)initLB(lb);
}

// ------------------------------------------------------------------ listados (provisional)
function listado(meta,cat){
 [].forEach.call(document.querySelectorAll('.lc'),function(c){
  var cid=rid(c), mt=meta[cid]; if(!mt)return;
  var m=cat.medios[mt[2][0]], k=c.querySelector('.kicker');
  if(mt[0]&&SECN[mt[0]])c.insertAdjacentHTML('afterbegin','<span class="sec">'+SECN[mt[0]]+'</span>');
  if(m)k.innerHTML=medsK(mt[2].map(function(i){return cat.medios[i];}))+' · '+k.textContent.replace(/^»\s*/,'');
  var tt=c.querySelector('.tt'),tid=TIT[cid]; if(tid&&mt[0]!=='m')tt.textContent=quita(tid); if(!tt.textContent.trim()){var tx=(c.dataset.txt||'').replace(/<([^<>]{1,120})>/g,'$1').replace(/^[\s⩔]+/,'');var f=tx.match(/^(.{20,120}?[.!?:])(\s|$)/);tt.textContent=f?f[1]:tx.slice(0,100)+'…';}
  if(mt[0]==='m'){var mm=((tid||'')+' '+(c.dataset.txt||'')).replace(/&nbsp;/g,' ').match(/semana\s+([IVXLCDM]+)/i);tt.textContent='mucho más » semana '+(mm?mm[1].toUpperCase():'');}
  var ph=c.querySelector('.ph img'); if(ph&&!ph.getAttribute('src')){var u=(c.dataset.img||'').trim().split(/\s+/)[0];
   if(!u){var tp=c.querySelector('template.lb-body');if(tp){var ims=[].map.call(tp.content.querySelectorAll('img'),function(i){return {u:srcDe(i,600),w:+(i.getAttribute('data-orig-width')||0),h:+(i.getAttribute('data-orig-height')||0)};});
    var ok=ims.filter(function(im,k){return !esPortadilla(mt[0],k,im,'2099');});u=(ok[0]||ims[0]||{}).u;}}
   if(u)ph.setAttribute('s'+'rc',u);else ph.remove();}
 });
}

Promise.all([get('meta'),get('catalogo'),get('titulos').catch(function(){return {};}),get('ajustes_posts').catch(function(){return {};})]).then(function(r){
 TIT=r[2]||{};AJ=r[3]||{};
 // logos y avatares fijados al mismo commit que el código (así no se quedan versiones viejas en caché)
 if(window.INC_BASE)r[1].medios.forEach(function(m){['av','avw','logo'].forEach(function(k){if(m[k])m[k]=m[k].replace('https://cdn.jsdelivr.net/gh/inconsolataweb/inconsolata-datos@main/',INC_BASE);});});
 autocompleta(r[1]);META0=r[0]||{};cat0=r[1];prepEspIcos(r[1]);
 var art=document.querySelector('article.post'); if(RUTA)pagina(r[0],r[1]); else if(art)post(art,r[0],r[1]); else if(document.body.classList.contains('es-portada'))portada(r[0],r[1]); else listado(r[0],r[1]);
}).catch(function(e){console.error('inconsolata»: no se pudieron cargar los datos',e);});
document.addEventListener('click',function(e){var b=e.target.closest('.share .cp');if(!b)return;var u=b.dataset.u||location.href;
 var fin=function(){b.classList.add('done');b.setAttribute('aria-label','Enlace copiado');setTimeout(function(){b.classList.remove('done');b.setAttribute('aria-label','Copiar enlace');},1800);};
 if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(u).then(fin,fin);else{var t=document.createElement('textarea');t.value=u;document.body.appendChild(t);t.select();try{document.execCommand('copy');}catch(x){}t.remove();fin();}});
// sugerencias de medios con ficha y autores mientras se escribe en el buscador de la cabecera
function autocompleta(cat){
 var M=cat.medios.map(function(m,i){return {t:'m',n:m.n,k:fold(m.n),u:m.ficha?fichaMedio(m):'/buscador#m='+i,av:m.av,f:m.ficha};}).filter(function(o){return o.f;}),
     A=cat.autores.map(function(n,i){var mi=cat.am?cat.am[i]:-1,m=mi>=0?cat.medios[mi]:null;return {t:'a',n:n,k:fold(n),u:fichaAutor(n),av:m&&m.av,md:m&&m.n};});
 function busca(q){q=fold(q.trim());if(q.length<2)return [];var ok=function(o){var i=o.k.indexOf(q);return i===0||(i>0&&/[\s(.'-]/.test(o.k[i-1]));};
  return M.filter(ok).slice(0,4).concat(A.filter(ok).slice(0,6));}
 [].forEach.call(document.querySelectorAll('.srch'),function(f){var inp=f.querySelector('input'),box=document.createElement('div'),sel=-1,L=[];
  box.className='ac';box.hidden=true;box.setAttribute('role','listbox');box.id='ac-'+inp.id;f.appendChild(box);inp.setAttribute('aria-controls',box.id);inp.setAttribute('aria-autocomplete','list');
  function pinta(){box.innerHTML=L.map(function(o,i){return '<a href="'+o.u+'" role="option" class="'+(i===sel?'on':'')+'">'+(o.av?'<img src="'+esc(o.av)+'" alt="">':'<span class="ini'+(o.t==='a'?' a':'')+'">'+esc(o.n.charAt(0))+'</span>')+'<span class="nm">'+esc(o.n)+'</span><small>'+(o.t==='m'?'medio':'autor'+(o.md?' · '+esc(o.md):''))+'</small></a>';}).join('')+
   (inp.value.trim()?'<a href="/buscador#q='+encodeURIComponent(inp.value.trim())+'" class="todo'+(sel===L.length?' on':'')+'">Buscar «'+esc(inp.value.trim())+'» en todo el archivo »</a>':'');box.hidden=!inp.value.trim();}
  inp.addEventListener('input',function(){L=busca(inp.value);sel=-1;pinta();});
  inp.addEventListener('keydown',function(e){if(box.hidden)return;var n=L.length+1;
   if(e.key==='ArrowDown'){sel=(sel+1)%n;pinta();e.preventDefault();}else if(e.key==='ArrowUp'){sel=(sel+n-1)%n;pinta();e.preventDefault();}
   else if(e.key==='Escape'){box.hidden=true;}else if(e.key==='Enter'&&sel>=0&&sel<=L.length){e.preventDefault();e.stopImmediatePropagation();box.querySelectorAll('a')[sel].click();}});
  document.addEventListener('click',function(e){if(!f.contains(e.target))box.hidden=true;});});
}
// el buscador pequeño de la cabecera lleva al buscador
[].forEach.call(document.querySelectorAll('.srch'),function(f){f.addEventListener('submit',function(){var v=f.querySelector('input').value.trim();location.href='/buscador'+(v?'#q='+encodeURIComponent(v):'');});});
})();
"""

LEGACY = ('<div class="legacy" role="note" hidden><span class="lg-i" aria-hidden="true">»</span>'
          '<p><b>Post del archivo.</b> Se publicó originalmente en una versión anterior de inconsolata» '
          'y puede que algún elemento no se vea como debería. '
          '<a href="mailto:inconsolataweb@gmail.com?subject=Algo%20roto%20en%20un%20post">¿Ves algo roto? Avísame »</a></p></div>')

POST_CONTENT = """{block:Text}{Body}{/block:Text}{block:Photo}{Caption}{/block:Photo}{block:Photoset}{Caption}{/block:Photoset}{block:Video}<div class="vid">{Video-700}</div>{Caption}{/block:Video}{block:Quote}<blockquote class="q">{Quote}</blockquote>{block:Source}<p>— {Source}</p>{/block:Source}{/block:Quote}{block:Link}<p><a href="{URL}">{Name}</a></p>{block:Description}{Description}{/block:Description}{/block:Link}{block:Audio}{AudioEmbed}{block:Caption}{Caption}{/block:Caption}{/block:Audio}{block:Chat}{block:Lines}<p><b>{Label}</b> {Line}</p>{/block:Lines}{/block:Chat}"""
RAW_PHOTOS = """<div class="post-raw" aria-hidden="true">{block:Photo}<img data-hr="{PhotoURL-HighRes}" data-w="{PhotoWidth-HighRes}" data-h="{PhotoHeight-HighRes}" alt="">{/block:Photo}{block:Photoset}{block:Photos}<img data-hr="{PhotoURL-HighRes}" data-w="{PhotoWidth-HighRes}" data-h="{PhotoHeight-HighRes}" alt="">{/block:Photos}{/block:Photoset}</div>"""

PERMALINK = f"""{{block:PermalinkPage}}{{block:Posts}}
<article class="post" data-id="{{PostID}}" data-perm="{{Permalink}}" data-tags="{{block:Tags}}{{Tag}}|{{/block:Tags}}" data-root="{{block:RebloggedFrom}}{{ReblogRootURL}}{{/block:RebloggedFrom}}" data-date="{{Year}}-{{MonthNumberWithZero}}-{{DayOfMonthWithZero}}">
<div style="padding-top:20px">{LEGACY}</div>
<div class="crumbs caps"><a href="/">inconsolata</a></div>
<section class="title"><h1 class="soft">{{block:Title}}{{Title}}{{/block:Title}}</h1></section>
<section class="layout">
<div class="visual"></div>
<aside class="aside">
<div class="ficha"><span class="tape" aria-hidden="true"></span><span class="caps">Ficha »</span></div>
<div class="body">{POST_CONTENT}</div>
{RAW_PHOTOS}
<div style="display:flex;flex-direction:column;gap:10px"><span class="caps">Compartir</span>
<div class="share"><a href="https://bsky.app/intent/compose?text={{URLEncodedPermalink}}" target="_blank" rel="noopener" aria-label="Compartir en Bluesky" title="Bluesky"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="currentColor" d="M12 10.8c-1.087-2.114-4.046-6.053-6.798-7.995C2.566.944 1.561 1.266.902 1.565.139 1.908 0 3.08 0 3.768c0 .69.378 5.65.624 6.479.815 2.736 3.713 3.66 6.383 3.364.136-.02.275-.039.415-.056-.138.022-.276.04-.415.056-3.912.58-7.387 2.005-2.83 7.078 5.013 5.19 6.87-1.113 7.823-4.308.953 3.195 2.05 9.271 7.733 4.308 4.267-4.308 1.172-6.498-2.74-7.078a8.741 8.741 0 0 1-.415-.056c.14.017.279.036.415.056 2.67.297 5.568-.628 6.383-3.364.246-.828.624-5.79.624-6.478 0-.69-.139-1.861-.902-2.206-.659-.298-1.664-.62-4.3 1.24C16.046 4.748 13.087 8.687 12 10.8Z"/></svg></a><a href="https://x.com/intent/post?url={{URLEncodedPermalink}}" target="_blank" rel="noopener" aria-label="Compartir en X" title="X"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="currentColor" d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"/></svg></a><a href="{{ReblogURL}}" aria-label="Rebloguear en Tumblr" title="Reblog"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="currentColor" d="M7 7h10v3l4-4-4-4v3H5v6h2V7zm10 10H7v-3l-4 4 4 4v-3h12v-6h-2v4z"/></svg></a><button type="button" class="cp" aria-label="Copiar enlace" title="Copiar enlace" data-u="{{Permalink}}"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="currentColor" d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"/></svg><span class="ok"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="currentColor" d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"/></svg></span></button></div></div>
<a href="{APOYA}" class="support"><span class="soft" style="font-size:30px;line-height:1">¿Te gusta lo que hago?</span><span style="font-size:15px;line-height:1.4">Si quieres ayudarme, puedes hacerlo con una aportación.</span><span class="caps">Apóyanos »</span></a>
</aside>
</section>
</article>
{{/block:Posts}}
{{block:PermalinkPagination}}<nav class="pn" aria-label="Posts anterior y siguiente">{{block:NextPost}}<a href="{{NextPost}}"><span class="caps">« Anterior</span><span class="t">Post anterior</span></a>{{/block:NextPost}}{{block:PreviousPost}}<a href="{{PreviousPost}}"><span class="caps">Siguiente »</span><span class="t">Post siguiente</span></a>{{/block:PreviousPost}}</nav>{{/block:PermalinkPagination}}
{{/block:PermalinkPage}}"""

LIST = """{block:IndexPage}
{block:TagPage}<div class="tag-head"><span class="caps" style="color:var(--accent)">Etiqueta »</span><h1 class="soft">{Tag}</h1></div>{/block:TagPage}
{block:SearchPage}<div class="tag-head"><span class="caps" style="color:var(--accent)">Búsqueda »</span><h1 class="soft">{SearchQuery}</h1></div>{/block:SearchPage}
<div class="lst">{block:Posts}<a class="lc" href="{Permalink}" data-id="{PostID}" data-date="{Year}-{MonthNumberWithZero}-{DayOfMonthWithZero}" data-tags="{block:Tags}{Tag}|{/block:Tags}" data-hr="{block:Photo}{PhotoURL-HighRes}{/block:Photo}{block:Photoset}{block:Photos}{PhotoURL-HighRes} {/block:Photos}{/block:Photoset}" data-link="{block:Link}{URL}{/block:Link}" data-root="{block:RebloggedFrom}{ReblogRootURL}{/block:RebloggedFrom}" data-txt="{block:Text}{PlaintextBody}{/block:Text}{block:Photo}{PlaintextCaption}{/block:Photo}{block:Photoset}{PlaintextCaption}{/block:Photoset}{block:Link}{PlaintextDescription}{/block:Link}" data-img="{block:Photo}{PhotoURL-500}{/block:Photo}{block:Photoset}{block:Photos}{PhotoURL-500} {/block:Photos}{/block:Photoset}{block:Text}{block:Thumbnail}{ThumbnailURL}{/block:Thumbnail}{/block:Text}"><div class="ph"><img loading="lazy" src="" alt=""></div><span class="kicker">» {DayOfMonth} {ShortMonth} {Year}</span><span class="tt">{block:Title}{Title}{/block:Title}{block:Link}{Name}{/block:Link}</span><template class="lb-body">{block:Text}{Body}{/block:Text}{block:Link}{Description}{/block:Link}</template></a>{/block:Posts}</div>
{block:Pagination}<nav class="pag">{block:PreviousPage}<a href="{PreviousPage}">« Más recientes</a>{/block:PreviousPage}<span></span>{block:NextPage}<a href="{NextPage}">Más antiguos »</a>{/block:NextPage}</nav>{/block:Pagination}
{/block:IndexPage}"""

_H = os.path.dirname(os.path.abspath(__file__))
_CAT = next(p for p in (os.path.join(_H, '..', '..', 'datos', 'catalogo.json'), '/home/claude/inconsolata-datos/datos/catalogo.json') if os.path.exists(p))
_TEM = [t['n'] for t in json.load(open(_CAT))['temas']]
BIENVENIDA = r'''
// /bienvenida: la página de presentación ocupa toda la ventana (se sirve desde los datos, igual que el resto del código)
window.INC_BV=/\/bienvenida(\.html)?\/?$/.test(location.pathname);
(function(){if(!window.INC_BV)return;var h=document.documentElement;h.style.visibility='hidden';
 fetch((window.INC_BASE||'https://cdn.jsdelivr.net/gh/inconsolataweb/inconsolata-datos@main/')+'assets/bienvenida/index.html').then(function(r){if(!r.ok)throw new Error(r.status);return r.text();})
 .then(function(t){window.INC_BIENVENIDA=1;document.open();document.write(t);document.close();})
 .catch(function(e){console.error('inconsolata»: bienvenida',e);h.style.visibility='';});})();
'''
JS_FINAL = BIENVENIDA + JS.replace('__SYMS__', json.dumps('<svg width="0" height="0" style="position:absolute" aria-hidden="true">' + re.sub(r'</?svg[^>]*>', '', symbols() + tema_symbols()) + '</svg>', ensure_ascii=False)).replace('__VJS__', VJS.replace('ESPIRAL', json.dumps(ESPIRAL_COLOR))).replace('__TN__', json.dumps({k: v[0] for k, v in TIPOS.items()}, ensure_ascii=False)).replace('__TS__', json.dumps([tslug(n) for n in _TEM])).replace('__PJS__', PJS).replace('__PAGJS__', PAG_JS)
JS_FINAL += r"""
(function(){var h=document.documentElement,v=null;try{v=localStorage.getItem('inc-version');}catch(e){}
 if(v==='completa')h.classList.remove('lite');else if(v==='lite')h.classList.add('lite');
 var sw=document.querySelector('.ver-sw');if(sw)sw.hidden=h.classList.contains('lite')||innerWidth>900;
 var m=document.getElementById('lite-menu'),bm=document.querySelector('[data-lite=menu]');
 function abre(o){if(!m)return;m.hidden=!o;if(bm)bm.setAttribute('aria-expanded',o?'true':'false');document.body.classList.toggle('lm-abierto',o);}
 document.addEventListener('click',function(e){var b=e.target.closest('[data-lite],[data-version]');
  if(!b){if(m&&!m.hidden&&e.target.closest('#lite-menu a'))abre(false);return;}
  if(b.dataset.version){try{localStorage.setItem('inc-version',b.dataset.version);}catch(x){}location.reload();return;}
  if(b.dataset.lite==='menu')abre(m.hidden);
  if(b.dataset.lite==='buscar'){abre(true);var q=document.getElementById('q-lite');if(q)q.focus();}});
 document.addEventListener('keydown',function(e){if(e.key==='Escape'&&m&&!m.hidden){abre(false);if(bm)bm.focus();}});})();

document.addEventListener('click',function(e){var b=e.target.closest('.dd-b');document.querySelectorAll('.dd').forEach(function(d){var bt=d.querySelector('.dd-b'),m=d.querySelector('.dd-m'),ab=b&&d.contains(b)?bt.getAttribute('aria-expanded')!=='true':false;bt.setAttribute('aria-expanded',ab?'true':'false');m.hidden=!ab;});});
document.addEventListener('keydown',function(e){if(e.key==='Escape')document.querySelectorAll('.dd-b[aria-expanded=true]').forEach(function(b){b.click();b.focus();});});
"""
JS_FINAL = JS_FINAL[:len(BIENVENIDA)] + 'if(!window.INC_BV){\n' + JS_FINAL[len(BIENVENIDA):] + '\n}'
page = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{block:PostTitle}}{{PostTitle}} · {{/block:PostTitle}}{{Title}}</title>
<meta name="description" content="{{MetaDescription}}">
<link rel="icon" href="https://cdn.jsdelivr.net/gh/inconsolataweb/inconsolata-datos@main/assets/marca/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="https://cdn.jsdelivr.net/gh/inconsolataweb/inconsolata-datos@main/assets/marca/favicon-32.png"><link rel="apple-touch-icon" href="https://cdn.jsdelivr.net/gh/inconsolataweb/inconsolata-datos@main/assets/marca/apple-touch-icon.png">
<link rel="alternate" type="application/rss+xml" href="{{RSS}}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://cdn.jsdelivr.net">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1;1,9..144,100..900,0..100,0..1&display=swap">
<style>{CSS}{HEAD_CSS}{MINI_CSS}{TEMAS_CSS}{LEGACY_CSS}{LB_CSS}{TCSS}{VCSS}{PCSS}{PAG_CSS}</style>
</head>
<body>
{{block:IndexPage}}<script>if(/(^[/]$|[/]index[.]html$)/.test(location.pathname))document.body.classList.add('es-portada');</script>{{/block:IndexPage}}<script>if(/[/](buscador|medios|autores|estadisticas|especiales|novedades|cronologia)([.]html)?[/]?$/.test(location.pathname))document.body.classList.add('es-pagina');</script>
{symbols()}{tema_symbols()}
<script>if(matchMedia('(max-width:760px)').matches)document.documentElement.classList.add('lite')</script>
<div class="page">
{LITE}{HEAD}
<div id="home"></div>
<main class="wrap">
{PERMALINK}
{LIST}
</main>
<footer>
<div class="cmyk-bar" aria-hidden="true"><span style="background:#00A0DC"></span><span style="background:#66C6EA"></span><span style="background:#E5007E"></span><span style="background:#EF66B2"></span><span style="background:#FFD400"></span><span style="background:#FFE566"></span><span style="background:#16140F"></span><span style="background:#7A766C"></span></div>
<div class="wrap foot"><span class="soft" style="font-size:56px;line-height:1">inc<span style="color:#D1006F">»</span></span><span>© inconsolata» 2011–<span id="y-now">2026</span> · un blog de Saúl Castillo<br><button type="button" class="ver-sw" data-version="lite" hidden>Ver la versión lite</button></span><span style="display:flex;gap:20px;font-weight:700;text-transform:uppercase;letter-spacing:1px"><a href="https://x.com/inconsolata">X</a><a href="{{RSS}}">RSS</a><a href="{APOYA}" style="color:var(--yellow)">Apóyanos »</a></span></div>
</footer>
</div>
{LB_HTML}
<script>{LB_JS.replace("img.onerror=function(){img.onerror=null; img.src=list[cur].src;};",'').replace('img.src=big(list[cur].src);',"img.setAttribute('s'+'rc',list[cur].src);")}</script>
<script>{JS_FINAL}</script>
{MINI_JS}
</body>
</html>
"""
# Tumblr no admite «{» sueltos en el CSS/JS que se parezcan a variables: comprobación rápida
bad = re.findall(r'\{(?:text|color|font|image|lang|select):|\{[A-Z][A-Za-z0-9-]*\}', JS_FINAL)
assert not bad, bad
# Instrument Sans: solo el texto del destacado, de la ficha y del cuadro negro de los posts (el resto sigue en Archivo)
page = page.replace("fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&", "fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&")
open(OUT, 'w').write(page)
print('ok', round(len(page.encode()) / 1024), 'KB')
