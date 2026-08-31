"""
LeetCode 329. Longest Increasing Path in a Matrix (Hard)
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Given an m x n integer matrix, return the length of the longest strictly
increasing path. From each cell you can move up, down, left, or right
(no diagonals, no wrap-around).

Run just this file:   python two_d_dp/longest_increasing_path_in_a_matrix.py
Run its tests:        pytest two_d_dp/longest_increasing_path_in_a_matrix.py -v
"""


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # Longest path is [1, 2, 6, 9]
    assert Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4


def test_example_2():
    # Longest path is [3, 4, 5, 6]; diagonal moves not allowed
    assert Solution().longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4


def test_example_3_single_cell():
    assert Solution().longestIncreasingPath([[1]]) == 1


def test_all_equal():
    assert Solution().longestIncreasingPath([[7, 7], [7, 7]]) == 1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))  # expected 4
    print(s.longestIncreasingPath([[1]]))                              # expected 1
