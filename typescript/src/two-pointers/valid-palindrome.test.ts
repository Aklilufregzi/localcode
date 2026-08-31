import { describe, expect, it } from "vitest";
import { isPalindrome } from "./valid-palindrome.ts";

describe("isPalindrome", () => {
  it("example 1", () => {
    expect(isPalindrome("A man, a plan, a canal: Panama")).toBe(true);
  });

  it("example 2", () => {
    expect(isPalindrome("race a car")).toBe(false);
  });

  it("example 3: only non-alphanumerics", () => {
    // After removing non-alphanumerics, s is empty, which is a palindrome.
    expect(isPalindrome(" ")).toBe(true);
  });

  it("single character", () => {
    expect(isPalindrome("a")).toBe(true);
  });
});
