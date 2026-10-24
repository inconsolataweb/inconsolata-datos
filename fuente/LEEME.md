# Fuente del tema de inconsolata»

Aquí está el código que genera el tema. Lo que se publica es la carpeta `tema/`:

- `tema/tema.html` — lo único que se pega en Tumblr (estructura y etiquetas de Tumblr). Solo hay que volver a pegarlo si cambia la estructura.
- `tema/tema.css` y `tema/tema.js` — estilos y código. El tema los carga desde jsDelivr fijados al último commit, así que basta con subirlos al repositorio.

Para regenerar:

```
python3 fuente/gen/tumblr_theme.py /tmp/tema.html
python3 fuente/scripts/ascii_tema.py /tmp/tema.html /tmp/tema-ascii.html
python3 fuente/scripts/partir_tema.py /tmp/tema-ascii.html tema
```

- `gen/tumblr_theme.py`: plantilla general (post, listado) y montaje.
- `gen/tema_vistas.*`: vistas de mucho más, EXTRA! y metablog.
- `gen/tema_portada.*`: portada y avisos.
- `gen/tema_paginas.*`: buscador, medios, autores, estadísticas, especiales y novedades.
- `html/`: maquetas de las que se toman los estilos de la portada y del mucho más.
- `scripts/sim_sitio.py`: mini web de prueba a partir de un volcado de la API.
