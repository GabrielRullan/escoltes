import os
import json
import re
import subprocess
import sys

DATA_PATH = os.path.join("data", "rutes_mallorca.json")

TURISMEPETIT_ROUTES = [
    {
        "slug": "betlem-a-playa-es-calo",
        "nom": "Excursió de Betlem a Platja des Caló (Artà)",
        "municipi": "Artà",
        "zona": "Llevant",
        "distancia_km": 7.0,
        "desnivell_positiu_m": 80,
        "dificultat": "Molt Fàcil",
        "durada_estimada": "2h 15min",
        "apte_unitats": ["Castors/Fures", "Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"],
        "punts_aigua": ["Llogaret de Betlem"],
        "passos_finca_privada": ["Sender públic del Parc Natural de Llevant"],
        "punts_interes": ["Platja verge des Caló", "Llogaret de Betlem", "Vistes a la Badia d'Alcúdia"],
        "consells_seguretat": "Ruta molt accessible amb ombres parcials. Ideal per a la branca de Castors i Llops.",
        "descripcio": "Plàcida passejada litoral per la costa nord d'Artà que connecta les darreres cases de Betlem amb la platja verge i refugi de pescadors des Caló.",
        "turismepetit_url": "https://www.turismepetit.com/excursion/excursion-de-betlem-a-playa-es-calo/",
        "lat": 39.7550,
        "lon": 3.3280,
        "track_coordinates": [
            [39.7550, 3.3280],
            [39.7610, 3.3410],
            [39.7690, 3.3550]
        ],
        "itinerari_passos": [
            {"pas": 1, "nom": "Inici a la urbanització de Betlem", "desc": "Fi de l'asfalt al carrer de la badia de Betlem."},
            {"pas": 2, "nom": "Camí de sa Cova des Pescadors", "desc": "Sendera plana que discorre entre la pineda i la mar."},
            {"pas": 3, "nom": "Arribada a es Caló", "desc": "Embarcador tradicional de fusta i platja verge."}
        ]
    },
    {
        "slug": "mirador-de-ses-basses-son-gual-valldemossa",
        "nom": "Mirador de ses Basses i Son Gual (Valldemossa)",
        "municipi": "Valldemossa",
        "zona": "Tramuntana Central",
        "distancia_km": 6.8,
        "desnivell_positiu_m": 290,
        "dificultat": "Fàcil",
        "durada_estimada": "2h 30min",
        "apte_unitats": ["Castors/Fures", "Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"],
        "punts_aigua": ["Vila de Valldemossa"],
        "passos_finca_privada": ["Miradors públics de sa Comuna de Valldemossa"],
        "punts_interes": ["Mirador de ses Basses", "Mirador de Son Gual", "Panoràmica de Valldemossa"],
        "consells_seguretat": "Bosc frondós d'alzinar. Atenció als nins a la vora del mirador penjat.",
        "descripcio": "Ruta panoràmica des de Valldemossa que ascendeix per l'alzinar fins als miradors naturals de ses Basses i Son Gual amb vistes directes a la Cartoixa.",
        "turismepetit_url": "https://www.turismepetit.com/excursion/excursion-al-mirador-de-ses-basses-y-mirador-de-son-gual/",
        "lat": 39.7120,
        "lon": 2.6230,
        "track_coordinates": [
            [39.7120, 2.6230],
            [39.7180, 2.6310],
            [39.7240, 2.6390]
        ],
        "itinerari_passos": [
            {"pas": 1, "nom": "Inici a Valldemossa", "desc": "Sortida des de la part alta del poble cap al bosc."},
            {"pas": 2, "nom": "Alzinar des Cairats", "desc": "Pujada amena a l'ombra de les alzines centenàries."},
            {"pas": 3, "nom": "Mirador de Son Gual", "desc": "Balcó natural amb vistes impressionants a tota la vall."}
        ]
    },
    {
        "slug": "estanyol-a-torre-estalella-llucmajor",
        "nom": "s'Estanyol a la Torre de s'Estalella (Llucmajor)",
        "municipi": "Llucmajor",
        "zona": "Migjorn",
        "distancia_km": 4.2,
        "desnivell_positiu_m": 20,
        "dificultat": "Molt Fàcil",
        "durada_estimada": "1h 30min",
        "apte_unitats": ["Castors/Fures", "Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"],
        "punts_aigua": ["Poble de s'Estanyol de Migjorn"],
        "passos_finca_privada": ["Camí de sa costa (públic)"],
        "punts_interes": ["Torre de guaita de s'Estalella (S. XVI)", "Nidos de metralladora", "Far de s'Estalella"],
        "consells_seguretat": "Ruta completament plana sense desnivell. Portar gorra i protecció solar.",
        "descripcio": "Agradable passejada costera ideal per als més petits que recorre el litoral verge de Llucmajor des del port de s'Estanyol fins a la històrica torre de guaita de s'Estalella.",
        "turismepetit_url": "https://www.turismepetit.com/excursion/excursion-desde-estanyol-a-torre-estalella/",
        "lat": 39.3620,
        "lon": 2.9150,
        "track_coordinates": [
            [39.3620, 2.9150],
            [39.3580, 2.9020],
            [39.3520, 2.8910]
        ],
        "itinerari_passos": [
            {"pas": 1, "nom": "Inici al Port de s'Estanyol", "desc": "Camí litoral que voreja les casetes de pescadors."},
            {"pas": 2, "nom": "Far i Jaciments costers", "desc": "Tram pla sobre pedra de marès."},
            {"pas": 3, "nom": "Torre de s'Estalella", "desc": "Arribada a la torre defensiva amb vistes a Cabrera."}
        ]
    },
    {
        "slug": "coves-blanques-pollenca",
        "nom": "Coves Blanques (Cala Sant Vicenç / Pollença)",
        "municipi": "Pollença",
        "zona": "Tramuntana Nord",
        "distancia_km": 5.4,
        "desnivell_positiu_m": 150,
        "dificultat": "Fàcil",
        "durada_estimada": "2h 00min",
        "apte_unitats": ["Castors/Fures", "Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"],
        "punts_aigua": ["Cala Sant Vicenç"],
        "passos_finca_privada": ["Camí dels presoners (històric públic)"],
        "punts_interes": ["Coves Blanques (túnels militars)", "Cala Molins", "Cavall Bernat"],
        "consells_seguretat": "Portar llanterna per explorar els túnels excavats a la roca amb precaució.",
        "descripcio": "Ruta històrica construïda durant la Segona Guerra Mundial per presoners que s'endinsa a les cavitats de les Coves Blanques sobre la mar de Cala Sant Vicenç.",
        "turismepetit_url": "https://www.turismepetit.com/excursion/excursion-a-las-coves-blanques-en-pollenca/",
        "lat": 39.9210,
        "lon": 3.0540,
        "track_coordinates": [
            [39.9210, 3.0540],
            [39.9280, 3.0610],
            [39.9340, 3.0680]
        ],
        "itinerari_passos": [
            {"pas": 1, "nom": "Cala Molins", "desc": "Inici a la Platja de Cala Molins a Cala Sant Vicenç."},
            {"pas": 2, "nom": "Camí dels Presoners", "desc": "Pujada ample en zig-zag amb pineda."},
            {"pas": 3, "nom": "Túnels de les Coves Blanques", "desc": "Galeries militars excavades a la roca."}
        ]
    },
    {
        "slug": "finca-publica-planicia-banyalbufar",
        "nom": "Finca Pública de Planícia (Banyalbufar)",
        "municipi": "Banyalbufar",
        "zona": "Tramuntana Sud",
        "distancia_km": 9.2,
        "desnivell_positiu_m": 320,
        "dificultat": "Moderada",
        "durada_estimada": "3h 15min",
        "apte_unitats": ["Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"],
        "punts_aigua": ["Font de Planícia", "Cases de Planícia"],
        "passos_finca_privada": ["Finca Pública de Planícia (Govern de les Illes Balears)"],
        "punts_interes": ["Cases de Planícia", "Alabern", "Font de sa Mentida", "Tafona tradicional"],
        "consells_seguretat": "Finca pública de gran extensió. Seguir els itineraris senyalitzats.",
        "descripcio": "Ruta semicircular per una de les possessions públiques més emblemàtiques de la serra de Tramuntana, entre alzinars centenaris, fonts i l'antiga tafona d'oli.",
        "turismepetit_url": "https://www.turismepetit.com/excursion/excursion-semicircular-por-la-finca-publica-de-planicia/",
        "lat": 39.6780,
        "lon": 2.4980,
        "track_coordinates": [
            [39.6780, 2.4980],
            [39.6850, 2.5080],
            [39.6920, 2.5160]
        ],
        "itinerari_passos": [
            {"pas": 1, "nom": "Entrada de la Ma-10", "desc": "Aparcament a l'accés de la Finca de Planícia."},
            {"pas": 2, "nom": "Cases de Planícia", "desc": "Arribada al nucli històric i tafona de la finca."},
            {"pas": 3, "nom": "Font de sa Mentida", "desc": "Retorn circular per l'alzinar alt."}
        ]
    }
]

# Mapa d'enllaços de Turisme Petit per a rutes existents al dataset
EXISTING_TURISMEPETIT_MAP = {
    "es-salt-des-freu-orient": "https://www.turismepetit.com/excursion/excursion-es-salt-des-freu/",
    "ses-fonts-ufanes-campanet": "https://www.turismepetit.com/excursion/ses-fonts-ufanes/",
    "puig-de-galatzo-font-des-pi": "https://www.turismepetit.com/excursion/excursion-a-la-finca-publica-de-galatzo/",
    "castell-d-alaro": "https://www.turismepetit.com/excursion/el-castell-dalaro/",
    "parc-natural-mondrago": "https://www.turismepetit.com/excursion/parque-natural-de-mondrago/",
    "torrent-de-pareis": "https://www.turismepetit.com/excursion/torrent-de-pareis-en-bus-y-barco/"
}

def sync_turismepetit_dataset():
    print("=== Sincronitzant rutes de Turisme Petit al Dataset ===")
    routes = []
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            routes = json.load(f)
            
    routes_dict = {r["slug"]: r for r in routes}
    
    # 1. Actualitzar enllaços a rutes existents
    for slug, url in EXISTING_TURISMEPETIT_MAP.items():
        if slug in routes_dict:
            routes_dict[slug]["turismepetit_url"] = url
            print(f"[VINCULAT] Ruta '{slug}' enllaçada amb Turisme Petit.")
            
    # 2. Afegir noves rutes de Turisme Petit
    for new_r in TURISMEPETIT_ROUTES:
        routes_dict[new_r["slug"]] = new_r
        print(f"[AFEGIDA/ACTUALITZADA] '{new_r['nom']}' amb enllaç Turisme Petit.")
        
    full_list = list(routes_dict.values())
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(full_list, f, ensure_ascii=False, indent=2)
        
    print(f"S'han sincronitzat {len(full_list)} rutes a {DATA_PATH}.")
    
    print("Reconstruint la Wiki...")
    subprocess.run([sys.executable, "scripts/build_wiki_pages.py"], check=True)
    print("=== Sincronització de Turisme Petit completada amb èxit! ===")

if __name__ == "__main__":
    sync_turismepetit_dataset()
