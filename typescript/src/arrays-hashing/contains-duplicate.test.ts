import { describe, expect, it } from "vitest";
import { containsDuplicate } from "./contains-duplicate.ts";

describe("containsDuplicate", () => {
  it("example 1", () => {
    expect(containsDuplicate([1, 2, 3, 1])).toBe(true);
  });

  it("example 2", () => {
    expect(containsDuplicate([1, 2, 3, 4])).toBe(false);
  });

  it("example 3", () => {
    expect(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])).toBe(true);
  });

  it("single element", () => {
    expect(containsDuplicate([7])).toBe(false);
  });
});
