/**
 * LeetCode 518. Coin Change II (Medium)
 * https://leetcode.com/problems/coin-change-ii/
 *
 * Given coin denominations and an amount, return the number of combinations
 * of coins that make up that amount (infinite supply of each coin). Return 0
 * if the amount cannot be made up.
 *
 * Run just this file:   npx tsx src/2d-dp/coin-change-ii.ts
 * Run its tests:        npx vitest run src/2d-dp/coin-change-ii.test.ts
 */

export function change(amount: number, coins: number[]): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(change(5, [1, 2, 5])); // expected 4
  console.log(change(3, [2])); // expected 0
}
