/**
 * LeetCode 300. Longest Increasing Subsequence (Medium)
 * https://leetcode.com/problems/longest-increasing-subsequence/
 *
 * Given an integer array nums, return the length of the longest strictly
 * increasing subsequence (elements keep their relative order but need
 * not be contiguous).
 *
 * Run just this file:   npx tsx src/1d-dp/longest-increasing-subsequence.ts
 * Run its tests:        npx vitest run src/1d-dp/longest-increasing-subsequence.test.ts
 */

export function lengthOfLIS(nums: number[]): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])); // expected 4
  console.log(lengthOfLIS([0, 1, 0, 3, 2, 3])); // expected 4
}
