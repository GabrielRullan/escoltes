#!/usr/bin/env python3
"""
Independent Victory Verification Script
Victory Auditor 1
"""
import os
import sys
import glob
import json
import subprocess

def run_checks():
    base_dir = r"c:\Users\gabri\Documents\escoltes"
    results = {}
    
    print("=== INITIATING INDEPENDENT VICTORY AUDIT CHECKS ===")

    # Check 1: R1 Form fields in scripts/build_wiki_pages.py
    build_wiki_py = os.path.join(base_dir, "scripts", "build_wiki_pages.py")
    with open(build_wiki_py, "r", encoding="utf-8") as f:
        wiki_code = f.read()

    r1_fields = [
        ('id="exp-nom"', "Nom field"),
        ('id="exp-email"', "Email field"),
        ('id="exp-agrupament"', "Agrupament field"),
        ('id="exp-branca"', "Branca field"),
        ('id="exp-puntuacio"', "Puntuacio field"),
        ('id="exp-comentari"', "Comentari field"),
        ('Castors/Fures', "Branca Castors/Fures"),
        ('Llops/Daines', "Branca Llops/Daines"),
        ('Pioners/Rangers', "Branca Pioners/Rangers"),
        ('Rovers/Rutes', "Branca Rovers/Rutes"),
        ('Caps/Monitors', "Branca Caps/Monitors"),
        ('authorized: false', "Authorized false flag"),
        ('"experiencies"', "Firestore collection"),
        ("✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament.", "Exact notification message")
    ]
    
    r1_missing = []
    for snippet, label in r1_fields:
        if snippet not in wiki_code:
            r1_missing.append(label)
    
    results['R1_source_fields'] = (len(r1_missing) == 0, r1_missing)

    # Check 2: All 65 markdown route files generated in docs/mallorca/rutes/
    route_files = glob.glob(os.path.join(base_dir, "docs", "mallorca", "rutes", "*.md"))
    results['route_files_count'] = len(route_files)
    
    expected_msg = "✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament."
    routes_missing_msg = []
    for rf in route_files:
        with open(rf, "r", encoding="utf-8") as f:
            content = f.read()
            if expected_msg not in content:
                routes_missing_msg.append(os.path.basename(rf))
    
    results['routes_with_notification'] = (len(routes_missing_msg) == 0, routes_missing_msg)

    # Check 3: R2 Public Filtering in build_wiki_pages.py
    r2_public_checks = [
        ('data.authorized === true || data.authorized === undefined', "Public authorization filter")
    ]
    r2_pub_missing = [lbl for snip, lbl in r2_public_checks if snip not in wiki_code]
    results['R2_public_filter'] = (len(r2_pub_missing) == 0, r2_pub_missing)

    # Check 4: R2 Admin page docs/mallorca/admin_comentaris.md
    admin_md = os.path.join(base_dir, "docs", "mallorca", "admin_comentaris.md")
    admin_exists = os.path.exists(admin_md)
    admin_missing = []
    if admin_exists:
        with open(admin_md, "r", encoding="utf-8") as f:
            admin_code = f.read()
        
        admin_checks = [
            ('firebase.initializeApp', "Firebase init"),
            ('db.collection("experiencies").onSnapshot', "Realtime listener"),
            ('authorized === true', "Approved condition"),
            ('authorized: false', "Pending condition"),
            ('approveComment', "Approve function"),
            ('authorized: true', "Approve sets authorized true"),
            ('deleteComment', "Delete function"),
            ('.delete()', "Delete calls doc.delete()"),
            ('revokeComment', "Revoke function"),
            ('escapeHtml', "XSS escaping function")
        ]
        for snip, lbl in admin_checks:
            if snip not in admin_code:
                admin_missing.append(lbl)
    
    results['R2_admin_page'] = (admin_exists and len(admin_missing) == 0, admin_missing)

    # Check 5: mkdocs.yml registration
    mkdocs_yml = os.path.join(base_dir, "mkdocs.yml")
    with open(mkdocs_yml, "r", encoding="utf-8") as f:
        mkdocs_content = f.read()
    
    registered = "mallorca/admin_comentaris.md" in mkdocs_content
    results['mkdocs_registration'] = registered

    # Check 6: Built files in site/
    site_admin = os.path.join(base_dir, "site", "mallorca", "admin_comentaris", "index.html")
    results['site_admin_exists'] = os.path.exists(site_admin)
    site_routes = glob.glob(os.path.join(base_dir, "site", "mallorca", "rutes", "*", "index.html"))
    results['site_routes_count'] = len(site_routes)

    # Print summary
    print("\n--- RESULTS ---")
    for k, v in results.items():
        print(f"  {k}: {v}")

    all_pass = (
        results['R1_source_fields'][0] and
        results['route_files_count'] == 65 and
        results['routes_with_notification'][0] and
        results['R2_public_filter'][0] and
        results['R2_admin_page'][0] and
        results['mkdocs_registration'] and
        results['site_admin_exists'] and
        results['site_routes_count'] == 65
    )
    
    print(f"\nOVERALL VICTORY STATUS: {'ALL CHECKS PASSED' if all_pass else 'CHECKS FAILED'}")
    return 0 if all_pass else 1

if __name__ == "__main__":
    sys.exit(run_checks())
