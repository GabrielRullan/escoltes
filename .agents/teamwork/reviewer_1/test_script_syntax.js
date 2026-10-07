const fs = require('fs');

const html = fs.readFileSync('site/mallorca/rutes/es-salt-des-freu-orient/index.html', 'utf8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/g);

console.log('Total scripts found:', scriptMatch.length);

for (let i = 0; i < scriptMatch.length; i++) {
    const raw = scriptMatch[i].replace(/<\/?script>/g, '');
    try {
        new Function(raw);
        console.log(`Script ${i}: OK`);
    } catch (e) {
        console.log(`Script ${i}: SYNTAX ERROR -> ${e.message}`);
    }
}

// Test with the fix applied:
let script3 = scriptMatch[3].replace(/<\/?script>/g, '');
const brokenLine = "statusMsg.innerText = '✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament.';";
const fixedLine = 'statusMsg.innerText = "✅ Comentari enviat amb èxit! Està pendent d\'autorització per part de l\'administrador per ser visible públicament.";';

if (script3.includes(brokenLine)) {
    console.log('Confirmed: script3 contains the exact broken line with unescaped single quotes!');
    const fixedScript3 = script3.replace(brokenLine, fixedLine);
    try {
        new Function(fixedScript3);
        console.log('With fix applied: Script 3 parses completely cleanly!');
    } catch (e) {
        console.log('With fix applied, secondary error:', e.message);
    }
} else {
    console.log('Could not find broken line directly.');
}
