const fs = require('fs');

function inspectScripts(file) {
  console.log('=== File:', file, '===');
  if (!fs.existsSync(file)) {
    console.log('File does not exist:', file);
    return;
  }
  const html = fs.readFileSync(file, 'utf8');
  const regex = /<script\b([^>]*)>([\s\S]*?)<\/script>/gi;
  let match;
  let idx = 0;
  while ((match = regex.exec(html)) !== null) {
    const attrs = match[1].trim();
    const content = match[2];
    console.log('Script [' + idx + '] attrs: "' + attrs + '", content length: ' + content.length + ', content snippet: ' + JSON.stringify(content.trim().slice(0, 60)));
    idx++;
  }
}

inspectScripts('site/mallorca/rutes/es-salt-des-freu-orient/index.html');
inspectScripts('site/mallorca/admin_comentaris/index.html');
inspectScripts('site/mallorca/rutes/index.html');
