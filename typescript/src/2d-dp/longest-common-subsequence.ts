/**
 * LeetCode 1143. Longest Common Subsequence (Medium)
 * https://leetcode.com/problems/longest-common-subsequence/
 *
 * Given two strings text1 and text2, return the length of their longest
 * common subsequence (a sequence derived by deleting some or no characters
 * without changing the relative order of the rest). Return 0 if there is none.
 *
 * Run just this file:   npx tsx src/2d-dp/longest-common-subsequence.ts
 * Run its tests:        npx vitest run src/2d-dp/longest-common-subsequence.test.ts
 */

export function longestCommonSubsequence(text1: string, text2: string): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(longestCommonSubsequence("abcde", "ace")); // expected 3
  console.log(longestCommonSubsequence("abc", "def")); // expected 0
}
