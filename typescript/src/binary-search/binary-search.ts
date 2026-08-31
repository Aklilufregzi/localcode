/**
 * LeetCode 704. Binary Search (Easy)
 * https://leetcode.com/problems/binary-search/
 *
 * Given a sorted (ascending) array of distinct integers and a target,
 * return the index of target if it exists, otherwise -1.
 * Must run in O(log n) time.
 *
 * Run just this file:   npx tsx src/binary-search/binary-search.ts
 * Run its tests:        npx vitest run src/binary-search/binary-search.test.ts
 */

export function search(nums: number[], target: number): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(search([-1, 0, 3, 5, 9, 12], 9)); // expected 4
  console.log(search([-1, 0, 3, 5, 9, 12], 2)); // expected -1
}
