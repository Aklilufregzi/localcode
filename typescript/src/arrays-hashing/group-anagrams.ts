/**
 * LeetCode 49. Group Anagrams (Medium)
 * https://leetcode.com/problems/group-anagrams/
 *
 * Given an array of strings strs, group the anagrams together.
 * Return the answer in any order (group order and in-group order are free).
 *
 * Run just this file:   npx tsx src/arrays-hashing/group-anagrams.ts
 * Run its tests:        npx vitest run src/arrays-hashing/group-anagrams.test.ts
 */

export function groupAnagrams(strs: string[]): string[][] {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
  // expected (any order): [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
}
