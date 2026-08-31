"""
LeetCode 200. Number of Islands (Medium)
https://leetcode.com/problems/number-of-islands/

Given an m x n grid of "1"s (land) and "0"s (water), return the number of
islands. An island is surrounded by water and formed by connecting adjacent
land cells horizontally or vertically.

Run just this file:   python graphs/number_of_islands.py
Run its tests:        pytest graphs/number_of_islands.py -v
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert Solution().numIslands(grid) == 1


def test_example_2():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert Solution().numIslands(grid) == 3


def test_all_water():
    assert Solution().numIslands([["0", "0"], ["0", "0"]]) == 0


def test_single_land_cell():
    assert Solution().numIslands([["1"]]) == 1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(s.numIslands(grid))  # expected 3
