"""
LeetCode 79. Word Search (Medium)
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if
word exists in the grid, constructed from sequentially adjacent cells
(horizontally or vertically). The same cell may not be used more than once.

Run just this file:   python backtracking/word_search.py
Run its tests:        pytest backtracking/word_search.py -v
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

BOARD = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
]


def test_example_1():
    assert Solution().exist([row[:] for row in BOARD], "ABCCED") is True


def test_example_2():
    assert Solution().exist([row[:] for row in BOARD], "SEE") is True


def test_example_3():
    # "ABCB" would need to reuse the B cell.
    assert Solution().exist([row[:] for row in BOARD], "ABCB") is False


def test_single_cell():
    assert Solution().exist([["a"]], "a") is True


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.exist([row[:] for row in BOARD], "ABCCED"))  # expected True
    print(s.exist([row[:] for row in BOARD], "ABCB"))    # expected False
