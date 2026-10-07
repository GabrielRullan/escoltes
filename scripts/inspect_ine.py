import urllib.request
import re

req = urllib.request.Request('https://www.aemet.es/es/eltiempo/prediccion/municipios?p=07&w=t', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('iso-8859-15')

# The page has a table or JSON
pattern = r'\{\s*"nombreNormalizado"\s*:\s*"([^"]+)"\s*,\s*"provincia"\s*:\s*"[^"]*"\s*,\s*"nombre"\s*:\s*"([^"]+)"\s*\}'
matches = re.findall(pattern, html)

for slug, name in matches:
    if '-id07' in slug:
        ine = slug.split('-id')[-1]
        print(f"{ine} | {slug} | {name}")
