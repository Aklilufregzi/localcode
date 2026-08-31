/**
 * LeetCode 746. Min Cost Climbing Stairs (Easy)
 * https://leetcode.com/problems/min-cost-climbing-stairs/
 *
 * cost[i] is the cost of stepping on stair i; after paying you may climb
 * 1 or 2 steps. You may start at index 0 or 1. Return the minimum cost
 * to reach the top of the floor (one past the last stair).
 *
 * Run just this file:   npx tsx src/1d-dp/min-cost-climbing-stairs.ts
 * Run its tests:        npx vitest run src/1d-dp/min-cost-climbing-stairs.test.ts
 */

export function minCostClimbingStairs(cost: number[]): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(minCostClimbingStairs([10, 15, 20])); // expected 15
  console.log(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])); // expected 6
}
