import urllib.request
import re
import json
from html import unescape

url = 'https://www.aemet.es/es/eltiempo/prediccion/municipios?p=07&w=t'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
except Exception as e:
    print(f"Error fetching URL: {e}")
    # Fallback to local markdown file if available
    exit(1)

# Find all links to prediccion/municipios/<slug>-id07...
matches = re.findall(r'href="(/es/eltiempo/prediccion/municipios/([^"?]+(?:id07\d+)[^"]*))"[^>]*>([^<]+)</a>', html)

results = []
seen = set()

for full_href, slug_id, raw_name in matches:
    name = unescape(raw_name).strip()
    full_url = f"https://www.aemet.es{full_href}"
    if full_url not in seen:
        seen.add(full_url)
        # Extract ID (e.g. id07001)
        id_match = re.search(r'id(07\d+)', slug_id)
        codi_ine = id_match.group(1) if id_match else ""
        results.append({
            "municipi": name,
            "codi_ine": codi_ine,
            "url": full_url
        })

# Sort alphabetically by municipality name
results.sort(key=lambda x: x["municipi"])

print(f"Total municipis trobats: {len(results)}")

with open('data/aemet_municipis_balears.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Fitxer 'data/aemet_municipis_balears.json' creat correctament.")
