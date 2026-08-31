import { describe, expect, it } from "vitest";
import { arrayToList, listToArray } from "../helpers.ts";
import { removeNthFromEnd } from "./remove-nth-node-from-end-of-list.ts";

describe("removeNthFromEnd", () => {
  it("example 1", () => {
    expect(listToArray(removeNthFromEnd(arrayToList([1, 2, 3, 4, 5]), 2))).toEqual([1, 2, 3, 5]);
  });

  it("example 2: single node", () => {
    expect(removeNthFromEnd(arrayToList([1]), 1)).toBeNull();
  });

  it("example 3: remove last", () => {
    expect(listToArray(removeNthFromEnd(arrayToList([1, 2]), 1))).toEqual([1]);
  });

  it("remove head", () => {
    expect(listToArray(removeNthFromEnd(arrayToList([1, 2]), 2))).toEqual([2]);
  });
});
