/**
 * LeetCode 5. Longest Palindromic Substring (Medium)
 * https://leetcode.com/problems/longest-palindromic-substring/
 *
 * Given a string s, return the longest palindromic substring in s.
 *
 * Run just this file:   npx tsx src/1d-dp/longest-palindromic-substring.ts
 * Run its tests:        npx vitest run src/1d-dp/longest-palindromic-substring.test.ts
 */

export function longestPalindrome(s: string): string {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(longestPalindrome("babad")); // expected "bab" or "aba"
  console.log(longestPalindrome("cbbd")); // expected "bb"
}
