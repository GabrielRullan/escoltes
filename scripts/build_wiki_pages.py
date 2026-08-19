import os
import json
import math
import urllib.parse

def haversine_km(lat1, lon1, lat2, lon2):
    """Calcula la distància en quilòmetres entre dues coordenades (fórmula de Haversine)."""
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def load_json(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def get_leaflet_track_map_html(route):
    """Genera un mapa interactiu Leaflet amb el track d'itinerari exacte (Polyline) i punts de pas."""
    track_coords = route.get("track_coordinates", [])
    lat, lon = route.get("lat", 39.65), route.get("lon", 2.90)
    map_id = f"map-route-{route['slug']}"
    
    if not track_coords:
        track_coords = [[lat, lon]]

    coords_json = json.dumps(track_coords)
    itinerari = route.get("itinerari_passos", [])
    itinerari_json = json.dumps(itinerari, ensure_ascii=False)

    return f"""
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="{map_id}" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_{route['slug'].replace('-', '_')}() {{
    if (typeof L === 'undefined') {{
        setTimeout(initRouteTrackMap_{route['slug'].replace('-', '_')}, 200);
        return;
    }}
    
    const trackPoints = {coords_json};
    const itinerariPassos = {itinerari_json};
    
    const rMap = L.map('{map_id}');
    L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }}).addTo(rMap);
    
    if (trackPoints.length > 1) {{
        const polyline = L.polyline(trackPoints, {{
            color: '#00897b',
            weight: 5,
            opacity: 0.85,
            lineJoin: 'round'
        }}).addTo(rMap);
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> {route['nom']}");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> {route['nom']}");
        
        rMap.fitBounds(polyline.getBounds(), {{ padding: [30, 30] }});
    }} else {{
        rMap.setView([{lat}, {lon}], 14);
        L.marker([{lat}, {lon}]).addTo(rMap).bindPopup("<b>{route['nom']}</b>");
    }}
}}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_{route['slug'].replace('-', '_')});
setTimeout(initRouteTrackMap_{route['slug'].replace('-', '_')}, 400);
</script>
"""

def get_osm_widget_html(lat, lon, zoom_delta=0.015):
    lat_min = lat - (zoom_delta * 0.7)
    lat_max = lat + (zoom_delta * 0.7)
    lon_min = lon - zoom_delta
    lon_max = lon + zoom_delta
    return f"""<iframe width="100%" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox={lon_min}%2C{lat_min}%2C{lon_max}%2C{lat_max}&amp;layer=mapnik&amp;marker={lat}%2C{lon}" style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"></iframe>
<p style="margin-top: 4px; margin-bottom: 16px;"><small><a href="https://www.openstreetmap.org/?mlat={lat}&amp;mlon={lon}#map=15/{lat}/{lon}" target="_blank">🗺️ Obrir mapa complet a OpenStreetMap</a></small></p>"""

def find_tib_lines_for_route(route, transport_data):
    """Assigna intel·ligentment les línies de bus TIB o tren SFM més properes a la ruta."""
    lines = []
    r_mun = route.get("municipi", "").lower()
    r_zon = route.get("zona", "").lower()

    # 1. Comprovar línies de bus
    for bus in transport_data.get("linies_bus", []):
        coberts = [m.lower() for m in bus.get("municipis_coberts", [])]
        if any(m in r_mun for m in coberts) or any(m in r_zon for m in coberts):
            lines.append(bus)

    # 2. Comprovar trens SFM i Sóller
    for train in transport_data.get("linies_tren", []):
        coberts = [m.lower() for m in train.get("municipis_coberts", [])]
        if any(m in r_mun for m in coberts):
            lines.append({
                "codi": train["codi"],
                "nom": train["nom"],
                "parades_clau": train["estacions_clau"],
                "link_horaris": train["link_horaris"]
            })

    if not lines:
        lines.append({
            "codi": "TIB / SFM Xarxa General",
            "nom": f"Línia d'autobús o tren comarcal ({route.get('municipi', 'Mallorca')})",
            "parades_clau": [route.get('municipi', 'Mallorca')],
            "link_horaris": "https://www.tib.org/"
        })

    return lines

# --- GENERACIÓ DE PÀGINES INDIVIDUALS PER RUTA ---
def build_individual_route_pages(rutes, refugis, agrupaments, transport_data):
    os.makedirs("docs/mallorca/rutes", exist_ok=True)
    
    for rut in rutes:
        r_lat, r_lon = rut["lat"], rut["lon"]
        track_map = get_leaflet_track_map_html(rut)
        tib_lines = find_tib_lines_for_route(rut, transport_data)
        
        refugis_directes = []
        refugis_propers_transport = []
        for ref in refugis:
            dist = haversine_km(r_lat, r_lon, ref["lat"], ref["lon"])
            if dist <= 2.0:
                refugis_directes.append((dist, ref))
            elif dist <= 10.0:
                refugis_propers_transport.append((dist, ref))
                
        refugis_directes.sort(key=lambda x: x[0])
        refugis_propers_transport.sort(key=lambda x: x[0])
        
        agrupaments_amb_dist = []
        for agr in agrupaments:
            dist = haversine_km(r_lat, r_lon, agr["lat"], agr["lon"])
            agrupaments_amb_dist.append((dist, agr))
        agrupaments_amb_dist.sort(key=lambda x: x[0])
        
        unitats_str = ", ".join(rut["apte_unitats"])
        aigua_str = ", ".join(rut["punts_aigua"])
        interes_str = ", ".join(rut["punts_interes"])
        passos_str = ", ".join(rut["passos_finca_privada"])
        
        wikiloc_url = rut.get("wikiloc_url")
        if wikiloc_url:
            wikiloc_str = f"[💚 Obrir Track Oficial a Wikiloc 🔗]({wikiloc_url})"
        else:
            search_query = urllib.parse.quote(rut['nom'])
            wikiloc_str = f"[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q={search_query})"

        turismepetit_url = rut.get("turismepetit_url")
        turismepetit_row = f"| **Guia Turisme Petit** | **[👶 Veure Guia de Família a Turisme Petit 🔗]({turismepetit_url})** |\n" if turismepetit_url else ""

        md = f"""# 🏔️ {rut['nom']}

{rut['descripcio']}

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)

{track_map}

---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **{rut.get('municipi', 'Mallorca')}** |
| **Zona / Comarca** | **{rut.get('zona', 'Serra de Tramuntana')}** |
| **Distància Total** | **{rut['distancia_km']} km** |
| **Desnivell Positiu** | **+{rut['desnivell_positiu_m']} m** |
| **Dificultat Tècnica** | **{rut['dificultat']}** |
| **Durada Estimada** | **{rut['durada_estimada']}** |
| **Unitats Recomanades** | **{unitats_str}** |
| **Track a Wikiloc** | **{wikiloc_str}** |
{turismepetit_row}
---

"""
        itinerari_passos = rut.get("itinerari_passos", [])
        if itinerari_passos:
            md += """## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
"""
            for item in itinerari_passos:
                md += f"| **Pas {item['pas']}** | **{item['nom']}** | {item['desc']} |\n"
            md += "\n---\n\n"

        md += f"""## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **{rut.get('municipi', 'Mallorca')}**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
"""
        for b in tib_lines:
            parades = ", ".join(b["parades_clau"][:4])
            md += f"| **{b['codi']}** ({b['nom']}) | {parades} | [Consultar Horaris Oficials 🔗]({b['link_horaris']}) |\n"

        md += f"""

---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** {aigua_str}
- **Passos per Finques Privades:** {passos_str}
- **Punts d'Interès Cultural i Natural:** {interes_str}

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> {rut['consells_seguretat']}

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
"""
        if refugis_directes:
            md += """| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
"""
            for dist, ref in refugis_directes:
                md += f"| **{ref['nom']}** | {ref['titularitat']} | {ref['capacitat']} pers. | **{dist:.2f} km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/{ref['slug']}.md) |\n"
        else:
            md += """
> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

"""

        if refugis_propers_transport:
            md += """### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
"""
            for dist, ref in refugis_propers_transport[:3]:
                md += f"| **{ref['nom']}** | **{dist:.1f} km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/{ref['slug']}.md) |\n"

        md += """
### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
"""
        for dist, agr in agrupaments_amb_dist[:2]:
            md += f"| **{agr['nom']}** | {agr['municipi']} | **{dist:.1f} km** | [Veure Casal](../agrupaments/{agr['slug']}.md) |\n"

        file_path = f"docs/mallorca/rutes/{rut['slug']}.md"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md)

# --- GENERACIÓ DE PÀGINES INDIVIDUALS PER REFUGI / ACAMPADA ---
def build_individual_acampada_pages(refugis, rutes, agrupaments, transport_data):
    os.makedirs("docs/mallorca/acampada", exist_ok=True)
    
    for ref in refugis:
        c_lat, c_lon = ref["lat"], ref["lon"]
        osm_widget = get_osm_widget_html(c_lat, c_lon, zoom_delta=0.015)
        
        rutes_directes = []
        rutes_amb_transport = []
        for rut in rutes:
            dist = haversine_km(c_lat, c_lon, rut["lat"], rut["lon"])
            if dist <= 2.0:
                rutes_directes.append((dist, rut))
            elif dist <= 12.0:
                rutes_amb_transport.append((dist, rut))
                
        rutes_directes.sort(key=lambda x: x[0])
        rutes_amb_transport.sort(key=lambda x: x[0])
        
        agrupaments_amb_dist = []
        for agr in agrupaments:
            dist = haversine_km(c_lat, c_lon, agr["lat"], agr["lon"])
            agrupaments_amb_dist.append((dist, agr))
        agrupaments_amb_dist.sort(key=lambda x: x[0])
        
        serveis_str = ", ".join(ref["serveis"])
        
        md = f"""# ⛺ {ref['nom']}

{ref['descripcio']}

---

## 🗺️ Mapa Interactiu (OpenStreetMap)

{osm_widget}

---

## 📋 Informació i Serveis de la instal·lació

| Característica | Detall |
| :--- | :--- |
| **Titularitat** | **{ref['titularitat']}** |
| **Municipi** | **{ref['municipi']}** |
| **Capacitat Màxima** | **{ref['capacitat']} persones** |
| **Antelació Permís** | **{ref['permis_antelacio']}** |
| **Contacte / Reserves** | **{ref['contacte']}** |
| **Accés d'Emergència** | **{ref['acces_emergencia']}** |

---

## 🛠️ Infraestructura disponible
- **Serveis:** {serveis_str}
- **Normativa de Foc:** {ref['restriccio_foc']}

> [!IMPORTANT]
> Recordeu que entre l'1 de maig i el 15 d'octubre està **prohibit qualsevol tipus de foc** a l'aire lliure a totes les zones boscoses de Mallorca.

---

## 📍 Relació Realista de Rutes i Excursions

### 🥾 Rutes directament accessibles a peu des del refugi (<= 2.0 km)
"""
        if rutes_directes:
            md += """| Ruta | Distància Ruta | Dificultat | Distància al Refugi | Enllaç |
| :--- | :---: | :---: | :---: | :--- |
"""
            for dist, rut in rutes_directes:
                md += f"| **{rut['nom']}** | {rut['distancia_km']} km | {rut['dificultat']} | **{dist:.2f} km** (🟢 A peu) | [Veure Ruta](../rutes/{rut['slug']}.md) |\n"
        else:
            md += """
> [!NOTE]
> **Sense inici directe a peu**: No hi ha rutes catalogades que comencin o passin a menys de 2.0 km d'aquest terreny. Per fer les excursions principals cal utilitzar transport.

"""

        if rutes_amb_transport:
            md += """### 🚌 Excursions a la zona que requereixen transport (> 2.0 km)
| Ruta | Distància Ruta | Dificultat | Distància des del refugi | Enllaç |
| :--- | :---: | :---: | :---: | :--- |
"""
            for dist, rut in rutes_amb_transport[:3]:
                md += f"| **{rut['nom']}** | {rut['distancia_km']} km | {rut['dificultat']} | **{dist:.1f} km** | [Veure Ruta](../rutes/{rut['slug']}.md) |\n"

        md += """
### ⚜️ Agrupaments Escoltes Més Propers
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
"""
        for dist, agr in agrupaments_amb_dist[:2]:
            md += f"| **{agr['nom']}** | {agr['municipi']} | **{dist:.1f} km** | [Veure Casal](../agrupaments/{agr['slug']}.md) |\n"

        file_path = f"docs/mallorca/acampada/{ref['slug']}.md"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md)

# --- GENERACIÓ DE PÀGINES INDIVIDUALS PER AGRUPAMENT / CASAL ---
def build_individual_agrupament_pages(agrupaments, refugis, rutes, transport_data):
    os.makedirs("docs/mallorca/agrupaments", exist_ok=True)
    
    for agr in agrupaments:
        a_lat, a_lon = agr["lat"], agr["lon"]
        osm_widget = get_osm_widget_html(a_lat, a_lon, zoom_delta=0.012)
        
        refugis_directes = []
        refugis_transport = []
        for ref in refugis:
            dist = haversine_km(a_lat, a_lon, ref["lat"], ref["lon"])
            if dist <= 2.0:
                refugis_directes.append((dist, ref))
            else:
                refugis_transport.append((dist, ref))
                
        refugis_directes.sort(key=lambda x: x[0])
        refugis_transport.sort(key=lambda x: x[0])
        
        rutes_directes = []
        rutes_transport = []
        for rut in rutes:
            dist = haversine_km(a_lat, a_lon, rut["lat"], rut["lon"])
            if dist <= 2.0:
                rutes_directes.append((dist, rut))
            else:
                rutes_transport.append((dist, rut))
                
        rutes_directes.sort(key=lambda x: x[0])
        rutes_transport.sort(key=lambda x: x[0])
        
        md = f"""# ⚜️ {agr['nom']}

{agr['descripcio']}

---

## 🗺️ Ubicació del Casal (OpenStreetMap)

{osm_widget}

---

## 🏛️ Fitxa de l'Agrupament / Casal

| Camp | Informació |
| :--- | :--- |
| **Associació** | **{agr['associacio']}** |
| **Municipi / Zona** | **{agr['municipi']} ({agr['zona']})** |
| **Ubicació / Parròquia** | **{agr['ubicacio_detall']}** |
| **Correu electrònic** | `{agr['email']}` |
| **Lloc Web Oficial** | [{agr['web']}]({agr['web']}) |

---

## 📍 Anàlisi de Mobilitat des del Casal

### 🥾 Rutes accessibles a peu des del Casal (<= 2.0 km)
"""
        if rutes_directes:
            md += """| Ruta | Dificultat | Distància des del casal | Enllaç |
| :--- | :---: | :---: | :--- |
"""
            for dist, rut in rutes_directes:
                md += f"| **{rut['nom']}** | {rut['dificultat']} | **{dist:.2f} km** (🟢 A peu) | [Veure Ruta](../rutes/{rut['slug']}.md) |\n"
        else:
            md += """
> [!NOTE]
> Les excursions principals de la Serra de Tramuntana requereixen transport col·lectiu des d'aquest casal (> 2.0 km).

"""

        md += """### 🚌 Rutes principals de la Serra de Tramuntana (Amb Transport)
| Ruta | Dificultat | Distància des del casal | Enllaç |
| :--- | :---: | :---: | :--- |
"""
        for dist, rut in rutes_transport[:3]:
            md += f"| **{rut['nom']}** | {rut['dificultat']} | **{dist:.1f} km** | [Veure Ruta](../rutes/{rut['slug']}.md) |\n"

        md += """
### ⛺ Zones d'Acampada i Refugis més propers al Casal
"""
        if refugis_directes:
            md += """| Terreny / Refugi | Capacitat | Distància des del casal | Enllaç |
| :--- | :---: | :---: | :--- |
"""
            for dist, ref in refugis_directes:
                md += f"| **{ref['nom']}** | {ref['capacitat']} pers. | **{dist:.2f} km** (🟢 A peu) | [Veure Refugi](../acampada/{ref['slug']}.md) |\n"
        else:
            md += """| Terreny / Refugi | Capacitat | Distància des del casal | Enllaç |
| :--- | :---: | :---: | :--- |
"""
            for dist, ref in refugis_transport[:3]:
                md += f"| **{ref['nom']}** | {ref['capacitat']} pers. | **{dist:.1f} km** | [Veure Refugi](../acampada/{ref['slug']}.md) |\n"

        file_path = f"docs/mallorca/agrupaments/{agr['slug']}.md"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md)

# --- PÀGINA D'OVERVIEW DE TRANSPORT PÚBLIC I TRENS ---
def build_transport_overview_page(transport_data):
    md = """# 🚌 i 🚆 Guia Completa de Mobilitat i Transport Públic (TIB / SFM / Tren de Sóller)

Per tal de reduir l'impacte ambiental, fomentar l'autonomia dels escoltes i facilitar la logística de les excursions lineals, Mallorca disposa d'una xarxa integrada d'**Autobusos TIB**, **Trens de Mallorca (SFM)**, **Metro de Palma** i el **Ferrocarril de Sóller**.

---

## 🚆 1. Xarxa Ferroviària de Mallorca (Serveis Ferroviaris de Mallorca - SFM & Sóller)

| Línia | Operador | Trajecte i Estacions Principals | Connexió Escolta i Rutes | Horaris Oficials |
| :--- | :--- | :--- | :--- | :--- |
"""
    for train in transport_data.get("linies_tren", []):
        estacions = ", ".join(train["estacions_clau"][:5])
        md += f"| **{train['codi']}** | {train.get('operator', 'SFM')} | {train['nom']} ({estacions}...) | Connexió directa amb Marratxí, Santa Maria, Binissalem, Inca, Sa Pobla, Manacor i Sóller | [Horaris Tren 🔗]({train['link_horaris']}) |\n"

    md += """
---

## 🚍 2. Xarxa d'Autobusos TIB per Corredors

| Línia | Trajecte i Parades Clau | Corredor | Enllaç Horaris TIB |
| :--- | :--- | :--- | :--- |
"""
    for bus in transport_data.get("linies_bus", []):
        parades = ", ".join(bus["parades_clau"])
        md += f"| **{bus['codi']}** | {bus['nom']} ({parades}) | {bus['corredor']} | [Horaris i Targeta TIB 🔗]({bus['link_horaris']}) |\n"

    md += """
---

## 💡 Recomanacions Logístiques per a Grups Escoltes

> [!TIP]
> 1. **Gratuïtat per a Escoltes Menors de 16 Anys**: Els escoltes balears menors de 16 anys viatgen **100% de franc** a tots els trens de l'SFM, Metro i autobusos del TIB amb la Targeta Intermodal.
> 2. **Notificació de Grups (>20 persones)**: Per viatjar en tren o bus amb més de 20 escoltes, s'ha d'enviar un correu a `[email protected]` amb **48h d'antelació** per reservar cotxe de reforç o vagó específic.
> 3. **Línia 341 (Alta Muntanya Ma-10)**: La línia TIB 341 recorrer tota la carretera de la serra Ma-10 connectant Pollença, Lluc, Cúber, Gorg Blau, sa Calobra i Sóller, ideal per a travesses del GR-221.
"""
    with open("docs/mallorca/transport.md", "w", encoding="utf-8") as f:
        f.write(md)

# --- PÀGINES D'OVERVIEW (INDEX) ---
def build_agrupaments_overview(agrupaments):
    md = """# Agrupaments Escoltes i Guies a Mallorca

Directori general dels **Agrupaments Escoltes i Guies (AEG)** de Mallorca. Feu clic sobre qualsevol agrupament per veure la seva **fitxa individual**, mapa interactiu OpenStreetMap, llocs d'acampada propers i anàlisi de mobilitat des del casal.

---

## 🏡 Agrupaments de Part Forana (Pobles)

| Agrupament | Municipi | Ubicació | Fitxa Individual |
| :--- | :--- | :--- | :--- |
"""
    pobles = [g for g in agrupaments if g.get("zona") == "Poble"]
    for g in pobles:
        md += f"| **{g['nom']}** | {g['municipi']} | {g['ubicacio_detall']} | [Fitxa del Casal i Mapa 🔗](agrupaments/{g['slug']}.md) |\n"

    md += """
---

## 🏙️ Agrupaments de Palma de Mallorca

| Agrupament | Municipi | Ubicació | Fitxa Individual |
| :--- | :--- | :--- | :--- |
"""
    barris = [g for g in agrupaments if g.get("zona") == "Barri"]
    for g in barris:
        md += f"| **{g['nom']}** | {g['municipi']} | {g['ubicacio_detall']} | [Fitxa del Casal i Mapa 🔗](agrupaments/{g['slug']}.md) |\n"

    with open("docs/mallorca/agrupaments.md", "w", encoding="utf-8") as f:
        f.write(md)

def build_acampada_overview(refugis):
    md = """# Zones d'Acampada, Àrees Recreatives i Refugis a Mallorca

Directori centralitzat d'infraestructures per a l'acampada i l'aixopluc escolta. Prem sobre el nom de qualsevol refugi per obrir la seva **fitxa detallada, mapa OpenStreetMap i rutes accessibles a peu (<= 2.0 km)**.

> [!WARNING]
> Recordeu que entre l'**1 de maig i el 15 d'octubre** està totalment prohibit fer foc a l'aire lliure (IBANAT).

---

## ⛺ Llista de Refugis i Terrenys

| Nom del Refugi / Terreny | Titularitat | Municipi | Capacitat | Fitxa Completa i Mapa |
| :--- | :--- | :--- | :---: | :--- |
"""
    for r in refugis:
        md += f"| **{r['nom']}** | {r['titularitat']} | {r['municipi']} | **{r['capacitat']} pers.** | [Veure Fitxa i Mapa 🔗](acampada/{r['slug']}.md) |\n"

    with open("docs/mallorca/acampada_i_refugis.md", "w", encoding="utf-8") as f:
        f.write(md)

def build_rutes_overview(rutes):
    rutes_json_str = json.dumps(rutes, ensure_ascii=False)
    
    municipis = sorted(list(set([r.get('municipi', 'Mallorca').split('/')[0].strip() for r in rutes])))
    zones = sorted(list(set([r.get('zona', 'Serra de Tramuntana') for r in rutes])))
    dificultats = ["Molt Fàcil", "Fàcil", "Fàcil - Moderada", "Moderada", "Moderada - Exigent", "Exigent", "Molt Exigent / Tècnica"]
    branques = ["Castors/Fures", "Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"]

    municipi_options = "".join([f'<option value="{m}">{m}</option>' for m in municipis])
    zona_options = "".join([f'<option value="{z}">{z}</option>' for z in zones])
    dificultat_options = "".join([f'<option value="{d}">{d}</option>' for d in dificultats])
    branca_options = "".join([f'<option value="{b}">{b}</option>' for b in branques])

    md = f"""# 🥾 Cercador i Índex de Rutes de Senderisme a Mallorca

Benvinguts al cercador interactiu de la base de dades d'excursions. Podeu filtrar les **{len(rutes)} rutes catalogades** per **Municipi**, **Zona**, **Dificultat** o **Branca Escolta**, i veure la posició exacte dels inicis de ruta al mapa interactiu.

---

## 🗺️ Mapa d'Inicis de Ruta (OpenStreetMap / Leaflet)

<!-- Leaflet CSS i JS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-container" style="width: 100%; height: 420px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.15); margin-bottom: 24px;"></div>

---

## 🔍 Cercador i Filtres d'Excursions

<div style="background-color: var(--md-code-bg-color, #f8f9fa); padding: 18px; border-radius: 10px; border: 1px solid #e0e0e0; margin-bottom: 24px;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 12px;">
        <div>
            <label style="font-weight: bold; font-size: 0.85em;">📍 Municipi / Poble:</label>
            <select id="filter-municipi" onchange="applyRouteFilters()" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc;">
                <option value="">Tots els municipis</option>
                {municipi_options}
            </select>
        </div>
        <div>
            <label style="font-weight: bold; font-size: 0.85em;">⛰️ Zona / Comarca:</label>
            <select id="filter-zona" onchange="applyRouteFilters()" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc;">
                <option value="">Totes les zones</option>
                {zona_options}
            </select>
        </div>
        <div>
            <label style="font-weight: bold; font-size: 0.85em;">🎯 Dificultat:</label>
            <select id="filter-dificultat" onchange="applyRouteFilters()" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc;">
                <option value="">Totes les dificultats</option>
                {dificultat_options}
            </select>
        </div>
        <div>
            <label style="font-weight: bold; font-size: 0.85em;">⚜️ Branca Escolta:</label>
            <select id="filter-branca" onchange="applyRouteFilters()" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc;">
                <option value="">Totes les branques</option>
                {branca_options}
            </select>
        </div>
        <div>
            <label style="font-weight: bold; font-size: 0.85em;">🔗 Recurs / Enllaç / Seguretat:</label>
            <select id="filter-plataforma" onchange="applyRouteFilters()" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc; background-color: #f0f7f4; font-weight: bold;">
                <option value="">Tots els recursos</option>
                <option value="aigua">💧 Amb Font / Punt d'Aigua</option>
                <option value="privat">⚠️ Passos per Finca Privada</option>
                <option value="wikiloc">💚 Amb Track de Wikiloc</option>
                <option value="turismepetit">👶 Amb Guia Turisme Petit</option>
                <option value="both">🌟 Amb Wikiloc i Turisme Petit</option>
            </select>
        </div>
    </div>
    <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
        <input type="text" id="filter-search" oninput="applyRouteFilters()" placeholder="🔎 Cercar per nom, paratge o paraula clau..." style="flex: 1; min-width: 220px; padding: 8px 12px; border-radius: 6px; border: 1px solid #ccc;" />
        <button onclick="quickFilter('aigua')" style="padding: 8px 14px; background-color: #0288d1; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 0.85em; font-weight: bold;">💧 Amb Font</button>
        <button onclick="quickFilter('wikiloc')" style="padding: 8px 14px; background-color: #2e7d32; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 0.85em; font-weight: bold;">💚 Només Wikiloc</button>
        <button onclick="quickFilter('turismepetit')" style="padding: 8px 14px; background-color: #e65100; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 0.85em; font-weight: bold;">👶 Només Turisme Petit</button>
        <button onclick="resetFilters()" style="padding: 8px 16px; background-color: #00897b; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: bold;">Netejar Filtres</button>
    </div>
    <div id="filter-counter" style="margin-top: 10px; font-weight: bold; color: #00897b;">
        Mostrant {len(rutes)} de {len(rutes)} rutes catalogades.
    </div>
</div>

---

## 🥾 Llistat de Rutes Filtrades

<div id="routes-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 16px;">
</div>

<script>
const allRoutes = {rutes_json_str};
let map, markersGroup;

function initLeafletMap() {{
    if (typeof L === 'undefined') {{
        setTimeout(initLeafletMap, 200);
        return;
    }}
    
    map = L.map('map-container').setView([39.65, 2.90], 9);
    L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }}).addTo(map);
    
    markersGroup = L.layerGroup().addTo(map);
    applyRouteFilters();
}}

function getBadgeColor(dif) {{
    if (dif.includes('Molt Fàcil')) return '#2e7d32';
    if (dif.includes('Fàcil')) return '#43a047';
    if (dif.includes('Moderada')) return '#f57c00';
    if (dif.includes('Exigent')) return '#d32f2f';
    return '#7b1fa2';
}}

function renderRoutes(routesToRender) {{
    const grid = document.getElementById('routes-grid');
    grid.innerHTML = '';
    
    if (markersGroup) {{
        markersGroup.clearLayers();
    }}
    
    routesToRender.forEach(r => {{
        const card = document.createElement('div');
        card.style.cssText = 'border: 1px solid #e0e0e0; border-radius: 8px; padding: 14px; background: var(--md-code-bg-color, #fff); box-shadow: 0 2px 5px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: space-between;';
        
        const badgeColor = getBadgeColor(r.dificultat);
        const unitatsStr = r.apte_unitats ? r.apte_unitats.join(', ') : '';
        
        const wikilocUrl = r.wikiloc_url ? r.wikiloc_url : `https://www.wikiloc.com/wikiloc/map.do?q=${{encodeURIComponent(r.nom)}}`;

        const tpBtn = r.turismepetit_url ? `<a href="${{r.turismepetit_url}}" target="_blank" style="display: inline-block; padding: 6px 12px; background-color: #e65100; color: white; text-decoration: none; border-radius: 4px; font-size: 0.85em; font-weight: bold;">👶 Turisme Petit 🔗</a>` : '';

        card.innerHTML = `
            <div>
                <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 8px;">
                    <h3 style="margin: 0 0 6px 0; font-size: 1.05em;"><a href="../rutes/${{r.slug}}/" style="color: var(--md-typeset-a-color, #00897b); text-decoration: none;">${{r.nom}}</a></h3>
                    <span style="background-color: ${{badgeColor}}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.75em; font-weight: bold; whitespace: nowrap;">${{r.dificultat}}</span>
                </div>
                <p style="font-size: 0.85em; color: #666; margin: 4px 0 8px 0;">📍 <b>${{r.municipi || 'Mallorca'}}</b> (${{r.zona || 'Tramuntana'}})</p>
                <p style="font-size: 0.85em; margin: 4px 0;">📏 <b>${{r.distancia_km}} km</b> | 📈 <b>+${{r.desnivell_positiu_m}}m</b> | ⏱️ <b>${{r.durada_estimada}}</b></p>
                <p style="font-size: 0.8em; color: #555; margin: 4px 0;">⚜️ <i>${{unitatsStr}}</i></p>
            </div>
            <div style="margin-top: 12px; display: flex; justify-content: flex-end; gap: 8px; flex-wrap: wrap;">
                ${{tpBtn}}
                <a href="${{wikilocUrl}}" target="_blank" style="display: inline-block; padding: 6px 12px; background-color: #2e7d32; color: white; text-decoration: none; border-radius: 4px; font-size: 0.85em; font-weight: bold;">💚 Wikiloc 🔗</a>
                <a href="../rutes/${{r.slug}}/" style="display: inline-block; padding: 6px 12px; background-color: #00897b; color: white; text-decoration: none; border-radius: 4px; font-size: 0.85em; font-weight: bold;">Veure Fitxa i Mapa 🔗</a>
            </div>
        `;
        grid.appendChild(card);
        
        if (markersGroup && r.lat && r.lon) {{
            const marker = L.marker([r.lat, r.lon]);
            const popupContent = `
                <div style="min-width: 180px;">
                    <h4 style="margin: 0 0 4px 0;">${{r.nom}}</h4>
                    <p style="margin: 2px 0; font-size: 0.85em;">📍 <b>${{r.municipi || 'Mallorca'}}</b></p>
                    <p style="margin: 2px 0; font-size: 0.85em;">📏 <b>${{r.distancia_km}} km</b> (${{r.dificultat}})</p>
                    <a href="../rutes/${{r.slug}}/" style="display: inline-block; margin-top: 6px; color: #00897b; font-weight: bold;">Obrir Fitxa 🔗</a>
                </div>
            `;
            marker.bindPopup(popupContent);
            markersGroup.addLayer(marker);
        }}
    }});
    
    document.getElementById('filter-counter').innerText = `Mostrant ${{routesToRender.length}} de ${{allRoutes.length}} rutes catalogades.`;
}}

function applyRouteFilters() {{
    const mun = document.getElementById('filter-municipi').value.toLowerCase();
    const zon = document.getElementById('filter-zona').value.toLowerCase();
    const dif = document.getElementById('filter-dificultat').value.toLowerCase();
    const bra = document.getElementById('filter-branca').value.toLowerCase();
    const plat = document.getElementById('filter-plataforma').value;
    const txt = document.getElementById('filter-search').value.toLowerCase();
    
    const filtered = allRoutes.filter(r => {{
        const matchMun = !mun || (r.municipi && r.municipi.toLowerCase().includes(mun));
        const matchZon = !zon || (r.zona && r.zona.toLowerCase().includes(zon));
        const matchDif = !dif || (r.dificultat && r.dificultat.toLowerCase().includes(dif));
        const matchBra = !bra || (r.apte_unitats && r.apte_unitats.some(u => u.toLowerCase().includes(bra)));
        const matchTxt = !txt || (r.nom.toLowerCase().includes(txt) || (r.descripcio && r.descripcio.toLowerCase().includes(txt)) || (r.municipi && r.municipi.toLowerCase().includes(txt)));
        
        let matchPlat = true;
        if (plat === 'wikiloc') {{
            matchPlat = !!r.wikiloc_url;
        }} else if (plat === 'turismepetit') {{
            matchPlat = !!r.turismepetit_url;
        }} else if (plat === 'both') {{
            matchPlat = !!r.wikiloc_url && !!r.turismepetit_url;
        }} else if (plat === 'aigua') {{
            matchPlat = r.punts_aigua && r.punts_aigua.length > 0 && !r.punts_aigua.some(a => a.toLowerCase().includes('sense') || a.toLowerCase().includes('no hi ha'));
        }} else if (plat === 'privat') {{
            matchPlat = r.passos_finca_privada && r.passos_finca_privada.length > 0 && !r.passos_finca_privada.some(p => p.toLowerCase().includes('cap'));
        }}
        
        return matchMun && matchZon && matchDif && matchBra && matchTxt && matchPlat;
    }});
    
    renderRoutes(filtered);
}}

function quickFilter(platType) {{
    document.getElementById('filter-plataforma').value = platType;
    applyRouteFilters();
}}

function resetFilters() {{
    document.getElementById('filter-municipi').value = '';
    document.getElementById('filter-zona').value = '';
    document.getElementById('filter-dificultat').value = '';
    document.getElementById('filter-branca').value = '';
    document.getElementById('filter-plataforma').value = '';
    document.getElementById('filter-search').value = '';
    applyRouteFilters();
}}

document.addEventListener('DOMContentLoaded', initLeafletMap);
setTimeout(initLeafletMap, 500);
</script>
"""

    with open("docs/mallorca/rutes.md", "w", encoding="utf-8") as f:
        f.write(md)

def main():
    agrupaments = load_json("data/agrupaments_mallorca.json")
    refugis = load_json("data/acampada_mallorca.json")
    rutes = load_json("data/rutes_mallorca.json")
    transport_data = load_json("data/transport_mallorca.json")
    
    print("Incloent TOTS els trens de Mallorca (SFM T1, T2, T3, Metro M1/M2 i Sóller) a la guia i rutes...")
    build_individual_route_pages(rutes, refugis, agrupaments, transport_data)
    build_individual_acampada_pages(refugis, rutes, agrupaments, transport_data)
    build_individual_agrupament_pages(agrupaments, refugis, rutes, transport_data)
    
    build_agrupaments_overview(agrupaments)
    build_acampada_overview(refugis)
    build_rutes_overview(rutes)
    build_transport_overview_page(transport_data)
    print("Secció de Trens de Mallorca actualitzada amb èxit!")

if __name__ == "__main__":
    main()
