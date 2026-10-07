import json

with open('data/aemet_municipis_balears.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

lines = []
lines.append("# Directori de URLs de Previsió Meteorològica AEMET - Illes Balears\n")
lines.append("Aquest llistat conté els 66 municipis de les Illes Balears (província 07) amb el seu codi oficial INE / AEMET i la URL directa de predicció diària i horària.\n")

for illa in ["Mallorca", "Menorca", "Eivissa / Formentera"]:
    subset = [d for d in data if d.get("illa") == illa]
    lines.append(f"\n## 📍 {illa} ({len(subset)} municipis)\n")
    lines.append("| Codi INE | Municipi | URL AEMET |")
    lines.append("|---|---|---|")
    for d in subset:
        lines.append(f"| `{d['codi_ine']}` | **{d['municipi']}** | [{d['slug']}]({d['url']}) |")

output_md = "\n".join(lines)

with open('docs_md/aemet_previsions_municipis.md', 'w', encoding='utf-8') as f:
    f.write(output_md)

print("Fitxer 'docs_md/aemet_previsions_municipis.md' generat amb èxit!")
