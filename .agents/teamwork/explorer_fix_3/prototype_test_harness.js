const fs = require('fs');
const path = require('path');
const vm = require('vm');

const rutesDir = path.resolve('site/mallorca/rutes');
const adminFile = path.resolve('site/mallorca/admin_comentaris/index.html');

const entries = fs.readdirSync(rutesDir, { withFileTypes: true });
const routeDirs = entries.filter(e => e.isDirectory()).map(e => e.name);

console.log('Testing ' + routeDirs.length + ' route directories...');

const results = {
  routesTested: 0,
  routesFailed: 0,
  routesPassed: 0,
  adminPassed: false,
  errors: []
};

function testHtmlFile(filePath, label) {
  if (!fs.existsSync(filePath)) {
    return { ok: false, error: 'File not found: ' + filePath };
  }
  const html = fs.readFileSync(filePath, 'utf8');
  const regex = /<script\b([^>]*)>([\s\S]*?)<\/script>/gi;
  let match;
  let scriptIndex = 0;
  let fileOk = true;
  const fileErrors = [];

  while ((match = regex.exec(html)) !== null) {
    const attrs = match[1];
    const content = match[2];
    scriptIndex++;

    // Skip external scripts
    if (/src\s*=/i.test(attrs)) continue;

    // Skip JSON data scripts
    const typeMatch = attrs.match(/type\s*=\s*["']([^"']+)["']/i);
    if (typeMatch && typeMatch[1].toLowerCase() === 'application/json') {
      try {
        JSON.parse(content);
      } catch (err) {
        fileOk = false;
        fileErrors.push({ scriptIndex, error: 'Invalid JSON: ' + err.message });
      }
      continue;
    }

    // Skip empty inline scripts
    if (!content.trim()) continue;

    // Test JavaScript syntax with vm.Script
    try {
      new vm.Script(content, { filename: label + '#script' + scriptIndex });
    } catch (err) {
      fileOk = false;
      fileErrors.push({
        scriptIndex,
        error: err.message,
        snippet: content.split('\n').slice(Math.max(0, (err.lineNumber || 1) - 3), (err.lineNumber || 1) + 2).join('\n')
      });
    }
  }

  return { ok: fileOk, errors: fileErrors };
}

// Test routes
for (const dir of routeDirs) {
  const file = path.join(rutesDir, dir, 'index.html');
  results.routesTested++;
  const res = testHtmlFile(file, 'route/' + dir);
  if (res.ok) {
    results.routesPassed++;
  } else {
    results.routesFailed++;
    results.errors.push({ label: 'route/' + dir, errors: res.errors });
  }
}

// Test admin
const adminRes = testHtmlFile(adminFile, 'admin_comentaris');
results.adminPassed = adminRes.ok;
if (!adminRes.ok) {
  results.errors.push({ label: 'admin_comentaris', errors: adminRes.errors });
}

console.log('Results summary:');
console.log('Routes tested:', results.routesTested);
console.log('Routes passed:', results.routesPassed);
console.log('Routes failed:', results.routesFailed);
console.log('Admin passed:', results.adminPassed);
if (results.errors.length > 0) {
  console.log('\nSample error from first failed route (' + results.errors[0].label + '):');
  console.log(JSON.stringify(results.errors[0].errors, null, 2));
}
