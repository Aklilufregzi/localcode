/**
 * LeetCode 76. Minimum Window Substring (Hard)
 * https://leetcode.com/problems/minimum-window-substring/
 *
 * Given strings s and t, return the minimum window substring of s that
 * contains every character of t (including duplicates). If there is no such
 * substring, return the empty string "". The answer is guaranteed unique.
 *
 * Run just this file:   npx tsx src/sliding-window/minimum-window-substring.ts
 * Run its tests:        npx vitest run src/sliding-window/minimum-window-substring.test.ts
 */

export function minWindow(s: string, t: string): string {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(minWindow("ADOBECODEBANC", "ABC")); // expected "BANC"
  console.log(minWindow("a", "aa")); // expected ""
}
