#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[ESBORRANY] Eina de Càlcul de Pressupost, Menús i Llista de la Compra per a Campaments Escoltes
Agrupament Escolta Jaume I i Verge de Lluc (Escoltes de Mallorca)

Aquest script calcula:
  1. La quantitat d'ingredients necessaris segons el nombre de participants i dies.
  2. El pressupost estimat per persona/dia i el total de la sortida.
  3. Genera un resum imprès de la llista de la compra per als responsables de cuina.
"""

import sys
import argparse

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Ràtio d'ingredients per persona i dia (en grams o unitats)
RATIONS_PER_PERSON_DAY = {
    "arròs_pasta_g": 90,           # 90g de pasta o arròs per àpat
    "llegums_secs_g": 80,          # 80g de llenties o cigrons
    "carn_peix_g": 120,            # 120g de pit de pollastre o peix
    "pa_g": 150,                   # 150g de pa diari
    "fruita_unitats": 2,           # 2 peces de fruita diàries
    "verdura_g": 200,              # 200g de verdura de temporada
    "llet_ml": 250,                # 250ml de llet pel berenar/berenar
    "oli_oliva_ml": 30             # 30ml d'oli d'oliva verge extra
}

# Preus de referència estimats a Mallorca (€/unitat o €/kg)
ESTIMATED_PRICES = {
    "arròs_pasta_g": 0.002,        # 2€/kg
    "llegums_secs_g": 0.0025,      # 2.50€/kg
    "carn_peix_g": 0.009,          # 9€/kg
    "pa_g": 0.0025,                # 2.50€/kg
    "fruita_unitats": 0.35,        # 0.35€/peça
    "verdura_g": 0.003,            # 3€/kg
    "llet_ml": 0.001,              # 1€/L
    "oli_oliva_ml": 0.008          # 8€/L
}

def calculate_budget_and_menu(num_participants, num_days, transport_cost=0.0, extra_cost=0.0):
    """Calcula els ingredients, el cost d'alimentació i el cost total per escolta."""
    total_person_days = num_participants * num_days
    
    print(f"\n=======================================================")
    print(f" [ESBORRANY] CALCULADORA DE PRESSUPOST I MENUS ESCOLTES")
    print(f" Agrupament Escolta Jaume I i Verge de Lluc")
    print(f"=======================================================")
    print(f" Participants: {num_participants} escoltes/caps")
    print(f" Durada: {num_days} dies ({total_person_days} estades/dia)")
    print(f"-------------------------------------------------------\n")
    
    print(" LLISTA DE LA COMPRA ESTIMADA (D'ALIMENTACIÓ):")
    total_food_cost = 0.0
    
    for item, qty_per_day in RATIONS_PER_PERSON_DAY.items():
        total_qty = qty_per_day * total_person_days
        unit_price = ESTIMATED_PRICES.get(item, 0.0)
        cost = total_qty * unit_price
        total_food_cost += cost
        
        unit_label = "g"
        display_qty = total_qty
        if "ml" in item:
            unit_label = "ml"
            if total_qty >= 1000:
                display_qty = total_qty / 1000.0
                unit_label = "L"
        elif "g" in item:
            if total_qty >= 1000:
                display_qty = total_qty / 1000.0
                unit_label = "kg"
        elif "unitats" in item:
            unit_label = "unitats"

        item_name = item.replace("_g", "").replace("_ml", "").replace("_unitats", "").replace("_", " ").title()
        print(f" • {item_name:<20}: {display_qty:>7.2f} {unit_label:<4}  (~{cost:>6.2f} €)")

    food_cost_per_person = total_food_cost / num_participants
    transport_per_person = transport_cost / num_participants
    extra_per_person = extra_cost / num_participants
    
    total_event_cost = total_food_cost + transport_cost + extra_cost
    total_per_person = total_event_cost / num_participants
    
    print(f"\n-------------------------------------------------------")
    print(f" RESUM FINANCER DEL CAMPAMENT / SORTIDA:")
    print(f" • Cost Alimentació Total : {total_food_cost:>8.2f} €  ({food_cost_per_person:.2f} € / escolta)")
    print(f" • Cost Transport (Bus/Tren): {transport_cost:>8.2f} €  ({transport_per_person:.2f} € / escolta)")
    print(f" • Costos Extres (Permisos): {extra_cost:>8.2f} €  ({extra_per_person:.2f} € / escolta)")
    print(f" ------------------------------------------------------")
    print(f" QUOTA RECOMANADA PER ESCOLTA: {total_per_person:>6.2f} €")
    print(f"=======================================================\n")

def main():
    parser = argparse.ArgumentParser(description="Calculadora de Pressupost i Menús per a Campaments Escoltes")
    parser.add_argument("-p", "--participants", type=int, default=25, help="Nombre total d'escoltes i caps")
    parser.add_argument("-d", "--days", type=int, default=2, help="Nombre de dies de la sortida/campament")
    parser.add_argument("-t", "--transport", type=float, default=150.0, help="Cost total de transport col·lectiu (€)")
    parser.add_argument("-e", "--extra", type=float, default=30.0, help="Costos extres com material o permís (€)")
    
    args = parser.parse_args()
    calculate_budget_and_menu(args.participants, args.days, args.transport, args.extra)

if __name__ == "__main__":
    main()
