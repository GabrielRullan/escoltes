# Test Python f-string rendering
def render_snippet():
    return f"""
    statusMsg.innerText = "✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament.";
    """

rendered = render_snippet()
print("Rendered snippet:")
print(rendered)
assert 'statusMsg.innerText = "✅ Comentari enviat amb èxit! Està pendent d\'autorització per part de l\'administrador per ser visible públicament.";' in rendered
print("Assertion passed!")
