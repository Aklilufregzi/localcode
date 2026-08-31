/**
 * LeetCode 198. House Robber (Medium)
 * https://leetcode.com/problems/house-robber/
 *
 * Given an array of money in each house along a street, return the max
 * amount you can rob without robbing two adjacent houses.
 *
 * Run just this file:   npx tsx src/1d-dp/house-robber.ts
 * Run its tests:        npx vitest run src/1d-dp/house-robber.test.ts
 */

export function rob(nums: number[]): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(rob([1, 2, 3, 1])); // expected 4
  console.log(rob([2, 7, 9, 3, 1])); // expected 12
}
