const vm = require('vm');

try {
  new vm.Script('{"annotate": null}');
  console.log('Parsed successfully');
} catch (e) {
  console.log('Error parsing JSON as JS:', e.message);
}
