import { describe, expect, it } from "vitest";
import { threeSum } from "./3sum.ts";

// Output order doesn't matter (outer or inner) — sort copies of both sides.
function normalize(triplets: number[][]): number[][] {
  return triplets
    .map((t) => [...t].sort((a, b) => a - b))
    .sort((a, b) => (a[0] ?? 0) - (b[0] ?? 0) || (a[1] ?? 0) - (b[1] ?? 0) || (a[2] ?? 0) - (b[2] ?? 0));
}

describe("threeSum", () => {
  it("example 1", () => {
    const result = threeSum([-1, 0, 1, 2, -1, -4]);
    expect(normalize(result)).toEqual(normalize([[-1, -1, 2], [-1, 0, 1]]));
  });

  it("example 2: no triplet sums to zero", () => {
    expect(threeSum([0, 1, 1])).toEqual([]);
  });

  it("example 3: only one distinct triplet", () => {
    expect(normalize(threeSum([0, 0, 0]))).toEqual([[0, 0, 0]]);
  });
});
