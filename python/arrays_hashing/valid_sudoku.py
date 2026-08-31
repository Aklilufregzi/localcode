"""
LeetCode 36. Valid Sudoku (Medium)
https://leetcode.com/problems/valid-sudoku/

Determine if a 9x9 Sudoku board is valid: each row, each column, and each
of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.
Only filled cells ('.') need to be validated; the board need not be solvable.

Run just this file:   python arrays_hashing/valid_sudoku.py
Run its tests:        pytest arrays_hashing/valid_sudoku.py -v
Run everything:       pytest
"""


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

VALID_BOARD = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

# Same board with the top-left 5 changed to 8: the column has no clash, but
# there are two 8's in the top-left 3x3 box (and in column 0).
INVALID_BOARD = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


def test_example_1_valid():
    assert Solution().isValidSudoku(VALID_BOARD) is True


def test_example_2_invalid():
    assert Solution().isValidSudoku(INVALID_BOARD) is False


def test_row_duplicate():
    board = [["." for _ in range(9)] for _ in range(9)]
    board[0][0] = "1"
    board[0][8] = "1"
    assert Solution().isValidSudoku(board) is False


def test_empty_board():
    board = [["." for _ in range(9)] for _ in range(9)]
    assert Solution().isValidSudoku(board) is True


if __name__ == "__main__":
    # Quick manual run / debugging playground — set breakpoints here.
    s = Solution()
    print(s.isValidSudoku(VALID_BOARD))    # expected True
    print(s.isValidSudoku(INVALID_BOARD))  # expected False
