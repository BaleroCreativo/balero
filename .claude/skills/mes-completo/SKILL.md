---
name: mes-completo
description: Orquesta el flujo completo del contenido mensual de un cliente, de la ficha al borrador en Metricool, encadenando los skills de cada etapa (cliente-onboarding, plan-mensual, investigacion-verificada, guion-pieza, diseño con balero-imagenes, revision-visual, publicar-metricool, reporte-estado) y deteniéndose en cada punto de aprobación; también retoma un mes a medias leyendo el estado en Notion. Úsala siempre que el usuario diga "haz el mes de [cliente]", "prepara el contenido de [mes]", "arranca el mes", "retoma el calendario", "por dónde vamos y sigue", "hazlo de principio a fin" o quiera correr el proceso completo para un cliente, aunque no nombre ninguna etapa.
---

# Mes completo

Es el director de orquesta. No hace el trabajo de cada etapa: decide cuál toca, llama al skill correcto, se detiene donde una persona tiene que decidir y avanza en lotes pequeños para que nada se acumule sin revisar.

## Por qué en lotes y con pausas
Un error en el plan o en un dato se multiplica en guion, diseño y publicación. Revisar una semana a la vez cuesta unos minutos; descubrir al final que un dato de las primeras piezas estaba mal cuesta rehacer todo el mes. Por eso el flujo avanza semana por semana desde la etapa de guiones, y se detiene en los cinco puntos de aprobación.

## Las ocho etapas y sus puntos de aprobación
| # | Etapa | Skill | Punto de aprobación |
|---|---|---|---|
| 1 | Ficha del cliente | `cliente-onboarding` | La persona y el cliente confirman marca, tono y reglas de verdad |
| 2 | Plan del mes | `plan-mensual` | La persona aprueba el calendario antes de crear filas |
| 3 | Investigar y verificar | `investigacion-verificada` | La persona valida qué temas y datos entran |
| 4 | Guion y copy | `guion-pieza` | La persona aprueba textos y afirmaciones |
| 5 | Diseño gráfico | `balero-imagenes` | Sin aprobación, corre solo |
| 6 | Revisión visual | `revision-visual` | La persona da el visto a la portada |
| 7 | Publicar borradores | `publicar-metricool` | La persona quita marcadores y programa |
| 8 | Estado y pendientes | `reporte-estado` | Sin aprobación; propone sincronizar Notion |

## Flujo

### 1. Definir cliente y mes
Pregunta solo lo que falta: cliente y mes. Busca `clientes/<slug>/ficha.md` y lee su sección de pendientes. Si el usuario no dice nada más, el objetivo es llegar a borradores en Metricool de todo el mes.

### 2. Descubrir en qué punto está el mes
Si el mes ya tiene avance, retómalo en lugar de empezar de cero. Lee las filas de Notion del periodo y Metricool (con `reporte-estado`) y ubica cada pieza:

| Lo que se observa | Etapa que sigue |
|---|---|
| No hay ficha | 1. `cliente-onboarding` |
| No hay filas del mes | 2. `plan-mensual` |
| Fila en "Idea" sin datos o con hueco de noticia | 3. `investigacion-verificada` |
| Fila en "Idea" con datos aprobados | 4. `guion-pieza` |
| Fila en "Guionizado" | 5. diseño |
| Fila con imágenes en Recurso, sin revisión | 6. `revision-visual` |
| Imágenes aprobadas, sin borrador en Metricool | 7. `publicar-metricool` |
| Borrador en Metricool | La persona programa; luego 8. `reporte-estado` |
| Programado o publicado | Nada que hacer en esa pieza |

Muestra este diagnóstico en una tabla corta y confirma por dónde empezar.

### 3. Ejecutar por tandas
- **Etapas 1 a 3 (cliente y mes completo):** una sola vez, con su aprobación cada una. Sin plan aprobado no se pasa a investigación; sin datos aprobados no se escriben guiones con cifras.
- **Etapas 4 a 7 (por semana de contenido):** toma las piezas de una semana, guioniza, diseña, revisa y crea borradores; pausa para que la persona revise esa semana y recién después sigue con la siguiente. Si las semanas son independientes y el usuario quiere velocidad, varias pueden avanzar en paralelo con subagentes, uno por pieza, aplicando tú los cambios en archivos compartidos.
- **Etapa 8:** al terminar cada tanda y al final del mes.

### 4. En cada pausa
Entrega un resumen corto: qué se hizo, qué decide la persona, qué sigue. No sigas hasta recibir la decisión. Si una aprobación vuelve con cambios, reabre solo la etapa afectada y rehaz lo que depende de ella (un cambio de dato obliga a revisar guion y diseño de esa pieza).

### 5. Antes de la etapa de diseño, comprueba la marca
El generador de carruseles hoy tiene los colores de Balero escritos dentro del código. Si el cliente no es Balero y la ficha marca "pendiente de diseño: parametrizar el generador", detén el flujo antes del paso 5 y avisa. Se puede seguir con las etapas 1 a 4 y diseñar cuando la marca esté lista; no generes imágenes con la marca equivocada.

### 6. Cierre del mes
Corre `reporte-estado`, entrega el informe con pendientes por cliente y propone los aprendizajes que alimentarán el plan del mes siguiente. Pregunta si arrancas el siguiente mes con `plan-mensual`.

## Reglas
- Una persona programa y publica. Este flujo termina en borradores.
- Cada etapa conserva sus propias reglas: datos verificados, cero casos inventados, marcadores `[BORRADOR]` visibles. No las relajes por avanzar rápido.
- Un dato dudoso detiene su pieza, no el mes: sigue con las demás y deja el pendiente anotado.
- Si una herramienta (Notion, Metricool, correo) no responde, dilo y propone un siguiente paso; no completes por suposición.
- Si el usuario pide saltar una etapa, dile qué riesgo corre, y si insiste, déjala anotada como pendiente.

## Cómo se ve una corrida típica
1. "Haz noviembre de Balero." → diagnóstico, ficha existe, no hay filas de noviembre.
2. `plan-mensual` → tabla → la persona aprueba → filas creadas.
3. `investigacion-verificada` → informe → la persona aprueba temas y datos.
4. Semana 1: guiones → aprobación; diseño; revisión visual → visto bueno a portadas; borradores en Metricool.
5. Semanas 2, 3 y 4: igual.
6. `reporte-estado` → informe, sincronizar Notion, aprendizajes.
