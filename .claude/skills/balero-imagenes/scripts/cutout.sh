#!/usr/bin/env bash
# Quita el fondo liso de una ilustración 3D generada (JPG/PNG) y la deja como PNG transparente.
# Uso: bash cutout.sh entrada.jpg salida.png
set -euo pipefail
IN="$1"; OUT="$2"
W=$(identify -format %w "$IN"); H=$(identify -format %h "$IN")
convert "$IN" -filter Lanczos -resize 400% -fuzz 9% -fill none \
  -draw "color 0,0 floodfill" -draw "color $((W*4-1)),0 floodfill" \
  -draw "color 0,$((H*4-1)) floodfill" -draw "color $((W*4-1)),$((H*4-1)) floodfill" \
  -channel A -morphology Erode Disk:2 -blur 0x1.2 -level 8%,100% +channel "$OUT"
echo "ok: $OUT (revisar bordes al ampliar)"
