const fs = require('fs');
const vm = require('vm');

const content = fs.readFileSync('site/mallorca/admin_comentaris/index.html', 'utf8');
const scriptMatches = content.match(/<script\b(?![^>]*\bsrc=)(?![^>]*application\/json)[^>]*>([\s\S]*?)<\/script>/gi);

console.log('Found inline JS scripts in site index.html:', scriptMatches ? scriptMatches.length : 0);

if (scriptMatches) {
    scriptMatches.forEach((s, idx) => {
        const code = s.replace(/<script[^>]*>|<\/script>/gi, '');
        try {
            new vm.Script(code);
            console.log('Script ' + (idx + 1) + ': SYNTAX OK (len=' + code.length + ', preview=' + code.trim().slice(0, 40).replace(/\n/g, ' ') + ')');
        } catch (e) {
            console.error('Script ' + (idx + 1) + ': SYNTAX ERROR:', e.message);
        }
    });
}
