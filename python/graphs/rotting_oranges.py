"""
LeetCode 994. Rotting Oranges (Medium)
https://leetcode.com/problems/rotting-oranges/

In a grid, 0 = empty, 1 = fresh orange, 2 = rotten orange. Every minute, any
fresh orange 4-directionally adjacent to a rotten one becomes rotten. Return
the minimum minutes until no fresh orange remains, or -1 if impossible.

Run just this file:   python graphs/rotting_oranges.py
Run its tests:        pytest graphs/rotting_oranges.py -v
"""


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4


def test_example_2_unreachable_orange():
    assert Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1


def test_example_3_no_fresh_oranges():
    assert Solution().orangesRotting([[0, 2]]) == 0


def test_empty_grid_cell_only():
    assert Solution().orangesRotting([[0]]) == 0


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # expected 4
