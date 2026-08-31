import { describe, expect, it } from "vitest";
import { arrayToList, listToArray } from "../helpers.ts";
import { mergeTwoLists } from "./merge-two-sorted-lists.ts";

describe("mergeTwoLists", () => {
  it("example 1", () => {
    const merged = mergeTwoLists(arrayToList([1, 2, 4]), arrayToList([1, 3, 4]));
    expect(listToArray(merged)).toEqual([1, 1, 2, 3, 4, 4]);
  });

  it("example 2: both empty", () => {
    expect(mergeTwoLists(null, null)).toBeNull();
  });

  it("example 3: one empty", () => {
    const merged = mergeTwoLists(null, arrayToList([0]));
    expect(listToArray(merged)).toEqual([0]);
  });
});
