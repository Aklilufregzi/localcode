/**
 * LeetCode 15. 3Sum (Medium)
 * https://leetcode.com/problems/3sum/
 *
 * Given an integer array nums, return all the triplets
 * [nums[i], nums[j], nums[k]] such that i != j, i != k, j != k, and
 * nums[i] + nums[j] + nums[k] == 0. The solution set must not contain
 * duplicate triplets. Answer may be returned in any order.
 *
 * Run just this file:   npx tsx src/two-pointers/3sum.ts
 * Run its tests:        npx vitest run src/two-pointers/3sum.test.ts
 */

export function threeSum(nums: number[]): number[][] {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(threeSum([-1, 0, 1, 2, -1, -4])); // expected [[-1, -1, 2], [-1, 0, 1]] (any order)
  console.log(threeSum([0, 0, 0])); // expected [[0, 0, 0]]
}
