const fs = require('fs');

const content = fs.readFileSync('scripts/build_wiki_pages.py', 'utf8');
const lines = content.split('\n');

console.log('--- Searching for \\\' in scripts/build_wiki_pages.py ---');
lines.forEach((line, idx) => {
    if (line.includes("\\'")) {
        console.log(`Line ${idx + 1}: ${line}`);
    }
});

console.log('--- Searching for apostrophes in lines that look like JS code ---');
let inScript = false;
lines.forEach((line, idx) => {
    if (line.includes('<script>')) inScript = true;
    if (line.includes('</script>')) inScript = false;
    if (inScript) {
        // Look for Catalan contractions
        if (/([dlstmn]['’][a-zA-ZÀ-ÿ])/i.test(line)) {
            console.log(`Script Line ${idx + 1}: ${line}`);
        }
    }
});
