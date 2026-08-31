import { describe, expect, it } from "vitest";
import { arrayToList, listToArray } from "../helpers.ts";
import { reverseList } from "./reverse-linked-list.ts";

describe("reverseList", () => {
  it("example 1", () => {
    expect(listToArray(reverseList(arrayToList([1, 2, 3, 4, 5])))).toEqual([5, 4, 3, 2, 1]);
  });

  it("example 2", () => {
    expect(listToArray(reverseList(arrayToList([1, 2])))).toEqual([2, 1]);
  });

  it("example 3: empty list", () => {
    expect(reverseList(null)).toBeNull();
  });

  it("single node", () => {
    expect(listToArray(reverseList(arrayToList([7])))).toEqual([7]);
  });
});
