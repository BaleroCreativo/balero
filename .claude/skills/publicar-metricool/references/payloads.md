# Ejemplos de borradores para Metricool

Todos usan `draft: true`. Sustituye `blogId`, fechas y textos. Zona horaria de ejemplo: America/Mexico_City (UTC−6).

## Instagram, carrusel de 5 imágenes
Parámetros de la llamada:
- `blogId`: `<id de la ficha>`
- `date`: `2026-10-30T10:00:00-06:00`

`info`:
```json
{
  "autoPublish": true,
  "descendants": [],
  "draft": true,
  "firstCommentText": "",
  "hasNotReadNotes": false,
  "media": ["https://...1.png", "https://...2.png", "https://...3.png", "https://...4.png", "https://...5.png"],
  "mediaAltText": ["ALT 1", "ALT 2", "ALT 3", "ALT 4", "ALT 5"],
  "providers": [{"network": "instagram"}],
  "publicationDate": {"dateTime": "2026-10-30T10:00:00", "timezone": "America/Mexico_City"},
  "shortener": false,
  "smartLinkData": {"ids": []},
  "text": "Caption del guion\n\n#Hashtag1 #Hashtag2",
  "instagramData": {"type": "POST", "showReelOnFeed": true, "isAiGenerated": false}
}
```

## Facebook, mismo carrusel
Cambia `providers` a `[{"network": "facebook"}]` y `instagramData` por `"facebookData": {"type": "POST"}`. Reusa las URLs de `media` que devolvió Metricool al crear el de Instagram.

## LinkedIn, carrusel como PDF
Cambia `providers` a `[{"network": "linkedin"}]` y agrega:
```json
"linkedinData": {"documentTitle": "Titular de la portada", "publishImagesAsPDF": true, "previewIncluded": true, "type": "POST"}
```
El texto lleva el enlace con UTM (`utm_content=<pieza>`).

## LinkedIn, poll
Sin `media`. En `linkedinData`:
```json
{"previewIncluded": true, "type": "poll", "poll": {"question": "Pregunta", "options": [{"text": "Opción 1"}, {"text": "Opción 2"}, {"text": "Opción 3"}, {"text": "Otro (cuéntanos)"}], "settings": {"duration": "SEVEN_DAYS"}}}
```

## Actualizar un borrador
`updateScheduledPost` pide `id`, `uuid`, `blogId` e `info` completo. Guarda el `id` que devuelve la respuesta: cambia en cada actualización.

## Subida a Notion (resumen)
1. `notion-create-file-upload` por cada PNG → devuelve un id y la dirección de subida.
2. `curl` del archivo a esa dirección con el token exacto y revisión del código HTTP.
3. En la propiedad Recurso: `{"type": "file_upload", "file_upload": {"id": "<id>"}}` por archivo.
4. Para URLs temporales: `notion-fetch` con `include_file_urls` o `notion-get-file-download-urls`; duran 5 minutos.
