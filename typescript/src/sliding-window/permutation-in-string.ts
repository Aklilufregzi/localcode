/**
 * LeetCode 567. Permutation in String (Medium)
 * https://leetcode.com/problems/permutation-in-string/
 *
 * Given two strings s1 and s2, return true if s2 contains a permutation of
 * s1 as a substring, and false otherwise (i.e. some window of s2 is an
 * anagram of s1).
 *
 * Run just this file:   npx tsx src/sliding-window/permutation-in-string.ts
 * Run its tests:        npx vitest run src/sliding-window/permutation-in-string.test.ts
 */

export function checkInclusion(s1: string, s2: string): boolean {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(checkInclusion("ab", "eidbaooo")); // expected true
  console.log(checkInclusion("ab", "eidboaoo")); // expected false
}
