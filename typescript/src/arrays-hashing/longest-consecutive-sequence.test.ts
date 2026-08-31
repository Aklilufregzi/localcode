import { describe, expect, it } from "vitest";
import { longestConsecutive } from "./longest-consecutive-sequence.ts";

describe("longestConsecutive", () => {
  it("example 1", () => {
    // 1, 2, 3, 4
    expect(longestConsecutive([100, 4, 200, 1, 3, 2])).toBe(4);
  });

  it("example 2", () => {
    // 0..8
    expect(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])).toBe(9);
  });

  it("example 3", () => {
    // duplicates don't extend the run: 0, 1, 2
    expect(longestConsecutive([1, 0, 1, 2])).toBe(3);
  });

  it("empty array", () => {
    expect(longestConsecutive([])).toBe(0);
  });
});
