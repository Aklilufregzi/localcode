import { describe, expect, it } from "vitest";
import { arrayToList, listToArray } from "../helpers.ts";
import { addTwoNumbers } from "./add-two-numbers.ts";

describe("addTwoNumbers", () => {
  it("example 1", () => {
    // 342 + 465 = 807
    const result = addTwoNumbers(arrayToList([2, 4, 3]), arrayToList([5, 6, 4]));
    expect(listToArray(result)).toEqual([7, 0, 8]);
  });

  it("example 2", () => {
    expect(listToArray(addTwoNumbers(arrayToList([0]), arrayToList([0])))).toEqual([0]);
  });

  it("example 3", () => {
    // 9999999 + 9999 = 10009998
    const result = addTwoNumbers(arrayToList([9, 9, 9, 9, 9, 9, 9]), arrayToList([9, 9, 9, 9]));
    expect(listToArray(result)).toEqual([8, 9, 9, 9, 0, 0, 0, 1]);
  });

  it("carry extends length", () => {
    // 5 + 5 = 10
    expect(listToArray(addTwoNumbers(arrayToList([5]), arrayToList([5])))).toEqual([0, 1]);
  });
});
