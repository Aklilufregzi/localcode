/**
 * LeetCode 322. Coin Change (Medium)
 * https://leetcode.com/problems/coin-change/
 *
 * Given coin denominations and an amount, return the fewest number of
 * coins needed to make up that amount (unlimited supply of each coin),
 * or -1 if it cannot be made. amount == 0 needs 0 coins.
 *
 * Run just this file:   npx tsx src/1d-dp/coin-change.ts
 * Run its tests:        npx vitest run src/1d-dp/coin-change.test.ts
 */

export function coinChange(coins: number[], amount: number): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(coinChange([1, 2, 5], 11)); // expected 3
  console.log(coinChange([2], 3)); // expected -1
}
