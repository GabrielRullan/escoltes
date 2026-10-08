import json

routes = json.load(open('data/rutes_mallorca.json', encoding='utf-8'))
acampades = json.load(open('data/acampada_mallorca.json', encoding='utf-8'))

# Import the dictionaries
from check_origins import ROUTE_ORIGINS, ACAMPADA_ORIGINS

for r in routes:
    slug = r['slug']
    r['punt_origen'] = ROUTE_ORIGINS.get(slug, f"{r.get('municipi', 'Mallorca')} (punt d'inici de la ruta)")
    
    # Generate structured punts a tenir en compte if not present
    punts = []
    # 1. Punt d'origen
    punts.append(f"Inici i aparcament: Sortida des de {r['punt_origen']}.")
    
    # 2. Aigua
    if r.get('punts_aigua') and len(r['punts_aigua']) > 0:
        punts.append(f"Aigua potable disponible a: {', '.join(r['punts_aigua'])}. Recomanat dur cantimplora de reserva.")
    else:
        punts.append("Sense fonts d'aigua potables: És indispensable que cada escolta dugui un mínim de 2 a 2,5 litres d'aigua des de l'inici.")
        
    # 3. Finques i barreres
    if r.get('passos_finca_privada') and len(r['passos_finca_privada']) > 0:
        punts.append(f"Pas per finques i servituds: Respecteu les propietats i tanqueu sempre totes les barreres ({', '.join(r['passos_finca_privada'])}).")
    else:
        punts.append("Respecte pel medi i barreres: Camí públic senyalitzat. Tanqueu qualsevol portell que trobeu al vostre pas.")

    # 4. Prevenció d'incendis
    punts.append("Prevenció d'incendis a les Illes Balears: Prohibició absoluta de fer foc a terreny forestal (especialment època d'alt risc de l'1 de maig al 15 d'octubre).")

    # 5. Cobertura i material
    punts.append("Seguretat i orientació: Calçat de muntanya adequat, farmaciola d'unitat, mapa/track GPS descarregat i protecció solar/gorra.")

    r['punts_a_tenir_en_compte'] = punts

with open('data/rutes_mallorca.json', 'w', encoding='utf-8') as f:
    json.dump(routes, f, indent=2, ensure_ascii=False)

for a in acampades:
    slug = a['slug']
    a['punt_origen'] = ACAMPADA_ORIGINS.get(slug, f"Accés des de {a.get('municipi', 'Mallorca')}")

with open('data/acampada_mallorca.json', 'w', encoding='utf-8') as f:
    json.dump(acampades, f, indent=2, ensure_ascii=False)

print("Updated data/rutes_mallorca.json and data/acampada_mallorca.json successfully!")
