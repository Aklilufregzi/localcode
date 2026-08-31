/**
 * LeetCode 139. Word Break (Medium)
 * https://leetcode.com/problems/word-break/
 *
 * Given a string s and a dictionary wordDict, return true if s can be
 * segmented into a space-separated sequence of one or more dictionary
 * words (words may be reused).
 *
 * Run just this file:   npx tsx src/1d-dp/word-break.ts
 * Run its tests:        npx vitest run src/1d-dp/word-break.test.ts
 */

export function wordBreak(s: string, wordDict: string[]): boolean {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(wordBreak("leetcode", ["leet", "code"])); // expected true
  console.log(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])); // expected false
}
