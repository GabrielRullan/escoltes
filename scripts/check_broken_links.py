import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def check_markdown_links():

    docs_dir = "docs"
    broken_links = []
    total_links = 0
    
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                rel_dir = os.path.dirname(file_path)
                
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                matches = link_pattern.findall(content)
                for text, target in matches:
                    # Ignore external http/https links and anchor-only links
                    if target.startswith("http://") or target.startswith("https://") or target.startswith("#") or target.startswith("mailto:"):
                        continue
                    
                    total_links += 1
                    # Strip anchor if present
                    target_path_clean = target.split("#")[0]
                    if not target_path_clean:
                        continue
                        
                    # Resolve path relative to current file's directory
                    resolved_path = os.path.normpath(os.path.join(rel_dir, target_path_clean))
                    
                    if not os.path.exists(resolved_path):
                        broken_links.append((file_path, target, resolved_path))
                        
    print(f"Comprovació finalitzada: {total_links} enllaços interns analitzats.")
    if broken_links:
        print(f"⚠️ S me S'HAN TROBAT {len(broken_links)} ENLLAÇOS ROMPUTS:")
        for source, orig, resolved in broken_links:
            print(f"  - A {source} -> enllaç '{orig}' (fitxer no trobat: {resolved})")
    else:
        print("✅ TOTS ELS ENLLAÇOS INTERNS SÓN VÀLIDS!")

if __name__ == "__main__":
    check_markdown_links()
