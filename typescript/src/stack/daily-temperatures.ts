/**
 * LeetCode 739. Daily Temperatures (Medium)
 * https://leetcode.com/problems/daily-temperatures/
 *
 * Given an array of daily temperatures, return an array answer where
 * answer[i] is the number of days you have to wait after day i to get a
 * warmer temperature. If there is no future warmer day, answer[i] = 0.
 *
 * Run just this file:   npx tsx src/stack/daily-temperatures.ts
 * Run its tests:        npx vitest run src/stack/daily-temperatures.test.ts
 */

export function dailyTemperatures(temperatures: number[]): number[] {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])); // expected [1,1,4,2,1,1,0,0]
}
