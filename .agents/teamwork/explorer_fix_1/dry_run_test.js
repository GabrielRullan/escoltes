const fs = require('fs');
const vm = require('vm');

const sampleFile = 'site/mallorca/rutes/gr221-etapa-1-port-andratx-trapa/index.html';
const content = fs.readFileSync(sampleFile, 'utf8');

// Replace the broken line with the fixed line
const brokenLine = "statusMsg.innerText = '✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament.';";
const fixedLine = 'statusMsg.innerText = "✅ Comentari enviat amb èxit! Està pendent d\'autorització per part de l\'administrador per ser visible públicament.";';

if (!content.includes(brokenLine)) {
    console.error("Could not find broken line in sample file!");
    process.exit(1);
}

const fixedContent = content.replace(brokenLine, fixedLine);

// Extract all inline JS scripts and test them
const regex = /<script\b([^>]*)>([\s\S]*?)<\/script>/gi;
let match;
let index = 0;
let errors = 0;

while ((match = regex.exec(fixedContent)) !== null) {
    index++;
    const attrs = match[1];
    const code = match[2];
    if (attrs.includes('src=') || attrs.includes('type="application/json"') || attrs.includes("type='application/json'")) {
        continue;
    }
    if (!code.trim()) continue;
    try {
        new vm.Script(code, { filename: `script_${index}` });
        console.log(`Script ${index}: PASSED clean JS compile`);
    } catch (e) {
        errors++;
        console.error(`Script ${index}: FAILED - ${e.message}`);
    }
}

console.log(`Test complete. Errors: ${errors}`);
