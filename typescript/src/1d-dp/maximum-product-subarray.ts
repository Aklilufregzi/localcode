/**
 * LeetCode 152. Maximum Product Subarray (Medium)
 * https://leetcode.com/problems/maximum-product-subarray/
 *
 * Given an integer array nums, find a contiguous non-empty subarray with
 * the largest product and return that product.
 *
 * Run just this file:   npx tsx src/1d-dp/maximum-product-subarray.ts
 * Run its tests:        npx vitest run src/1d-dp/maximum-product-subarray.test.ts
 */

export function maxProduct(nums: number[]): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(maxProduct([2, 3, -2, 4])); // expected 6
  console.log(maxProduct([-2, 0, -1])); // expected 0
}
