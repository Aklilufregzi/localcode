import { describe, expect, it } from "vitest";
import { isValidSudoku } from "./valid-sudoku.ts";

const VALID_BOARD = [
  ["5", "3", ".", ".", "7", ".", ".", ".", "."],
  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
  [".", "9", "8", ".", ".", ".", ".", "6", "."],
  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
  [".", "6", ".", ".", ".", ".", "2", "8", "."],
  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
  [".", ".", ".", ".", "8", ".", ".", "7", "9"],
];

// Same board with the top-left 5 changed to 8: two 8's in the top-left
// 3x3 box (and in column 0).
const INVALID_BOARD = [
  ["8", "3", ".", ".", "7", ".", ".", ".", "."],
  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
  [".", "9", "8", ".", ".", ".", ".", "6", "."],
  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
  [".", "6", ".", ".", ".", ".", "2", "8", "."],
  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
  [".", ".", ".", ".", "8", ".", ".", "7", "9"],
];

function emptyBoard(): string[][] {
  return Array.from({ length: 9 }, () => Array<string>(9).fill("."));
}

describe("isValidSudoku", () => {
  it("example 1 (valid)", () => {
    expect(isValidSudoku(VALID_BOARD)).toBe(true);
  });

  it("example 2 (invalid)", () => {
    expect(isValidSudoku(INVALID_BOARD)).toBe(false);
  });

  it("row duplicate", () => {
    const board = emptyBoard();
    board[0]![0] = "1";
    board[0]![8] = "1";
    expect(isValidSudoku(board)).toBe(false);
  });

  it("empty board", () => {
    expect(isValidSudoku(emptyBoard())).toBe(true);
  });
});
