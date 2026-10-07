import urllib.request
import re
import json

req = urllib.request.Request('https://www.aemet.es/es/eltiempo/prediccion/municipios?p=07&w=t', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    raw = resp.read()
    html = raw.decode('iso-8859-15')

pattern = r'\{\s*"nombreNormalizado"\s*:\s*"([^"]+)"\s*,\s*"provincia"\s*:\s*"[^"]*"\s*,\s*"nombre"\s*:\s*"([^"]+)"\s*\}'
matches = re.findall(pattern, html)

# Canonical Catalan names for Balearic municipalities
official_catalan_names = {
    '07001': ('Alaró', 'Mallorca'),
    '07002': ('Alaior', 'Menorca'),
    '07003': ('Alcúdia', 'Mallorca'),
    '07004': ('Algaida', 'Mallorca'),
    '07005': ('Andratx', 'Mallorca'),
    '07006': ('Artà', 'Mallorca'),
    '07007': ('Banyalbufar', 'Mallorca'),
    '07008': ('Binissalem', 'Mallorca'),
    '07009': ('Búger', 'Mallorca'),
    '07010': ('Bunyola', 'Mallorca'),
    '07011': ('Calvià', 'Mallorca'),
    '07012': ('Campanet', 'Mallorca'),
    '07013': ('Campos', 'Mallorca'),
    '07014': ('Capdepera', 'Mallorca'),
    '07015': ('Ciutadella de Menorca', 'Menorca'),
    '07016': ('Consell', 'Mallorca'),
    '07017': ('Costitx', 'Mallorca'),
    '07018': ('Deià', 'Mallorca'),
    '07019': ('Escorca', 'Mallorca'),
    '07020': ('Esporles', 'Mallorca'),
    '07021': ('Estellencs', 'Mallorca'),
    '07022': ('Felanitx', 'Mallorca'),
    '07023': ('Ferreries', 'Menorca'),
    '07024': ('Formentera', 'Eivissa / Formentera'),
    '07025': ('Fornalutx', 'Mallorca'),
    '07026': ('Eivissa', 'Eivissa / Formentera'),
    '07027': ('Inca', 'Mallorca'),
    '07028': ('Lloret de Vistalegre', 'Mallorca'),
    '07029': ('Lloseta', 'Mallorca'),
    '07030': ('Llubí', 'Mallorca'),
    '07031': ('Llucmajor', 'Mallorca'),
    '07032': ('Maó', 'Menorca'),
    '07033': ('Manacor', 'Mallorca'),
    '07034': ('Mancor de la Vall', 'Mallorca'),
    '07035': ('Maria de la Salut', 'Mallorca'),
    '07036': ('Marratxí', 'Mallorca'),
    '07037': ('Es Mercadal', 'Menorca'),
    '07038': ('Montuïri', 'Mallorca'),
    '07039': ('Muro', 'Mallorca'),
    '07040': ('Palma', 'Mallorca'),
    '07041': ('Petra', 'Mallorca'),
    '07042': ('Pollença', 'Mallorca'),
    '07043': ('Porreres', 'Mallorca'),
    '07044': ('Sa Pobla', 'Mallorca'),
    '07045': ('Puigpunyent', 'Mallorca'),
    '07046': ('Sant Antoni de Portmany', 'Eivissa / Formentera'),
    '07047': ('Sencelles', 'Mallorca'),
    '07048': ('Sant Josep de sa Talaia', 'Eivissa / Formentera'),
    '07049': ('Sant Joan', 'Mallorca'),
    '07050': ('Sant Joan de Labritja', 'Eivissa / Formentera'),
    '07051': ('Sant Llorenç des Cardassar', 'Mallorca'),
    '07052': ('Sant Lluís', 'Menorca'),
    '07053': ('Santa Eugènia', 'Mallorca'),
    '07054': ('Santa Eulària des Riu', 'Eivissa / Formentera'),
    '07055': ('Santa Margalida', 'Mallorca'),
    '07056': ('Santa Maria del Camí', 'Mallorca'),
    '07057': ('Santanyí', 'Mallorca'),
    '07058': ('Selva', 'Mallorca'),
    '07059': ('Ses Salines', 'Mallorca'),
    '07060': ('Sineu', 'Mallorca'),
    '07061': ('Sóller', 'Mallorca'),
    '07062': ('Son Servera', 'Mallorca'),
    '07063': ('Valldemossa', 'Mallorca'),
    '07064': ('Es Castell', 'Menorca'),
    '07065': ('Vilafranca de Bonany', 'Mallorca'),
    '07901': ('Ariany', 'Mallorca'),
    '07902': ('Es Migjorn Gran', 'Menorca')
}

formatted = []
seen = set()

for slug, raw_name in matches:
    if '-id07' in slug and slug not in seen:
        seen.add(slug)
        id_code = slug.split('-id')[-1]
        cat_info = official_catalan_names.get(id_code, (raw_name, 'Mallorca'))
        cat_name, illa = cat_info
        
        formatted.append({
            'municipi': cat_name,
            'nom_oficial_aemet': raw_name,
            'codi_ine': id_code,
            'slug': slug,
            'url': f"https://www.aemet.es/es/eltiempo/prediccion/municipios/{slug}",
            'xml_url': f"https://www.aemet.es/xml/municipios/localidad_{id_code}.xml",
            'illa': illa
        })

# Sort: Mallorca first, then Menorca, Pitiüses, alphabetical by municipi
formatted.sort(key=lambda x: (x['illa'] != 'Mallorca', x['illa'], x['municipi']))

with open('data/aemet_municipis_balears.json', 'w', encoding='utf-8') as f:
    json.dump(formatted, f, ensure_ascii=False, indent=2)

print(f"Total: {len(formatted)} municipis")
mallorca = [x for x in formatted if x['illa'] == 'Mallorca']
print(f"Mallorca: {len(mallorca)} municipis")
for x in mallorca[:10]:
    print(f"  {x['codi_ine']} - {x['municipi']} -> {x['url']}")
