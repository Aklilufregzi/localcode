import { describe, expect, it } from "vitest";
import { twoSum } from "./two-sum.ts";

describe("twoSum", () => {
  it("example 1", () => {
    expect(twoSum([2, 7, 11, 15], 9)).toEqual([0, 1]);
  });

  it("example 2", () => {
    expect(twoSum([3, 2, 4], 6)).toEqual([1, 2]);
  });

  it("same number twice", () => {
    expect(twoSum([3, 3], 6)).toEqual([0, 1]);
  });
});
