import json
import unicodedata

with open('data/aemet_municipis_balears.json', 'r', encoding='utf-8') as f:
    aemet = json.load(f)
with open('data/rutes_mallorca.json', 'r', encoding='utf-8') as f:
    rutes = json.load(f)
with open('data/acampada_mallorca.json', 'r', encoding='utf-8') as f:
    acampada = json.load(f)

def norm(s):
    if not s:
        return ''
    s = s.split('(')[0].replace('Salines, ses', 'ses salines').replace('Pobla, sa', 'sa pobla').strip()
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')

def get_tokens(text):
    if not text:
        return []
    cleaned = text.replace('/', ',').replace('-', ',').split('(')[0]
    return [t.strip() for t in cleaned.split(',') if t.strip()]

mallorca_aemet = [x for x in aemet if x.get('illa') == 'Mallorca']

result = []
for m in mallorca_aemet:
    cat = m.get('municipi_cat', m['municipi'])
    n_cat = norm(cat)
    n_raw = norm(m['municipi'])

    m_rutes = []
    for r in rutes:
        r_tokens = [norm(t) for t in get_tokens(r.get('municipi', ''))]
        for t in r_tokens:
            if t == n_cat or t == n_raw or (len(t) > 4 and (t in n_cat or n_cat in t)):
                m_rutes.append({
                    'nom': r['nom'],
                    'slug': r['slug'],
                    'dificultat': r.get('dificultat', ''),
                    'distancia_km': r.get('distancia_km', 0),
                    'desnivell_positiu_m': r.get('desnivell_positiu_m', 0),
                    'durada_estimada': r.get('durada_estimada', '')
                })
                break

    m_acampades = []
    for ac in acampada:
        ac_tokens = [norm(t) for t in get_tokens(ac.get('municipi', ''))]
        for t in ac_tokens:
            if t == n_cat or t == n_raw or (len(t) > 4 and (t in n_cat or n_cat in t)):
                m_acampades.append({
                    'nom': ac['nom'],
                    'titularitat': ac.get('titularitat', ''),
                    'capacitat': ac.get('capacitat', ''),
                    'web': ac.get('web', '')
                })
                break

    result.append({
        'codi_ine': m['codi_ine'],
        'municipi': m['municipi'],
        'municipi_cat': cat,
        'slug': m['slug'],
        'url': m['url'],
        'xml_url': m['xml_url'],
        'illa': m['illa'],
        'rutes': m_rutes,
        'acampades': m_acampades,
        'total_recursos': len(m_rutes) + len(m_acampades)
    })

# Sort alphabetically by Catalan name for intuitive lookup
result.sort(key=lambda x: x['municipi_cat'])

with open('data/municipis_amb_recursos.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"Total Mallorca municipalities processed: {len(result)}")
with_resources = [x for x in result if x['total_recursos'] > 0]
print(f"Municipalities with routes or campsites: {len(with_resources)}")
