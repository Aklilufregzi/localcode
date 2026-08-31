import { describe, expect, it } from "vitest";
import { longestCommonSubsequence } from "./longest-common-subsequence.ts";

describe("longestCommonSubsequence", () => {
  it("example 1", () => {
    expect(longestCommonSubsequence("abcde", "ace")).toBe(3);
  });

  it("example 2", () => {
    expect(longestCommonSubsequence("abc", "abc")).toBe(3);
  });

  it("example 3", () => {
    expect(longestCommonSubsequence("abc", "def")).toBe(0);
  });

  it("single chars", () => {
    expect(longestCommonSubsequence("a", "a")).toBe(1);
  });
});
