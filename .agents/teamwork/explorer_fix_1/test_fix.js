// Test the fix
const vm = require('vm');

const fixedJs = `
statusMsg.innerText = "✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament.";
`;

try {
    new vm.Script(fixedJs);
    console.log("SUCCESS: Fixed JS string parses cleanly!");
} catch (e) {
    console.error("FAIL:", e.message);
}
