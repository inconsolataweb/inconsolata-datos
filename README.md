# inconsolata-datos

Datos y recursos de [inconsolata»](https://inconsolata.com), el blog de diseño periodístico de Saúl Castillo.

- `datos/indice.json`: índice del archivo para el buscador (posts, medios, autores y temas).
- `datos/estadisticas.json`: cifras totales y por año.
- `datos/especiales.json`: temas especiales (cada uno es una etiqueta de Tumblr).
- `datos/fichas_medios.json`: datos de las fichas de medios (Wikidata/Wikipedia, CC BY-SA).
- `datos/temas.json`: lista cerrada de temas.
- `datos/assets.json` y `assets/medios/`: avatares y logos de los medios.

La web lee estos archivos a través de jsDelivr. Un proceso automático los actualiza cada noche con los posts nuevos.

## Actualización automática

`.github/workflows/actualizar.yml` ejecuta `scripts/actualizar.py` cada noche (y a mano desde la pestaña *Actions → Actualizar datos → Run workflow*). Lee los últimos posts de Tumblr con la clave guardada en el secreto `TUMBLR_API_KEY`, los clasifica por etiquetas y texto, y actualiza índice, estadísticas y especiales.

Los autores y medios que aparecen por primera vez no se publican solos: quedan en `datos/pendientes.json` para revisarlos.
