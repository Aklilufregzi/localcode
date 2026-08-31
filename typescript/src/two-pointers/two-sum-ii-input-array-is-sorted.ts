/**
 * LeetCode 167. Two Sum II - Input Array Is Sorted (Medium)
 * https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
 *
 * Given a 1-indexed array of integers sorted in non-decreasing order, find
 * two numbers that add up to target and return their 1-indexed positions
 * [index1, index2] with index1 < index2. Exactly one solution exists; you
 * may not use the same element twice. Use only constant extra space.
 *
 * Run just this file:   npx tsx src/two-pointers/two-sum-ii-input-array-is-sorted.ts
 * Run its tests:        npx vitest run src/two-pointers/two-sum-ii-input-array-is-sorted.test.ts
 */

export function twoSum(numbers: number[], target: number): number[] {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(twoSum([2, 7, 11, 15], 9)); // expected [1, 2]
  console.log(twoSum([2, 3, 4], 6)); // expected [1, 3]
}
