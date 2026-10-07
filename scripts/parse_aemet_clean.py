import urllib.request
import re
import json

url = 'https://www.aemet.es/es/eltiempo/prediccion/municipios?p=07&w=t'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

with urllib.request.urlopen(req) as resp:
    raw = resp.read()
    html = raw.decode('iso-8859-15')

matches = re.findall(r'\{\s*"nombreNormalizado"\s*:\s*"([^"]+)"\s*,\s*"provincia"\s*:\s*"[^"]*"\s*,\s*"nombre"\s*:\s*"([^"]+)"\s*\}', html)

menorca_slugs = {'alaior', 'castell-es', 'ciutadella-de-menorca', 'ferreries', 'mao-mahon', 'mercadal-es', 'migjorn-gran-es', 'sant-lluis'}
pitiuses_slugs = {'eivissa', 'formentera', 'sant-antoni-de-portmany', 'sant-joan-de-labritja', 'sant-josep-de-sa-talaia', 'santa-eularia-des-riu'}

formatted = []
seen = set()

for slug, name in matches:
    if '-id07' in slug and slug not in seen:
        seen.add(slug)
        slug_base = slug.split('-id')[0].lower()
        id_code = slug.split('-id')[-1]
        
        illa = 'Mallorca'
        if any(s in slug_base for s in menorca_slugs):
            illa = 'Menorca'
        elif any(s in slug_base for s in pitiuses_slugs):
            illa = 'Eivissa / Formentera'
            
        formatted.append({
            'municipi': name,
            'codi_ine': id_code,
            'slug': slug,
            'url': f"https://www.aemet.es/es/eltiempo/prediccion/municipios/{slug}",
            'xml_url': f"https://www.aemet.es/xml/municipios/localidad_{id_code}.xml",
            'illa': illa
        })

formatted.sort(key=lambda x: (x['illa'] != 'Mallorca', x['illa'], x['municipi']))

with open('data/aemet_municipis_balears.json', 'w', encoding='utf-8') as f:
    json.dump(formatted, f, ensure_ascii=False, indent=2)

print(f"Total municipis balears filtrats (província 07): {len(formatted)}")
mallorca = [x for x in formatted if x['illa'] == 'Mallorca']
menorca = [x for x in formatted if x['illa'] == 'Menorca']
pitiuses = [x for x in formatted if x['illa'] == 'Eivissa / Formentera']
print(f"Mallorca: {len(mallorca)}, Menorca: {len(menorca)}, Pitiüses: {len(pitiuses)}")
