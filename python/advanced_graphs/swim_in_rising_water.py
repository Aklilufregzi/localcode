"""
LeetCode 778. Swim in Rising Water (Hard)
https://leetcode.com/problems/swim-in-rising-water/

You are given an n x n grid where grid[r][c] is the elevation at (r, c). At
time t you can swim through any cell with elevation <= t (moving 4-way).
Return the least time t at which you can travel from (0, 0) to (n-1, n-1).

Run just this file:   python advanced_graphs/swim_in_rising_water.py
Run its tests:        pytest advanced_graphs/swim_in_rising_water.py -v
"""


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().swimInWater([[0, 2], [1, 3]]) == 3


def test_example_2():
    grid = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6],
    ]
    assert Solution().swimInWater(grid) == 16


def test_single_cell():
    assert Solution().swimInWater([[0]]) == 0


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.swimInWater([[0, 2], [1, 3]]))  # expected 3
