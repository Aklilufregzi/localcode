/**
 * LeetCode 84. Largest Rectangle in Histogram (Hard)
 * https://leetcode.com/problems/largest-rectangle-in-histogram/
 *
 * Given an array of bar heights (each bar has width 1), return the area of
 * the largest rectangle that fits inside the histogram.
 *
 * Run just this file:   npx tsx src/stack/largest-rectangle-in-histogram.ts
 * Run its tests:        npx vitest run src/stack/largest-rectangle-in-histogram.test.ts
 */

export function largestRectangleArea(heights: number[]): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(largestRectangleArea([2, 1, 5, 6, 2, 3])); // expected 10
}
