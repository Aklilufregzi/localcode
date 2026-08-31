/**
 * LeetCode 70. Climbing Stairs (Easy)
 * https://leetcode.com/problems/climbing-stairs/
 *
 * You are climbing a staircase with n steps. Each time you can climb
 * either 1 or 2 steps. In how many distinct ways can you reach the top?
 *
 * Run just this file:   npx tsx src/1d-dp/climbing-stairs.ts
 * Run its tests:        npx vitest run src/1d-dp/climbing-stairs.test.ts
 */

export function climbStairs(n: number): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(climbStairs(2)); // expected 2
  console.log(climbStairs(3)); // expected 3
}
