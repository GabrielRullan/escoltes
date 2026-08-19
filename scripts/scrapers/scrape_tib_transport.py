import os
import json

def get_tib_transport_network():
    network = {
        "linies_bus": [
            {
                "codi": "TIB 101",
                "nom": "Palma - Andratx - Port d'Andratx",
                "corredor": "Ponent (100)",
                "municipis_coberts": ["Andratx", "Port d'Andratx"],
                "parades_clau": ["Palma (Estació Intermodal)", "Andratx (Grava)", "Port d'Andratx"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/101"
            },
            {
                "codi": "TIB 102",
                "nom": "Palma - Sant Elm",
                "corredor": "Ponent (100)",
                "municipis_coberts": ["Andratx", "Sant Elm"],
                "parades_clau": ["Palma", "Andratx", "Sant Elm (Plaça de na Caragola)"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/102"
            },
            {
                "codi": "TIB 108",
                "nom": "Palma - Calvià - Es Capdellà",
                "corredor": "Ponent (100)",
                "municipis_coberts": ["Calvià", "Es Capdellà"],
                "parades_clau": ["Palma", "Calvià", "Es Capdellà (sa Vinya)"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/108"
            },
            {
                "codi": "TIB 202",
                "nom": "Palma - Estellencs",
                "corredor": "Tramuntana Sud (200)",
                "municipis_coberts": ["Puigpunyent", "Banyalbufar", "Estellencs"],
                "parades_clau": ["Palma", "Puigpunyent", "Banyalbufar", "Estellencs vila"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/202"
            },
            {
                "codi": "TIB 203",
                "nom": "Palma - Valldemossa - Deià - Sóller",
                "corredor": "Tramuntana Central (200)",
                "municipis_coberts": ["Valldemossa", "Deià", "Sóller"],
                "parades_clau": ["Palma", "Valldemossa", "Son Marroig", "Deià", "Llucalcari", "Sóller"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/203"
            },
            {
                "codi": "TIB 204",
                "nom": "Palma - Sóller - Port de Sóller (Express Túnel)",
                "corredor": "Tramuntana Central (200)",
                "municipis_coberts": ["Sóller", "Port de Sóller"],
                "parades_clau": ["Palma (Estació Intermodal)", "Sóller (Ma-11)", "Port de Sóller"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/204"
            },
            {
                "codi": "TIB 205",
                "nom": "Palma - Bunyola - Orient",
                "corredor": "Tramuntana Central (200)",
                "municipis_coberts": ["Bunyola", "Orient"],
                "parades_clau": ["Palma", "Raixa", "Bunyola", "Orient"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/205"
            },
            {
                "codi": "TIB 301",
                "nom": "Palma - Inca - Port de Pollença",
                "corredor": "Raiguer / Nord (300)",
                "municipis_coberts": ["Inca", "Pollença", "Port de Pollença"],
                "parades_clau": ["Palma", "Inca (Estació)", "Pollença", "Port de Pollença"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/301"
            },
            {
                "codi": "TIB 302",
                "nom": "Can Picafort - Son Real - Alcúdia",
                "corredor": "Raiguer / Nord (300)",
                "municipis_coberts": ["Santa Margalida", "Muro", "Alcúdia"],
                "parades_clau": ["Can Picafort", "Son Real", "Alcúdia"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/302"
            },
            {
                "codi": "TIB 312",
                "nom": "Sa Pobla - Campanet - Inca",
                "corredor": "Raiguer (300)",
                "municipis_coberts": ["Campanet", "Sa Pobla"],
                "parades_clau": ["Inca", "Campanet", "Sa Pobla"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/312"
            },
            {
                "codi": "TIB 334",
                "nom": "Alcúdia - Port de Pollença - Formentor",
                "corredor": "Nord (300)",
                "municipis_coberts": ["Pollença", "Alcúdia"],
                "parades_clau": ["Port de Pollença", "Cala Murta", "Far de Formentor"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/334"
            },
            {
                "codi": "TIB 341",
                "nom": "Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)",
                "corredor": "Serra de Tramuntana Ma-10 (300)",
                "municipis_coberts": ["Escorca", "Selva", "Pollença", "Fornalutx", "Sóller"],
                "parades_clau": ["Pollença", "Lluc (Monestir)", "Binifaldó", "Gorg Blau", "Cúber", "Biniaraix", "Port de Sóller"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/341"
            },
            {
                "codi": "TIB 401",
                "nom": "Palma - Manacor - Cala Millor",
                "corredor": "Llevant (400)",
                "municipis_coberts": ["Manacor"],
                "parades_clau": ["Palma", "Manacor (Estació)", "Porto Cristo"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/401"
            },
            {
                "codi": "TIB 411",
                "nom": "Manacor - Artà - Capdepera - Cala Rajada",
                "corredor": "Llevant (400)",
                "municipis_coberts": ["Artà", "Capdepera"],
                "parades_clau": ["Manacor (Estació)", "Artà", "Cala Rajada"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/411"
            },
            {
                "codi": "TIB 501",
                "nom": "Palma - Llucmajor - Campos - Felanitx",
                "corredor": "Migjorn (500)",
                "municipis_coberts": ["Llucmajor", "Campos", "Felanitx"],
                "parades_clau": ["Palma", "Llucmajor", "Campos", "Felanitx"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/501"
            },
            {
                "codi": "TIB 514",
                "nom": "Felanitx - Porreres - Vilafranca",
                "corredor": "Migjorn (500)",
                "municipis_coberts": ["Porreres", "Vilafranca", "Montuïri"],
                "parades_clau": ["Felanitx", "Porreres", "Vilafranca", "Montuïri"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/514"
            },
            {
                "codi": "TIB 517",
                "nom": "Campos - Santanyí - Cala Mondragó",
                "corredor": "Migjorn (500)",
                "municipis_coberts": ["Santanyí", "Ses Salines"],
                "parades_clau": ["Campos", "Santanyí", "s'Amarador", "Cala Mondragó"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/517"
            },
            {
                "codi": "EMT L46 / L4",
                "nom": "EMT Palma - Castell de Bellver",
                "corredor": "Palma Urbà",
                "municipis_coberts": ["Palma"],
                "parades_clau": ["Plaça d'Espanya", "El Terreno", "Castell de Bellver"],
                "link_horaris": "https://www.emtpalma.cat/"
            }
        ],
        "linies_tren": [
            {
                "codi": "SFM Línia T1",
                "nom": "Tren Palma - Inca (Raiguer)",
                "operator": "Serveis Ferroviaris de Mallorca (SFM)",
                "municipis_coberts": ["Palma", "Marratxí", "Santa Maria", "Consell", "Binissalem", "Lloseta", "Inca"],
                "estacions_clau": ["Palma (Estació Intermodal)", "Verge de Lluc", "Pont d'Inca", "Marratxí", "Santa Maria", "Consell-Alaró", "Binissalem", "Lloseta", "Inca (Estació Central)"],
                "rutes_connectades": ["avenc-de-son-pou", "torrent-de-coanegra-santa-maria", "castell-d-alaro", "tossals-verds"],
                "agrupaments_connectats": ["aeg-soca-arrel", "aeg-terra-de-pous", "aeg-pedra-viva"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/tren/linia/T1"
            },
            {
                "codi": "SFM Línia T2",
                "nom": "Tren Palma - Inca - Sa Pobla",
                "operator": "Serveis Ferroviaris de Mallorca (SFM)",
                "municipis_coberts": ["Inca", "Llubí", "Muro", "Sa Pobla"],
                "estacions_clau": ["Inca", "Llubí", "Muro", "Sa Pobla"],
                "rutes_connectades": ["ses-fonts-ufanes-campanet", "parc-natural-albufera-mallorca"],
                "agrupaments_connectats": ["aeg-sa-marjal"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/tren/linia/T2"
            },
            {
                "codi": "SFM Línia T3",
                "nom": "Tren Palma - Inca - Sineu - Manacor",
                "operator": "Serveis Ferroviaris de Mallorca (SFM)",
                "municipis_coberts": ["Inca", "Sineu", "Petra", "Manacor"],
                "estacions_clau": ["Inca", "Sineu", "Petra", "Manacor (Estació)"],
                "rutes_connectades": ["ermita-bonany-petra", "son-talent-manacor", "puig-dalanar-manacor", "cala-varques-manacor"],
                "agrupaments_connectats": ["aeg-eladi-homs"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/tren/linia/T3"
            },
            {
                "codi": "SFM Metro M1 / M2",
                "nom": "Metro de Palma (Palma - UIB / Marratxí)",
                "operator": "Serveis Ferroviaris de Mallorca (SFM)",
                "municipis_coberts": ["Palma", "Marratxí"],
                "estacions_clau": ["Palma Intermodal", "Son Costa-Son Forteza", "Son Sardina", "UIB", "Pont d'Inca Nou", "Marratxí"],
                "agrupaments_connectats": ["aeg-son-sardina", "aeg-verge-de-lluc"],
                "link_horaris": "https://www.tib.org/ca/web/ctm/metro/linia/M1"
            },
            {
                "codi": "Ferrocarril de Sóller",
                "nom": "Tren de Fusta de Sóller (Palma - Bunyola - Sóller)",
                "operator": "Ferrocarril de Sóller S.A.",
                "municipis_coberts": ["Palma", "Bunyola", "Sóller"],
                "estacions_clau": ["Palma (Plaça d'Espanya)", "Son Sardina", "Bunyola", "Mirador des Pujol d'en Banya", "Sóller (Estació Central)"],
                "rutes_connectades": ["gr221-etapa-6-soller-tossals-verds", "cami-de-sa-sirereta-soller", "clot-des-cirers-soller", "puig-de-sa-comuna-bunyola"],
                "agrupaments_connectats": ["aeg-capita-angelats", "aeg-nuredduna"],
                "link_horaris": "http://trendesoller.com/"
            },
            {
                "codi": "Tramvia de Sóller",
                "nom": "Tranvia Històric de Sóller (Sóller Vila - Port de Sóller)",
                "operator": "Ferrocarril de Sóller S.A.",
                "municipis_coberts": ["Sóller", "Port de Sóller"],
                "estacions_clau": ["Sóller Estació", "Mercat de Sóller", "Es Control", "Sa Torre", "Port de Sóller (Marintorn)"],
                "rutes_connectades": ["gr221-etapa-5-deia-port-soller", "refugi-muleta", "fonts-de-sa-costera-soller"],
                "agrupaments_connectats": ["aeg-capita-angelats"],
                "link_horaris": "http://trendesoller.com/tramvia/"
            }
        ]
    }
    return network

def main():
    os.makedirs("data", exist_ok=True)
    data = get_tib_transport_network()
    output_path = os.path.join("data", "transport_mallorca.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"S'han desat les dades de TOTS els trens de Mallorca (SFM T1/T2/T3, Metro M1/M2 i Ferrocarril/Tramvia de Sóller) a {output_path}")

if __name__ == "__main__":
    main()
