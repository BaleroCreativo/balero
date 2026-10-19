---
name: guion-pieza
description: Escribe el guion completo de una pieza de contenido de un cliente (hook con variantes, caption por red, hashtags, guion slide por slide con ilustración sugerida y fondo, texto ALT borrador y la lista de pendientes antes de publicar) a partir de una fila del plan y de datos ya verificados, y lo deja en la página de Notion de la pieza con la etapa en "Guionizado". Es la etapa 4 del sistema de contenido mensual. Úsala siempre que el usuario pida "escribe el guion de...", "el copy de la pieza del [fecha]", "guionizar el mes", "haz el carrusel de...", "hook y caption para...", "texto de este post", o cuando haya filas en estado "Idea" con temas aprobados y datos listos para convertirse en contenido.
---

# Guion de pieza

Convierte una fila del calendario (tema, red, formato, pilar) y sus datos verificados en todo lo que las etapas siguientes necesitan: el diseñador y el script de carruseles leen el guion slide por slide; la publicación lee los captions y los textos ALT. Un guion bien cerrado evita rehacer diseño por un cambio de texto.

## Entradas obligatorias
1. **Ficha del cliente** (`clientes/<slug>/ficha.md`): tono, ICP, reglas de verdad, llamado a la acción, hashtags, enlaces con UTM.
2. **Fila de Notion** de la pieza: fecha, redes, formato, pilar, tema de trabajo.
3. **Datos verificados** del informe de investigación (`clientes/<slug>/investigacion/AAAA-MM.md`) cuando la pieza usa cifras, noticias o casos.

Si falta la ficha, usa `cliente-onboarding`. Si la pieza necesita datos y no hay informe, usa `investigacion-verificada`. Escribir sobre datos sin verificar es el error más caro de esta etapa, porque después hay que rehacer texto y diseño.

## Reglas de verdad en el texto
- Usa solo datos con estado **Verificado**, o **Parcial** con la redacción exacta que el informe permite ("según reportes").
- No inventes casos, clientes, cifras, citas ni experiencias. Si una anécdota no ocurrió, la pieza se escribe como postura de la marca ("así cotizamos"), sin cliente ni cifra y sin presentarla como historia.
- Respeta las listas "no se puede afirmar" y "requiere permiso" de la ficha.
- Todo lo dudoso lleva el marcador `[BORRADOR: …]` al inicio del caption y una línea en "Pendientes antes de publicar". Así nadie publica sin ver el aviso.

## Flujo

### 1. Elegir el ángulo
Define en una frase qué cambia para el lector después de ver la pieza (qué hace, qué decide, qué revisa). Si no se puede decir en una frase, el tema es demasiado grande: divídelo en dos piezas o recórtalo.

### 2. Hook
Escribe cinco hooks con `hook-writing` como apoyo y elige uno principal con dos respaldos. Criterios que funcionaron:
- Corto y concreto, que cuente la promesa de la pieza, no que la anuncie ("Nadie nos paga por recomendarte su herramienta", no "Te contamos cómo elegimos herramientas").
- Afirmativo mejor que pregunta cuando se pueda; las preguntas son aceptables si abren una tensión real. Prueba ambas en piezas distintas y compara resultados con el tiempo, sin citar estudios como justificación salvo que estén verificados.
- Si el hook promete un número ("3 cosas"), el carrusel debe desarrollar exactamente ese número.
- Un hook que depende de un dato propio (un número del mes, un caso) se deja como `[POR CONFIRMAR]` hasta tenerlo.
En la portada del carrusel el hook se parte en: línea fina, frase fuerte y frase de énfasis (caja o color).

### 3. Guion slide por slide (carruseles)
Estructura base: portada → 3 a 5 slides de contenido → cierre con llamado a la acción. Una idea por slide, una ilustración por slide.
Para cada slide escribe:
- **Título** (frase corta) y **cuerpo** (una o dos frases; en el diseño se acorta, así que escribe pensando en 25 palabras o menos).
- **Ilustración sugerida** (un objeto concreto que represente la idea; el banco de objetos está en `balero-imagenes/references/ilustraciones-3d.md`).
- **Fondo** alternando ritmo (negro, lila, blanco, diagonales) para que el deslizar no sea monótono.
- Cuando uses cifras, el dato exacto y su redacción permitida.
El cierre repite la oferta de la ficha y el canal de contacto.
Para el formato exacto del JSON que consume el generador de carruseles, ver `balero-imagenes/SKILL.md` y `balero-imagenes/scripts/example-spec.json`; este guion es el contenido, y el JSON se arma en la etapa de diseño.

### 4. Captions por red
Cada red tiene su manera; no copies el mismo texto en todas.
- **Instagram:** primeras dos líneas fuertes (es lo que se ve antes de "más"), párrafos cortos, tres o cuatro hashtags al final, cierre con la acción de la ficha. Sin enlace pulsable.
- **Facebook:** parecido a Instagram, un poco más explicativo; admite enlace.
- **LinkedIn:** tono más profesional sin volverse rígido; el enlace con UTM va en el texto, no dentro de las páginas del PDF; si es carrusel se publica como PDF con título de documento.
- **Polls:** pregunta corta y cuatro opciones, la última abierta ("Otro").
Para adaptar una idea a varias redes, `content-repurposer` puede servir de apoyo. Revisa el resultado con `brand-voice-enforcement` si el cliente tiene guía de voz. Si el texto suena a plantilla, pásalo por `humanizer` y vuelve a comprobar que no cambió ningún dato.

### 5. Texto ALT borrador
Una frase por imagen: qué se ve y qué dice, con palabras clave naturales (tema, marca, ciudad) sin rellenar. Márcalo como borrador: se ajusta cuando existan las imágenes, porque el guion describe lo planeado y no necesariamente lo que quedó.

### 6. Pendientes antes de publicar
Lista corta y concreta: permisos de cliente por obtener, afirmaciones por confirmar, datos con vigencia que hay que volver a verificar, huecos del guion. Cada pendiente dice quién lo resuelve.

### 7. Entregar y guardar
1. Muestra el guion al usuario con la estructura de `references/estructura-pieza.md`. Es un punto de aprobación: se corrige aquí, antes de diseñar.
2. Con el visto bueno, escribe el guion en el cuerpo de la página de Notion de la pieza y cambia **Etapa** a "Guionizado". Si hay varias piezas, hazlas una por una y resume al final cuántas quedaron listas y cuáles esperan datos.
3. Si el usuario pide un lote, trabaja pieza por pieza y pausa para aprobación al terminar cada semana de contenido, no al final del mes.

### 8. Cerrar
Resume qué quedó guionizado y qué sigue pendiente. El siguiente paso es el diseño (`balero-imagenes` para Balero; para otros clientes, primero habrá que parametrizar el generador con su marca).

## Qué no hacer
- No publiques ni programes nada desde aquí.
- No cambies el tema aprobado en el plan sin avisar.
- No metas claims fuera de las reglas de verdad de la ficha, por atractivos que sean.
- No uses más texto del que cabe en un slide: si un cuerpo pasa de 25 palabras, pártelo o recórtalo.
