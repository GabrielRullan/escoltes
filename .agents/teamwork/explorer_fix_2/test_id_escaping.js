function escapeHtml(text) {
    if (!text) return '';
    return String(text)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

const testIds = [
    "normalId12345",
    "id-with-dash_and_under",
    "id'with'quote",
    "id\"with\"doublequote",
    "id<with>html"
];

testIds.forEach(id => {
    const escaped = escapeHtml(id);
    const htmlSnippet = `<button onclick="deleteComment('${escaped}')">Esborrar</button>`;
    console.log(`Original: [${id}]`);
    console.log(`Rendered HTML: ${htmlSnippet}`);
});
