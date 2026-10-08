import json

routes = json.load(open('data/rutes_mallorca.json', encoding='utf-8'))
print(f"Total rutes: {len(routes)}")
for i, r in enumerate(routes):
    passos = r.get('itinerari_passos', [])
    first_step = passos[0] if passos else ''
    if isinstance(first_step, dict):
        step_str = f"{first_step.get('nom')}: {first_step.get('desc')}"
    else:
        step_str = str(first_step)
    print(f"{i+1}. [{r['slug']}] {r['nom']} ({r['municipi']}) -> Step1: {step_str[:60]}")

acampades = json.load(open('data/acampada_mallorca.json', encoding='utf-8'))
print(f"\nTotal acampades: {len(acampades)}")
for i, a in enumerate(acampades):
    print(f"{i+1}. [{a['slug']}] {a['nom']} ({a['municipi']}) -> Accés: {a.get('acces_emergencia', '')[:50]}")
