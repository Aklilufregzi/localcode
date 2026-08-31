/**
 * LeetCode 424. Longest Repeating Character Replacement (Medium)
 * https://leetcode.com/problems/longest-repeating-character-replacement/
 *
 * You are given a string s of uppercase English letters and an integer k.
 * You can change any character to any other uppercase letter, at most k
 * times total. Return the length of the longest substring containing the
 * same letter you can get after performing the operations.
 *
 * Run just this file:   npx tsx src/sliding-window/longest-repeating-character-replacement.ts
 * Run its tests:        npx vitest run src/sliding-window/longest-repeating-character-replacement.test.ts
 */

export function characterReplacement(s: string, k: number): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(characterReplacement("ABAB", 2)); // expected 4
  console.log(characterReplacement("AABABBA", 1)); // expected 4
}
