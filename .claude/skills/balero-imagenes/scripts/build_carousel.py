#!/usr/bin/env python3
"""Genera un carrusel de Balero (PNG por slide + PDF) a partir de un JSON.

Uso:  python3 build_carousel.py spec.json carpeta_salida/

Las rutas de ilustración del JSON son relativas a la carpeta del JSON.
Antes, una sola vez:  bash setup_fonts.sh
Reglas de marca: ver ../SKILL.md
"""
import glob
import json
import os
import shutil
import subprocess
import sys

SKILL = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOGO = os.path.join(SKILL, "assets", "logo-balero.png")
FONTS_CSS = os.path.join(SKILL, "fonts", "fonts.css")

# Marca
INDIGO, INK, LAVENDER = "#665FE9", "#000000", "#F6F5FF"
COVER_BG = "linear-gradient(180deg,#F4D9EE 0%,#F8E6DA 45%,#FFF3D6 100%)"
CLOSING_BG = "linear-gradient(180deg,#FFF8E3 0%,#F6EEFA 100%)"
MX, MY = 0.08, 0.06  # márgenes como fracción del borde: 8% laterales, 6% vertical (todas las piezas)
M_COVER = M_INNER = MX

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:%(W)dpx;height:%(H)dpx}
.slide{position:relative;width:%(W)dpx;height:%(H)dpx;overflow:hidden;background:%(LAV)s;
  font-family:'Source Sans Pro',sans-serif;color:%(INK)s;page-break-after:always;break-after:page}
.cover{background:%(COVER_BG)s}.closing{background:%(CLOSING_BG)s}
.pad{position:absolute;left:var(--mx);right:var(--mx)}
.logo{position:absolute;right:var(--mx);top:var(--my);width:%(logo)dpx}
.foot,.next{position:absolute;bottom:var(--my);font-family:'Poppins';font-weight:300;
  font-size:%(foot)dpx;text-transform:uppercase}
.foot{left:var(--mx)}.next{right:var(--mx)}
.kick{font-family:'Poppins';font-weight:300;font-size:%(kick)dpx;text-transform:uppercase;line-height:1}
.light{text-wrap:balance;font-family:'Poppins';font-weight:300;text-transform:uppercase;
  font-size:%(light)dpx;line-height:1.08;letter-spacing:-0.02em}
.heavy{text-wrap:balance;font-family:'Poppins';font-weight:800;text-transform:uppercase;
  font-size:%(heavy)dpx;line-height:1.03;letter-spacing:-0.045em;color:%(INDIGO)s}
.dark{font-family:'Poppins';font-weight:800;text-transform:uppercase;font-size:%(dark)dpx;
  line-height:1.02;letter-spacing:-0.045em;color:%(INK)s}
.body{font-family:'Source Sans Pro';font-weight:400;font-size:%(body)dpx;line-height:1.3;max-width:%(bodyw)dpx}
.body b{font-weight:700;color:%(INDIGO)s}
.body .strong{font-weight:700;color:%(INK)s}
.ill{position:absolute}
.dots{position:absolute;left:var(--mx);top:calc(var(--my) + %(dotoff)dpx);display:flex;gap:%(dotgap)dpx}
.dots i{width:%(dot)dpx;height:%(dot)dpx;border-radius:50%%;background:#DAD7F5}
.dots i.on{background:%(INDIGO)s}
"""


def find_chrome():
    for pat in ("/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell",
                "/opt/pw-browsers/chromium-*/chrome-linux/chrome"):
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1], "headless_shell" in hits[-1]
    for name in ("chromium", "chromium-browser", "google-chrome"):
        p = shutil.which(name)
        if p:
            return p, False
    sys.exit("No encontré Chrome/Chromium.")


def build(spec_path, out_dir):
    out_dir = os.path.abspath(out_dir)
    spec = json.load(open(spec_path, encoding="utf-8"))
    base = os.path.dirname(os.path.abspath(spec_path))
    W, H = spec.get("width", 1080), spec.get("height", 1440)
    sx, sy = W / 1080, H / 1440
    os.makedirs(os.path.join(out_dir, "html"), exist_ok=True)
    if not os.path.exists(FONTS_CSS):
        sys.exit("Faltan las tipografías: ejecuta  bash scripts/setup_fonts.sh")

    def ill(path):
        return os.path.join(base, path) if path else None

    css = CSS % dict(W=W, H=H, LAV=LAVENDER, INK=INK, INDIGO=INDIGO, COVER_BG=COVER_BG,
                     CLOSING_BG=CLOSING_BG, logo=96 * sx, foot=30 * sx, kick=38 * sx, light=80 * sx,
                     heavy=96 * sx, dark=104 * sx, body=48 * sx, bodyw=860 * sx,
                     dot=16 * sx, dotgap=12 * sx, dotoff=0)
    css = open(FONTS_CSS).read() + css
    logo = f'<img class="logo" src="file://{LOGO}">'
    arrow = ('<svg width="70" height="20" viewBox="0 0 70 20" style="vertical-align:middle;margin-left:14px">'
             '<path d="M0 10H66M58 2l8 8-8 8" fill="none" stroke="#000" stroke-width="2"/></svg>')

    def style_vars(m):
        return f"--mx:{round(W * m)}px;--my:{round(H * MY)}px"

    def img(path, style):
        return f'<img class="ill" src="file://{ill(path)}" style="{style}">' if path else ""

    total = len(spec["slides"])
    show_dots = spec.get("progress_dots", False)

    def dots(i):
        if not show_dots:
            return ""
        return '<div class="dots">' + "".join(f'<i class="{"on" if k == i else ""}"></i>' for k in range(1, total + 1)) + "</div>"

    slides = []
    for idx, s in enumerate(spec["slides"], 1):
        t = s["type"]
        if t == "cover":
            m = M_COVER
            slides.append(
                f'<div class="slide cover" style="{style_vars(m)}">{logo}{dots(idx)}'
                f'{img(s.get("illustration"), f"left:{390*sx}px;top:{105*sy}px;width:{580*sx}px")}'
                f'<div class="pad" style="top:{690*sy}px"><div class="light">{s["light"]}</div>'
                f'<div class="dark" style="margin-top:8px">{s["heavy"]}</div></div>'
                f'<div class="body" style="position:absolute;left:var(--mx);top:{1170*sy}px">{s.get("subtitle","")}</div>'
                f'<div class="foot">Balero Creativo</div>'
                f'{"<div class=next>Desliza" + arrow + "</div>" if s.get("swipe") else ""}</div>')
        elif t == "lesson":
            m = M_INNER
            if s.get("layout") == "top":
                pic = img(s.get("illustration"), f"left:{round(W*m)}px;top:{round(H*MY) + 64*sy}px;width:{380*sx}px")  # debajo de los puntos de progreso
                top = 600 * sy
            else:
                pic = img(s.get("illustration"), f"right:{round(W*m)}px;bottom:{round(H*MY)}px;width:{420*sx}px")
                top = 270 * sy
            slides.append(
                f'<div class="slide" style="{style_vars(m)}">{logo}{dots(idx)}{pic}'
                f'<div class="pad" style="top:{top}px"><div class="kick">Lección {s["number"]}</div>'
                f'<div class="heavy" style="margin-top:34px">{s["title"]}</div>'
                f'<div class="body" style="margin-top:56px">{s["body"]}</div></div>'
                f'<div class="foot">Balero Creativo</div></div>')
        elif t == "closing":
            m = M_INNER
            slides.append(
                f'<div class="slide closing" style="{style_vars(m)}">{logo}{dots(idx)}'
                f'{img(s.get("illustration"), f"right:{round(W*m)}px;bottom:{round(H*MY)}px;width:{240*sx}px")}'
                f'<div class="pad" style="top:{400*sy}px"><div class="light" style="font-size:{72*sx}px">{s["light"]}</div>'
                f'<div class="heavy" style="margin-top:10px;font-size:{100*sx}px">{s["heavy"]}</div></div>'
                f'<div class="pad" style="top:{940*sy}px"><div class="body" style="font-weight:700">'
                f'{s.get("offer_bold","")} <span style="color:{INDIGO}">{s.get("offer_accent","")}</span></div>'
                f'<div class="body" style="margin-top:6px">{s.get("action","")}</div></div>'
                f'<div class="foot">Balero Creativo</div></div>')
        else:
            sys.exit(f"Tipo de slide desconocido: {t}")

    head = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head><body>'
    for i, body in enumerate(slides, 1):
        open(os.path.join(out_dir, "html", f"slide-{i}.html"), "w", encoding="utf-8").write(head + body + "</body></html>")
    all_html = os.path.join(out_dir, "html", "all.html")
    open(all_html, "w", encoding="utf-8").write(
        head.replace("</style>", f"@page{{size:{W}px {H}px;margin:0}}</style>") + "".join(slides) + "</body></html>")

    chrome, headless_shell = find_chrome()
    base_cmd = [chrome, "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                "--force-device-scale-factor=1", "--virtual-time-budget=4000"]
    # Si no es headless_shell, el modo nuevo recorta alto por la barra: se pide una ventana más alta y se recorta.
    extra_h = 0 if headless_shell else 130
    if not headless_shell:
        base_cmd.insert(1, "--headless=new")
    for i in range(1, len(slides) + 1):
        png = os.path.join(out_dir, f"slide-{i}.png")
        subprocess.run(base_cmd + [f"--window-size={W},{H + extra_h}", f"--screenshot={png}",
                                   "file://" + os.path.join(out_dir, "html", f"slide-{i}.html")],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        if extra_h and shutil.which("convert"):
            subprocess.run(["convert", png, "-crop", f"{W}x{H}+0+0", "+repage", png], check=True)
    pdf = os.path.join(out_dir, spec.get("name", "carrusel") + ".pdf")
    subprocess.run(base_cmd + ["--no-pdf-header-footer", f"--print-to-pdf={pdf}", "file://" + all_html],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    verify(out_dir, pdf, len(slides), W, H)


def verify(out_dir, pdf, n, W, H):
    print(f"\nPDF: {pdf}  ({n} páginas)")
    if shutil.which("pdffonts"):
        names = subprocess.run(["pdffonts", pdf], capture_output=True, text=True).stdout.splitlines()[2:]
        fonts = sorted({ln.split()[0].split("+")[-1] for ln in names if ln.strip()})
        bad = [f for f in fonts if not f.startswith(("Poppins", "SourceSansPro"))]
        if not fonts:
            sys.exit("ERROR: el PDF salió sin texto; revisa las rutas (salida y spec).")
        print("Fuentes en el PDF:", ", ".join(fonts))
        print("OK: solo Poppins y Source Sans Pro" if not bad else f"ATENCIÓN, fuentes ajenas: {bad}")
    if shutil.which("convert"):
        print("Cajas de contenido oscuro (ancho x alto + x + y), para revisar márgenes:")
        for i in range(1, n + 1):
            png = os.path.join(out_dir, f"slide-{i}.png")
            box = subprocess.run(["convert", png, "-colorspace", "Gray", "-threshold", "60%", "-negate",
                                  "-trim", "info:"], capture_output=True, text=True).stdout.split()
            size = subprocess.run(["identify", "-format", "%wx%h", png], capture_output=True, text=True).stdout
            print(f"  slide-{i}: {size} | contenido {box[2] if len(box) > 2 else '?'} {box[3] if len(box) > 3 else ''}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    build(sys.argv[1], sys.argv[2])
