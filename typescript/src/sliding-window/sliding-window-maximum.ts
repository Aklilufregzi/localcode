/**
 * LeetCode 239. Sliding Window Maximum (Hard)
 * https://leetcode.com/problems/sliding-window-maximum/
 *
 * You are given an integer array nums and a window of size k sliding from
 * the very left to the very right, moving one position at a time. Return an
 * array of the maximum value in each window position.
 *
 * Run just this file:   npx tsx src/sliding-window/sliding-window-maximum.ts
 * Run its tests:        npx vitest run src/sliding-window/sliding-window-maximum.test.ts
 */

export function maxSlidingWindow(nums: number[], k: number): number[] {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)); // expected [3, 3, 5, 5, 6, 7]
  console.log(maxSlidingWindow([1], 1)); // expected [1]
}
