import { describe, expect, it } from "vitest";
import { longestIncreasingPath } from "./longest-increasing-path-in-a-matrix.ts";

describe("longestIncreasingPath", () => {
  it("example 1", () => {
    // Longest path is [1, 2, 6, 9]
    expect(longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])).toBe(4);
  });

  it("example 2", () => {
    // Longest path is [3, 4, 5, 6]; diagonal moves not allowed
    expect(longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]])).toBe(4);
  });

  it("example 3: single cell", () => {
    expect(longestIncreasingPath([[1]])).toBe(1);
  });

  it("all equal", () => {
    expect(longestIncreasingPath([[7, 7], [7, 7]])).toBe(1);
  });
});
