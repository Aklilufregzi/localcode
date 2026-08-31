import { describe, expect, it } from "vitest";
import { trap } from "./trapping-rain-water.ts";

describe("trap", () => {
  it("example 1", () => {
    expect(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])).toBe(6);
  });

  it("example 2", () => {
    expect(trap([4, 2, 0, 3, 2, 5])).toBe(9);
  });

  it("monotonic elevation traps nothing", () => {
    expect(trap([1, 2, 3])).toBe(0);
  });

  it("single bar", () => {
    expect(trap([5])).toBe(0);
  });
});
