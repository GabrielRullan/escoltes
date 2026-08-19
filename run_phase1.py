import os
import sys
import subprocess

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def run_scrapers():
    print("=== Phase 1: Executant Scrapers de Dades ===")
    
    # 1. Scrape MEGM & Mallorca Groups
    print("[1/4] Executant scrape_megm.py...")
    subprocess.run([sys.executable, "scripts/scrapers/scrape_megm.py"], check=True)
    
    # 2. Import Complete Google Spreadsheet Camping & Refuge Dataset (43 sites)
    print("[2/4] Executant import_spreadsheet_acampada.py...")
    subprocess.run([sys.executable, "scripts/scrapers/import_spreadsheet_acampada.py"], check=True)

    
    # 3. Scrape Extended Hiking Routes (47+ routes, including Turisme Petit)
    print("[3/4] Executant scrape_extended_routes.py...")
    subprocess.run([sys.executable, "scripts/scrapers/scrape_extended_routes.py"], check=True)


    # 4. Scrape International Repository
    print("[4/5] Executant scrape_international.py...")
    subprocess.run([sys.executable, "scripts/scrapers/scrape_international.py"], check=True)

    # 5. Scrape TIB Public Transport Network
    print("[5/5] Executant scrape_tib_transport.py...")
    subprocess.run([sys.executable, "scripts/scrapers/scrape_tib_transport.py"], check=True)


def build_wiki():
    print("\n=== Phase 1: Generant Pagines Markdown del Wiki ===")
    subprocess.run([sys.executable, "scripts/build_wiki_pages.py"], check=True)
    
    print("\n=== Compilant MkDocs (Validacio de construccio) ===")
    result = subprocess.run(["mkdocs", "build"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode == 0:
        print("[OK] El Wiki s'ha compilat satisfactoriament a /site!")
    else:
        print("[AVIS] Advertencia en compilar MkDocs:")
        print(result.stderr or result.stdout)

def main():
    run_scrapers()
    build_wiki()
    
    if "--serve" in sys.argv or "-s" in sys.argv:
        print("\n=== Iniciant el Servidor Wiki Local de Python (http://127.0.0.1:8000) ===")
        subprocess.run(["mkdocs", "serve"])

if __name__ == "__main__":
    main()

