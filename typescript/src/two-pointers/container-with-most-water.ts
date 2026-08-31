/**
 * LeetCode 11. Container With Most Water (Medium)
 * https://leetcode.com/problems/container-with-most-water/
 *
 * You are given an integer array height of length n; the i-th line goes
 * from (i, 0) to (i, height[i]). Find two lines that together with the
 * x-axis form a container holding the most water, and return that maximum
 * amount (area = width * min of the two heights). No slanting.
 *
 * Run just this file:   npx tsx src/two-pointers/container-with-most-water.ts
 * Run its tests:        npx vitest run src/two-pointers/container-with-most-water.test.ts
 */

export function maxArea(height: number[]): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])); // expected 49
  console.log(maxArea([1, 1])); // expected 1
}
