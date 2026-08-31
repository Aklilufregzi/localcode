/**
 * LeetCode 242. Valid Anagram (Easy)
 * https://leetcode.com/problems/valid-anagram/
 *
 * Given two strings s and t, return true if t is an anagram of s
 * (same characters with the same counts, rearranged), false otherwise.
 *
 * Run just this file:   npx tsx src/arrays-hashing/valid-anagram.ts
 * Run its tests:        npx vitest run src/arrays-hashing/valid-anagram.test.ts
 */

export function isAnagram(s: string, t: string): boolean {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(isAnagram("anagram", "nagaram")); // expected true
  console.log(isAnagram("rat", "car")); // expected false
}
