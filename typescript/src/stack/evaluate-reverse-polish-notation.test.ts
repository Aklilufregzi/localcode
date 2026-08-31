import { describe, expect, it } from "vitest";
import { evalRPN } from "./evaluate-reverse-polish-notation.ts";

describe("evalRPN", () => {
  it("example 1", () => {
    // (2 + 1) * 3 = 9
    expect(evalRPN(["2", "1", "+", "3", "*"])).toBe(9);
  });

  it("example 2", () => {
    // 4 + (13 / 5) = 4 + 2 = 6
    expect(evalRPN(["4", "13", "5", "/", "+"])).toBe(6);
  });

  it("example 3", () => {
    // ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22 (division truncates toward zero)
    expect(
      evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]),
    ).toBe(22);
  });

  it("single token", () => {
    expect(evalRPN(["18"])).toBe(18);
  });

  it("negative division truncates toward zero", () => {
    // -7 / 2 truncates to -3, not -4
    expect(evalRPN(["-7", "2", "/"])).toBe(-3);
  });
});
