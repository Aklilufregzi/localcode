import { describe, expect, it } from "vitest";
import { isValid } from "./valid-parentheses.ts";

describe("isValid", () => {
  it("example 1", () => {
    expect(isValid("()")).toBe(true);
  });

  it("example 2", () => {
    expect(isValid("()[]{}")).toBe(true);
  });

  it("example 3", () => {
    expect(isValid("(]")).toBe(false);
  });

  it("wrong nesting order", () => {
    expect(isValid("([)]")).toBe(false);
  });

  it("single open bracket", () => {
    expect(isValid("(")).toBe(false);
  });
});
