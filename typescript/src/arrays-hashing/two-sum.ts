/**
 * LeetCode 1. Two Sum (Easy)
 * https://leetcode.com/problems/two-sum/
 *
 * Given an array of integers nums and an integer target, return indices of
 * the two numbers such that they add up to target.
 *
 * Run just this file:   npx tsx src/arrays-hashing/two-sum.ts
 * Run its tests:        npx vitest run src/arrays-hashing/two-sum.test.ts
 * Run everything:       npm test
 */

export function twoSum(nums: number[], target: number): number[] {
  const seen = new Map<number, number>();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i]!;
    const j = seen.get(complement);
    if (j !== undefined) return [j, i];
    seen.set(nums[i]!, i);
  }
  return [];
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(twoSum([2, 7, 11, 15], 9)); // expected [0, 1]
  console.log(twoSum([3, 2, 4], 6)); // expected [1, 2]
}
