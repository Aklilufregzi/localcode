/**
 * LeetCode 212. Word Search II (Hard)
 * https://leetcode.com/problems/word-search-ii/
 *
 * Given an m x n board of characters and a list of words, return all words
 * that can be constructed from sequentially adjacent cells (horizontally or
 * vertically neighboring); the same cell may not be used more than once per word.
 *
 * Run just this file:   npx tsx src/tries/word-search-ii.ts
 * Run its tests:        npx vitest run src/tries/word-search-ii.test.ts
 */

export function findWords(board: string[][], words: string[]): string[] {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  const board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
  ];
  console.log(findWords(board, ["oath", "pea", "eat", "rain"])); // expected ["eat", "oath"] in any order
}
