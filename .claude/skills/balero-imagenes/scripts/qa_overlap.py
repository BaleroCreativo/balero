#!/usr/bin/env python3
"""QA de superposición por píxeles para un carrusel ya generado.

Uso:  python3 qa_overlap.py carpeta_salida/ [--slides 2,3,4]
Lee carpeta_salida/html/slide-N.html, renderiza cuatro variantes (solo fondo, solo ilustración, solo texto, solo logo/puntos/pie)
y mide cuántos píxeles se pisan: ilustración vs texto, ilustración vs logo/puntos/pie, texto vs logo/puntos/pie.
Un slide pasa si ninguna de las tres cuentas pasa de TOL píxeles (ruido de sombras suaves). Requiere Pillow y Chrome headless_shell.
"""
import argparse, glob, os, re, subprocess, sys, tempfile
from PIL import Image, ImageChops

ILL = ".ill"
TEXT = ".zstack,.hero-t,.hero-b,.hero-k,.layer,.chip,.bar,.sticker,.arrowbtn,.poster-t,.poster-s,.pad,.body"
CHROME = ".logo,.dots,.foot,.next"
TOL = 40


def chrome():
    for pat in ("/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell",):
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    sys.exit("No encontré headless_shell.")


def shot(exe, html, hide, W, H, out):
    css = "<style>" + (hide + "{visibility:hidden !important}" if hide else "") + "</style>"
    src = open(html, encoding="utf-8").read().replace("</head>", css + "</head>", 1)
    tmp = html.replace(".html", ".qa.html")
    open(tmp, "w", encoding="utf-8").write(src)
    subprocess.run([exe, "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                    "--force-device-scale-factor=1", "--virtual-time-budget=4000", f"--window-size={W},{H}",
                    f"--screenshot={out}", "file://" + tmp], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    os.remove(tmp)
    return Image.open(out).convert("RGB")


def mask(img, bg):
    d = ImageChops.difference(img, bg).convert("L")
    return d.point(lambda v: 255 if v > 28 else 0)


def count(a, b):
    m = ImageChops.multiply(a, b)
    return m.histogram()[255]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("salida")
    ap.add_argument("--slides")
    a = ap.parse_args()
    exe = chrome()
    htmls = sorted(glob.glob(os.path.join(a.salida, "html", "slide-*.html")), key=lambda p: int(re.findall(r"slide-(\d+)", p)[0]))
    only = {int(x) for x in a.slides.split(",")} if a.slides else None
    bad = 0
    tmpd = tempfile.mkdtemp()
    for h in htmls:
        n = int(re.findall(r"slide-(\d+)", h)[0])
        if only and n not in only:
            continue
        W, H = 1080, 1440
        allhide = ",".join([ILL, TEXT, CHROME])
        bg = shot(exe, h, allhide, W, H, os.path.join(tmpd, "bg.png"))
        ic = mask(shot(exe, h, ",".join([TEXT, CHROME]), W, H, os.path.join(tmpd, "ic.png")), bg)
        tx = mask(shot(exe, h, ",".join([ILL, CHROME]), W, H, os.path.join(tmpd, "tx.png")), bg)
        ch = mask(shot(exe, h, ",".join([ILL, TEXT]), W, H, os.path.join(tmpd, "ch.png")), bg)
        r = {"icono/texto": count(ic, tx), "icono/logo-puntos-pie": count(ic, ch), "texto/logo-puntos-pie": count(tx, ch)}
        ok = all(v <= TOL for v in r.values())
        bad += 0 if ok else 1
        print(f"slide-{n}: " + ("OK " if ok else "REVISAR ") + "  ".join(f"{k}={v}px" for k, v in r.items()))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
