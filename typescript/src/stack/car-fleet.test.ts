import { describe, expect, it } from "vitest";
import { carFleet } from "./car-fleet.ts";

describe("carFleet", () => {
  it("example 1", () => {
    expect(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])).toBe(3);
  });

  it("example 2", () => {
    expect(carFleet(10, [3], [3])).toBe(1);
  });

  it("example 3", () => {
    // Cars starting at 0 and 2 merge at x=4; that fleet catches the car from 4 at x=6.
    expect(carFleet(100, [0, 2, 4], [4, 2, 1])).toBe(1);
  });

  it("no car catches up", () => {
    expect(carFleet(10, [6, 8], [3, 2])).toBe(2);
  });
});
