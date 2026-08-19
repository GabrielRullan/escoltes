#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script per generar un calendari mensual en PDF a partir d'un fitxer CSV.
Dissenyat per al Portal de Suport del Grup Escolta (Mallorca).

Títol per defecte: "Calendari Jaume I i Verge de Lluc"
Amb el logotip d'Escoltes de Mallorca.

Ús:
    python scripts/generate_calendar_pdf.py --csv data/calendari_escolta_exemple.csv -o Calendari_Jaume_I_Verge_de_Lluc.pdf
"""

import os
import sys
import csv
import calendar
import argparse
from datetime import datetime, date

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.pdfgen import canvas

# Nom dels mesos i dies en català
MESOS_CA = [
    "", "GENER", "FEBRER", "MARÇ", "ABRIL", "MAIG", "JUNY",
    "JULIOL", "AGOST", "SETEMBRE", "OCTUBRE", "NOVEMBRE", "DESEMBRE"
]

DIES_SETMANA_CA = ["DILLUNS", "DIMARTS", "DIMECRES", "DIJOUS", "DIVENDRES", "DISSABTE", "DIUMENGE"]

# Paleta de colors escolta
COLOR_PRIMARY = colors.HexColor("#065F46")       # Emerald 800 (Verd Escolta Principal)
COLOR_PRIMARY_LIGHT = colors.HexColor("#F0FDF4") # Emerald 50
COLOR_SECONDARY = colors.HexColor("#D97706")     # Amber 600 (Or / Taronja)
COLOR_TEXT_DARK = colors.HexColor("#1F2937")     # Gray 800
COLOR_TEXT_MUTED = colors.HexColor("#9CA3AF")    # Gray 400
COLOR_BG_WEEKEND = colors.HexColor("#FFFBEB")    # Soft Amber Cream per cap de setmana
COLOR_BG_OTHER_MONTH = colors.HexColor("#F9FAFB")# Soft Gray per dies d'altres mesos
COLOR_BORDER = colors.HexColor("#E5E7EB")        # Border Gray
COLOR_HEADER_BG = colors.HexColor("#047857")     # Emerald 700

# Colors per unitats / categories d'activitats escoltes
UNIT_COLORS = {
    "tot el grup": colors.HexColor("#059669"),      # Emerald Green
    "esquirols": colors.HexColor("#2563EB"),        # Blau
    "castors": colors.HexColor("#2563EB"),          # Blau
    "rangers": colors.HexColor("#0891B2"),          # Cyan / Ciber Blau
    "pioners": colors.HexColor("#D97706"),          # Amber / Taronja
    "rovers": colors.HexColor("#7C3AED"),           # Purpra
    "caps": colors.HexColor("#DC2626"),             # Vermell
    "default": colors.HexColor("#4B5563")           # Slate Gray
}

def parse_date(date_str):
    """Parseja dates en formats comuns: YYYY-MM-DD, DD/MM/YYYY, YYYY/MM/DD, DD-MM-YYYY."""
    if not date_str:
        return None
    date_str = str(date_str).strip()
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d", "%d-%m-%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            pass
    return None

def load_events_from_csv(csv_path):
    """Carrega els esdeveniments d'un CSV i els agrupa per (year, month, day)."""
    events = {}
    if not os.path.exists(csv_path):
        print(f"[ERR] No s'ha trobat el fitxer CSV a: {csv_path}")
        return events

    with open(csv_path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Cercar columnes amb noms en català o anglès
            d_str = (row.get("date") or row.get("Data") or row.get("data") or 
                     row.get("start_date") or row.get("data_inici"))
            evt_title = (row.get("event") or row.get("Esdeveniment") or row.get("esdeveniment") or 
                         row.get("title") or row.get("Titol") or row.get("titol"))
            unit = (row.get("unit") or row.get("Unitat") or row.get("unitat") or 
                    row.get("group") or row.get("category") or "Tot el grup")
            location = row.get("location") or row.get("Lloc") or row.get("lloc") or ""
            notes = row.get("notes") or row.get("Notes") or row.get("notes") or ""

            if d_str and evt_title:
                d_obj = parse_date(d_str)
                if d_obj:
                    key = (d_obj.year, d_obj.month, d_obj.day)
                    if key not in events:
                        events[key] = []
                    events[key].append({
                        "title": evt_title.strip(),
                        "unit": unit.strip(),
                        "location": location.strip(),
                        "notes": notes.strip()
                    })
    return events

def get_unit_color(unit_name):
    """Torna el color corresponent a la unitat o categoria escolta."""
    u_lower = unit_name.lower()
    for key, color in UNIT_COLORS.items():
        if key in u_lower:
            return color
    return UNIT_COLORS["default"]

def draw_month_page(c, year, month, events, logo_path, title_text):
    """Dibuixa una pàgina completa de calendari mensual (A4 Horitzontal)."""
    page_w, page_h = landscape(A4) # 841.89 x 595.27 pt
    
    margin_x = 30
    margin_top = 25
    margin_bottom = 25
    
    # Altura del bloc de capçalera: 65pt
    header_y = page_h - margin_top - 65
    
    # 1. Marc Fons Capçalera
    c.setFillColor(COLOR_PRIMARY_LIGHT)
    c.setStrokeColor(COLOR_PRIMARY)
    c.setLineWidth(1)
    c.roundRect(margin_x, header_y, page_w - (margin_x * 2), 65, 8, fill=1, stroke=1)
    
    # Logotip Escoltes de Mallorca (esquerra)
    logo_w, logo_h = 55, 55
    if logo_path and os.path.exists(logo_path):
        try:
            c.drawImage(logo_path, margin_x + 10, header_y + 5, width=logo_w, height=logo_h, mask='auto', preserveAspectRatio=True)
        except Exception as e:
            print(f"[AVÍS] No s'ha pogut incloure el logo: {e}")
    
    # Text del Capçalera
    text_x = margin_x + 75
    c.setFillColor(COLOR_PRIMARY)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(text_x, header_y + 46, "ESCOLTES DE MALLORCA — GRUP ESCOLTA JAUME I I VERGE DE LLUC")
    
    c.setFillColor(COLOR_TEXT_DARK)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(text_x, header_y + 22, title_text)
    
    # Banner destacat del Mes i Any (dreta)
    month_name = MESOS_CA[month]
    month_str = f"{month_name} {year}"
    
    c.setFillColor(COLOR_HEADER_BG)
    c.roundRect(page_w - margin_x - 230, header_y + 10, 220, 45, 6, fill=1, stroke=0)
    
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(page_w - margin_x - 120, header_y + 25, month_str)
    
    # 2. Graella del Calendari
    grid_top = header_y - 12
    grid_bottom = margin_bottom + 35 # Espai per al peu de pàgina
    grid_h = grid_top - grid_bottom
    grid_w = page_w - (margin_x * 2)
    
    col_w = grid_w / 7.0
    day_header_h = 22.0
    
    # Fila de noms dels dies de la setmana
    c.setFillColor(COLOR_HEADER_BG)
    c.rect(margin_x, grid_top - day_header_h, grid_w, day_header_h, fill=1, stroke=0)
    
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 10)
    for i, dname in enumerate(DIES_SETMANA_CA):
        cx = margin_x + (i * col_w) + (col_w / 2.0)
        cy = grid_top - day_header_h + 6
        c.drawCentredString(cx, cy, dname)
    
    # Matriu de setmanes i dies
    cal = calendar.Calendar(firstweekday=0) # 0 = Dilluns
    month_days = cal.monthdatescalendar(year, month)
    num_weeks = len(month_days)
    
    row_h = (grid_h - day_header_h) / float(num_weeks)
    
    for r_idx, week in enumerate(month_days):
        y_top = grid_top - day_header_h - (r_idx * row_h)
        y_bot = y_top - row_h
        
        for c_idx, day_obj in enumerate(week):
            x_left = margin_x + (c_idx * col_w)
            x_right = x_left + col_w
            
            is_current_month = (day_obj.month == month)
            is_weekend = (c_idx >= 5) # Dissabte / Diumenge
            
            # Color de fons de la cel·la
            if not is_current_month:
                c.setFillColor(COLOR_BG_OTHER_MONTH)
            elif is_weekend:
                c.setFillColor(COLOR_BG_WEEKEND)
            else:
                c.setFillColor(colors.white)
                
            c.setStrokeColor(COLOR_BORDER)
            c.setLineWidth(0.75)
            c.rect(x_left, y_bot, col_w, row_h, fill=1, stroke=1)
            
            # Número del dia
            c.setFont("Helvetica-Bold", 11 if is_current_month else 10)
            if is_current_month:
                if is_weekend:
                    c.setFillColor(COLOR_SECONDARY)
                else:
                    c.setFillColor(COLOR_TEXT_DARK)
            else:
                c.setFillColor(COLOR_TEXT_MUTED)
                
            day_str = str(day_obj.day)
            c.drawRightString(x_right - 6, y_top - 14, day_str)
            
            # Renderitzar esdeveniments per a aquest dia
            evt_key = (day_obj.year, day_obj.month, day_obj.day)
            day_events = events.get(evt_key, [])
            
            if day_events:
                evt_y = y_top - 26
                pill_height = 14
                pill_spacing = 16
                max_evts_fit = int((row_h - 28) // pill_spacing)
                
                for ev_idx, ev in enumerate(day_events[:max_evts_fit]):
                    unit_color = get_unit_color(ev["unit"])
                    
                    # Fons de la píndola d'esdeveniment
                    c.setFillColor(unit_color)
                    c.roundRect(x_left + 4, evt_y - 2, col_w - 8, pill_height, 3, fill=1, stroke=0)
                    
                    # Text de l'esdeveniment
                    c.setFillColor(colors.white)
                    c.setFont("Helvetica-Bold", 7.5)
                    
                    display_text = ev["title"]
                    if ev["location"]:
                        display_text += f" ({ev['location']})"
                        
                    max_chars = int((col_w - 14) / 4.8)
                    if len(display_text) > max_chars:
                        display_text = display_text[:max_chars-2] + ".."
                        
                    c.drawString(x_left + 8, evt_y + 2, display_text)
                    
                    evt_y -= pill_spacing
                
                # Indicador de més esdeveniments
                if len(day_events) > max_evts_fit:
                    c.setFillColor(COLOR_TEXT_MUTED)
                    c.setFont("Helvetica-Oblique", 7)
                    c.drawString(x_left + 8, evt_y + 3, f"+ {len(day_events) - max_evts_fit} més...")

    # 3. Peu de pàgina / Banner SOP de Seguretat
    footer_y = margin_bottom
    c.setLineWidth(0.5)
    c.setStrokeColor(COLOR_BORDER)
    c.line(margin_x, footer_y + 25, page_w - margin_x, footer_y + 25)
    
    # Nota de protocol escolta
    c.setFillColor(COLOR_PRIMARY)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(margin_x, footer_y + 10, "⚠️ PROTOCOL DE SEGURETAT I PERMISOS:")
    
    c.setFillColor(COLOR_TEXT_DARK)
    c.setFont("Helvetica", 8)
    c.drawString(margin_x + 195, footer_y + 10, "T-60: Permisos d'acampada (IBANAT) | T-30: Reconèixer ruta | T-15: Menjar i pressupost | T-7: Fitxes mèdiques i 112")
    
    # Marca de peu
    c.setFillColor(COLOR_TEXT_MUTED)
    c.setFont("Helvetica", 8)
    c.drawRightString(page_w - margin_x, footer_y + 10, "Escoltes de Mallorca — Portal de Suport")

def generate_pdf_calendar(csv_path, output_pdf, logo_path, title_text, year=None, full_year=False):
    """Genera el PDF del calendari mensual a partir del CSV."""
    events = load_events_from_csv(csv_path)
    
    months_to_generate = []
    
    if full_year:
        target_year = year or datetime.now().year
        for m in range(1, 13):
            months_to_generate.append((target_year, m))
    elif events:
        # Obtenir tots els mesos que tenen esdeveniments al CSV
        evt_months = sorted(list(set((k[0], k[1]) for k in events.keys())))
        if year:
            evt_months = [m for m in evt_months if m[0] == year]
        months_to_generate = evt_months
    
    if not months_to_generate:
        # Per defecte generar el trimestre d'inici de curs (Oct, Nov, Des)
        target_year = year or datetime.now().year
        months_to_generate = [(target_year, 10), (target_year, 11), (target_year, 12)]

    c = canvas.Canvas(output_pdf, pagesize=landscape(A4))
    c.setTitle(f"{title_text}")
    c.setAuthor("Escoltes de Mallorca")
    
    print(f"=== Generant PDF Calendari Escoltes de Mallorca ===")
    print(f"• Títol: {title_text}")
    print(f"• CSV Font: {csv_path}")
    print(f"• Fitxer de Sortida: {output_pdf}")
    print(f"• Mesos a generar: {len(months_to_generate)}")

    for y, m in months_to_generate:
        draw_month_page(c, y, m, events, logo_path, title_text)
        c.showPage()

    c.save()
    print(f"[OK] El PDF s'ha generat amb èxit: {output_pdf}")

def main():
    parser = argparse.ArgumentParser(description="Generador de Calendari PDF mensual per al Grup Escolta (Escoltes de Mallorca)")
    parser.add_argument("--csv", default="data/calendari_escolta_exemple.csv", help="Ruta al fitxer CSV d'esdeveniments")
    parser.add_argument("-o", "--output", default="Calendari_Jaume_I_Verge_de_Lluc.pdf", help="Ruta del PDF de sortida")
    parser.add_argument("--logo", default="assets/logo_escoltes.png", help="Ruta al logo en PNG/JPG")
    parser.add_argument("--title", default="Calendari Jaume I i Verge de Lluc", help="Títol principal del calendari")
    parser.add_argument("--year", type=int, default=None, help="Any específic (ex: 2026)")
    parser.add_argument("--full-year", action="store_true", help="Generar els 12 mesos de l'any complet")

    args = parser.parse_args()

    generate_pdf_calendar(
        csv_path=args.csv,
        output_pdf=args.output,
        logo_path=args.logo,
        title_text=args.title,
        year=args.year,
        full_year=args.full_year
    )

if __name__ == "__main__":
    main()
