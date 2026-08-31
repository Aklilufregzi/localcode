"""
LeetCode 212. Word Search II (Hard)
https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of words, return all words that
can be constructed from sequentially adjacent cells (horizontally or
vertically neighboring); the same cell may not be used more than once per word.

Run just this file:   python tries/word_search_ii.py
Run its tests:        pytest tries/word_search_ii.py -v
"""


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    # Output order doesn't matter — normalize by sorting.
    assert sorted(Solution().findWords(board, words)) == ["eat", "oath"]


def test_example_2():
    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    assert Solution().findWords(board, words) == []


def test_single_cell_board():
    board = [["a"]]
    words = ["a", "b", "aa"]
    assert sorted(Solution().findWords(board, words)) == ["a"]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    print(s.findWords(board, ["oath", "pea", "eat", "rain"]))  # expected ["eat", "oath"] in any order
