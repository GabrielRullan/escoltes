#!/usr/bin/env node
/**
 * Master E2E Test Suite Runner
 * Project: Escoltes de les Illes Balears (Balearic Islands Expansion)
 * Standard: Node.js CommonJS Native TAP v13 & ANSI Formatted Runner
 *
 * Usage:
 *   node tests/run_e2e_tests.cjs              # Run all tiers (1-4)
 *   node tests/run_e2e_tests.cjs --tier=1     # Run Tier 1: Feature Coverage
 *   node tests/run_e2e_tests.cjs --tier=2     # Run Tier 2: Boundary & Corner Cases
 *   node tests/run_e2e_tests.cjs --tier=3     # Run Tier 3: Cross-Feature Interactions
 *   node tests/run_e2e_tests.cjs --tier=4     # Run Tier 4: Real-World Scout Scenarios
 *   node tests/run_e2e_tests.cjs --tap        # Output in TAP v13 format
 *   node tests/run_e2e_tests.cjs --verbose    # Show error stack traces
 */

const path = require('path');
const { harness } = require('./test_harness.cjs');

// Parse CLI arguments
const args = process.argv.slice(2);
let selectedTier = null;
let tapMode = false;
let verbose = false;

for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg.startsWith('--tier=')) {
        selectedTier = parseInt(arg.split('=')[1], 10);
    } else if (arg === '--tier' || arg === '-t') {
        selectedTier = parseInt(args[++i], 10);
    } else if (arg === '--tap') {
        tapMode = true;
    } else if (arg === '--verbose' || arg === '-v') {
        verbose = true;
    } else if (arg === '--help' || arg === '-h') {
        console.log(`
Balearic Islands Expansion E2E Test Suite Runner

Options:
  --tier=N, -t N   Run only tier N (1, 2, 3, or 4)
  --tap            Emit machine-readable TAP v13 output
  --verbose, -v    Display stack traces on failure
  --help, -h       Show this help message
`);
        process.exit(0);
    }
}

harness.setTapMode(tapMode);
harness.setVerbose(verbose);
if (selectedTier) {
    harness.setFilterTier(selectedTier);
}

// Tier file mapping
const tierFiles = {
    1: './tier1_feature_coverage.test.cjs',
    2: './tier2_boundary_corner.test.cjs',
    3: './tier3_cross_feature.test.cjs',
    4: './tier4_real_world_scenarios.test.cjs'
};

if (selectedTier) {
    if (!tierFiles[selectedTier]) {
        console.error(`❌ Error: Unknown tier ${selectedTier}. Valid tiers are 1, 2, 3, 4.`);
        process.exit(1);
    }
    require(tierFiles[selectedTier]);
} else {
    // Run all tiers in sequence
    require(tierFiles[1]);
    require(tierFiles[2]);
    require(tierFiles[3]);
    require(tierFiles[4]);
}

// Print report and determine exit code
const report = harness.printReport();

if (report.success) {
    process.exit(0);
} else {
    process.exit(1);
}
