import { describe, expect, it } from "vitest";
import { findWords } from "./word-search-ii.ts";

describe("findWords", () => {
  it("example 1", () => {
    const board = [
      ["o", "a", "a", "n"],
      ["e", "t", "a", "e"],
      ["i", "h", "k", "r"],
      ["i", "f", "l", "v"],
    ];
    // Output order doesn't matter — normalize by sorting.
    expect(findWords(board, ["oath", "pea", "eat", "rain"]).toSorted()).toEqual(["eat", "oath"]);
  });

  it("example 2", () => {
    const board = [
      ["a", "b"],
      ["c", "d"],
    ];
    expect(findWords(board, ["abcb"])).toEqual([]);
  });

  it("single cell board", () => {
    expect(findWords([["a"]], ["a", "b", "aa"]).toSorted()).toEqual(["a"]);
  });
});
