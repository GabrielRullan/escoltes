"""
Script per generar il·lustracions de pobles de Mallorca amb Gemini Free Tier (gemini-2.5-flash-image).
Utilitza la clau gratuïta de GOOGLE_API_KEY del fitxer .env (com a anki_helper).

Límit i proteccions Free Tier:
- Models: gemini-2.5-flash-image, gemini-3.1-flash-image, gemini-3-pro-image
- Delay: 5.0 segons entre crides (12 RPM) per mantenir-se sota el límit de 15 RPM.
- Guardat a: public/images/pobles/{slug}.png
"""

import os
import sys
import time
import json
import unicodedata
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Assegurar sortida UTF-8 per a caràcters catalans
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

if not api_key:
    print("[ERROR] No s'ha trobat GOOGLE_API_KEY ni GEMINI_API_KEY a .env.")
    sys.exit(1)

client = genai.Client(api_key=api_key)

IMAGE_MODELS = ['gemini-2.5-flash-image', 'gemini-3.1-flash-image', 'gemini-3-pro-image']

output_dir = Path("public/images/pobles")
output_dir.mkdir(parents=True, exist_ok=True)

# Llista completa dels 31 municipis de Mallorca amb rutes
TOWNS_WITH_ROUTES = [
    ("Alaró", "castell d'Alaró sobre el penyal i oliveres"),
    ("Alcúdia", "murades medievals de pedra i badia d'Alcúdia"),
    ("Algaida", "molins de vent tradicionals i pla de Mallorca"),
    ("Andratx", "la Trapa, port natural i costa rocosa"),
    ("Artà", "santuari de Sant Salvador i camí costaner de Betlem"),
    ("Banyalbufar", "marjades de pedra seca vora la mar"),
    ("Bunyola", "bosc de la Comuna de Bunyola i alzines"),
    ("Calvià", "finca pública de Galatzó i camí de muntanya"),
    ("Campanet", "monument natural de ses Fonts Ufanes"),
    ("Deià", "cases de pedra sobre el turó i cala de Deià"),
    ("Escorca", "monestir de Lluc i cims de la Serra de Tramuntana"),
    ("Esporles", "camí des Correu i plàtans d'ombra vora el torrent"),
    ("Estellencs", "carrers empedrats de poble i mar de Tramuntana"),
    ("Felanitx", "castell de Santueri i santuari de Sant Salvador"),
    ("Fornalutx", "carrers estrets florits i tarongers"),
    ("Lloret de Vistalegre", "sa Comuna de Lloret i pinar mediterrani"),
    ("Llucmajor", "penya-segats amb torre de defensa d'Estalella"),
    ("Manacor", "camins rurals de terra i cales verges"),
    ("Montuïri", "puig de Sant Miquel i camps de Mallorca"),
    ("Muro", "Parc Natural de s'Albufera amb canals i aus"),
    ("Palma", "castell i bosc de Bellver amb vistes a la badia"),
    ("Petra", "ermita de Bonany i vistes panoràmiques al Pla"),
    ("Pollença", "escalonada del Calvari amb xiprers i Formentor"),
    ("Puigpunyent", "puig de Galatzó i alzinar verd"),
    ("Sa Pobla", "marjals agrícoles i camps tradicionals"),
    ("Santa Margalida", "finca pública de Son Real vora la mar"),
    ("Santa Maria del Camí", "camí de la vall de Coanegra i avencs"),
    ("Santanyí", "Parc Natural de Mondragó amb cala verge"),
    ("Selva", "camí empedrat de Caimari i oliveres centenàries"),
    ("Sóller", "vall dels tarongers i muntanyes de Tramuntana"),
    ("Valldemossa", "la Cartoixa de Valldemossa i camí de s'Arxiduc"),
]

def norm_slug(name: str) -> str:
    s = ''.join(c for c in unicodedata.normalize('NFD', name.lower()) if unicodedata.category(c) != 'Mn')
    return s.replace(' ', '_').replace("'", '')

def generate_town_image(town: str, details: str, delay: float = 5.0) -> bool:
    slug = norm_slug(town)
    # Check both png and jpg
    dest_png = output_dir / f"{slug}.png"
    dest_jpg = output_dir / f"{slug}.jpg"
    
    if dest_png.exists() or dest_jpg.exists():
        print(f"  [JA EXISTEIX] {town} ({slug}) -> saltant.")
        return True

    prompt = (
        f"Generate image: un scout a {town} Mallorca, {details}, "
        "en estil de dibuix molt senzill a pinzell, simple brush watercolor drawing, "
        "minimalist ink contour lines, soft earthy natural washes, no modern text, clean artistic illustration"
    )

    for model_id in IMAGE_MODELS:
        print(f"  Provant model {model_id} per a {town}...", end=" ", flush=True)
        for attempt in range(2):
            try:
                response = client.models.generate_content(
                    model=model_id,
                    contents=prompt
                )
                
                if response and response.candidates:
                    for cand in response.candidates:
                        if cand.content and cand.content.parts:
                            for part in cand.content.parts:
                                if part.inline_data and part.inline_data.data:
                                    image_bytes = part.inline_data.data
                                    with open(dest_png, "wb") as f:
                                        f.write(image_bytes)
                                    print("✓ Èxit! Desat a", dest_png.name)
                                    time.sleep(delay)
                                    return True
                    print("No s'ha retornat cap imatge inline.")
                else:
                    print("Cap candidat retornat.")
            except Exception as e:
                err = str(e)
                if "429" in err or "RESOURCE_EXHAUSTED" in err:
                    print(f"Rate limited (intent {attempt+1}/2). Esperant 12s...", end=" ", flush=True)
                    time.sleep(12)
                else:
                    print(f"Error: {err}")
                    break
    return False

def main():
    print(f"==================================================")
    print(f" Generador d'imatges de pobles amb Gemini Free Tier")
    print(f" Total pobles a processar: {len(TOWNS_WITH_ROUTES)}")
    print(f" Destinació: {output_dir.resolve()}")
    print(f"==================================================\n")

    success_count = 0
    total = len(TOWNS_WITH_ROUTES)

    for idx, (town, details) in enumerate(TOWNS_WITH_ROUTES, 1):
        print(f"[{idx}/{total}] Processant {town}...")
        ok = generate_town_image(town, details, delay=5.0)
        if ok:
            success_count += 1

    print(f"\nFinalitzat! {success_count}/{total} municipis llestos.")

if __name__ == "__main__":
    main()
