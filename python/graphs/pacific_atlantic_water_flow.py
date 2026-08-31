"""
LeetCode 417. Pacific Atlantic Water Flow (Medium)
https://leetcode.com/problems/pacific-atlantic-water-flow/

Given an m x n heights grid, the Pacific touches the top and left edges and
the Atlantic the bottom and right edges. Water flows from a cell to a
4-directional neighbor of equal or lower height. Return all cells [r, c]
from which water can flow to BOTH oceans.

Run just this file:   python graphs/pacific_atlantic_water_flow.py
Run its tests:        pytest graphs/pacific_atlantic_water_flow.py -v
"""


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------
# Output order doesn't matter — both sides are sorted before comparing.

def test_example_1():
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    assert sorted(Solution().pacificAtlantic(heights)) == sorted(expected)


def test_example_2_single_cell():
    assert sorted(Solution().pacificAtlantic([[1]])) == [[0, 0]]


def test_flat_grid_all_cells():
    heights = [[1, 1], [1, 1]]
    expected = [[0, 0], [0, 1], [1, 0], [1, 1]]
    assert sorted(Solution().pacificAtlantic(heights)) == sorted(expected)


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    print(s.pacificAtlantic(heights))
    # expected (any order): [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
