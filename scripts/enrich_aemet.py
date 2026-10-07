import json

with open('data/aemet_municipis_balears.json', 'r', encoding='utf-8') as f:
    municipis = json.load(f)

menorca_names = {
    'Alaior', 'Castell, Es', 'Es Castell', 'Ciutadella de Menorca', 'Ferreries',
    'Maó-Mahón', 'Maó', 'Mahon', 'Mercadal, Es', 'Es Mercadal',
    'Migjorn Gran, Es', 'Es Migjorn Gran', 'Sant Lluís'
}

pitiuses_names = {
    'Eivissa', 'Ibiza', 'Santa Eulària des Riu', 'Santa Eulalia del Río',
    'Sant Antoni de Portmany', 'Sant Josep de sa Talaia',
    'Sant Joan de Labritja', 'Formentera'
}

for m in municipis:
    nom = m['municipi']
    if any(k.lower() in nom.lower() for k in menorca_names) or 'menorca' in m['slug']:
        m['illa'] = 'Menorca'
    elif any(k.lower() in nom.lower() for k in pitiuses_names) or 'formentera' in m['slug'] or 'ibiza' in m['slug'] or 'eivissa' in m['slug']:
        m['illa'] = 'Eivissa / Formentera'
    else:
        m['illa'] = 'Mallorca'

# Sort by illa, then municipi
municipis.sort(key=lambda x: (x['illa'] != 'Mallorca', x['illa'], x['municipi']))

with open('data/aemet_municipis_balears.json', 'w', encoding='utf-8') as f:
    json.dump(municipis, f, ensure_ascii=False, indent=2)

mallorca_count = sum(1 for m in municipis if m['illa'] == 'Mallorca')
menorca_count = sum(1 for m in municipis if m['illa'] == 'Menorca')
pitiuses_count = sum(1 for m in municipis if m['illa'] == 'Eivissa / Formentera')

print(f"Total: {len(municipis)}")
print(f"- Mallorca: {mallorca_count}")
print(f"- Menorca: {menorca_count}")
print(f"- Pitiüses: {pitiuses_count}")
