import { describe, expect, it } from "vitest";
import { dailyTemperatures } from "./daily-temperatures.ts";

describe("dailyTemperatures", () => {
  it("example 1", () => {
    expect(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])).toEqual([
      1, 1, 4, 2, 1, 1, 0, 0,
    ]);
  });

  it("example 2", () => {
    expect(dailyTemperatures([30, 40, 50, 60])).toEqual([1, 1, 1, 0]);
  });

  it("example 3", () => {
    expect(dailyTemperatures([30, 60, 90])).toEqual([1, 1, 0]);
  });

  it("single day", () => {
    expect(dailyTemperatures([50])).toEqual([0]);
  });
});
