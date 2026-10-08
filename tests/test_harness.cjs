/**
 * Test Harness for Balearic Islands Expansion E2E Verification
 * Project: Escoltes de les Illes Balears
 * Standard: Node.js CommonJS Native TAP v13 & ANSI Formatted Runner
 */

const fs = require('fs');
const path = require('path');
const assert = require('assert');

class TestHarness {
    constructor() {
        this.suites = [];
        this.currentSuite = null;
        this.totalAssertions = 0;
        this.passedAssertions = 0;
        this.filterTier = null;
        this.tapMode = false;
        this.verbose = false;
    }

    setFilterTier(tier) {
        this.filterTier = tier ? parseInt(tier, 10) : null;
    }

    setTapMode(enabled) {
        this.tapMode = !!enabled;
    }

    setVerbose(enabled) {
        this.verbose = !!enabled;
    }

    describe(name, fn) {
        const suite = {
            name,
            tests: [],
            passed: 0,
            failed: 0,
            skipped: 0
        };
        this.suites.push(suite);
        const previousSuite = this.currentSuite;
        this.currentSuite = suite;
        try {
            fn();
        } catch (err) {
            this.test('Suite Initialization', () => {
                throw err;
            });
        } finally {
            this.currentSuite = previousSuite;
        }
    }

    test(name, fn) {
        if (!this.currentSuite) {
            this.describe('Default Suite', () => {});
        }
        const suite = this.currentSuite;
        const testCase = {
            name,
            passed: false,
            error: null,
            durationMs: 0,
            assertionsCount: 0
        };
        suite.tests.push(testCase);

        const initialAssertions = this.totalAssertions;
        const startTime = Date.now();
        try {
            fn();
            testCase.passed = true;
            suite.passed++;
        } catch (err) {
            testCase.passed = false;
            testCase.error = err;
            suite.failed++;
        } finally {
            testCase.durationMs = Date.now() - startTime;
            testCase.assertionsCount = this.totalAssertions - initialAssertions;
        }
    }

    // Assertion engine with assertion count tracking
    assert(condition, message) {
        this.totalAssertions++;
        if (!condition) {
            throw new Error(message || 'Assertion failed');
        }
        this.passedAssertions++;
    }

    assertEqual(actual, expected, message) {
        this.totalAssertions++;
        if (actual !== expected) {
            const detail = `Expected: ${JSON.stringify(expected)}, Actual: ${JSON.stringify(actual)}`;
            throw new Error(message ? `${message} (${detail})` : detail);
        }
        this.passedAssertions++;
    }

    assertNotEqual(actual, expected, message) {
        this.totalAssertions++;
        if (actual === expected) {
            const detail = `Expected not equal to: ${JSON.stringify(expected)}`;
            throw new Error(message ? `${message} (${detail})` : detail);
        }
        this.passedAssertions++;
    }

    assertDeepEqual(actual, expected, message) {
        this.totalAssertions++;
        try {
            assert.deepStrictEqual(actual, expected);
            this.passedAssertions++;
        } catch (e) {
            throw new Error(message ? `${message}: ${e.message}` : e.message);
        }
    }

    assertMatches(str, regex, message) {
        this.totalAssertions++;
        if (!regex.test(str)) {
            throw new Error(message || `String did not match pattern ${regex}: "${str}"`);
        }
        this.passedAssertions++;
    }

    assertInRange(val, min, max, message) {
        this.totalAssertions++;
        if (typeof val !== 'number' || isNaN(val) || val < min || val > max) {
            throw new Error(message || `Value ${val} is outside expected range [${min}, ${max}]`);
        }
        this.passedAssertions++;
    }

    assertArrayContains(arr, predicateOrValue, message) {
        this.totalAssertions++;
        if (!Array.isArray(arr)) {
            throw new Error(message || 'Expected an array');
        }
        let found = false;
        if (typeof predicateOrValue === 'function') {
            found = arr.some(predicateOrValue);
        } else {
            found = arr.includes(predicateOrValue);
        }
        if (!found) {
            throw new Error(message || `Array does not contain expected item`);
        }
        this.passedAssertions++;
    }

    // Helpers for file system inspection
    readJson(relativeOrAbsPath) {
        const fullPath = path.isAbsolute(relativeOrAbsPath)
            ? relativeOrAbsPath
            : path.resolve(process.cwd(), relativeOrAbsPath);
        this.assert(fs.existsSync(fullPath), `File does not exist: ${fullPath}`);
        const raw = fs.readFileSync(fullPath, 'utf8');
        try {
            return JSON.parse(raw);
        } catch (err) {
            throw new Error(`JSON parse error in ${fullPath}: ${err.message}`);
        }
    }

    readText(relativeOrAbsPath) {
        const fullPath = path.isAbsolute(relativeOrAbsPath)
            ? relativeOrAbsPath
            : path.resolve(process.cwd(), relativeOrAbsPath);
        this.assert(fs.existsSync(fullPath), `File does not exist: ${fullPath}`);
        return fs.readFileSync(fullPath, 'utf8');
    }

    fileExists(relativeOrAbsPath) {
        const fullPath = path.isAbsolute(relativeOrAbsPath)
            ? relativeOrAbsPath
            : path.resolve(process.cwd(), relativeOrAbsPath);
        return fs.existsSync(fullPath);
    }

    // Reporting & Summary
    printReport() {
        let totalTests = 0;
        let totalPassed = 0;
        let totalFailed = 0;

        for (const suite of this.suites) {
            totalTests += suite.tests.length;
            totalPassed += suite.passed;
            totalFailed += suite.failed;
        }

        if (this.tapMode) {
            this.printTap(totalTests);
        } else {
            this.printFormatted(totalTests, totalPassed, totalFailed);
        }

        return {
            totalTests,
            totalPassed,
            totalFailed,
            totalAssertions: this.totalAssertions,
            passedAssertions: this.passedAssertions,
            success: totalFailed === 0
        };
    }

    printTap(totalTests) {
        console.log('TAP version 13');
        console.log(`1..${totalTests}`);
        let testIndex = 1;
        for (const suite of this.suites) {
            for (const t of suite.tests) {
                if (t.passed) {
                    console.log(`ok ${testIndex} - ${suite.name} > ${t.name}`);
                } else {
                    console.log(`not ok ${testIndex} - ${suite.name} > ${t.name}`);
                    console.log(`  ---`);
                    console.log(`  message: "${(t.error ? t.error.message : 'Unknown error').replace(/"/g, '\\"')}"`);
                    console.log(`  ...`);
                }
                testIndex++;
            }
        }
        console.log(`# total assertions: ${this.totalAssertions}`);
    }

    printFormatted(totalTests, totalPassed, totalFailed) {
        console.log('\n================================================================');
        console.log('      BALEARIC ISLANDS EXPANSION E2E TEST VERIFICATION REPORT   ');
        console.log('================================================================\n');

        for (const suite of this.suites) {
            const suiteStatus = suite.failed === 0 ? '✅' : '❌';
            console.log(`${suiteStatus} SUITE: ${suite.name} (${suite.passed}/${suite.tests.length} passed)`);
            for (const t of suite.tests) {
                if (t.passed) {
                    console.log(`    ✅ [PASS] ${t.name} (${t.durationMs}ms, ${t.assertionsCount} asserts)`);
                } else {
                    console.log(`    ❌ [FAIL] ${t.name} (${t.durationMs}ms)`);
                    console.log(`       Error: ${t.error ? t.error.message : 'Unknown error'}`);
                    if (this.verbose && t.error && t.error.stack) {
                        const stackLines = t.error.stack.split('\n').slice(1, 4).map(l => `         ${l}`).join('\n');
                        console.log(stackLines);
                    }
                }
            }
            console.log('');
        }

        console.log('----------------------------------------------------------------');
        console.log(`TOTAL SUITES:      ${this.suites.length}`);
        console.log(`TOTAL TEST CASES:  ${totalTests}`);
        console.log(`TESTS PASSED:      ${totalPassed}`);
        console.log(`TESTS FAILED:      ${totalFailed}`);
        console.log(`TOTAL ASSERTIONS:  ${this.totalAssertions}`);
        console.log(`ASSERTION STATUS:  ${this.totalAssertions >= 120 ? '✅ Threshold (>=120) SATISFIED' : '❌ Threshold (<120) FAILED'}`);
        console.log('================================================================');
        if (totalFailed === 0) {
            console.log('🎉 VERDICT: ALL E2E REQUIREMENTS VERIFIED SUCCESSFULLY (PASS)');
        } else {
            console.log(`⚠️  VERDICT: ${totalFailed} E2E REQUIREMENTS PENDING OR FAILED`);
        }
        console.log('================================================================\n');
    }
}

const harness = new TestHarness();
module.exports = {
    harness,
    describe: harness.describe.bind(harness),
    test: harness.test.bind(harness),
    assert: harness.assert.bind(harness),
    assertEqual: harness.assertEqual.bind(harness),
    assertNotEqual: harness.assertNotEqual.bind(harness),
    assertDeepEqual: harness.assertDeepEqual.bind(harness),
    assertMatches: harness.assertMatches.bind(harness),
    assertInRange: harness.assertInRange.bind(harness),
    assertArrayContains: harness.assertArrayContains.bind(harness),
    readJson: harness.readJson.bind(harness),
    readText: harness.readText.bind(harness),
    fileExists: harness.fileExists.bind(harness)
};
