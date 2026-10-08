#!/usr/bin/env python3
"""
Generate authentic public transport datasets for Menorca and Pitiüses (Eivissa and Formentera).
Outputs:
  - data/transport_menorca.json
  - data/transport_pitiuses.json
"""

import json
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

MENORCA_LINES = [
    {
        "codi": "MEN L01",
        "nom": "Maó - Alaior - Es Mercadal - Ferreries - Ciutadella",
        "corredor": "Eix Central (Connexió Total)",
        "municipis_coberts": ["Maó", "Alaior", "Es Mercadal", "Ferreries", "Ciutadella"],
        "parades_clau": [
            "Estació d'Autobusos de Maó",
            "Alaior Centre",
            "Es Mercadal",
            "Ferreries",
            "Via Perimetral de Ciutadella"
        ],
        "link_horaris": "https://www.tib.org/ca/web/ctm/autobus/linia/01"
    },
    {
        "codi": "MEN L02",
        "nom": "Maó - Es Castell",
        "corredor": "Llevant",
        "municipis_coberts": ["Maó", "Es Castell"],
        "parades_clau": [
            "Estació d'Autobusos de Maó",
            "Es Castell Centre",
            "Cala de Sant Esteve"
        ],
        "link_horaris": "https://www.tmsa.es/"
    },
    {
        "codi": "MEN L03",
        "nom": "Maó - Sant Lluís",
        "corredor": "Llevant",
        "municipis_coberts": ["Maó", "Sant Lluís"],
        "parades_clau": [
            "Estació d'Autobusos de Maó",
            "Sant Lluís Centre",
            "Campament Biniparratx / Punta Prima"
        ],
        "link_horaris": "https://www.tmsa.es/"
    },
    {
        "codi": "MEN L21",
        "nom": "Maó - Sant Climent",
        "corredor": "Llevant Sud",
        "municipis_coberts": ["Maó", "Sant Climent"],
        "parades_clau": [
            "Estació d'Autobusos de Maó",
            "Sant Climent",
            "Binissafúller"
        ],
        "link_horaris": "https://www.tmsa.es/"
    },
    {
        "codi": "MEN L22",
        "nom": "Maó - Canutells",
        "corredor": "Llevant Sud",
        "municipis_coberts": ["Maó", "Sant Lluís"],
        "parades_clau": [
            "Estació d'Autobusos de Maó",
            "Sant Climent",
            "Es Canutells",
            "Binisafúller"
        ],
        "link_horaris": "https://www.tmsa.es/"
    },
    {
        "codi": "MEN L31",
        "nom": "Maó - Fornells",
        "corredor": "Tramuntana Nord",
        "municipis_coberts": ["Maó", "Es Mercadal", "Fornells"],
        "parades_clau": [
            "Estació d'Autobusos de Maó",
            "Es Mercadal",
            "Arenal d'en Castell",
            "Fornells Port"
        ],
        "link_horaris": "https://www.tmsa.es/"
    },
    {
        "codi": "MEN L51",
        "nom": "Maó - Alaior - Ferreries - Cala Galdana",
        "corredor": "Migjorn Sud",
        "municipis_coberts": ["Maó", "Alaior", "Ferreries", "Cala Galdana"],
        "parades_clau": [
            "Estació d'Autobusos de Maó",
            "Alaior",
            "Ferreries",
            "Cala Galdana"
        ],
        "link_horaris": "https://www.tmsa.es/"
    },
    {
        "codi": "MEN L52",
        "nom": "Ciutadella - Ferreries - Cala Galdana",
        "corredor": "Migjorn Oest",
        "municipis_coberts": ["Ciutadella", "Ferreries", "Cala Galdana"],
        "parades_clau": [
            "Plaça dels Pins (Ciutadella)",
            "Ferreries",
            "Cala Galdana"
        ],
        "link_horaris": "https://www.tmsa.es/"
    },
    {
        "codi": "MEN L62",
        "nom": "Ciutadella - Cala Morell - La Vall",
        "corredor": "Ponent / Nord",
        "municipis_coberts": ["Ciutadella"],
        "parades_clau": [
            "Via Perimetral (Ciutadella)",
            "Cala Morell",
            "La Vall (Algaiarens)"
        ],
        "link_horaris": "https://e-torres.net/"
    },
    {
        "codi": "MEN L65",
        "nom": "Ciutadella - Caleta - Cala en Bosc - Son Xoriguer",
        "corredor": "Ponent Sud",
        "municipis_coberts": ["Ciutadella"],
        "parades_clau": [
            "Ciutadella Centre",
            "Sa Caleta",
            "Cap d'Artrutx",
            "Cala en Bosc",
            "Son Xoriguer"
        ],
        "link_horaris": "https://e-torres.net/"
    },
    {
        "codi": "MEN L68",
        "nom": "Ciutadella - Cala Turqueta",
        "corredor": "Platges Sud",
        "municipis_coberts": ["Ciutadella"],
        "parades_clau": [
            "Via Perimetral (Ciutadella)",
            "Pàrquing Cala Turqueta"
        ],
        "link_horaris": "https://e-torres.net/"
    },
    {
        "codi": "MEN L73",
        "nom": "Maó - Alaior - Es Migjorn Gran",
        "corredor": "Migjorn Central",
        "municipis_coberts": ["Maó", "Alaior", "Es Migjorn Gran"],
        "parades_clau": [
            "Estació d'Autobusos de Maó",
            "Alaior",
            "Es Migjorn Gran",
            "Sant Tomàs"
        ],
        "link_horaris": "https://www.tmsa.es/"
    }
]

PITIUSES_LINES = [
    # Eivissa (9 lines)
    {
        "codi": "IBZ L03",
        "nom": "Sant Antoni - Sant Rafel - Eivissa",
        "corredor": "Eix Central",
        "municipis_coberts": ["Sant Antoni de Portmany", "Sant Josep de sa Talaia", "Eivissa"],
        "parades_clau": [
            "Estació d'Autobusos de Sant Antoni",
            "Sant Rafel",
            "CETIS Estació Eivissa",
            "Can Coix"
        ],
        "link_horaris": "https://ibiza.avanzagrupo.com/lineas-y-horarios"
    },
    {
        "codi": "IBZ L08",
        "nom": "Sant Antoni - Sant Josep - Eivissa",
        "corredor": "Sud-Oest",
        "municipis_coberts": ["Sant Antoni de Portmany", "Sant Josep de sa Talaia", "Eivissa"],
        "parades_clau": [
            "Sant Antoni",
            "Sant Josep de sa Talaia",
            "Cala Vedella",
            "Cala de Bou",
            "CETIS Eivissa"
        ],
        "link_horaris": "https://ibiza.avanzagrupo.com/lineas-y-horarios"
    },
    {
        "codi": "IBZ L10",
        "nom": "Eivissa - Sant Jordi - Aeroport",
        "corredor": "Sud Metropolità",
        "municipis_coberts": ["Eivissa", "Sant Josep de sa Talaia"],
        "parades_clau": [
            "CETIS Estació Eivissa",
            "Sant Jordi de ses Salines",
            "Aeroport d'Eivissa"
        ],
        "link_horaris": "https://ibiza.avanzagrupo.com/lineas-y-horarios"
    },
    {
        "codi": "IBZ L11",
        "nom": "Eivissa - Sant Jordi - Ses Salines",
        "corredor": "Parc Natural Ses Salines",
        "municipis_coberts": ["Eivissa", "Sant Josep de sa Talaia"],
        "parades_clau": [
            "CETIS Estació Eivissa",
            "Sant Jordi de ses Salines",
            "Sant Francesc de s'Estany",
            "Platja de ses Salines"
        ],
        "link_horaris": "https://voramarelgaucho.com/"
    },
    {
        "codi": "IBZ L13",
        "nom": "Santa Eulària des Riu - Eivissa",
        "corredor": "Llevant",
        "municipis_coberts": ["Santa Eulària des Riu", "Eivissa"],
        "parades_clau": [
            "Estació d'Autobusos de Santa Eulària",
            "Ca na Negreta",
            "CETIS Estació Eivissa"
        ],
        "link_horaris": "https://ibiza.avanzagrupo.com/lineas-y-horarios"
    },
    {
        "codi": "IBZ L14",
        "nom": "Eivissa - Platja d'en Bossa",
        "corredor": "Sud Platja",
        "municipis_coberts": ["Eivissa", "Sant Josep de sa Talaia"],
        "parades_clau": [
            "CETIS Estació Eivissa",
            "Platja d'en Bossa",
            "Torre de sa Sal Rossa"
        ],
        "link_horaris": "https://ibiza.avanzagrupo.com/lineas-y-horarios"
    },
    {
        "codi": "IBZ L16",
        "nom": "Santa Eulària - Sant Carles",
        "corredor": "Nord-Est",
        "municipis_coberts": ["Santa Eulària des Riu"],
        "parades_clau": [
            "Estació d'Autobusos de Santa Eulària",
            "Sant Carles de Peralta",
            "Es Figueral",
            "Pou des Lleó"
        ],
        "link_horaris": "https://ibiza.avanzagrupo.com/lineas-y-horarios"
    },
    {
        "codi": "IBZ L20A",
        "nom": "Eivissa - Sant Llorenç - Sant Joan - Portinatx",
        "corredor": "Els Amunts / Nord",
        "municipis_coberts": ["Eivissa", "Sant Joan de Labritja"],
        "parades_clau": [
            "CETIS Estació Eivissa",
            "Sant Llorenç de Balàfia",
            "Sant Joan de Labritja",
            "Portinatx"
        ],
        "link_horaris": "https://sagalesibiza.com/"
    },
    {
        "codi": "IBZ L25",
        "nom": "Eivissa - Santa Gertrudis - Sant Miquel",
        "corredor": "Nord Central",
        "municipis_coberts": ["Eivissa", "Santa Eulària des Riu", "Sant Joan de Labritja"],
        "parades_clau": [
            "CETIS Estació Eivissa",
            "Santa Gertrudis de Fruitera",
            "Sant Miquel de Balansat",
            "Port de Sant Miquel"
        ],
        "link_horaris": "https://sagalesibiza.com/"
    },
    # Formentera (4 lines)
    {
        "codi": "FOR L1",
        "nom": "Port de la Savina - Es Pujols - Sant Francesc (Circular)",
        "corredor": "Ponent Circular",
        "municipis_coberts": ["Formentera"],
        "parades_clau": [
            "Port de la Savina",
            "Es Pujols",
            "Sant Ferran de ses Roques",
            "Sant Francesc Xavier"
        ],
        "link_horaris": "https://busformentera.com/"
    },
    {
        "codi": "FOR L2",
        "nom": "Port de la Savina - Sant Francesc - Es Caló - El Pilar de la Mola",
        "corredor": "Eix Longitudinal",
        "municipis_coberts": ["Formentera"],
        "parades_clau": [
            "Port de la Savina",
            "Sant Francesc Xavier",
            "Sant Ferran de ses Roques",
            "Ca Marí",
            "Es Caló de Sant Agustí",
            "El Pilar de la Mola"
        ],
        "link_horaris": "https://busformentera.com/"
    },
    {
        "codi": "FOR L3",
        "nom": "Port de la Savina - Ses Illetes (Línia Parc Natural)",
        "corredor": "Parc Natural de ses Salines",
        "municipis_coberts": ["Formentera"],
        "parades_clau": [
            "Port de la Savina",
            "Platja de ses Illetes",
            "Pas des Trucadors"
        ],
        "link_horaris": "https://busformentera.com/"
    },
    {
        "codi": "FOR L5",
        "nom": "Port de la Savina - Sant Francesc - Cala Saona",
        "corredor": "Sud-Oest",
        "municipis_coberts": ["Formentera"],
        "parades_clau": [
            "Port de la Savina",
            "Sant Francesc Xavier",
            "Cala Saona"
        ],
        "link_horaris": "https://busformentera.com/"
    }
]


def write_json_dataset(file_path: Path, lines: list):
    payload = {"linies_bus": lines}
    # Ensure UTF-8 without BOM, nice indenting matching repository style
    json_str = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    file_path.write_text(json_str, encoding="utf-8")
    print(f"Written {len(lines)} bus lines to {file_path}")


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    write_json_dataset(DATA_DIR / "transport_menorca.json", MENORCA_LINES)
    write_json_dataset(DATA_DIR / "transport_pitiuses.json", PITIUSES_LINES)
    print("Balearic transport datasets generation completed successfully.")


if __name__ == "__main__":
    main()
