/**
 * LeetCode 42. Trapping Rain Water (Hard)
 * https://leetcode.com/problems/trapping-rain-water/
 *
 * Given n non-negative integers representing an elevation map where the
 * width of each bar is 1, compute how much water it can trap after raining.
 *
 * Run just this file:   npx tsx src/two-pointers/trapping-rain-water.ts
 * Run its tests:        npx vitest run src/two-pointers/trapping-rain-water.test.ts
 */

export function trap(height: number[]): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])); // expected 6
  console.log(trap([4, 2, 0, 3, 2, 5])); // expected 9
}
