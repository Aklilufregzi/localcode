import { describe, expect, it } from "vitest";
import { isAnagram } from "./valid-anagram.ts";

describe("isAnagram", () => {
  it("example 1", () => {
    expect(isAnagram("anagram", "nagaram")).toBe(true);
  });

  it("example 2", () => {
    expect(isAnagram("rat", "car")).toBe(false);
  });

  it("different lengths", () => {
    expect(isAnagram("a", "ab")).toBe(false);
  });

  it("same letters different counts", () => {
    expect(isAnagram("aabb", "abbb")).toBe(false);
  });
});
