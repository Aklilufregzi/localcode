import { describe, expect, it } from "vitest";
import { search } from "./binary-search.ts";

describe("search", () => {
  it("example 1", () => {
    expect(search([-1, 0, 3, 5, 9, 12], 9)).toBe(4);
  });

  it("example 2", () => {
    expect(search([-1, 0, 3, 5, 9, 12], 2)).toBe(-1);
  });

  it("single element found", () => {
    expect(search([5], 5)).toBe(0);
  });

  it("single element not found", () => {
    expect(search([5], -5)).toBe(-1);
  });
});
