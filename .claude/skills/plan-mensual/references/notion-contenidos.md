# Base de Contenidos en Notion

Antes de crear filas, haz `notion-fetch` de la colección del cliente (ID en su ficha, sección Conexiones) para leer el esquema real. Lo de abajo describe la base de Balero y sirve de guía; otro cliente puede tener opciones distintas.

## Propiedades (base de Balero)
| Propiedad | Tipo | Valores o notas |
|---|---|---|
| Nombre | título | Convención `DD Mes · Día · tema` |
| Etapa | estado | Idea, Revisión, Guionizado, Diseño, Grabación, Edición, Realizado, Programado, Publicado, Archivado |
| Formato | select | Carrusel, Stories, Reel, Post, Tweet, Artículo de newsletter, Encuesta, Blog |
| Plataforma | multi-select | Facebook, Linkedin, Instagram, TikTok, Threads, Tweet, Google Ads |
| Pilar de contenido | select | Educación y Concientización, Promociones y ventas, Informativo, Servicios, Autoridad, Autoridad y rendimiento, Testimonios y Casos de Éxito, Entretenimiento, entre otros |
| Publicación | fecha con hora | Con zona horaria |
| Recurso | archivos | Aquí van las imágenes (etapa de diseño) |
| 📂 Proyectos | relación | Máximo una página (el proyecto del cliente) |
| Responsable | persona | Opcional |

## Ejemplo de creación (herramienta `notion-create-pages`)
Padre: la colección de Contenidos. Propiedades de una fila:

```json
{
  "Nombre": "16 Oct · Vie · Postura de cómo cotizamos",
  "Etapa": "Idea",
  "Formato": "Carrusel",
  "Plataforma": "[\"Instagram\",\"Facebook\"]",
  "Pilar de contenido": "Autoridad",
  "date:Publicación:start": "2026-10-16T10:00:00-06:00",
  "date:Publicación:is_datetime": 1,
  "📂 Proyectos": "[\"https://app.notion.com/p/<id-de-la-pagina-del-proyecto>\"]"
}
```

Notas aprendidas:
- Las propiedades de fecha usan el nombre expandido `date:Publicación:start` y `date:Publicación:is_datetime`.
- Plataforma y la relación se pasan como texto con un arreglo JSON.
- Si una opción de select no existe, la creación falla con "Invalid select value". En ese caso hay que ampliar las opciones del esquema, restateando todas las existentes, y solo con aprobación del usuario.
- El contenido de la fila (guion, caption) no se escribe en esta etapa; queda vacío o con una nota de una línea con el tema.

## Consulta de lo que ya existe en el mes
Con `notion-query-data-sources` en modo SQL, por ejemplo:
```sql
SELECT url, Nombre, Plataforma, Formato, "date:Publicación:start" AS d
FROM "collection://<id>"
WHERE "date:Publicación:start" >= '2026-11-01' AND "date:Publicación:start" < '2026-12-01'
ORDER BY d
```
