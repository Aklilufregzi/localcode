/**
 * LeetCode 97. Interleaving String (Medium)
 * https://leetcode.com/problems/interleaving-string/
 *
 * Given strings s1, s2, s3, return true if s3 is formed by an interleaving of
 * s1 and s2: s3 uses all characters of s1 and s2, keeping the relative order
 * within each source string.
 *
 * Run just this file:   npx tsx src/2d-dp/interleaving-string.ts
 * Run its tests:        npx vitest run src/2d-dp/interleaving-string.test.ts
 */

export function isInterleave(s1: string, s2: string, s3: string): boolean {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(isInterleave("aabcc", "dbbca", "aadbbcbcac")); // expected true
  console.log(isInterleave("aabcc", "dbbca", "aadbbbaccc")); // expected false
}
