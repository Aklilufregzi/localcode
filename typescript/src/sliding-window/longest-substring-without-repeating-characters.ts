/**
 * LeetCode 3. Longest Substring Without Repeating Characters (Medium)
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 *
 * Given a string s, find the length of the longest substring (contiguous)
 * without duplicate characters.
 *
 * Run just this file:   npx tsx src/sliding-window/longest-substring-without-repeating-characters.ts
 * Run its tests:        npx vitest run src/sliding-window/longest-substring-without-repeating-characters.test.ts
 */

export function lengthOfLongestSubstring(s: string): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(lengthOfLongestSubstring("abcabcbb")); // expected 3
  console.log(lengthOfLongestSubstring("pwwkew")); // expected 3
}
