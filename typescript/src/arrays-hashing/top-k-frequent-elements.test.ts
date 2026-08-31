import { describe, expect, it } from "vitest";
import { topKFrequent } from "./top-k-frequent-elements.ts";

describe("topKFrequent", () => {
  it("example 1", () => {
    // Order doesn't matter — compare sorted copies.
    expect([...topKFrequent([1, 1, 1, 2, 2, 3], 2)].sort((a, b) => a - b)).toEqual([1, 2]);
  });

  it("example 2", () => {
    expect([...topKFrequent([1], 1)].sort((a, b) => a - b)).toEqual([1]);
  });

  it("k equals distinct count", () => {
    expect([...topKFrequent([4, 4, 5, 5, 6], 3)].sort((a, b) => a - b)).toEqual([4, 5, 6]);
  });
});
