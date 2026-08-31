/**
 * LeetCode 329. Longest Increasing Path in a Matrix (Hard)
 * https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
 *
 * Given an m x n integer matrix, return the length of the longest strictly
 * increasing path. From each cell you can move up, down, left, or right
 * (no diagonals, no wrap-around).
 *
 * Run just this file:   npx tsx src/2d-dp/longest-increasing-path-in-a-matrix.ts
 * Run its tests:        npx vitest run src/2d-dp/longest-increasing-path-in-a-matrix.test.ts
 */

export function longestIncreasingPath(matrix: number[][]): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])); // expected 4
  console.log(longestIncreasingPath([[1]])); // expected 1
}
