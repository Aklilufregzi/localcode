import { describe, expect, it } from "vitest";
import { twoSum } from "./two-sum-ii-input-array-is-sorted.ts";

describe("twoSum (II, sorted, 1-indexed)", () => {
  it("example 1", () => {
    expect(twoSum([2, 7, 11, 15], 9)).toEqual([1, 2]);
  });

  it("example 2", () => {
    expect(twoSum([2, 3, 4], 6)).toEqual([1, 3]);
  });

  it("example 3", () => {
    expect(twoSum([-1, 0], -1)).toEqual([1, 2]);
  });
});
