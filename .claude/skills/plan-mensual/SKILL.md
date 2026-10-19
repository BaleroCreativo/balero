---
name: plan-mensual
description: Arma el calendario de contenido de un cliente para un mes (fechas, redes, formatos, pilares, huecos reservados para noticias) y crea las filas en la base de Contenidos de Notion con estado "Idea", después de que el usuario apruebe el plan. Es la etapa 2 del sistema de contenido mensual. Úsala siempre que el usuario pida "el calendario de [mes]", "planear el mes", "plan de contenido", "qué publicamos en [mes]", "llenar el calendario de un cliente" o "armar la parrilla", aunque no mencione Notion, y también cuando haya que rehacer o rellenar huecos de un calendario existente.
---

# Plan mensual: el calendario del mes

Convierte la ficha de un cliente en un calendario concreto: qué se publica, dónde y cuándo, bajo qué pilar. El producto son filas en Notion con estado "Idea". Todavía no hay copy ni diseño; eso viene en las etapas siguientes.

## Por qué hay un punto de aprobación antes de crear filas
Un calendario equivocado se paga en cada etapa posterior: investigación, guiones y diseño se hacen sobre él. Por eso se muestra completo en una tabla y se crea en Notion solo cuando la persona responsable lo aprueba. Revisar una tabla toma un minuto; borrar 40 filas, no.

## Flujo

### 1. Leer la ficha del cliente
Abre `clientes/<slug>/ficha.md`. Necesitas: redes activas y formatos, días y horas, frecuencia, pilares con su proporción, fechas importantes, reglas de verdad y conexiones (base de Notion, proyecto, marca de Metricool y zona horaria).
- Si no existe ficha, usa el skill `cliente-onboarding` primero.
- Si la frecuencia o la proporción de pilares están como `[POR CONFIRMAR]`, propón un valor razonable, dilo en voz alta y deja que el usuario lo corrija en la aprobación. No lo guardes en la ficha sin su visto bueno.

### 2. Ver qué ya existe en ese mes
Antes de proponer nada, lee lo que hay:
- **Notion:** filas de Contenidos con fecha de publicación dentro del mes (consulta la base; ver `references/notion-contenidos.md`).
- **Metricool:** publicaciones programadas o en borrador del mes (`getScheduledPosts`; el resultado es largo, así que consulta por rangos de una o dos semanas).

El objetivo es no duplicar fechas ni temas y respetar lo que el cliente ya programó por su cuenta. Si algo ya existe, entra al plan marcado como "existente" y no se vuelve a crear.

### 3. Mirar el mes anterior
Si hay datos de Metricool o comentarios del cliente del mes pasado, extrae dos o tres aprendizajes (qué formato o tema funcionó mejor, qué se ignoró) y úsalos para ajustar proporciones. Si no hay datos suficientes, dilo y sigue; no inventes tendencias.

### 4. Construir los huecos
- Genera la lista de fechas con día de la semana, según los días y la frecuencia de la ficha, por red.
- Marca las fechas especiales que dé la ficha o el usuario (promociones, eventos, cierres, puentes). Para días festivos del país, verifícalos en una fuente antes de usarlos; no los des por sabidos.
- **Reserva huecos para noticias:** deja libre alrededor del 15 al 20 % de las fechas para lo que surja durante el mes (cambios de plataforma, noticias del sector). Se rellenan en la etapa de investigación con el criterio de la ficha: noticia reciente con impacto inmediato entra a un hueco libre del mes en curso; si no cumple, pasa al mes siguiente.

### 5. Asignar pilares, formatos y temas de trabajo
- Reparte los pilares según la proporción de la ficha y evita repetir el mismo pilar dos publicaciones seguidas en la misma red.
- Alterna formatos (carrusel, post, reel, poll, texto) para que el mes no se vea monótono.
- Una misma idea puede salir en varias redes con adaptación: carrusel en Instagram y Facebook, y versión en PDF para LinkedIn. Cuando sea así, agrúpalas en una sola fila de planeación con las redes en la columna Plataforma, salvo que el cliente quiera calendarios separados por red.
- Cada fila lleva un **tema de trabajo** de una línea, no un título final. Los temas salen de los pilares, de las dudas y objeciones del cliente ideal y de los aprendizajes del mes anterior. Cuando no haya tema todavía, escribe "Hueco noticia" o "Tema por definir". No rellenes con temas genéricos solo para que el calendario se vea lleno.
- Anota si la pieza necesita permiso o dato del cliente (caso con nombre, cifra, reseña), según las reglas de verdad de la ficha.

### 6. Mostrar el plan para aprobación
Presenta una tabla con estas columnas: **Fecha y hora, Día, Red(es), Formato, Pilar, Tema de trabajo, Necesita**. Abajo, un resumen de tres líneas: total de piezas, proporción real de pilares contra la ficha y número de huecos para noticias. Pregunta qué se cambia. Itera hasta que se apruebe.

### 7. Crear las filas en Notion
Con el plan aprobado, crea una fila por pieza en la base de Contenidos del cliente. Para los nombres de propiedades, valores permitidos y un ejemplo de llamada, lee `references/notion-contenidos.md`; lee primero el esquema real de la base porque cada cliente puede tener opciones distintas.

Convenciones:
- **Nombre:** `DD Mes · Día · tema de trabajo`, por ejemplo `16 Oct · Vie · Postura de cómo cotizamos`.
- **Etapa:** "Idea".
- **Publicación:** fecha y hora con la zona horaria de la ficha.
- **Relación de proyecto:** la página del cliente indicada en la ficha.
- Si una opción de Formato o Pilar no existe en la base, avísalo y pregunta antes de modificar el esquema.

### 8. Cerrar
Resume en pocas líneas qué se creó (cuántas filas, en qué fechas) y qué queda abierto. El siguiente paso es la investigación (`investigacion-verificada`) para llenar los huecos de noticias y respaldar los temas que necesitan datos, y después los guiones (`guion-pieza`).

## Qué no hacer
- No crees filas sin aprobación del plan.
- No sobrescribas ni borres filas existentes; si algo choca, pregunta.
- No inventes fechas festivas, cifras de mercado ni "mejores horarios". Si el usuario pide horarios óptimos, usa los datos de Metricool (`getBestTimeToPostByNetwork`) y di de dónde salen.
- No escribas copy ni titulares finales aquí.
