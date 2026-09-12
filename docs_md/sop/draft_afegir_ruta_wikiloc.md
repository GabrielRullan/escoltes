# 💚 SOP: Procés per Afegir Rutes de Wikiloc al Repositori Escolta

Aquest Procediment Operatiu Estàndard (SOP) formalitza el protocol per afegir qualsevol ruta o itinerari de **Wikiloc** al repositori central i a la Wiki de GitHub Pages de l'Agrupament.

---

## 📌 Com Compartir una Ruta de Wikiloc amb l'Agent d'IA

Quan qualsevol cap o membre de l'equip de suport vulgui afegir una nova ruta de Wikiloc al repositori, simplement ha de:

1. **Enganxar l'enllaç de Wikiloc al xat amb l'Agent d'IA**, per exemple:
   > *"Afegeix aquesta ruta de Wikiloc al repositori: https://es.wikiloc.com/rutas-senderismo/torrent-de-pareis-escorca-sa-calobra-2194812"*

2. **L'Agent d'IA executarà automàticament l'script d'ingestió**:
   ```bash
   python scripts/add_wikiloc_route.py "https://es.wikiloc.com/rutas-senderismo/..."
   ```

3. **Acció automàtica de l'script**:
   - Escrapeja el títol, descripció, distància, desnivell, dificultat, mapa i coordenades de Wikiloc.
   - Assigna intel·ligentment les unitats escoltes recomanades segons el desnivell i distància.
   - Actualitza la base de dades [`data/rutes_mallorca.json`](file:///c:/Users/gabri/Documents/scouts/data/rutes_mallorca.json).
   - Reconstrueix les pàgines de la Wiki amb [`scripts/build_wiki_pages.py`](file:///c:/Users/gabri/Documents/scouts/scripts/build_wiki_pages.py).
   - Publica automàticament la nova ruta a GitHub Pages.

---

## 🛠️ Execució Manual (Per a Desenvolupadors / Administradors)

Si preferiu afegir la ruta directament des de la consola de comandes:

```bash
python scripts/add_wikiloc_route.py "<URL_DE_WIKILOC>"
```

### Exemple:
```bash
python scripts/add_wikiloc_route.py "https://es.wikiloc.com/rutas-senderismo/es-salt-des-freu-orient-4291823"
```

---

## 📋 Estructura de Dades Generada

L'script converteix la ruta de Wikiloc al format estàndard del repositori:

```json
{
  "slug": "es-salt-des-freu-orient",
  "nom": "Es Salt des Freu (Orient / Bunyola)",
  "municipi": "Bunyola",
  "zona": "Tramuntana Central",
  "distancia_km": 4.5,
  "desnivell_positiu_m": 120,
  "dificultat": "Molt Fàcil",
  "durada_estimada": "1h 45min",
  "apte_unitats": ["Castors/Fures", "Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"],
  "wikiloc_url": "https://es.wikiloc.com/rutas-senderismo/es-salt-des-freu-orient-4291823",
  "lat": 39.7210,
  "lon": 2.7680
}
```
