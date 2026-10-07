---
name: reporte-estado
description: Genera el informe de estado del contenido de un cliente en un periodo (qué está publicado, programado, en borrador o sin crear por fecha y red; qué falta confirmar; qué desajustes hay entre Notion y Metricool) y propone sincronizar la columna Etapa de Notion con la realidad. Es la etapa 8 del sistema de contenido mensual. Úsala siempre que el usuario diga "dame el estatus", "actualiza el status", "cómo va el plan", "qué falta", "resumen del mes", "qué está programado", "recapitulemos" o cuando el mes esté por cerrar o empiece uno nuevo, aunque no mencione Metricool ni Notion.
---

# Reporte de estado

Contesta con evidencia a una pregunta que se repite cada semana: ¿cómo va el contenido y qué falta? Cruza dos fuentes, Notion (el plan) y Metricool (la realidad), y marca donde no coinciden. Su valor está en lo que nadie tiene que ir a buscar: una pieza programada con un marcador `[BORRADOR]` en el texto, un Instagram sin imágenes, un post que alguien movió de hora.

## Siempre con lectura fresca
El reporte se hace con una lectura nueva de Metricool y Notion, no con lo que se recuerda de la conversación. El estado cambia entre mensajes: en octubre varias publicaciones pasaron de borrador a programadas, con otra hora, mientras se trabajaba en otra cosa, y cada actualización en Metricool genera un id nuevo, así que los ids anteriores ya no sirven.

## Flujo

### 1. Leer la ficha y el periodo
Ficha del cliente para conexiones (marca de Metricool, base de Notion, zona horaria, redes). El periodo por defecto es el mes en curso; si el usuario dice "esta semana" o "lo que falta", acótalo.

### 2. Leer Metricool
Consulta `getScheduledPosts` por rangos de una o dos semanas. Las respuestas grandes se guardan en un archivo; no intentes pegarlas completas en la conversación.
Para pasar de datos crudos a tabla, usa `scripts/resumen_metricool.py archivo1.json archivo2.json …`: junta los rangos sin duplicar, clasifica cada publicación como PUBLICADO, PROGRAMADO o BORRADOR, cuenta imágenes y textos ALT, y marca marcadores `[BORRADOR]`, Instagram sin imágenes y programadas con marcador.

### 3. Leer Notion
Consulta las filas del periodo en la base de Contenidos (fecha, redes, formato, etapa). Ver `plan-mensual/references/notion-contenidos.md` para el esquema y la consulta.

### 4. Cruzar y detectar desajustes
Compara por fecha y red. Los desajustes que más importan:
- **Fila de Notion sin publicación en Metricool** en una red que el plan indica.
- **Publicación en Metricool sin fila en Notion** (alguien la creó por su cuenta; se reporta, no se borra).
- **Etapa de Notion distinta del estado real**, por ejemplo "Revisión" cuando ya está programado, o "Programado" cuando solo es borrador.
- **Hora o fecha cambiada** respecto al plan.
- **Programada con `[BORRADOR]`** en el texto: la persona programó sin resolver el pendiente.
- **Instagram o Facebook sin imágenes**, o imágenes sin ALT.
- **Piezas del plan sin guion o sin diseño** cuando faltan pocos días.

### 5. Armar el informe
Estructura (plantilla en `references/formato-reporte.md`):
1. **Resumen en tres líneas:** totales por estado y qué es lo más urgente.
2. **Tabla por fecha y red** con estado, imágenes y alertas.
3. **Desajustes** entre Notion y Metricool.
4. **Pendientes por confirmar:** permisos de clientes, afirmaciones de la sección de reglas de verdad, datos con vigencia, marcadores `[BORRADOR]`; cada uno con quién lo resuelve y desde cuándo.
5. **Lo que falta crear:** piezas sin guion, sin diseño, sin borrador, y huecos sin cubrir.
6. **Siguiente paso recomendado**, uno solo.

Guarda el informe en `clientes/<slug>/reportes/AAAA-MM-DD.md`.

### 6. Sincronizar Notion
Propón los cambios de Etapa antes de aplicarlos:
- Publicado en Metricool → "Publicado".
- Programado en Metricool → "Programado".
- Borrador creado, sin programar → "Revisión".
Aplica solo después de que la persona lo confirme y solo a filas que reconoces. Nunca cambies el contenido de una fila ni borres filas desde este informe.

### 7. Aprendizajes del mes (al cerrar)
Cuando el mes ya pasó, lee los resultados de las publicaciones (herramientas de analítica de Metricool) y extrae dos o tres aprendizajes que alimenten el siguiente `plan-mensual`: qué formato y tema funcionó mejor, qué se ignoró. Si hay pocos datos, dilo y no saques conclusiones fuertes: con pocas publicaciones las diferencias pueden ser ruido.

## Reglas
- Reporta lo que se ve en las fuentes, no lo que se esperaría. Si no puedes leer una de las dos, dilo y no completes por suposición.
- No cambies nada en Metricool desde aquí. Si hay algo que arreglar, propón la acción y pásala a `publicar-metricool`.
- Distingue "no lo vi" de "no existe". Un rango que no consultaste no está vacío.
- Un reporte corto y exacto vale más que uno largo. Si todo está bien, dilo en tres líneas.
