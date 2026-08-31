/**
 * LeetCode 128. Longest Consecutive Sequence (Medium)
 * https://leetcode.com/problems/longest-consecutive-sequence/
 *
 * Given an unsorted integer array nums, return the length of the longest run
 * of consecutive integers (values, not positions). Must run in O(n) time.
 *
 * Run just this file:   npx tsx src/arrays-hashing/longest-consecutive-sequence.ts
 * Run its tests:        npx vitest run src/arrays-hashing/longest-consecutive-sequence.test.ts
 */

export function longestConsecutive(nums: number[]): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(longestConsecutive([100, 4, 200, 1, 3, 2])); // expected 4
  console.log(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])); // expected 9
}
