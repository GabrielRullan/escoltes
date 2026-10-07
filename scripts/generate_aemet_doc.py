import json

with open('data/municipis_amb_recursos.json', 'r', encoding='utf-8') as f:
    mallorca_mun = json.load(f)

with open('data/aemet_municipis_balears.json', 'r', encoding='utf-8') as f:
    all_aemet = json.load(f)

menorca_mun = [x for x in all_aemet if x['illa'] == 'Menorca']
pitiuses_mun = [x for x in all_aemet if x['illa'] == 'Eivissa / Formentera']

md = []
md.append("# 🌤️ Directori AEMET & Recursos Escoltistes per Municipi")
md.append("")
md.append("Aquest document relaciona tots els municipis de les Illes Balears amb la predicció meteorològica oficial de l'Agència Estatal de Meteorologia (**AEMET**), indicant quines rutes escoltes i zones d'acampada/refugis passen o es troben a cadascun d'ells.")
md.append("")
md.append("> [!TIP]")
md.append("> Clica a **«Visualitza a l'AEMET»** per accedir a la predicció a 7 dies, probabilitat de precipitació i alertes d'avís groc/taronja abans de qualsevol sortida escolta.")
md.append("")
md.append("## 📍 Mallorca (53 municipis)")
md.append("")
md.append("| Municipi | Previsió AEMET | Rutes Escoltes | Refugis & Acampada |")
md.append("|---|:---:|---|---|")

for m in mallorca_mun:
    name = m['municipi_cat']
    btn = f"[{name} ↗]({m['url']})"
    
    # Rutes list
    if m['rutes']:
        r_links = [f"[{r['nom']}](/rutes/{r['slug']})" for r in m['rutes']]
        r_str = f"**{len(m['rutes'])} rutes:**<br>" + "<br>".join(r_links)
    else:
        r_str = "<span style='color:#888;'>Cap ruta registrada</span>"
        
    # Acampades list
    if m['acampades']:
        ac_names = [f"{a['nom']} *({a['titularitat']})*" for a in m['acampades']]
        ac_str = f"**{len(m['acampades'])} llocs:**<br>" + "<br>".join(ac_names)
    else:
        ac_str = "<span style='color:#888;'>Cap refugi/zona</span>"
        
    md.append(f"| **{name}** | {btn} | {r_str} | {ac_str} |")

md.append("")
md.append("## 📍 Menorca (8 municipis)")
md.append("")
md.append("| Municipi | Previsió AEMET |")
md.append("|---|:---:|")
for m in menorca_mun:
    name = m.get('municipi_cat', m['municipi'])
    btn = f"[{name} ↗]({m['url']})"
    md.append(f"| **{name}** | {btn} |")

md.append("")
md.append("## 📍 Eivissa i Formentera (6 municipis)")
md.append("")
md.append("| Municipi | Previsió AEMET |")
md.append("|---|:---:|")
for m in pitiuses_mun:
    name = m.get('municipi_cat', m['municipi'])
    btn = f"[{name} ↗]({m['url']})"
    md.append(f"| **{name}** | {btn} |")

content = "\n".join(md) + "\n"
with open('docs_md/aemet_previsions_municipis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated docs_md/aemet_previsions_municipis.md successfully!")
