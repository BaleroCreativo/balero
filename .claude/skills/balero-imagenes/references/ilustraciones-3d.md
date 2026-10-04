# Ilustraciones 3D de Balero

## Prompt base (copiar y sustituir el objeto)
```
A 3D render of [OBJETO, con 1 o 2 detalles], glossy clay-style, soft inflated rounded forms like a 3D emoji icon, in saturated indigo violet (#665FE9), golden yellow (#FEC72E) and white accents. Centered, slightly rotated three-quarter view, soft studio lighting, gentle highlights and a subtle contact shadow. The background is a plain pale lavender (#F6F5FF). Playful premium 3D icon illustration. No text, no letters, no logos, no watermark.
```
- Herramienta: `generate-image` de Canva con `aspectRatio: SQUARE_1_1`.
- Un objeto por imagen. Máximo dos elementos (por ejemplo reloj + globo de chat).
- Después: recortar fondo con `scripts/cutout.sh`. Para objetos con cuerpo blanco (celular, robot, megáfono) usar tolerancia 3: `bash scripts/cutout.sh in.jpg out.png 3`; con la tolerancia por defecto (9) el relleno se come las partes blancas.

## Banco de objetos ya usados (por tema)
| Tema | Objeto |
|---|---|
| Crecimiento, resultado | Gráfica de barras con flecha hacia arriba |
| Objetivo, medición | Diana con dardo en el centro |
| Registro, CRM, tareas | Portapapeles con palomita y lápiz amarillo |
| Filtro, elegir clientes | Embudo índigo con borde amarillo y fichas con palomita |
| Tiempo, seguimiento | Reloj despertador amarillo con globo de chat índigo |
| Planeación | Calendario con palomita blanca y chincheta amarilla |
| Mensajes, contacto | Dos globos de chat superpuestos (índigo y amarillo) |
| Mensajes entrantes | Celular blanco con dos globos de chat (índigo y amarillo) |
| Investigar, revisar | Lupa con aro índigo y destello amarillo |
| Agente de IA | Robot pequeño blanco con pantalla índigo y globo de chat |
| Anuncios, difusión | Megáfono blanco con campana índigo y mango amarillo |
| Presupuesto, costo | Pila de monedas amarillas con una moneda índigo |

## Objetos sugeridos para próximas piezas
Cohete (lanzamiento), candado (seguridad), moneda o alcancía (presupuesto), trofeo (casos de éxito), engranes (automatización), robot pequeño con globo de chat (agente de IA).

## Reglas
- Sin rostros ni personas.
- Sin texto dentro de la ilustración (el texto va en el diseño).
- Si el resultado trae otros colores fuertes (rojo, verde), regenerar: la paleta es índigo, amarillo y blanco.
- Marcar como **borrador de IA** y pedir al usuario la versión grande desde Canva para publicar.

## Alta resolución (importante)
Canva entrega las ilustraciones en 200 px; si se estiran con un resize normal se ven pixeladas. Flujo correcto:
1. `scripts/upscale.py` (Real-ESRGAN x4, funciona sin GPU, ~25 s por imagen) para llegar a 800 px reales.
2. `scripts/cutout.sh` sobre el resultado (tolerancia 9, o 3 en objetos blancos).
3. En objetos blancos (celular, robot, megáfono, calendario, portapapeles) el recorte se come brillos blancos del borde. Cerrar los huecos del alfa:
   `convert recorte.png -resize 800x800 -alpha extract -threshold 50% -morphology Close Disk:20 -blur 0x1 mascara.png` y volver a aplicar la máscara a la imagen ampliada (`-compose CopyOpacity`). El celular necesita `Disk:60`.
4. Guardar a 1200 px. El generador exporta además `slide-N@2x.png` (2160×2880) para publicar en alta resolución.
