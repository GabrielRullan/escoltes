import urllib.request
import re
import json

url = 'https://www.aemet.es/es/eltiempo/prediccion/municipios?p=07&w=t'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

with urllib.request.urlopen(req) as resp:
    charset = resp.headers.get_content_charset() or 'iso-8859-15'
    print("Charset:", charset)
    raw = resp.read()
    try:
        html = raw.decode(charset)
    except Exception:
        html = raw.decode('iso-8859-15', errors='replace')

# Match href='...' and municipality name
pattern = r"<a\s+href=['\"](/es/eltiempo/prediccion/municipios/([^'\"]+))['\"][^>]*>([^<]+)</a>"
matches = re.findall(pattern, html)

results = []
seen = set()

for full_path, slug_id, name in matches:
    clean_name = name.strip()
    full_url = f"https://www.aemet.es{full_path}"
    if clean_name not in seen and 'id07' in slug_id:
        seen.add(clean_name)
        id_match = re.search(r'id(07\d+)', slug_id)
        ine_code = id_match.group(1) if id_match else ""
        results.append({
            "municipi": clean_name,
            "codi_ine": ine_code,
            "slug": slug_id,
            "url": full_url
        })

results.sort(key=lambda x: x["municipi"])
print(f"Total municipis balears trobats: {len(results)}")

for r in results[:10]:
    print(f"{r['codi_ine']}: {r['municipi']} -> {r['url']}")

with open('data/aemet_municipis_balears.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nDesat amb èxit a 'data/aemet_municipis_balears.json'")
