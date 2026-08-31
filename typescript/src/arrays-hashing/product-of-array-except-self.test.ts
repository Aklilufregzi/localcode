import { describe, expect, it } from "vitest";
import { productExceptSelf } from "./product-of-array-except-self.ts";

describe("productExceptSelf", () => {
  it("example 1", () => {
    expect(productExceptSelf([1, 2, 3, 4])).toEqual([24, 12, 8, 6]);
  });

  it("example 2", () => {
    expect(productExceptSelf([-1, 1, 0, -3, 3])).toEqual([0, 0, 9, 0, 0]);
  });

  it("two elements", () => {
    expect(productExceptSelf([2, 5])).toEqual([5, 2]);
  });

  it("two zeros", () => {
    expect(productExceptSelf([0, 4, 0])).toEqual([0, 0, 0]);
  });
});
