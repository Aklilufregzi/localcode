"""
LeetCode 695. Max Area of Island (Medium)
https://leetcode.com/problems/max-area-of-island/

Given an m x n binary grid, return the area of the largest island (group of
1s connected 4-directionally). Return 0 if there is no island.

Run just this file:   python graphs/max_area_of_island.py
Run its tests:        pytest graphs/max_area_of_island.py -v
"""


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    assert Solution().maxAreaOfIsland(grid) == 6


def test_example_2_no_island():
    assert Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0


def test_single_cell_island():
    assert Solution().maxAreaOfIsland([[1]]) == 1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.maxAreaOfIsland([[1, 1, 0], [0, 1, 0], [0, 0, 1]]))  # expected 3
