import urllib.request
import re

url = 'https://www.aemet.es/es/eltiempo/prediccion/municipios?p=07&w=t'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

print("Longitud HTML:", len(html))
# Find some links
links = re.findall(r'href="([^"]*municipios[^"]*)"', html)
print(f"Total hrefs amb 'municipios': {len(links)}")
for l in links[:15]:
    print("Link:", l)
