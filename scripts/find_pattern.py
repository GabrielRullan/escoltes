import urllib.request
import re

url = 'https://www.aemet.es/es/eltiempo/prediccion/municipios?p=07&w=t'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

# Search for Alaro or Soller
for m in re.finditer(r'Alar[oó]', html, re.I):
    start = max(0, m.start() - 150)
    end = min(len(html), m.end() + 150)
    print("Match Alaro context:\n", html[start:end])
    print("-" * 50)
    break

# Search for id07 or 070
for m in re.finditer(r'id07\d{3}', html):
    start = max(0, m.start() - 100)
    end = min(len(html), m.end() + 100)
    print("Match id07 context:\n", html[start:end])
    break
