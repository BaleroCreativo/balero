#!/usr/bin/env bash
# Descarga Poppins (300, 400, 600, 800) y Source Sans Pro (300, 400, 600, 700, 700 itálica)
# a ../fonts/ y escribe ../fonts/fonts.css con los @font-face. Se ejecuta una sola vez.
set -euo pipefail
DIR="$(cd "$(dirname "$0")/.." && pwd)/fonts"
mkdir -p "$DIR"
UA="Mozilla/5.0 Chrome/120"
fetch_css() { curl -fsS -m 20 -A "$UA" "https://fonts.googleapis.com/css2?family=$1&display=swap"; }
python3 - "$DIR" <<'PY'
import re, subprocess, sys, urllib.request
d = sys.argv[1]
UA = "Mozilla/5.0 Chrome/120"
def css(fam):
    req = urllib.request.Request(f"https://fonts.googleapis.com/css2?family={fam}&display=swap", headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=20).read().decode()
out = []
for family, query in (("Poppins", "Poppins:wght@300;400;600;800"),
                      ("Source Sans Pro", "Source+Sans+Pro:ital,wght@0,300;0,400;0,600;0,700;1,700")):
    for block in re.findall(r"@font-face \{(.*?)\}", css(query), re.S):
        style = re.search(r"font-style: (\w+)", block).group(1)
        weight = re.search(r"font-weight: (\d+)", block).group(1)
        url = re.search(r"url\((.*?)\)", block).group(1)
        fn = f"{family.replace(' ', '')}-{weight}-{style}.ttf"
        urllib.request.urlretrieve(url, f"{d}/{fn}")
        out.append(f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};src:url('{d}/{fn}') format('truetype');}}")
open(f"{d}/fonts.css", "w").write("\n".join(out))
print(f"{len(out)} fuentes listas en {d}")
PY
