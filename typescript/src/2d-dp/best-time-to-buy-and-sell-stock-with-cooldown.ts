/**
 * LeetCode 309. Best Time to Buy and Sell Stock with Cooldown (Medium)
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
 *
 * Given daily stock prices, maximize profit with as many transactions as you
 * like, but after selling you must cool down one day before buying again,
 * and you may not hold more than one share at a time.
 *
 * Run just this file:   npx tsx src/2d-dp/best-time-to-buy-and-sell-stock-with-cooldown.ts
 * Run its tests:        npx vitest run src/2d-dp/best-time-to-buy-and-sell-stock-with-cooldown.test.ts
 */

export function maxProfit(prices: number[]): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(maxProfit([1, 2, 3, 0, 2])); // expected 3
  console.log(maxProfit([1])); // expected 0
}
