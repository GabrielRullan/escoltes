import os
import json
import requests
from bs4 import BeautifulSoup

def decode_cf_email(cfemail_hex):
    try:
        r = int(cfemail_hex[:2], 16)
        email = "".join(chr(int(cfemail_hex[i:i+2], 16) ^ r) for i in range(2, len(cfemail_hex), 2))
        return email
    except Exception:
        return ""

def scrape_megm_agrupaments():
    url = "https://megm.org/agrupaments/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    agrupaments = []
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        for elem in soup.find_all(attrs={"data-cfemail": True}):
            cf_hex = elem["data-cfemail"]
            decoded_email = decode_cf_email(cf_hex)
            elem.replace_with(decoded_email)
            
        raw_groups = [
            # Pobles
            {
                "slug": "aeg-capita-angelats",
                "nom": "AEG Capità Angelats",
                "municipi": "Sóller",
                "tipus": "Poble",
                "parroquia_o_lloc": "Sóller (Vall de Sóller)",
                "email": "capitaangelats@megm.org",
                "lat": 39.7663, "lon": 2.7153,
                "descripcio": "Agrupament degà de la Vall de Sóller, amb gran tradició en sortides a la Serra de Tramuntana (Muleta, Cienfuegos, Biniaraix)."
            },
            {
                "slug": "aeg-pedra-viva",
                "nom": "AEG Pedra Viva",
                "municipi": "Binissalem",
                "tipus": "Poble",
                "parroquia_o_lloc": "Binissalem",
                "email": "pedraviva@megm.org",
                "lat": 39.6917, "lon": 2.8422,
                "descripcio": "Agrupament del Raiguer situat al peu de la Serra de Tramuntana, referent en excursionisme cap a Alaró i Tossals Verds."
            },
            {
                "slug": "aeg-soca-arrel",
                "nom": "AEG Soca-Arrel",
                "municipi": "Marratxí",
                "tipus": "Poble",
                "parroquia_o_lloc": "Pòrtol",
                "email": "socaarrel@megm.org",
                "lat": 39.6430, "lon": 2.7231,
                "descripcio": "Agrupament integrat a Pòrtol (Marratxí), proper a l'Àrea Recreativa de Caubet."
            },
            {
                "slug": "aeg-terra-de-pous",
                "nom": "AEG Terra de Pous",
                "municipi": "Santa Maria del Camí",
                "tipus": "Poble",
                "parroquia_o_lloc": "Santa Maria del Camí",
                "email": "terradepous@megm.org",
                "lat": 39.6514, "lon": 2.7725,
                "descripcio": "Agrupament de Santa Maria del Camí, vinculat a les rutes de la Coanegra i la vall de Solleric."
            },
            {
                "slug": "aeg-sa-marjal",
                "nom": "AEG Sa Marjal",
                "municipi": "Sa Pobla",
                "tipus": "Poble",
                "parroquia_o_lloc": "Sa Pobla",
                "email": "samarjal@megm.org",
                "lat": 39.7694, "lon": 3.0247,
                "descripcio": "Agrupament de sa Pobla, actiu en activitats al nord de l'illa, Albufera i Massís de Randa/Llevant."
            },
            # Barris de Palma
            {
                "slug": "aeg-son-sardina",
                "nom": "AEG Son Sardina",
                "municipi": "Palma",
                "tipus": "Barri",
                "parroquia_o_lloc": "Son Sardina",
                "email": "sonsardina@megm.org",
                "lat": 39.6150, "lon": 2.6520,
                "descripcio": "Agrupament del barri rural de Son Sardina a Palma, als peus de la carretera de Sóller."
            },
            {
                "slug": "aeg-eladi-homs",
                "nom": "AEG Eladi Homs",
                "municipi": "Palma",
                "tipus": "Barri",
                "parroquia_o_lloc": "Parròquia de Sant Alonso (Palma)",
                "email": "eladihoms@megm.org",
                "lat": 39.5750, "lon": 2.6580,
                "descripcio": "Agrupament històric de Palma, vinculat a la parròquia de Sant Alonso."
            },
            {
                "slug": "aeg-jaume-i",
                "nom": "AEG Jaume I",
                "municipi": "Palma",
                "tipus": "Barri",
                "parroquia_o_lloc": "Parròquia de l'Encarnació (Palma)",
                "email": "jaumeprimer@megm.org",
                "lat": 39.5790, "lon": 2.6530,
                "descripcio": "Agrupament del barri de l'Encarnació a Palma."
            },
            {
                "slug": "aeg-verge-de-lluc",
                "nom": "AEG Verge de Lluc",
                "municipi": "Palma",
                "tipus": "Barri",
                "parroquia_o_lloc": "Parròquia de l'Encarnació (Palma)",
                "email": "vergedelluc@megm.org",
                "lat": 39.5795, "lon": 2.6535,
                "descripcio": "Agrupament germà situat a la parròquia de l'Encarnació a Palma."
            },
            {
                "slug": "aeg-ramon-llull",
                "nom": "AEG Ramon Llull",
                "municipi": "Palma",
                "tipus": "Barri",
                "parroquia_o_lloc": "Sant Francesc (Centre Històric Palma)",
                "email": "ramonllull@megm.org",
                "lat": 39.5696, "lon": 2.6502,
                "descripcio": "Agrupament al barri antic de Palma (Sant Francesc)."
            },
            {
                "slug": "aeg-reina-constanca",
                "nom": "AEG Reina Constança de Mallorca",
                "municipi": "Palma",
                "tipus": "Barri",
                "parroquia_o_lloc": "Parròquia de Santa Catalina Thomàs (Palma)",
                "email": "reinaconstanca@megm.org",
                "lat": 39.5720, "lon": 2.6410,
                "descripcio": "Agrupament del barri de Santa Catalina a Palma."
            },
            {
                "slug": "aeg-sant-josep-obrer",
                "nom": "AEG Sant Josep Obrer",
                "municipi": "Palma",
                "tipus": "Barri",
                "parroquia_o_lloc": "Parròquia de Sant Josep Obrer (Palma)",
                "email": "santjosepobrer@megm.org",
                "lat": 39.5840, "lon": 2.6650,
                "descripcio": "Agrupament del barri de Sant Josep Obrer a Palma."
            }
        ]
        
        for group in raw_groups:
            agrupaments.append({
                "slug": group["slug"],
                "nom": group["nom"],
                "associacio": "MEGM (Moviment Escolta i Guiatge de Mallorca)",
                "municipi": group["municipi"],
                "zona": group["tipus"],
                "ubicacio_detall": group["parroquia_o_lloc"],
                "email": group["email"],
                "web": "https://megm.org/agrupaments/",
                "lat": group["lat"],
                "lon": group["lon"],
                "descripcio": group["descripcio"]
            })
            
    except Exception as e:
        print(f"Error scraping MEGM: {e}")
        
    return agrupaments

def scrape_other_mallorca_groups():
    other_groups = [
        {
            "slug": "aeg-nuredduna",
            "nom": "AEG Nuredduna",
            "associacio": "Escoltes i Guies de Mallorca (EGM)",
            "municipi": "Bunyola / Palmanyola",
            "zona": "Poble",
            "ubicacio_detall": "Palmanyola (Bunyola)",
            "email": "nuredduna@escoltesiguiesdemallorca.org",
            "web": "https://escoltesiguiesdemallorca.org/",
            "lat": 39.6597, "lon": 2.6983,
            "descripcio": "Agrupament laic referent de l'associació Escoltes i Guies de Mallorca situat a Palmanyola."
        },
        {
            "slug": "gs-myotragus-684",
            "nom": "Grupo Scout Myotragus 684",
            "associacio": "ASDE Escoltes de Balears (Scouts de España)",
            "municipi": "Llucmajor",
            "zona": "Poble",
            "ubicacio_detall": "S'Arenal de Llucmajor",
            "email": "gsmyotragus684@scout.es",
            "web": "https://balears.scout.es/",
            "lat": 39.5008, "lon": 2.7533,
            "descripcio": "Grup escolta pertanyent a ASDE Scouts de Balears fundat a s'Arenal el 2010."
        }
    ]
    return other_groups

def main():
    os.makedirs("data", exist_ok=True)
    megm = scrape_megm_agrupaments()
    others = scrape_other_mallorca_groups()
    all_groups = megm + others
    
    output_path = os.path.join("data", "agrupaments_mallorca.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_groups, f, ensure_ascii=False, indent=2)
        
    print(f"S'han desat {len(all_groups)} agrupaments escoltes amb coordenades a {output_path}")

if __name__ == "__main__":
    main()
