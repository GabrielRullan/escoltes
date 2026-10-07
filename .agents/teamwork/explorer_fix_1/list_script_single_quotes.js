const fs = require('fs');

const content = fs.readFileSync('scripts/build_wiki_pages.py', 'utf8');
const lines = content.split('\n');

let inScript = false;
lines.forEach((line, idx) => {
    if (line.includes('<script>')) inScript = true;
    if (line.includes('</script>')) inScript = false;
    if (inScript && line.includes("'")) {
        console.log(`Line ${idx + 1}: ${line}`);
    }
});
