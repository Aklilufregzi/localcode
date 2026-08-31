/**
 * LeetCode 91. Decode Ways (Medium)
 * https://leetcode.com/problems/decode-ways/
 *
 * A message of letters A-Z is encoded as digits "1"-"26". Given a digit
 * string s, return the number of ways to decode it ("0" alone or a leading
 * zero in a pair is invalid).
 *
 * Run just this file:   npx tsx src/1d-dp/decode-ways.ts
 * Run its tests:        npx vitest run src/1d-dp/decode-ways.test.ts
 */

export function numDecodings(s: string): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(numDecodings("12")); // expected 2
  console.log(numDecodings("226")); // expected 3
}
