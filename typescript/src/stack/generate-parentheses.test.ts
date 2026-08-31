import { describe, expect, it } from "vitest";
import { generateParenthesis } from "./generate-parentheses.ts";

// Output order doesn't matter — compare sorted copies.
const sorted = (xs: string[]) => [...xs].sort();

describe("generateParenthesis", () => {
  it("example 1", () => {
    expect(sorted(generateParenthesis(3))).toEqual(
      sorted(["((()))", "(()())", "(())()", "()(())", "()()()"]),
    );
  });

  it("example 2", () => {
    expect(sorted(generateParenthesis(1))).toEqual(["()"]);
  });

  it("n = 2", () => {
    expect(sorted(generateParenthesis(2))).toEqual(sorted(["(())", "()()"]));
  });
});
