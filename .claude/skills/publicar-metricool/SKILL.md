---
name: publicar-metricool
description: Sube las imágenes aprobadas de una pieza a la columna Recurso y al cuerpo de su página en Notion y crea los borradores en Metricool (Instagram, Facebook, LinkedIn, polls) con imágenes, caption de cada red, texto ALT, hora y zona horaria correctas, sin programar nada. Es la etapa 7 del sistema de contenido mensual. Úsala siempre que el usuario diga "sube las imágenes", "crea los borradores", "pasa esto a Metricool", "agrega las imágenes a los posts", "programa" (aquí solo crea borradores), "pon las imágenes en el recurso de los posts" o cuando una pieza ya tenga el visto bueno de revisión visual, aunque no mencione Metricool.
---

# Publicar borradores en Metricool

Lleva una pieza aprobada de Notion a Metricool como borrador, con todo lo que la red necesita. El producto es un borrador revisable. Programar y publicar lo decide una persona, porque ese es el último punto donde se atrapa un dato dudoso o un permiso que falta.

## Antes de empezar
Verifica estas condiciones; si una falla, para y dilo:
1. La pieza tiene **visto bueno de revisión visual** y los PNG finales (y PDF para LinkedIn si aplica).
2. El guion está en Notion con captions por red y el estado de pendientes.
3. La ficha del cliente trae marca de Metricool, zona horaria y redes conectadas.
4. No existe ya una publicación de esa pieza en esa fecha y red. Consulta `getScheduledPosts` por rangos cortos (una o dos semanas, el resultado es largo). Si la persona ya programó algo por su cuenta, no lo toques ni lo dupliques.

## Flujo por pieza

### 1. Subir las imágenes a Notion (Recurso)
Los PNG finales se adjuntan a la fila de la pieza para que el equipo los tenga junto al guion:
1. Crea una carga de archivo por imagen con `notion-create-file-upload`.
2. Sube el archivo con `curl` a la dirección que devuelve, con el token exacto. Copia el token completo y verifica el código de respuesta; un carácter mal copiado fue el error más repetido de octubre.
3. Adjunta los archivos a la propiedad **Recurso** de la fila (tipo `file_upload`) y, si el equipo lo quiere visible, inserta las imágenes en el cuerpo de la página bajo "Diseño del carrusel".
4. Sube solo PNG a esta columna junto con el PDF de LinkedIn. Cambia **Etapa** a "Diseño" si aún no lo está.

### 2. Crear el primer borrador con URLs frescas de Notion
Metricool descarga cada imagen desde una URL pública. Las URLs firmadas de Notion (de `notion-fetch` con `include_file_urls`) caducan en 5 minutos, así que:
- Pide las URLs **justo antes** de crear el borrador y pásalas de inmediato.
- Si Metricool responde "Failed to normalize media", las URLs ya caducaron: vuelve a pedirlas y reintenta rápido (con muchas imágenes, la llamada tarda; ahí influye el tamaño del texto y de las URLs).
- Empieza por la red con más restricciones: Instagram exige imagen y no admite borrador sin ella.

### 3. Reusar las imágenes ya alojadas
La respuesta de Metricool devuelve las imágenes re-alojadas (`static.metricool.com`), que no caducan. Úsalas como `media` para los demás borradores de la misma pieza (Facebook, LinkedIn). Así se evita volver a pedir URLs firmadas y se garantiza que todas las redes llevan exactamente las mismas imágenes.

### 4. Campos del borrador
Usa `createScheduledPost` con el `blogId` de la ficha y un `info` con esta forma (ejemplos completos en `references/payloads.md`):
- `draft: true` siempre, y `autoPublish: true` (solo afecta cuando alguien lo programe).
- `providers`: una red por borrador; así cada una tiene su caption y su hora.
- `publicationDate` con `dateTime` local y `timezone` IANA de la ficha. `date` en formato ISO con el desplazamiento correcto (CDMX es UTC−6).
- `text`: el caption de esa red desde el guion, con los marcadores `[BORRADOR: …]` intactos. Sirven para que nadie programe sin ver lo pendiente.
- `mediaAltText`: una frase por imagen. Parte del ALT borrador del guion y **ajústalo mirando la portada y cualquier slide con cifras**, porque el guion describe lo planeado y no siempre lo que quedó.
- Datos por red: Instagram `instagramData {type: "POST"}`; Facebook `facebookData {type: "POST"}`; LinkedIn con carrusel `linkedinData {publishImagesAsPDF: true, documentTitle: "<titular de portada>", type: "post"}`; LinkedIn poll con `type: "poll"` y sus opciones.
- No envíes datos de una red que no esté en `providers` (por ejemplo `twitterData`): Metricool rechaza el borrador.
- `shortener: false`, `smartLinkData: {ids: []}`.
- Los enlaces con UTM van en el texto de LinkedIn, no dentro de las imágenes.

### 5. Reglas de edición posteriores
Actualizar un borrador con `updateScheduledPost` cambia su `id` (el `uuid` no). Guarda siempre el id nuevo y envía el contenido completo, no solo el cambio, porque la actualización sobrescribe todo.

### 6. Registrar el estado en Notion
- Mientras el borrador existe y nadie lo programó: **Etapa** "Revisión".
- Cuando la persona lo programe en Metricool: "Programado". Si no tienes forma de enterarte, `reporte-estado` lo detecta en su siguiente corrida.
- Anota en la página el enlace del borrador (`plannerUrl` de la respuesta) para que sea fácil abrirlo.

### 7. Cerrar
Resume en una tabla: pieza, red, fecha y hora, imágenes, marcadores `[BORRADOR]` pendientes. Lista lo que la persona debe hacer antes de programar (quitar marcadores, confirmar permisos, revisar horarios). No programes por tu cuenta.

## Errores conocidos y cómo se resuelven
| Mensaje | Causa | Solución |
|---|---|---|
| `INSTAGRAM:MISSING_MEDIA` | Instagram sin imagen | Crear el borrador con imágenes; en Facebook y LinkedIn sí se permiten borradores de solo texto |
| `networkData … 'twitter' not listed in providers` | Se mandó `twitterData` sin esa red | Quitar `twitterData` |
| `Failed to normalize media` | URL firmada de Notion caducada | Pedir URLs nuevas y reintentar de inmediato, o reusar las de `static.metricool.com` |
| Respuesta enorme de `getScheduledPosts` | Rango muy largo | Consultar por semanas |

## Reglas
- Nunca programar ni publicar. Solo borradores.
- No tocar publicaciones que ya existen y que no creó este flujo.
- No modificar el caption salvo para pegar el del guion aprobado; si falta algo, volver al guion.
- No inventar ALT que contradiga lo que se ve en la imagen.
