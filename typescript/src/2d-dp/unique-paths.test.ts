import { describe, expect, it } from "vitest";
import { uniquePaths } from "./unique-paths.ts";

describe("uniquePaths", () => {
  it("example 1", () => {
    expect(uniquePaths(3, 7)).toBe(28);
  });

  it("example 2", () => {
    expect(uniquePaths(3, 2)).toBe(3);
  });

  it("single cell", () => {
    expect(uniquePaths(1, 1)).toBe(1);
  });

  it("single row", () => {
    expect(uniquePaths(1, 10)).toBe(1);
  });
});
