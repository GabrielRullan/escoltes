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

    # Demanding / Exigent routes
    if 'exigent' in diff or km >= 16 or desn >= 700:
        return ['Pioners i caravel·les', 'Rutes (i guies)']

    # Moderate routes
    if 'moderad' in diff or (km >= 9 or desn >= 350):
        return ['Ràngers i esplets', 'Pioners i caravel·les', 'Rutes (i guies)']

    # Easy routes suitable for Ferrerets
    if any('ferreret' in u or 'castor' in u for u in old) or 'molt fàcil' in diff or 'molt facil' in diff or (km <= 5 and desn <= 150):
        return ['Ferrerets', 'Llops i Daines', 'Ràngers i esplets', 'Pioners i caravel·les', 'Rutes (i guies)']

    # General easy (6-9 km, low elevation)
    return ['Llops i Daines', 'Ràngers i esplets', 'Pioners i caravel·les', 'Rutes (i guies)']

counts = {}
for p in ['data/rutes_mallorca.json', 'data/rutes_menorca.json', 'data/rutes_eivissa.json', 'data/rutes_formentera.json']:
    data = json.load(open(p, encoding='utf-8'))
    print(f"\n=== {p} ({len(data)} rutes) ===")
    for r in data:
        u = map_units(r)
        key = " -> ".join([u[0], u[-1]]) if len(u) > 1 else u[0]
        counts[key] = counts.get(key, 0) + 1
        if 'pareis' in r['nom'].lower() or 'ferreret' in str(r.get('apte_unitats')).lower():
            print(f"  [{r['nom']}] ({r['dificultat']}, {r['distancia_km']}km, +{r['desnivell_positiu_m']}m) -> {u}")

print("\nSummary distribution across all 97 routes:")
for k, v in sorted(counts.items()):
    print(f"  {k}: {v} rutes")
