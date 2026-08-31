import { describe, expect, it } from "vitest";
import { change } from "./coin-change-ii.ts";

describe("change", () => {
  it("example 1", () => {
    // 5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1
    expect(change(5, [1, 2, 5])).toBe(4);
  });

  it("example 2", () => {
    expect(change(3, [2])).toBe(0);
  });

  it("example 3", () => {
    expect(change(10, [10])).toBe(1);
  });

  it("zero amount", () => {
    // One way to make 0: use no coins.
    expect(change(0, [7])).toBe(1);
  });
});
