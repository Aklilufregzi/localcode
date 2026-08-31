/**
 * LeetCode 853. Car Fleet (Medium)
 * https://leetcode.com/problems/car-fleet/
 *
 * n cars at position[i] drive at speed[i] toward a destination at target
 * miles. A car cannot pass the car ahead; it catches up and travels at the
 * slower car's speed, forming a fleet. Return the number of fleets that
 * arrive at the destination (a fleet catching up exactly AT target counts as one).
 *
 * Run just this file:   npx tsx src/stack/car-fleet.ts
 * Run its tests:        npx vitest run src/stack/car-fleet.test.ts
 */

export function carFleet(target: number, position: number[], speed: number[]): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])); // expected 3
}
