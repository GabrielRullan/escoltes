#!/usr/bin/env node
/**
 * Test Harness & Specification Verifier
 * Escoltes de Mallorca — Route Comments & Admin Moderation Interface
 * 
 * Verifies:
 * 1. JavaScript syntax integrity across all generated HTML files in `site/mallorca/rutes/<slug>/index.html` (65 routes)
 *    and `site/mallorca/admin_comentaris/index.html`.
 * 2. Contract compliance with ORIGINAL_REQUEST.md (form fields, scout branches, containers, SDK tags, handlers).
 * 3. MkDocs config JSON validity.
 * 4. Zero runtime syntax errors.
 * 
 * Usage:
 *   node .agents/teamwork/explorer_fix_3/verify_site.js               # Run standard verification suite
 *   node .agents/teamwork/explorer_fix_3/verify_site.js --all         # Check all 134+ site HTML files
 *   node .agents/teamwork/explorer_fix_3/verify_site.js --simulate-fix # Test harness with simulated fix
 *   node .agents/teamwork/explorer_fix_3/verify_site.js --verbose     # Detailed logging
 */

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const PROJECT_ROOT = path.resolve(__dirname, '../../..');
const SITE_DIR = path.join(PROJECT_ROOT, 'site/mallorca');
const ROUTES_DIR = path.join(SITE_DIR, 'rutes');
const ADMIN_FILE = path.join(SITE_DIR, 'admin_comentaris', 'index.html');
const ROUTES_INDEX = path.join(ROUTES_DIR, 'index.html');

// CLI Flags
const ARGS = process.argv.slice(2);
const VERBOSE = ARGS.includes('--verbose') || ARGS.includes('-v');
const CHECK_ALL = ARGS.includes('--all');
const ROUTES_ONLY = ARGS.includes('--routes-only');
const ADMIN_ONLY = ARGS.includes('--admin-only');
const SIMULATE_FIX = ARGS.includes('--simulate-fix');

// Specification Constants from ORIGINAL_REQUEST.md
const EXPECTED_ROUTE_COUNT = 65;

const REQUIRED_SCOUT_BRANCHES = [
  'Castors/Fures',
  'Llops/Daines',
  'Pioners/Rangers',
  'Rovers/Rutes',
  'Caps/Monitors'
];

const REQUIRED_FORM_FIELDS = [
  'exp-nom',
  'exp-email',
  'exp-branca',
  'exp-agrupament',
  'exp-puntuacio',
  'exp-comentari'
];

const REQUIRED_ROUTE_CONTAINERS = [
  'exp-form-container',
  'toggle-exp-form-btn',
  'exp-submit-btn',
  'exp-status-msg',
  'experiences-list-container'
];

const REQUIRED_ROUTE_HANDLERS = [
  'initFirebaseExperiences',
  'toggleExpForm',
  'submitFirebaseExperience',
  'renderExperiencesList',
  'escapeHtml'
];

const REQUIRED_ADMIN_CONTAINERS = [
  'admin-panel-container',
  'pending-comments-list',
  'approved-comments-list',
  'pending-count-badge',
  'approved-count-badge'
];

const REQUIRED_ADMIN_HANDLERS = [
  'initAdminComments',
  'approveComment',
  'revokeComment',
  'deleteComment',
  'renderPendingComments',
  'renderApprovedComments',
  'escapeHtml'
];

const SUCCESS_NOTIFICATION_TEXT = "✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament.";

class SiteVerifier {
  constructor() {
    this.totalRoutes = 0;
    this.passedRoutes = 0;
    this.failedRoutes = 0;
    this.totalScriptsTested = 0;
    this.totalJsonTested = 0;
    this.totalExternalScripts = 0;
    this.syntaxErrors = [];
    this.contractErrors = [];
    this.adminPassed = true;
    this.adminErrors = [];
    this.startTime = Date.now();
  }

  logVerbose(msg) {
    if (VERBOSE) console.log(`  [VERBOSE] ${msg}`);
  }

  validateHtmlScripts(filePath, label) {
    const html = fs.readFileSync(filePath, 'utf8');
    const scriptRegex = /<script\b([^>]*)>([\s\S]*?)<\/script>/gi;
    let match;
    let scriptIdx = 0;
    const errors = [];

    while ((match = scriptRegex.exec(html)) !== null) {
      scriptIdx++;
      const attrs = match[1];
      let content = match[2];

      // External scripts
      if (/src\s*=/i.test(attrs)) {
        this.totalExternalScripts++;
        this.logVerbose(`${label} Script #${scriptIdx} [EXTERNAL] -> ${attrs}`);
        continue;
      }

      // JSON data scripts (e.g. MkDocs configuration)
      const typeMatch = attrs.match(/type\s*=\s*["']([^"']+)["']/i);
      if (typeMatch && typeMatch[1].toLowerCase() === 'application/json') {
        this.totalJsonTested++;
        try {
          JSON.parse(content);
          this.logVerbose(`${label} Script #${scriptIdx} [JSON OK]`);
        } catch (e) {
          errors.push({
            scriptIdx,
            type: 'JSON Syntax Error',
            message: e.message
          });
        }
        continue;
      }

      // Empty inline scripts
      if (!content.trim()) continue;

      this.totalScriptsTested++;

      // If simulated fix is requested, replace the known broken string literal
      if (SIMULATE_FIX) {
        content = content.replace(
          "statusMsg.innerText = '✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament.';",
          'statusMsg.innerText = "✅ Comentari enviat amb èxit! Està pendent d\'autorització per part de l\'administrador per ser visible públicament.";'
        );
      }

      // Validate JavaScript Syntax using vm.Script
      try {
        new vm.Script(content, { filename: `${label}#script${scriptIdx}` });
        this.logVerbose(`${label} Script #${scriptIdx} [JS OK] (${content.length} bytes)`);
      } catch (e) {
        const lines = content.split('\n');
        const errLineNo = e.lineNumber || 1;
        const start = Math.max(0, errLineNo - 3);
        const end = Math.min(lines.length, errLineNo + 2);
        const context = lines.slice(start, end).map((l, i) => `${start + i + 1}: ${l}`).join('\n');

        errors.push({
          scriptIdx,
          type: 'JavaScript Syntax Error',
          message: e.message,
          line: errLineNo,
          context
        });
      }
    }

    return errors;
  }

  validateRouteContract(filePath, routeSlug) {
    const html = fs.readFileSync(filePath, 'utf8');
    const errors = [];

    // 1. Required form fields
    for (const fieldId of REQUIRED_FORM_FIELDS) {
      if (!html.includes(`id="${fieldId}"`)) {
        errors.push(`Missing form field: id="${fieldId}"`);
      }
    }

    // 2. Required scout branches
    for (const branch of REQUIRED_SCOUT_BRANCHES) {
      if (!html.includes(branch)) {
        errors.push(`Missing scout branch option: "${branch}"`);
      }
    }

    // 3. Required UI containers
    for (const containerId of REQUIRED_ROUTE_CONTAINERS) {
      if (!html.includes(`id="${containerId}"`)) {
        errors.push(`Missing UI container: id="${containerId}"`);
      }
    }

    // 4. Required JavaScript handlers
    for (const handler of REQUIRED_ROUTE_HANDLERS) {
      if (!html.includes(handler)) {
        errors.push(`Missing route handler function: "${handler}"`);
      }
    }

    // 5. Route slug binding
    if (!html.includes(`const routeSlug = "${routeSlug}"`)) {
      errors.push(`Missing or mismatched routeSlug binding for "${routeSlug}"`);
    }

    // 6. Nearest Agrupaments section
    if (!html.includes('Agrupaments Escoltes') && !html.includes('agrupaments/')) {
      errors.push('Missing Nearest Agrupaments Escoltes section or links');
    }

    // 7. Authorization logic checks
    if (!html.includes('authorized: false')) {
      errors.push('Missing "authorized: false" on submission');
    }
    if (!html.includes('authorized === true')) {
      errors.push('Missing "authorized === true" filter for public display');
    }

    // 8. Firebase SDK dependencies
    if (!html.includes('firebase-app-compat.js') || !html.includes('firebase-firestore-compat.js')) {
      errors.push('Missing Firebase SDK script tags');
    }

    return errors;
  }

  validateAdminContract(filePath) {
    const html = fs.readFileSync(filePath, 'utf8');
    const errors = [];

    // 1. Required UI containers
    for (const id of REQUIRED_ADMIN_CONTAINERS) {
      if (!html.includes(`id="${id}"`)) {
        errors.push(`Admin page missing container: id="${id}"`);
      }
    }

    // 2. Required handlers
    for (const handler of REQUIRED_ADMIN_HANDLERS) {
      if (!html.includes(handler)) {
        errors.push(`Admin page missing handler: "${handler}"`);
      }
    }

    // 3. Authorization state transitions
    if (!html.includes('authorized: true') || !html.includes('authorized: false')) {
      errors.push('Admin page missing authorization state toggling logic');
    }

    // 4. Firebase SDK dependencies
    if (!html.includes('firebase-app-compat.js') || !html.includes('firebase-firestore-compat.js')) {
      errors.push('Admin page missing Firebase SDK script tags');
    }

    return errors;
  }

  runAllHtmlScan() {
    console.log('\n--- SCANNING ALL SITE HTML FILES FOR JS SYNTAX INTEGRITY ---');
    function getAllHtml(dir) {
      let results = [];
      const entries = fs.readdirSync(dir, { withFileTypes: true });
      for (const entry of entries) {
        const full = path.join(dir, entry.name);
        if (entry.isDirectory()) results = results.concat(getAllHtml(full));
        else if (entry.isFile() && entry.name.endsWith('.html')) results.push(full);
      }
      return results;
    }

    const allFiles = getAllHtml(path.join(PROJECT_ROOT, 'site'));
    console.log(`Found ${allFiles.length} total HTML files across site/`);

    let syntaxFails = 0;
    for (const file of allFiles) {
      const rel = path.relative(PROJECT_ROOT, file);
      const errs = this.validateHtmlScripts(file, rel);
      if (errs.length > 0) {
        syntaxFails++;
        console.log(`  ❌ ${rel} -> ${errs[0].message}`);
      }
    }

    console.log(`All-HTML Scan complete: ${allFiles.length - syntaxFails}/${allFiles.length} files completely clean.`);
  }

  run() {
    console.log('================================================================');
    console.log('   ESCOLTES DE MALLORCA — AUTOMATED SITE VERIFICATION HARNESS   ');
    console.log('================================================================');
    if (SIMULATE_FIX) console.log('MODE: [SIMULATE-FIX] Evaluating fix in-memory (dry run)\n');

    let allOk = true;

    // 1. Verify 65 Route Pages
    if (!ADMIN_ONLY) {
      if (!fs.existsSync(ROUTES_DIR)) {
        console.error(`FATAL: Routes directory does not exist: ${ROUTES_DIR}`);
        return false;
      }

      const entries = fs.readdirSync(ROUTES_DIR, { withFileTypes: true });
      const routeDirs = entries.filter(e => e.isDirectory()).map(e => e.name);
      this.totalRoutes = routeDirs.length;

      console.log(`Discovered ${this.totalRoutes} route directories (Expected: ${EXPECTED_ROUTE_COUNT})`);
      if (this.totalRoutes !== EXPECTED_ROUTE_COUNT) {
        console.warn(`⚠️ Warning: Route count is ${this.totalRoutes}, expected ${EXPECTED_ROUTE_COUNT}`);
      }

      for (const slug of routeDirs) {
        const routeHtml = path.join(ROUTES_DIR, slug, 'index.html');
        if (!fs.existsSync(routeHtml)) {
          this.failedRoutes++;
          this.contractErrors.push({ route: slug, errors: ['Missing index.html file'] });
          continue;
        }

        const syntaxErrs = this.validateHtmlScripts(routeHtml, `route/${slug}`);
        const contractErrs = this.validateRouteContract(routeHtml, slug);

        if (syntaxErrs.length === 0 && contractErrs.length === 0) {
          this.passedRoutes++;
        } else {
          this.failedRoutes++;
          if (syntaxErrs.length > 0) {
            this.syntaxErrors.push({ route: slug, errors: syntaxErrs });
          }
          if (contractErrs.length > 0) {
            this.contractErrors.push({ route: slug, errors: contractErrs });
          }
        }
      }
    }

    // 2. Verify Admin Moderation Page
    if (!ROUTES_ONLY) {
      console.log('Checking Admin moderation page (site/mallorca/admin_comentaris/index.html)...');
      if (!fs.existsSync(ADMIN_FILE)) {
        this.adminPassed = false;
        this.adminErrors.push('Admin index.html does not exist');
      } else {
        const adminSyntax = this.validateHtmlScripts(ADMIN_FILE, 'admin_comentaris');
        const adminContract = this.validateAdminContract(ADMIN_FILE);
        if (adminSyntax.length > 0 || adminContract.length > 0) {
          this.adminPassed = false;
          this.adminErrors = [...adminSyntax, ...adminContract];
        }
      }
    }

    // Optional all-html scan
    if (CHECK_ALL) {
      this.runAllHtmlScan();
    }

    // Print Diagnostics
    const elapsed = Date.now() - this.startTime;
    console.log('\n---------------------- VERIFICATION METRICS ----------------------');
    console.log(`Execution Time:          ${elapsed} ms`);
    console.log(`Inline Scripts Tested:   ${this.totalScriptsTested}`);
    console.log(`External SDK Scripts:    ${this.totalExternalScripts}`);
    console.log(`JSON Configs Validated:  ${this.totalJsonTested}`);
    if (!ADMIN_ONLY) {
      console.log(`Route Pages Tested:      ${this.totalRoutes}`);
      console.log(`Route Pages Passing:     ${this.passedRoutes} / ${this.totalRoutes}`);
      console.log(`Route Pages Failing:     ${this.failedRoutes}`);
    }
    if (!ROUTES_ONLY) {
      console.log(`Admin Page Passed:       ${this.adminPassed ? 'YES' : 'NO'}`);
    }
    console.log('------------------------------------------------------------------');

    // Report failures
    if (this.syntaxErrors.length > 0) {
      allOk = false;
      console.log(`\n❌ JAVASCRIPT SYNTAX FAILURES (${this.syntaxErrors.length} routes affected):`);
      for (const err of this.syntaxErrors.slice(0, 3)) {
        console.log(`\n  Route: ${err.route}`);
        for (const e of err.errors) {
          console.log(`    Script #${e.scriptIdx}: [${e.type}] ${e.message}`);
          if (e.context) {
            console.log('    Context:');
            console.log(e.context.split('\n').map(l => '      ' + l).join('\n'));
          }
        }
      }
      if (this.syntaxErrors.length > 3) {
        console.log(`\n  [... and ${this.syntaxErrors.length - 3} more routes with the identical syntax failure]`);
      }
    }

    if (this.contractErrors.length > 0) {
      allOk = false;
      console.log(`\n❌ CONTRACT FAILURES (${this.contractErrors.length} routes affected):`);
      for (const err of this.contractErrors.slice(0, 5)) {
        console.log(`  Route: ${err.route} -> ${err.errors.join('; ')}`);
      }
    }

    if (!this.adminPassed) {
      allOk = false;
      console.log('\n❌ ADMIN PAGE ERRORS:');
      for (const err of this.adminErrors) {
        console.log('  ', err);
      }
    }

    console.log('\n================================================================');
    if (allOk && (ROUTES_ONLY || this.adminPassed) && (ADMIN_ONLY || this.passedRoutes === this.totalRoutes)) {
      console.log('🎉 VERIFICATION STATUS: 100% PASSED — READY FOR COMMIT');
      console.log('================================================================\n');
      return true;
    } else {
      console.log('🚫 VERIFICATION STATUS: FAILED — FIX REQUIRED BEFORE COMMIT');
      console.log('================================================================\n');
      return false;
    }
  }
}

const verifier = new SiteVerifier();
const passed = verifier.run();
process.exit(passed ? 0 : 1);
