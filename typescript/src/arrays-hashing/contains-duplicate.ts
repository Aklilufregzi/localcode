/**
 * LeetCode 217. Contains Duplicate (Easy)
 * https://leetcode.com/problems/contains-duplicate/
 *
 * Given an integer array nums, return true if any value appears at least
 * twice in the array, and false if every element is distinct.
 *
 * Run just this file:   npx tsx src/arrays-hashing/contains-duplicate.ts
 * Run its tests:        npx vitest run src/arrays-hashing/contains-duplicate.test.ts
 */

export function containsDuplicate(nums: number[]): boolean {


  return nums.length > new Set(nums).size? true : false;
  // TODO: implement



}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(containsDuplicate([1, 2, 3, 1])); // expected true
  console.log(containsDuplicate([1, 2, 3, 4])); // expected false
}
