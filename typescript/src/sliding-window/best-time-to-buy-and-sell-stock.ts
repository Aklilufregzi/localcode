/**
 * LeetCode 121. Best Time to Buy and Sell Stock (Easy)
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 *
 * You are given an array prices where prices[i] is the price of a stock on
 * the i-th day. Choose a single day to buy and a later day to sell to
 * maximize profit. Return the maximum profit, or 0 if no profit is possible.
 *
 * Run just this file:   npx tsx src/sliding-window/best-time-to-buy-and-sell-stock.ts
 * Run its tests:        npx vitest run src/sliding-window/best-time-to-buy-and-sell-stock.test.ts
 */

export function maxProfit(prices: number[]): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(maxProfit([7, 1, 5, 3, 6, 4])); // expected 5
  console.log(maxProfit([7, 6, 4, 3, 1])); // expected 0
}
