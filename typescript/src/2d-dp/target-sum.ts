/**
 * LeetCode 494. Target Sum (Medium)
 * https://leetcode.com/problems/target-sum/
 *
 * Given an integer array nums and an integer target, assign '+' or '-' before
 * each number so the resulting expression evaluates to target. Return the
 * number of different expressions that do so.
 *
 * Run just this file:   npx tsx src/2d-dp/target-sum.ts
 * Run its tests:        npx vitest run src/2d-dp/target-sum.test.ts
 */

export function findTargetSumWays(nums: number[], target: number): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(findTargetSumWays([1, 1, 1, 1, 1], 3)); // expected 5
  console.log(findTargetSumWays([1], 1)); // expected 1
}
