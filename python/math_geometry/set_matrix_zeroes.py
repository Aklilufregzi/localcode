"""
LeetCode 73. Set Matrix Zeroes (Medium)
https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n matrix, if an element is 0, set its entire row and column to 0.
Do it IN PLACE (follow-up: O(1) extra space).

Run just this file:   python math_geometry/set_matrix_zeroes.py
Run its tests:        pytest math_geometry/set_matrix_zeroes.py -v
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """Do not return anything, modify matrix in-place instead."""
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


def test_example_2():
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Solution().setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]


def test_no_zeroes():
    matrix = [[1, 2], [3, 4]]
    Solution().setZeroes(matrix)
    assert matrix == [[1, 2], [3, 4]]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(m)
    print(m)  # expected [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
