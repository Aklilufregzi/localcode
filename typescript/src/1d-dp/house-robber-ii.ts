/**
 * LeetCode 213. House Robber II (Medium)
 * https://leetcode.com/problems/house-robber-ii/
 *
 * Same as House Robber, but the houses are arranged in a circle: the
 * first and last houses are adjacent. Return the max amount you can rob
 * without robbing two adjacent houses.
 *
 * Run just this file:   npx tsx src/1d-dp/house-robber-ii.ts
 * Run its tests:        npx vitest run src/1d-dp/house-robber-ii.test.ts
 */

export function rob(nums: number[]): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(rob([2, 3, 2])); // expected 3
  console.log(rob([1, 2, 3, 1])); // expected 4
}
