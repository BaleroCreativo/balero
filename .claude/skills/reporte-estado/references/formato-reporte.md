# Formato del reporte de estado

Archivo: `clientes/<slug>/reportes/AAAA-MM-DD.md`

```markdown
# Estado del contenido: [Cliente] · [periodo]

Fecha de lectura: [fecha y hora] · Fuentes: Metricool (rangos [..]) y Notion (base [..])

## Resumen
- Publicado: [n] · Programado: [n] · Borrador: [n] · Sin crear: [n]
- Lo más urgente: [una frase]

## Por fecha y red
| Fecha | Red | Estado | Img | ALT | Alertas |
|---|---|---|---|---|---|

## Desajustes Notion y Metricool
| Fecha | Qué pasa | Acción propuesta |
|---|---|---|

## Pendientes por confirmar
| Qué | Con quién | Desde |
|---|---|---|

## Falta crear
- Sin guion: [..]
- Sin diseño: [..]
- Sin borrador en [red]: [..]
- Huecos sin cubrir: [..]

## Siguiente paso recomendado
[uno solo]
```

## Cómo se obtiene la tabla de Metricool
1. `getScheduledPosts` por rangos de una a dos semanas. Si el resultado es largo, la herramienta lo guarda en un archivo.
2. `python3 .claude/skills/reporte-estado/scripts/resumen_metricool.py <archivos>`.
3. Pasa la tabla a este formato y suma las alertas.
