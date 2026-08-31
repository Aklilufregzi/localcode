/**
 * LeetCode 347. Top K Frequent Elements (Medium)
 * https://leetcode.com/problems/top-k-frequent-elements/
 *
 * Given an integer array nums and an integer k, return the k most frequent
 * elements. The answer is guaranteed unique; return it in any order.
 *
 * Run just this file:   npx tsx src/arrays-hashing/top-k-frequent-elements.ts
 * Run its tests:        npx vitest run src/arrays-hashing/top-k-frequent-elements.test.ts
 */

export function topKFrequent(nums: number[], k: number): number[] {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2)); // expected [1, 2] in any order
}
