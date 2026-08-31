import { describe, expect, it } from "vitest";
import { maxArea } from "./container-with-most-water.ts";

describe("maxArea", () => {
  it("example 1", () => {
    // Lines at indices 1 (h=8) and 8 (h=7): width 7 * min(8, 7) = 49.
    expect(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])).toBe(49);
  });

  it("example 2", () => {
    expect(maxArea([1, 1])).toBe(1);
  });

  it("increasing heights", () => {
    // Best pair is indices 1 and 4: width 3 * min(2, 5) = 6.
    expect(maxArea([1, 2, 3, 4, 5])).toBe(6);
  });
});
