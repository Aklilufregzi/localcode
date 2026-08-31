"""
LeetCode 62. Unique Paths (Medium)
https://leetcode.com/problems/unique-paths/

A robot starts at the top-left corner of an m x n grid and wants to reach
the bottom-right corner. It can only move down or right. Return the number
of possible unique paths.

Run just this file:   python two_d_dp/unique_paths.py
Run its tests:        pytest two_d_dp/unique_paths.py -v
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().uniquePaths(3, 7) == 28


def test_example_2():
    assert Solution().uniquePaths(3, 2) == 3


def test_single_cell():
    assert Solution().uniquePaths(1, 1) == 1


def test_single_row():
    assert Solution().uniquePaths(1, 10) == 1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.uniquePaths(3, 7))  # expected 28
    print(s.uniquePaths(3, 2))  # expected 3
