import json

data = json.load(open('data/rutes_mallorca.json', encoding='utf-8'))
print(f"Total rutes: {len(data)}")
for i, r in enumerate(data, 1):
    slug = r['slug']
    nom = r['nom']
    font = r.get('font', '')
    font_url = r.get('font_url', '')
    tp = r.get('turismepetit_url', '')
    wiki = r.get('wikiloc_url', '')
    print(f"{i:2d}. {slug}")
    print(f"    Nom: {nom}")
    print(f"    Font: {font} | Font URL: {font_url} | TP: {tp} | Wiki: {wiki}")
