import json

def map_units(route):
    nom = route.get('nom', '').lower()
    diff = route.get('dificultat', '').lower()
    km = route.get('distancia_km', 0)
    desn = route.get('desnivell_positiu_m', 0)
    old = [u.lower() for u in route.get('apte_unitats', [])]

    # Extreme / technical routes
    if 'pareis' in nom or 'tècnica' in diff or 'tecnica' in diff or (km > 22 and desn > 900):
        return ['Rutes (i guies)']

    # Easy routes (Fàcil or Molt Fàcil, including Fàcil - Moderada)
    if 'fàcil' in diff or 'facil' in diff:
        if (km <= 6.0 and desn <= 180) or 'molt fàcil' in diff or 'molt facil' in diff or any('ferreret' in u or 'castor' in u for u in old):
            return ['Ferrerets', 'Llops i Daines', 'Ràngers i esplets', 'Pioners i caravel·les', 'Rutes (i guies)']
        return ['Llops i Daines', 'Ràngers i esplets', 'Pioners i caravel·les', 'Rutes (i guies)']

    # Demanding / Exigent routes
    if 'exigent' in diff or km >= 16 or desn >= 700:
        return ['Pioners i caravel·les', 'Rutes (i guies)']

    # General / Moderate routes
    return ['Ràngers i esplets', 'Pioners i caravel·les', 'Rutes (i guies)']

# Process data/rutes_mallorca.json
routes_m = json.load(open('data/rutes_mallorca.json', encoding='utf-8'))
for r in routes_m:
    if r['slug'] == 'finca-publica-raixa':
        r['nom'] = 'Volta per la Finca Pública de Raixa'
    elif r['slug'] == 'castell-de-bellver-bosc-palma':
        r['nom'] = 'Passejada pel Bosc del Castell de Bellver (Palma)'
    r['apte_unitats'] = map_units(r)

with open('data/rutes_mallorca.json', 'w', encoding='utf-8') as f:
    json.dump(routes_m, f, indent=2, ensure_ascii=False)

# Process data/rutes_menorca.json
routes_me = json.load(open('data/rutes_menorca.json', encoding='utf-8'))
for r in routes_me:
    r['apte_unitats'] = map_units(r)

with open('data/rutes_menorca.json', 'w', encoding='utf-8') as f:
    json.dump(routes_me, f, indent=2, ensure_ascii=False)

# Process data/rutes_eivissa.json
routes_e = json.load(open('data/rutes_eivissa.json', encoding='utf-8'))
for r in routes_e:
    r['apte_unitats'] = map_units(r)

with open('data/rutes_eivissa.json', 'w', encoding='utf-8') as f:
    json.dump(routes_e, f, indent=2, ensure_ascii=False)

# Process data/rutes_formentera.json
routes_f = json.load(open('data/rutes_formentera.json', encoding='utf-8'))
for r in routes_f:
    r['apte_unitats'] = map_units(r)

with open('data/rutes_formentera.json', 'w', encoding='utf-8') as f:
    json.dump(routes_f, f, indent=2, ensure_ascii=False)

print("Applied unit mapping successfully!")
