/**
 * LeetCode 271. Encode and Decode Strings (Medium)
 * https://leetcode.com/problems/encode-and-decode-strings/  (premium — NeetCode version)
 *
 * Design an algorithm to encode a list of strings to a single string, and
 * decode that single string back to the original list. Strings may contain
 * any characters (including '#') and may be empty.
 *
 * Run just this file:   npx tsx src/arrays-hashing/encode-and-decode-strings.ts
 * Run its tests:        npx vitest run src/arrays-hashing/encode-and-decode-strings.test.ts
 */

export class Solution {
  encode(strs: string[]): string {
    // TODO: implement
    throw new Error("Not implemented");
  }

  decode(s: string): string[] {
    // TODO: implement
    throw new Error("Not implemented");
  }
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  const s = new Solution();
  const encoded = s.encode(["neet", "code", "love", "you"]);
  console.log(encoded);
  console.log(s.decode(encoded)); // expected ["neet", "code", "love", "you"]
}
