import { describe, expect, it } from "vitest";
import { arrayToList, listToArray } from "../helpers.ts";
import { reorderList } from "./reorder-list.ts";

describe("reorderList", () => {
  // In-place problem: call the function, then assert on the mutated list.
  it("example 1", () => {
    const head = arrayToList([1, 2, 3, 4]);
    reorderList(head);
    expect(listToArray(head)).toEqual([1, 4, 2, 3]);
  });

  it("example 2", () => {
    const head = arrayToList([1, 2, 3, 4, 5]);
    reorderList(head);
    expect(listToArray(head)).toEqual([1, 5, 2, 4, 3]);
  });

  it("two nodes", () => {
    const head = arrayToList([1, 2]);
    reorderList(head);
    expect(listToArray(head)).toEqual([1, 2]);
  });

  it("single node", () => {
    const head = arrayToList([1]);
    reorderList(head);
    expect(listToArray(head)).toEqual([1]);
  });
});
