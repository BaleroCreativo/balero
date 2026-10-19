# Marca por cliente (brand.json)

El generador `scripts/build_carousel.py` usa por defecto la marca de Balero. Para otro cliente se le pasa un `brand.json`; todo lo que el archivo no defina se hereda de Balero.

```
python3 scripts/brand_fonts.py clientes/<slug>/marca/brand.json      # una vez: descarga las fuentes de Google Fonts
python3 scripts/build_carousel.py spec.json salida/ --brand clientes/<slug>/marca/brand.json
```
También se puede poner `"brand": "ruta/brand.json"` dentro del spec. Las rutas del brand.json son relativas al propio archivo.

## Campos
| Campo | Qué es |
|---|---|
| `name` | Nombre que sale en el pie de cada slide (en mayúsculas). |
| `logo` | PNG con fondo transparente. Vacío o ausente: el slide sale sin logo (con aviso). |
| `font_title`, `font_body` | Familias (Google Fonts). Títulos y pie; párrafos. |
| `weights` | `light`, `heavy`, `body`, `body_bold` (por defecto 300/800/400/700). |
| `fonts_css` | CSS con las `@font-face`. Lo escribe `brand_fonts.py`. |
| `colors.accent` | Color de énfasis (titulares fuertes, negritas, puntos activos). |
| `colors.ink` | Texto y titular oscuro. |
| `colors.bg` | Fondo de slides interiores. |
| `colors.highlight` | Acento secundario (póster). |
| `colors.inv_text`, `inv_accent`, `inv_dot` | Texto, acento y puntos sobre fondo oscuro. |
| `colors.dot_off` | Puntos inactivos; si falta, se deriva del acento. |
| `colors.shadow` | `"R,G,B"` de la sombra de las ilustraciones. |
| `colors.cover_bg`, `closing_bg` | Fondos (CSS) de portada y cierre. |
| `backgrounds` | Fondos nombrados para `"bg"` en cada slide; los de acento y lila se derivan de `accent` y `bg` si no se definen. |

## Pasos para un cliente nuevo
1. Copia colores y fuentes de la ficha (hex exactos). Si el cliente no tiene guía de marca, propón una y que la apruebe.
2. Crea `clientes/<slug>/marca/brand.json` con lo de la tabla.
3. Corre `brand_fonts.py`. Si una fuente no es de Google Fonts, copia los archivos a `marca/fonts/` y escribe a mano el `fonts.css`.
4. Renderiza un spec de prueba y revisa portada, lección y cierre antes de producir el mes.
5. Revisa con `revision-visual/scripts/checks.py <carpeta> --fuentes NombreSinEspacios,Otra`.

## Límites
- Las ilustraciones (3D, línea, fotos) no se parametrizan: se generan por cliente, con el estilo de su ficha.
- Sin ilustración, la portada deja el titular y el subtítulo muy juntos si el titular ocupa tres líneas: acorta el texto o sube `title_px` menor.
- Los efectos del tipo `poster` (cajas negras, texto amarillo) usan negro y `highlight`; ajusta `highlight` a la marca.
