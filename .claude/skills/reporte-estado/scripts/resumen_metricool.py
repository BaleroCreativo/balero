#!/usr/bin/env python3
"""Resume la salida de getScheduledPosts de Metricool en una tabla por fecha.

Uso: python3 resumen_metricool.py archivo1.json [archivo2.json ...]

Acepta el archivo que guarda la herramienta cuando la respuesta es larga
(una lista con {"type":"text","text":"<json>"}) o el JSON directo con "data".
Marca por publicación: estado, imágenes, ALT, marcador [BORRADOR] y red.
Sin dependencias fuera de la biblioteca estándar.
"""
import json, sys
from collections import Counter


def cargar(ruta):
    raw = json.load(open(ruta, encoding="utf-8"))
    if isinstance(raw, list) and raw and isinstance(raw[0], dict) and "text" in raw[0]:
        raw = json.loads(raw[0]["text"])
    return raw.get("data", raw) if isinstance(raw, dict) else raw


def estado(p):
    red = p["providers"][0]
    det = (red.get("detailedStatus") or red.get("status") or "").lower()
    if "publish" in det:
        return "PUBLICADO"
    if p.get("draft"):
        return "BORRADOR"
    return "PROGRAMADO"


def main(rutas):
    posts = {}
    for r in rutas:
        for p in cargar(r):
            posts[p["uuid"]] = p  # dedupe por uuid entre rangos
    filas = []
    alertas = []
    for p in sorted(posts.values(), key=lambda x: x["publicationDate"]["dateTime"]):
        red = p["providers"][0]["network"]
        fecha = p["publicationDate"]["dateTime"][:16].replace("T", " ")
        est = estado(p)
        media = p.get("media") or []
        alts = [a for a in (p.get("mediaAltText") or []) if a]
        marcador = "[BORRADOR" in p.get("text", "")
        texto = p.get("text", "").replace("\n", " ")[:50]
        filas.append((fecha, red, est, len(media), len(alts), marcador, texto))
        if red in ("instagram", "facebook", "linkedin") and not media and \
                str((p.get("linkedinData") or {}).get("type", "")).upper() != "POLL":
            if red == "instagram" or est != "PUBLICADO":
                alertas.append(f"{fecha} {red}: sin imágenes")
        if media and len(alts) < len(media) and red == "instagram":
            alertas.append(f"{fecha} {red}: {len(media) - len(alts)} imagen(es) sin texto ALT")
        if marcador and est != "BORRADOR":
            alertas.append(f"{fecha} {red}: programado con marcador [BORRADOR] en el texto")
    print(f"{'Fecha':<17}{'Red':<10}{'Estado':<11}{'Img':>4}{'ALT':>5}  {'Marcador':<9}Texto")
    for f in filas:
        print(f"{f[0]:<17}{f[1]:<10}{f[2]:<11}{f[3]:>4}{f[4]:>5}  {'sí' if f[5] else '':<9}{f[6]}")
    c = Counter(f[2] for f in filas)
    print(f"\nTotal {len(filas)}: " + ", ".join(f"{k} {v}" for k, v in sorted(c.items())))
    if alertas:
        print("\nAlertas:")
        for a in alertas:
            print(" -", a)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
