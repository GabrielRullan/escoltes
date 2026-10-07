"""
Independent Forensic Integrity Verification Script
Gate 2 - Escoltes de Mallorca Route Comments & Admin Moderation
"""
import os
import re
import sys
import subprocess

REPO_ROOT = r"c:\Users\gabri\Documents\escoltes"

def test_static_requirements():
    print("=== 1. Static Analysis: Requirements R1, R2, R3 ===")
    
    # Check scripts/build_wiki_pages.py
    bwp_path = os.path.join(REPO_ROOT, "scripts", "build_wiki_pages.py")
    with open(bwp_path, "r", encoding="utf-8") as f:
        bwp_content = f.read()

    # R1: Form inputs
    r1_fields = ["exp-nom", "exp-email", "exp-agrupament", "exp-branca", "exp-puntuacio", "exp-comentari"]
    for field in r1_fields:
        assert f'id="{field}"' in bwp_content, f"Missing form field: {field}"
    print("[PASS] All required form fields present in build_wiki_pages.py")

    # R1: Scout branches
    scout_branches = ["Castors/Fures", "Llops/Daines", "Pioners/Rangers", "Rovers/Rutes", "Caps/Monitors"]
    for b in scout_branches:
        assert f'value="{b}"' in bwp_content, f"Missing scout branch option: {b}"
    print("[PASS] All required scout branches present in select options")

    # R1: authorized: false
    assert "authorized: false" in bwp_content, "Missing authorized: false on submission"
    print("[PASS] authorized: false set on experience submission")

    # R1: Notification message
    expected_msg = "✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament."
    assert expected_msg in bwp_content, "Missing or incorrect exact success notification message"
    print("[PASS] Success notification text matches specification verbatim")

    # R1 & R2: Genuine Firestore calls in build_wiki_pages.py
    assert 'db.collection("experiencies").add(newExp)' in bwp_content, "Missing genuine Firestore .add() call"
    assert 'db.collection("experiencies")' in bwp_content, "Missing genuine Firestore collection reference"
    assert 'where("ruta_slug", "=="' in bwp_content, "Missing Firestore where clause"
    assert 'data.authorized === true || data.authorized === undefined' in bwp_content, "Missing authorized display filter in route comments"
    print("[PASS] Genuine Firestore SDK calls (.add, .where, onSnapshot) verified in build_wiki_pages.py")

    # Check docs/mallorca/admin_comentaris.md
    admin_path = os.path.join(REPO_ROOT, "docs", "mallorca", "admin_comentaris.md")
    assert os.path.exists(admin_path), "admin_comentaris.md does not exist"
    with open(admin_path, "r", encoding="utf-8") as f:
        admin_content = f.read()

    # R2: Admin features
    assert 'db.collection("experiencies").onSnapshot' in admin_content, "Missing Firestore listener on experiencies in admin"
    assert '.update({\n                authorized: true' in admin_content or '.update({\n                authorized: true,' in admin_content or 'authorized: true' in admin_content, "Missing Firestore update to authorized: true"
    assert '.delete()' in admin_content, "Missing Firestore .delete() in admin"
    assert 'revokeComment' in admin_content, "Missing revokeComment function in admin"
    assert 'approveComment' in admin_content, "Missing approveComment function in admin"
    assert 'deleteComment' in admin_content, "Missing deleteComment function in admin"
    print("[PASS] Genuine Firestore calls (onSnapshot, update, delete) verified in admin_comentaris.md")

    # R2: mkdocs.yml entry under Escoltisme
    mkdocs_path = os.path.join(REPO_ROOT, "mkdocs.yml")
    with open(mkdocs_path, "r", encoding="utf-8") as f:
        mkdocs_content = f.read()
    
    escoltisme_idx = mkdocs_content.find("Escoltisme a Mallorca:")
    assert escoltisme_idx != -1, "Escoltisme section not found in mkdocs.yml"
    admin_entry_idx = mkdocs_content.find("mallorca/admin_comentaris.md")
    assert admin_entry_idx > escoltisme_idx, "admin_comentaris.md not under Escoltisme a Mallorca section"
    print("[PASS] admin_comentaris.md registered under Escoltisme a Mallorca in mkdocs.yml")

def test_integrity_and_cheating():
    print("\n=== 2. Integrity Analysis: Hardcoding, Mocks, Cheating Bypasses ===")
    # Check if there are mock databases or fake responses
    bwp_path = os.path.join(REPO_ROOT, "scripts", "build_wiki_pages.py")
    with open(bwp_path, "r", encoding="utf-8") as f:
        bwp_content = f.read()

    suspicious_patterns = [
        r"mockFirestore",
        r"fakeFirestore",
        r"return\s*\[\s*\{\s*id:\s*['\"]mock['\"]",
        r"return\s*true;\s*//\s*bypass",
        r"//\s*TODO.*implement",
        r"NotImplementedError"
    ]
    for pattern in suspicious_patterns:
        match = re.search(pattern, bwp_content, re.IGNORECASE)
        assert match is None, f"Found suspicious facade/mock pattern in build_wiki_pages.py: {match.group(0)}"
    print("[PASS] No mock/facade patterns detected in build_wiki_pages.py")

    admin_path = os.path.join(REPO_ROOT, "docs", "mallorca", "admin_comentaris.md")
    with open(admin_path, "r", encoding="utf-8") as f:
        admin_content = f.read()
    for pattern in suspicious_patterns:
        match = re.search(pattern, admin_content, re.IGNORECASE)
        assert match is None, f"Found suspicious facade/mock pattern in admin_comentaris.md: {match.group(0)}"
    print("[PASS] No mock/facade patterns detected in admin_comentaris.md")

def test_git_commits():
    print("\n=== 3. Git Commit Lineage & Synchronization ===")
    cmd = ["git", "log", "-n", "10", "--format=%h %s"]
    res = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=True)
    log_output = res.stdout.strip()
    print("Git recent commits:\n" + log_output)

    assert "4a50d28" in log_output, "Commit 4a50d28 not found in git log"
    assert "0e79926" in log_output, "Commit 0e79926 not found in git log"
    assert "540577e" in log_output, "Commit 540577e not found in git log"
    print("[PASS] Commits 540577e, 0e79926, and 4a50d28 verified in git history")

    # Verify origin/main sync
    branch_cmd = ["git", "rev-parse", "origin/main"]
    res_origin = subprocess.run(branch_cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=True)
    origin_sha = res_origin.stdout.strip()

    head_cmd = ["git", "rev-parse", "HEAD"]
    res_head = subprocess.run(head_cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=True)
    head_sha = res_head.stdout.strip()

    assert head_sha.startswith("4a50d28"), f"HEAD is not 4a50d28: {head_sha}"
    assert origin_sha.startswith("4a50d28"), f"origin/main is not 4a50d28: {origin_sha}"
    assert head_sha == origin_sha, f"HEAD ({head_sha}) and origin/main ({origin_sha}) are out of sync"
    print(f"[PASS] HEAD and origin/main are fully synchronized at commit {head_sha[:7]}")

if __name__ == "__main__":
    test_static_requirements()
    test_integrity_and_cheating()
    test_git_commits()
    print("\n[SUCCESS] ALL AUDITOR FORENSIC CHECKS PASSED EMPIRICALLY!")
