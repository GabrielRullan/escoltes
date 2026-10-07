const fs = require('fs');
const path = require('path');

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

const allHtml = getAllHtmlFiles('site/mallorca');
console.log('Total HTML files in site/mallorca:', allHtml.length);

const scriptTypes = new Set();
let totalScripts = 0;
let inlineScripts = 0;
let externalScripts = 0;

for (const file of allHtml) {
  const html = fs.readFileSync(file, 'utf8');
  const regex = /<script\b([^>]*)>([\s\S]*?)<\/script>/gi;
  let match;
  while ((match = regex.exec(html)) !== null) {
    totalScripts++;
    const attrs = match[1];
    const content = match[2].trim();
    const typeMatch = attrs.match(/type\s*=\s*["']([^"']+)["']/i);
    const scriptType = typeMatch ? typeMatch[1].toLowerCase() : 'text/javascript (default)';
    scriptTypes.add(scriptType);
    if (attrs.includes('src=')) {
      externalScripts++;
    } else {
      inlineScripts++;
    }
  }
}

console.log('Total scripts found:', totalScripts);
console.log('Inline scripts:', inlineScripts);
console.log('External scripts:', externalScripts);
console.log('Script types found:', Array.from(scriptTypes));
