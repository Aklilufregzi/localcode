/**
 * LeetCode 62. Unique Paths (Medium)
 * https://leetcode.com/problems/unique-paths/
 *
 * A robot starts at the top-left corner of an m x n grid and wants to reach
 * the bottom-right corner. It can only move down or right. Return the number
 * of possible unique paths.
 *
 * Run just this file:   npx tsx src/2d-dp/unique-paths.ts
 * Run its tests:        npx vitest run src/2d-dp/unique-paths.test.ts
 */

export function uniquePaths(m: number, n: number): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(uniquePaths(3, 7)); // expected 28
  console.log(uniquePaths(3, 2)); // expected 3
}
