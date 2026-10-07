const fs = require('fs');
const vm = require('vm');

const content = fs.readFileSync('docs/mallorca/admin_comentaris.md', 'utf8');
const scriptMatches = content.match(/<script\b(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/gi);

console.log('Found scripts:', scriptMatches ? scriptMatches.length : 0);

if (scriptMatches) {
    scriptMatches.forEach((s, idx) => {
        const code = s.replace(/<script[^>]*>|<\/script>/gi, '');
        try {
            new vm.Script(code);
            console.log(`Script ${idx + 1}: SYNTAX OK`);
        } catch (e) {
            console.error(`Script ${idx + 1}: SYNTAX ERROR:`, e.message);
        }
    });
}
