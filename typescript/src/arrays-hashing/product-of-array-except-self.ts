/**
 * LeetCode 238. Product of Array Except Self (Medium)
 * https://leetcode.com/problems/product-of-array-except-self/
 *
 * Given an integer array nums, return an array answer where answer[i] is the
 * product of all elements of nums except nums[i]. Run in O(n) without using
 * the division operation.
 *
 * Run just this file:   npx tsx src/arrays-hashing/product-of-array-except-self.ts
 * Run its tests:        npx vitest run src/arrays-hashing/product-of-array-except-self.test.ts
 */

export function productExceptSelf(nums: number[]): number[] {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(productExceptSelf([1, 2, 3, 4])); // expected [24, 12, 8, 6]
  console.log(productExceptSelf([-1, 1, 0, -3, 3])); // expected [0, 0, 9, 0, 0]
}
