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

for m in mallorca_aemet:
    cat = m.get('municipi_cat', m['municipi'])
    n_cat = norm(cat)
    n_raw = norm(m['municipi'])

    # Matching rutes
    matched_r = []
    for r in rutes:
        r_tokens = [norm(t) for t in get_tokens(r.get('municipi', ''))]
        for t in r_tokens:
            if t == n_cat or t == n_raw or (len(t) > 4 and (t in n_cat or n_cat in t)):
                matched_r.append({'nom': r['nom'], 'slug': r['slug'], 'dificultat': r.get('dificultat', '')})
                break
    m['rutes'] = matched_r

    # Matching acampada
    matched_ac = []
    for ac in acampada:
        ac_tokens = [norm(t) for t in get_tokens(ac.get('municipi', ''))]
        for t in ac_tokens:
            if t == n_cat or t == n_raw or (len(t) > 4 and (t in n_cat or n_cat in t)):
                matched_ac.append({'nom': ac['nom'], 'titularitat': ac.get('titularitat', '')})
                break
    m['acampades'] = matched_ac

print('Municipis summary:')
for m in sorted(mallorca_aemet, key=lambda x: -(len(x['rutes']) + len(x['acampades']))):
    num_r = len(m['rutes'])
    num_ac = len(m['acampades'])
    name = m.get('municipi_cat', m['municipi'])
    if num_r > 0 or num_ac > 0:
        print(f"{name}: {num_r} rutes, {num_ac} acampades")
