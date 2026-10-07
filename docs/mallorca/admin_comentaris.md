# 🛡️ Guia d'Administració de Comentaris i Experiències

Benvinguts al panell de coordinació dels Escoltes de Mallorca.

Per garantir la màxima fiabilitat, protecció antispam i seguretat de les dades, **els comentaris i experiències enviats des de qualsevol fitxa de ruta s'envien directament per correu electrònic a l'administrador (`escoltesmallorca@gmail.com`)**.

---

## 📬 Com funciona el flux de recepció i publicació

1. **Un cap o agrupament envia la seva experiència:**
   - Des de qualsevol de les 65+ fitxes de ruta, polsa *➕ Afegir la meva experiència*.
   - Selecciona el seu **agrupament** (s'ofereixen tots els caus de Mallorca, Menorca, Pitiüses i exteriors), la **unitat** (**Ferrerets**, **Llops/Daines**, **Rangers/Guies**, etc.), la puntuació d'estrelles i els consells.
   - El sistema envia automàticament les dades estructurades a la bústia de Gmail.

2. **L'administrador rep el correu:**
   Rebràs un correu amb aquest format:
   ```yaml
   Ruta: Ses Fonts Ufanes (Campanet) (ses-fonts-ufanes-campanet)
   Autor: Joan Bennàssar (joan@escoltes.cat)
   Agrupament: AEG Soca-Arrel
   Unitat: Ferrerets
   Valoració: 5 / 5 estrelles
   Data de la sortida: Març 2026
   Comentaris: "Camí pla, molt accessible per als més petits. Hi ha aigua corrent quan brollen les fonts."
   ```

3. **Afegir la ressenya a la base de dades local:**
   - Obre el fitxer `data/experiencies_rutes.json` i afegeix l'entrada a la llista:
   ```json
   {
     "ruta_slug": "ses-fonts-ufanes-campanet",
     "agrupament": "AEG Soca-Arrel",
     "unitat": "Ferrerets",
     "puntuacio": 5,
     "data": "Març 2026",
     "comentari": "Camí pla, molt accessible per als més petits. Hi ha aigua corrent quan brollen les fonts."
   }
   ```

4. **Regenerar i publicar:**
   Executa al terminal:
   ```bash
   python scripts/build_wiki_pages.py
   mkdocs build
   firebase deploy --only hosting
   ```
   La nova experiència quedarà compilada i visible públicament a la fitxa de la ruta per sempre.

---

## 📋 Generador ràpid de bloc JSON

Enganxa les dades del correu aquí si vols generar ràpidament el fragment de codi per afegir a `data/experiencies_rutes.json`:

<div style="background-color: var(--md-code-bg-color, #f8f9fa); border: 1px solid #ccc; border-radius: 8px; padding: 16px; margin: 16px 0;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; margin-bottom: 10px;">
        <input type="text" id="tool-slug" placeholder="Slug de la ruta (ex: ses-fonts-ufanes-campanet)" style="padding: 8px; border-radius: 6px; border: 1px solid #ccc;" />
        <input type="text" id="tool-agr" placeholder="Agrupament (ex: AEG Soca-Arrel)" style="padding: 8px; border-radius: 6px; border: 1px solid #ccc;" />
        <input type="text" id="tool-uni" placeholder="Unitat (ex: Ferrerets, Llops/Daines)" style="padding: 8px; border-radius: 6px; border: 1px solid #ccc;" />
        <input type="number" id="tool-pts" min="1" max="5" value="5" placeholder="Puntuació (1-5)" style="padding: 8px; border-radius: 6px; border: 1px solid #ccc;" />
        <input type="text" id="tool-data" placeholder="Data (ex: Març 2026)" style="padding: 8px; border-radius: 6px; border: 1px solid #ccc;" />
    </div>
    <textarea id="tool-com" rows="2" placeholder="Comentari rebut per correu..." style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc; box-sizing: border-box;"></textarea>
    <div style="margin-top: 10px; display: flex; gap: 10px;">
        <button onclick="generarBlocJson()" style="padding: 8px 16px; background-color: #00897b; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: bold;">Generar JSON</button>
        <button onclick="copiarJson()" style="padding: 8px 16px; background-color: #555; color: white; border: none; border-radius: 6px; cursor: pointer;">Copiar</button>
    </div>
    <pre id="tool-result" style="margin-top: 10px; background: #263238; color: #aeea00; padding: 12px; border-radius: 6px; display: none;"></pre>
</div>

<script>
function generarBlocJson() {
    const slug = document.getElementById('tool-slug').value.trim();
    const agr = document.getElementById('tool-agr').value.trim();
    const uni = document.getElementById('tool-uni').value.trim();
    const pts = parseInt(document.getElementById('tool-pts').value, 10) || 5;
    const dt = document.getElementById('tool-data').value.trim();
    const com = document.getElementById('tool-com').value.trim();

    const obj = {
        ruta_slug: slug,
        agrupament: agr,
        unitat: uni,
        puntuacio: pts,
        data: dt,
        comentari: com
    };

    const res = JSON.stringify(obj, null, 2);
    const el = document.getElementById('tool-result');
    el.style.display = 'block';
    el.innerText = ',\n' + res;
}

function copiarJson() {
    const el = document.getElementById('tool-result');
    if (el && el.innerText) {
        navigator.clipboard.writeText(el.innerText);
        alert('Copiat al porta-retalls!');
    }
}
</script>
