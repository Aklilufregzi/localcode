import { describe, expect, it } from "vitest";
import { isInterleave } from "./interleaving-string.ts";

describe("isInterleave", () => {
  it("example 1", () => {
    expect(isInterleave("aabcc", "dbbca", "aadbbcbcac")).toBe(true);
  });

  it("example 2", () => {
    expect(isInterleave("aabcc", "dbbca", "aadbbbaccc")).toBe(false);
  });

  it("example 3: all empty", () => {
    expect(isInterleave("", "", "")).toBe(true);
  });

  it("length mismatch", () => {
    expect(isInterleave("a", "b", "abc")).toBe(false);
  });
});
