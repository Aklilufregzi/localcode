import { describe, expect, it } from "vitest";
import { largestRectangleArea } from "./largest-rectangle-in-histogram.ts";

describe("largestRectangleArea", () => {
  it("example 1", () => {
    // Rectangle of height 5 spanning bars [5, 6] -> area 10.
    expect(largestRectangleArea([2, 1, 5, 6, 2, 3])).toBe(10);
  });

  it("example 2", () => {
    expect(largestRectangleArea([2, 4])).toBe(4);
  });

  it("single bar", () => {
    expect(largestRectangleArea([7])).toBe(7);
  });

  it("increasing then decreasing", () => {
    // Best is height 3 spanning the middle three bars -> 9.
    expect(largestRectangleArea([1, 3, 5, 3, 1])).toBe(9);
  });
});
