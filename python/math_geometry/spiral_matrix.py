"""
LeetCode 54. Spiral Matrix (Medium)
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all of its elements in spiral order
(right across the top, down the right side, left across the bottom,
up the left side, then inward).

Run just this file:   python math_geometry/spiral_matrix.py
Run its tests:        pytest math_geometry/spiral_matrix.py -v
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_example_2():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert Solution().spiralOrder(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


def test_single_cell():
    assert Solution().spiralOrder([[7]]) == [7]


def test_single_column():
    assert Solution().spiralOrder([[1], [2], [3]]) == [1, 2, 3]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # expected [1, 2, 3, 6, 9, 8, 7, 4, 5]
