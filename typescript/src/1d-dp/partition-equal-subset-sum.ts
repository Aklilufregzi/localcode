/**
 * LeetCode 416. Partition Equal Subset Sum (Medium)
 * https://leetcode.com/problems/partition-equal-subset-sum/
 *
 * Given an array nums of positive integers, return true if it can be
 * partitioned into two subsets whose sums are equal.
 *
 * Run just this file:   npx tsx src/1d-dp/partition-equal-subset-sum.ts
 * Run its tests:        npx vitest run src/1d-dp/partition-equal-subset-sum.test.ts
 */

export function canPartition(nums: number[]): boolean {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(canPartition([1, 5, 11, 5])); // expected true
  console.log(canPartition([1, 2, 3, 5])); // expected false
}
