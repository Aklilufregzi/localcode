"""
LeetCode 130. Surrounded Regions (Medium)
https://leetcode.com/problems/surrounded-regions/

Given an m x n board of "X" and "O", capture every region of "O"s that is
fully surrounded by "X"s by flipping those "O"s to "X" IN PLACE. A region
touching the border is not surrounded and stays "O".

Run just this file:   python graphs/surrounded_regions.py
Run its tests:        pytest graphs/surrounded_regions.py -v
"""


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """Do not return anything, modify board in-place instead."""
        ...  # TODO: implement


# ---------------------------- tests ----------------------------
# In-place problem: call solve(), then assert on the mutated board.

def test_example_1():
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    Solution().solve(board)
    assert board == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]


def test_example_2_single_cell():
    board = [["X"]]
    Solution().solve(board)
    assert board == [["X"]]


def test_border_region_survives():
    board = [
        ["O", "O"],
        ["O", "O"],
    ]
    Solution().solve(board)
    assert board == [
        ["O", "O"],
        ["O", "O"],
    ]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    s.solve(board)
    print(board)  # expected [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
