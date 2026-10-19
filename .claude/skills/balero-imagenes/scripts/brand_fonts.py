#!/usr/bin/env python3
"""Descarga las tipografías de una marca desde Google Fonts y escribe su fonts.css.

Uso: python3 brand_fonts.py ruta/brand.json

Lee "font_title" y "font_body" del brand.json y deja los archivos en
<carpeta del brand.json>/fonts/ junto con fonts/fonts.css. Después hay que
poner  "fonts_css": "fonts/fonts.css"  en el brand.json (el script lo añade si falta).

Pesos que pide el generador: light (por defecto 300), heavy (800), body (400) y
body_bold (700), más 600 para el subtítulo del póster. Si una familia no tiene
algún peso, se usa el más cercano disponible y se avisa. Fuentes que no estén en
Google Fonts (de pago o propias): copia los .ttf a la carpeta y escribe el
fonts.css a mano con @font-face usando los mismos nombres de familia.
"""
import json, os, re, sys, urllib.parse, urllib.request

UA = "Mozilla/5.0 Chrome/120"


def css(family, weights):
    q = f"{urllib.parse.quote_plus(family)}:wght@{';'.join(str(w) for w in sorted(weights))}"
    req = urllib.request.Request(f"https://fonts.googleapis.com/css2?family={q}&display=swap", headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=25).read().decode()


def fetch_family(family, wanted, outdir):
    """Intenta con todos los pesos; si falla, va quitando de uno en uno los que no existen."""
    weights = sorted(set(wanted))
    text = None
    while weights:
        try:
            text = css(family, weights)
            break
        except Exception:
            # probar pesos de uno en uno para encontrar los disponibles
            ok = []
            for w in weights:
                try:
                    css(family, [w]); ok.append(w)
                except Exception:
                    pass
            if not ok:
                sys.exit(f"No encontré la familia '{family}' en Google Fonts. Copia los .ttf a {outdir} y escribe fonts.css a mano.")
            missing = sorted(set(weights) - set(ok))
            print(f"  {family}: sin pesos {missing}; se usarán los disponibles {ok}")
            weights = ok
    faces = []
    for block in re.findall(r"@font-face \{(.*?)\}", text, re.S):
        style = re.search(r"font-style: (\w+)", block).group(1)
        weight = re.search(r"font-weight: (\d+)", block).group(1)
        url = re.search(r"url\((.*?)\)", block).group(1)
        if style != "normal":
            continue
        fn = f"{family.replace(' ', '')}-{weight}-{style}.ttf"
        urllib.request.urlretrieve(url, os.path.join(outdir, fn))
        faces.append((int(weight), fn))
    return faces


def main(path):
    path = os.path.abspath(path)
    brand = json.load(open(path, encoding="utf-8"))
    base = os.path.dirname(path)
    outdir = os.path.join(base, "fonts")
    os.makedirs(outdir, exist_ok=True)
    w = {"light": 300, "heavy": 800, "body": 400, "body_bold": 700}
    w.update(brand.get("weights", {}))
    wanted = [w["light"], w["heavy"], w["body"], w["body_bold"], 600]
    fam_title = brand.get("font_title", "Poppins")
    fam_body = brand.get("font_body", "Source Sans Pro")
    rules = []
    for fam in dict.fromkeys([fam_title, fam_body]):
        print(f"Descargando {fam}…")
        for weight, fn in fetch_family(fam, wanted, outdir):
            rules.append(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{weight};"
                         f"src:url('{os.path.join(outdir, fn)}') format('truetype');}}")
    open(os.path.join(outdir, "fonts.css"), "w").write("\n".join(rules))
    if not brand.get("fonts_css"):
        brand["fonts_css"] = "fonts/fonts.css"
        json.dump(brand, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print('Añadí "fonts_css" al brand.json.')
    print(f"{len(rules)} estilos listos en {outdir}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
