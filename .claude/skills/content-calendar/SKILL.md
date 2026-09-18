---
name: content-calendar
description: Convertí una lista de ideas o piezas de contenido en un calendario fechado y listo para producir. Calcula fechas sin pisarse, mapea cada pieza a los campos de tu base de contenido (Notion, Airtable, Google Sheets, Trello, lo que uses), respeta tu cadencia y ventanas horarias, y siempre muestra un preview antes de escribir nada. Usala cuando pidas "armá el calendario de contenido", "programá estas piezas", "pasá estas ideas a fechas" o "organizá el mes de contenido".
license: Distribuida gratis por Claura (claura-ai.com). Uso libre para tu marca; no la revendas como producto.
---

# content-calendar (standalone)

Skill para transformar un batch de ideas o piezas de contenido en un **calendario fechado**, coherente con la cadencia de tu marca y listo para que alguien (o un agente) lo produzca y publique. Es el paso que va entre "tengo ideas sueltas" y "tengo un plan con fechas".

Version standalone: no depende de ninguna infraestructura ni base de datos particular. Vos pegás la cadencia de tu marca y la lista de piezas en dos bloques, y la skill arma el calendario contra la herramienta que uses.

## Cómo se usa

1. Pegá tu **bloque de cadencia de marca** (abajo): frecuencia, ventanas horarias, mix de formatos, reglas AVOID/PREFER.
2. Pegá o apuntá a tu **lista de piezas** (cada una con al menos un Hook/Título y un Tipo).
3. Decile a la IA qué herramienta usás para el calendario y desde qué fecha querés arrancar.
4. La skill calcula fechas, mapea campos, y te muestra un **preview en tabla**.
5. Confirmás y recién ahí se crean las entradas.

### Bloque de cadencia de marca (completá y pegá)

```
MARCA: <nombre / handle>
FRECUENCIA: <ej: 1 post/día, 5 posts/semana, 3 reels + 2 carruseles/semana>
VENTANAS HORARIAS: <horarios donde tu audiencia rinde, ej: 11h y 20h hora local>
MIX DE FORMATOS: <proporción objetivo, ej: 2-3 carruseles/semana + resto reels>
PLATAFORMAS: <ej: Instagram, TikTok, YouTube, LinkedIn>
AVOID: <reglas de lo que NO calendarizar así, ej: no todo reel, no dos ventas seguidas>
PREFER: <reglas de lo que SÍ, ej: lunes educativo, viernes detrás de escena>
```

> Si no tenés estos datos medidos, arrancá con 1 post/día y un mix 60% del formato que mejor te rinde / 40% del resto. Ajustá cuando tengas métricas reales.

### Bloque de piezas (completá y pegá, o apuntá a un archivo)

```
1. Hook: "<título/gancho de la pieza>" | Tipo: <Carrusel|Video|Imagen|Guía> | Formato: <UGC|Avatar|Voice Over|Tweet|Photo Slideshow|...> | Plataformas: <...> | Script/Slides: <opcional> | Caption: <opcional>
2. ...
```

Mínimo requerido por pieza: **Hook y Tipo**. Todo lo demás es opcional y se completa después.

## Esquema del calendario (campos genéricos)

Mapeá cada pieza a estas columnas en tu base (renombralas según tu herramienta):

| Campo | Requerido | Valores típicos |
|---|---|---|
| Hook / Título | Sí | Texto libre (el gancho de la pieza) |
| Tipo | Sí | Carrusel, Video, Imagen, Guía |
| Estado | Sí | Idea, Generado, Programado, Publicado |
| Formato / Style | No | UGC, Avatar, Voice Over, Tweet, Photo Slideshow, Imágenes |
| Script | No | Slides ("Slide 1: ...\nSlide 2: ...") o guión de video |
| Caption | No | Copy sugerido (si va vacío, se genera después) |
| Fecha objetivo | Sí | YYYY-MM-DD (por default, 1 post/día por marca) |
| Plataformas | No | TikTok, Instagram, YouTube, LinkedIn, Facebook |
| Fuente de imagen | No | Generada por IA, Banco de imágenes, Mix |
| Output | No | Link al contenido **ya renderizado** (mp4/carrusel listo para publicar) |
| Referencia | No | Link al post **original que inspiró** la pieza (NO el render final) |
| Origen | No | Referencia, Clip, News, Idea propia, Clonado |
| Título sobreimpreso | No | Texto overlay para videos |

> **Output ≠ Referencia**: el contenido ya producido va en Output; el link que te inspiró va en Referencia. Confundirlos es un error clásico que después obliga a migrar entradas a mano.

## Workflow

### 1. Leer la cadencia y las piezas

Cargá el bloque de cadencia y la lista de piezas. Extraé, por pieza, al menos Hook y Tipo.

### 2. Encontrar la última fecha ya calendarizada

Antes de asignar fechas, mirá qué fecha objetivo es la **más lejana** ya cargada para esta marca en tu base. Esto evita pisar contenido existente o dejar huecos.

- Filtrá por marca/cliente y ordená por fecha objetivo descendente: la primera es tu punto de partida.
- Cuidado con los buscadores semánticos (tipo "search" de Notion): muchos rankean por relevancia o por fecha de creación, **no** por tu campo de fecha objetivo, y pueden esconder posts válidos. Para esto usá siempre una query/filtro real sobre el campo de fecha (vista filtrada, API con filter, o la relación de contenido del cliente como fuente de verdad), nunca el search genérico.
- Si no hay nada cargado, la primera fecha es mañana.

### 3. Calcular fechas

Reglas de fechas:

- Empezá desde el día siguiente a la última fecha objetivo encontrada.
- Si la fecha calculada cae hoy o en el pasado, usá mañana.
- 1 post por día por marca (default; ajustá según tu bloque de cadencia).
- Asigná fechas de forma secuencial a las piezas, en el orden que te sirva (podés agrupar por formato para respetar el mix).
- Honrá las ventanas horarias y el mix de formatos de tu bloque de cadencia: si tu regla es "2-3 carruseles/semana", distribuí los carruseles para que no queden todos juntos.

### 4. Mapear piezas al esquema

Para cada pieza, completá los campos del esquema. Estado:

- **Idea** → si todavía falta material (ej: fotos del banco sin cargar).
- **Generado** → si la pieza ya está lista para producir o publicar.

Campos vacíos: no los incluyas (mejor omitir que cargar un string vacío).

### 5. Preview al usuario (obligatorio)

Antes de escribir nada, mostrá la tabla completa:

```
Se van a crear {N} entradas en el calendario:

| # | Hook | Tipo | Formato | Plataformas | Fecha |
|---|------|------|---------|-------------|-------|
| 1 | "Cosas que nadie te dice de..." | Carrusel | UGC | TikTok, IG | 2026-04-15 |
| 2 | "Ranking de apps para..."       | Carrusel | UGC | TikTok, IG | 2026-04-16 |
...

Marca: {nombre}
Rango de fechas: {fecha_inicio} → {fecha_fin}

¿Confirmás?
```

Esperá la confirmación antes de crear nada.

### 6. Crear las entradas (en batch)

Creá todas las entradas de una, no de a una. Si tu herramienta tiene API o import, usá el batch.

### 7. Confirmar

```
✓ {N} entradas creadas en el calendario
  Marca: {nombre}
  Rango: {fecha_inicio} → {fecha_fin}
  Estado: {Idea/Generado}
  Siguiente paso: cargar material faltante (si aplica) y producir cada pieza.
```

## Reglas

1. **Siempre preview antes de crear.** Nunca escribas sin confirmación del usuario.
2. **1 post por día por marca** por default (salvo que la cadencia diga otra cosa).
3. **Nunca confíes en un buscador semántico para fechas.** Filtrá por el campo de fecha real, no por relevancia ni por fecha de creación (ver paso 2).
4. **Nunca concluyas "no existe post para la fecha X"** basándote solo en un search genérico: chequeá la fuente de verdad (query filtrada o la relación de contenido del cliente).
5. **Script obligatorio para videos narrados** (Avatar, Voice Over, Photo Slideshow): sin guión no hay pieza.
6. **Caption opcional**: si va vacío, se genera en la etapa de producción.
7. **Esta skill solo planifica.** No genera contenido ni sube archivos: crea entradas con fechas y campos.
8. **Campos vacíos: omitir**, no cargar propiedades en blanco.
9. **Batch create**: todas las páginas en una o dos llamadas, no una por una.
10. **Output ≠ Referencia** (ver esquema).
11. **Respetá el mix de formatos** de tu bloque de cadencia: no calendarices todo como el mismo formato aunque sea el más fácil de producir.

## Cómo se conecta con el resto de tu flujo

```
Ideas / piezas (de un brainstorm, un playbook, un batch de hooks)
     ↓
content-calendar → asigna fechas + mapea campos + preview → crea entradas (Estado: Idea/Generado)
     ↓
[cargás material faltante si hace falta]
     ↓
Producción (generás el contenido) → Estado: Programado
     ↓
Publicación → Estado: Publicado
```

- **Antes**: cualquier fuente de ideas (brainstorm, banco de hooks, campaña, análisis de referencias).
- **Después**: tu flujo de producción y publicación.

## Adaptá el esquema a tu herramienta

- **Notion / Airtable**: cada campo del esquema es una property. Fecha objetivo = Date, Tipo/Formato/Estado = Select, Plataformas = Multi-select, Output/Referencia = URL.
- **Google Sheets**: una columna por campo, una fila por pieza. La fecha en formato YYYY-MM-DD para poder ordenar.
- **Trello / Kanban**: una card por pieza, la fecha objetivo como due date, el Estado como lista/columna.

El framework es el mismo en todas: leer piezas, calcular fechas sin pisarse, mapear, preview, crear.
