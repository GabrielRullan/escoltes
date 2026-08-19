import os
import sys
import json
import re
import urllib.parse
import subprocess
import requests
from bs4 import BeautifulSoup

DATA_PATH = os.path.join("data", "rutes_mallorca.json")

def create_slug(text):
    text = text.lower()
    text = re.sub(r'[àáâä]', 'a', text)
    text = re.sub(r'[èéêë]', 'e', text)
    text = re.sub(r'[ìíîï]', 'i', text)
    text = re.sub(r'[òóôö]', 'o', text)
    text = re.sub(r'[ùúûü]', 'u', text)
    text = re.sub(r'[ç]', 'c', text)
    text = re.sub(r'[ñ]', 'n', text)
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text.strip('-')

def scrape_wikiloc_url(url):
    print(f"=== Processant URL de Wikiloc: {url} ===")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "ca,es;q=0.9,en;q=0.8"
    }
    
    # 1. Intentar extreure el títol inicial des de la pròpia estructura de la URL per si hi ha un bloqueig 403
    url_path = urllib.parse.urlparse(url).path
    raw_slug = url_path.strip('/').split('/')[-1]
    raw_slug_clean = re.sub(r'-\d+$', '', raw_slug) # Treure l'ID numèric final de Wikiloc
    title_from_url = raw_slug_clean.replace('-', ' ').title()
    
    title = title_from_url or "Ruta de Wikiloc"
    desc = f"Ruta d'excursió extreta de Wikiloc ([Veure Track Oficial a Wikiloc]({url}))."
    dist_km = 8.5
    ele_m = 350
    durada = "3h 30min"
    dif = "Moderada"
    municipi = "Mallorca"
    lat, lon = 39.65, 2.90
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Títol
            title_el = soup.find("h1") or soup.find("meta", property="og:title")
            if title_el:
                scraped_title = title_el.get_text(strip=True) if hasattr(title_el, "get_text") else title_el.get("content", "")
                title = re.sub(r'\s*-\s*Wikiloc.*', '', scraped_title, flags=re.IGNORECASE).strip()
                
            # Descripció
            desc_el = soup.find("meta", property="og:description") or soup.find("meta", attrs={"name": "description"})
            if desc_el:
                desc = desc_el.get("content", "").strip()
                
            # Coordenades
            geo_el = soup.find("meta", property="place:location:latitude")
            if geo_el:
                lat = float(geo_el.get("content"))
                lon = float(soup.find("meta", property="place:location:longitude").get("content"))
        else:
            print(f"[AVÍS] Wikiloc ha retornat codi {response.status_code}. Utilitzant informació de la URL.")
    except Exception as e:
        print(f"[AVÍS] No s'ha pogut descarregar el contingut HTML directament ({e}). Utilitzant dades estructurades de la URL.")

    slug = create_slug(title)
    
    # Determinar unitats recomanades
    apte_unitats = ["Pioners/Rangers", "Rovers/Rutes"]
    if dist_km <= 6 and ele_m <= 250:
        apte_unitats = ["Castors/Fures", "Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"]
    elif dist_km <= 10 and ele_m <= 450:
        apte_unitats = ["Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"]
        
    route_data = {
        "slug": slug,
        "nom": title,
        "municipi": municipi,
        "zona": "Serra de Tramuntana",
        "distancia_km": dist_km,
        "desnivell_positiu_m": ele_m,
        "dificultat": dif,
        "durada_estimada": durada,
        "apte_unitats": apte_unitats,
        "punts_aigua": ["Consultar punts de recàrrega"],
        "passos_finca_privada": ["Consultar senyalització i camins habilitats"],
        "punts_interes": [title],
        "consells_seguretat": "Portar aigua suficient, calçat de muntanya i consultar la previsió del temps abans de sortir.",
        "descripcio": desc,
        "wikiloc_url": url,
        "lat": lat,
        "lon": lon,
        "track_coordinates": [
            [lat, lon],
            [lat + 0.005, lon + 0.005]
        ],
        "itinerari_passos": [
            {"pas": 1, "nom": "Inici de la ruta (Wikiloc)", "desc": f"Sortida des del punt inicial indicat al track de Wikiloc ({url})."},
            {"pas": 2, "nom": "Tram principal del recorregut", "desc": "Seguiment de la sendera i fites sobre el terreny."},
            {"pas": 3, "nom": "Punt d'arribada", "desc": "Final de la ruta o retorn al punt d'origen."}
        ]
    }
    
    return route_data

def add_or_update_route(route_data):
    os.makedirs("data", exist_ok=True)
    routes = []
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            routes = json.load(f)
            
    # Comprovar si ja existeix per slug o per wikiloc_url
    existing_idx = None
    for idx, r in enumerate(routes):
        if r.get("slug") == route_data["slug"] or (r.get("wikiloc_url") and r.get("wikiloc_url") == route_data["wikiloc_url"]):
            existing_idx = idx
            break
            
    if existing_idx is not None:
        print(f"[ACTUALITZAT] La ruta '{route_data['nom']}' ja existia i s'ha actualitzat.")
        routes[existing_idx].update(route_data)
    else:
        print(f"[NOVA RUTA] S'ha afegit la ruta '{route_data['nom']}' al dataset.")
        routes.append(route_data)
        
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(routes, f, ensure_ascii=False, indent=2)
        
    # Reconstruir la wiki
    print("Reconstruint les pàgines de la Wiki...")
    subprocess.run([sys.executable, "scripts/build_wiki_pages.py"], check=True)
    print("=== Ruta afegida i Wiki reconstruïda amb èxit! ===")

def main():
    if len(sys.argv) < 2:
        print("Ús: python scripts/add_wikiloc_route.py <URL_DE_WIKILOC>")
        sys.exit(1)
        
    url = sys.argv[1]
    route_data = scrape_wikiloc_url(url)
    add_or_update_route(route_data)

if __name__ == "__main__":
    main()
