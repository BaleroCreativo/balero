#!/usr/bin/env python3
"""Revisiones mecánicas de un carrusel ya renderizado.

Uso: python3 checks.py <carpeta-con-pngs> [--ancho 1080] [--alto 1440] [--escala 2] [--fuentes Montserrat,OpenSans]

Revisa lo que se puede medir sin criterio humano:
  1. Tamaño exacto de cada PNG (ancho*escala por alto*escala).
  2. Caja de contenido contra márgenes (8% laterales, 6% verticales). Las
     portadas con ilustración que sangra por el borde son intencionales, así
     que el script solo informa; decide una persona con la imagen delante.
  3. Fuentes de los PDF de la carpeta, con pdffonts, si está instalado.

No detecta texto encimado ni jerarquía: eso lo hace la revisión visual.
"""
import argparse, glob, os, shutil, subprocess, sys
from PIL import Image, ImageChops

ap = argparse.ArgumentParser()
ap.add_argument("carpeta")
ap.add_argument("--ancho", type=int, default=1080)
ap.add_argument("--alto", type=int, default=1440)
ap.add_argument("--escala", type=int, default=2)
ap.add_argument("--fuentes", default="Poppins,SourceSans",
                help="familias de la marca, separadas por coma (nombre sin espacios; ej. Montserrat,OpenSans)")
a = ap.parse_args()

W, H = a.ancho * a.escala, a.alto * a.escala
mx, my = round(W * 0.08), round(H * 0.06)
pngs = sorted(glob.glob(os.path.join(a.carpeta, "*.png")))
if not pngs:
    sys.exit(f"No hay PNG en {a.carpeta}")

problemas = 0
print(f"Esperado: {W}x{H}  márgenes: {mx}px laterales, {my}px verticales\n")
for p in pngs:
    im = Image.open(p).convert("RGB")
    nombre = os.path.basename(p)
    estado = []
    if im.size != (W, H):
        estado.append(f"TAMAÑO {im.size[0]}x{im.size[1]}")
        problemas += 1
    # fondo = color de la esquina superior izquierda; la caja de contenido son los píxeles distintos
    bg = Image.new("RGB", im.size, im.getpixel((2, 2)))
    diff = ImageChops.difference(im, bg).convert("L").point(lambda v: 255 if v > 24 else 0)
    box = diff.getbbox()
    if box:
        l, t, r, b = box
        fuera = []
        if l < mx - 4: fuera.append(f"izq {l}px")
        if t < my - 4: fuera.append(f"arriba {t}px")
        if r > W - mx + 4: fuera.append(f"der {W - r}px al borde")
        if b > H - my + 4: fuera.append(f"abajo {H - b}px al borde")
        if fuera:
            estado.append("contenido fuera de margen: " + ", ".join(fuera) + " (revisar; puede ser un sangrado intencional)")
    print(f"{nombre}: {'OK' if not estado else ' | '.join(estado)}")

pdfs = sorted(glob.glob(os.path.join(a.carpeta, "*.pdf")))
if pdfs and shutil.which("pdffonts"):
    print()
    permitidas = tuple(f.strip().replace(" ", "").lower() for f in a.fuentes.split(",") if f.strip())
    for p in pdfs:
        out = subprocess.run(["pdffonts", p], capture_output=True, text=True).stdout.splitlines()[2:]
        nombres = {l.split()[0].split("+")[-1] for l in out if l.strip()}
        raras = sorted(n for n in nombres if not n.lower().startswith(permitidas))
        if raras:
            problemas += 1
            print(f"{os.path.basename(p)}: FUENTES FUERA DE MARCA {', '.join(raras)}")
        else:
            print(f"{os.path.basename(p)}: fuentes OK ({', '.join(sorted(nombres))})")

print(f"\n{'Sin problemas mecánicos.' if not problemas else str(problemas) + ' problema(s) mecánico(s).'}")
sys.exit(1 if problemas else 0)
