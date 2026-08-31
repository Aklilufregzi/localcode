import { describe, expect, it } from "vitest";
import { maxProfit } from "./best-time-to-buy-and-sell-stock-with-cooldown.ts";

describe("maxProfit (with cooldown)", () => {
  it("example 1", () => {
    // buy day0(1), sell day1(2), cooldown, buy day3(0), sell day4(2) -> 3
    expect(maxProfit([1, 2, 3, 0, 2])).toBe(3);
  });

  it("example 2", () => {
    expect(maxProfit([1])).toBe(0);
  });

  it("decreasing prices", () => {
    expect(maxProfit([5, 4, 3, 2, 1])).toBe(0);
  });

  it("two days", () => {
    expect(maxProfit([1, 5])).toBe(4);
  });
});
