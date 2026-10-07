const fs = require('fs');
const path = require('path');
const vm = require('vm');

function getAllHtmlFiles(dir) {
  let results = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results = results.concat(getAllHtmlFiles(fullPath));
    } else if (entry.isFile() && entry.name.endsWith('.html')) {
      results.push(fullPath);
    }
  }
  return results;
}

const allHtml = getAllHtmlFiles('site');
console.log('Testing all ' + allHtml.length + ' HTML files in site/ for JS syntax errors...');

let filesWithErrors = 0;
let totalInlineScriptsChecked = 0;

for (const file of allHtml) {
  const html = fs.readFileSync(file, 'utf8');
  const regex = /<script\b([^>]*)>([\s\S]*?)<\/script>/gi;
  let match;
  let hasErr = false;

  while ((match = regex.exec(html)) !== null) {
    const attrs = match[1];
    let content = match[2];
    if (/src=/i.test(attrs)) continue;
    if (/application\/json/i.test(attrs)) continue;
    if (!content.trim()) continue;

    totalInlineScriptsChecked++;
    try {
      new vm.Script(content, { filename: file });
    } catch (e) {
      if (!hasErr) {
        filesWithErrors++;
        hasErr = true;
        console.log(`FAIL: ${file} -> ${e.message}`);
      }
    }
  }
}

console.log('Total inline scripts checked:', totalInlineScriptsChecked);
console.log('Files with syntax errors:', filesWithErrors);
