import { describe, expect, it } from "vitest";
import { findTargetSumWays } from "./target-sum.ts";

describe("findTargetSumWays", () => {
  it("example 1", () => {
    // -1+1+1+1+1, +1-1+1+1+1, +1+1-1+1+1, +1+1+1-1+1, +1+1+1+1-1
    expect(findTargetSumWays([1, 1, 1, 1, 1], 3)).toBe(5);
  });

  it("example 2", () => {
    expect(findTargetSumWays([1], 1)).toBe(1);
  });

  it("unreachable target", () => {
    expect(findTargetSumWays([1], 2)).toBe(0);
  });

  it("with zero", () => {
    // +0+1 and -0+1 both reach 1
    expect(findTargetSumWays([0, 1], 1)).toBe(2);
  });
});
