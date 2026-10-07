const fs = require('fs');
const path = require('path');
const vm = require('vm');

let failures = 0;
let checkedScripts = 0;

function checkFile(filePath) {
    const content = fs.readFileSync(filePath, 'utf8');
    const regex = /<script\b([^>]*)>([\s\S]*?)<\/script>/gi;
    let match;
    let index = 0;
    while ((match = regex.exec(content)) !== null) {
        index++;
        const attrs = match[1];
        const code = match[2];
        if (attrs.includes('src=') || attrs.includes('type="application/json"') || attrs.includes("type='application/json'")) {
            continue;
        }
        if (!code.trim()) continue;
        checkedScripts++;
        try {
            new vm.Script(code, { filename: `${filePath}:script_${index}` });
        } catch (e) {
            failures++;
            console.log(`FAIL: ${filePath} script ${index}: ${e.message}`);
        }
    }
}

function walk(dir) {
    for (const f of fs.readdirSync(dir)) {
        const full = path.join(dir, f);
        if (fs.statSync(full).isDirectory()) walk(full);
        else if (full.endsWith('.html')) checkFile(full);
    }
}

walk('site');
console.log(`Done. Checked scripts: ${checkedScripts}, Failures: ${failures}`);
