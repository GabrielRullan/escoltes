const fs = require('fs');
const path = require('path');
const vm = require('vm');

const rutesDir = path.resolve('site/mallorca/rutes');
const entries = fs.readdirSync(rutesDir, { withFileTypes: true });
const routeDirs = entries.filter(e => e.isDirectory()).map(e => e.name);

console.log('Testing hypothetical fix across all 65 route directories...');

const brokenLine = "statusMsg.innerText = '✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament.';";
const fixedLine = 'statusMsg.innerText = "✅ Comentari enviat amb èxit! Està pendent d\'autorització per part de l\'administrador per ser visible públicament.";';

let totalTested = 0;
let totalPassed = 0;
let totalFailed = 0;
const failures = [];

for (const dir of routeDirs) {
  const file = path.join(rutesDir, dir, 'index.html');
  const html = fs.readFileSync(file, 'utf8');
  const regex = /<script\b([^>]*)>([\s\S]*?)<\/script>/gi;
  let match;
  let scriptIndex = 0;
  let fileOk = true;

  while ((match = regex.exec(html)) !== null) {
    const attrs = match[1];
    let content = match[2];
    scriptIndex++;

    if (/src\s*=/i.test(attrs)) continue;

    const typeMatch = attrs.match(/type\s*=\s*["']([^"']+)["']/i);
    if (typeMatch && typeMatch[1].toLowerCase() === 'application/json') continue;
    if (!content.trim()) continue;

    // Apply the fix
    content = content.replace(brokenLine, fixedLine);

    try {
      new vm.Script(content, { filename: 'route/' + dir + '#script' + scriptIndex });
    } catch (err) {
      fileOk = false;
      failures.push({
        dir,
        scriptIndex,
        error: err.message
      });
    }
  }

  totalTested++;
  if (fileOk) {
    totalPassed++;
  } else {
    totalFailed++;
  }
}

console.log('Results with fix applied:');
console.log('Routes tested:', totalTested);
console.log('Routes passed:', totalPassed);
console.log('Routes failed:', totalFailed);
if (failures.length > 0) {
  console.log('Failures:', JSON.stringify(failures, null, 2));
} else {
  console.log('ALL 65 ROUTES PASS 100% CLEANLY WITH THE QUOTING FIX APPLIED!');
}
