/**
 * LeetCode 647. Palindromic Substrings (Medium)
 * https://leetcode.com/problems/palindromic-substrings/
 *
 * Given a string s, return the number of palindromic substrings in it.
 * Substrings with different start/end positions count separately even
 * if they are equal as strings.
 *
 * Run just this file:   npx tsx src/1d-dp/palindromic-substrings.ts
 * Run its tests:        npx vitest run src/1d-dp/palindromic-substrings.test.ts
 */

export function countSubstrings(s: string): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(countSubstrings("abc")); // expected 3
  console.log(countSubstrings("aaa")); // expected 6
}
