"""
LeetCode 48. Rotate Image (Medium)
https://leetcode.com/problems/rotate-image/

You are given an n x n matrix representing an image. Rotate the image by
90 degrees clockwise, IN PLACE (modify the input matrix directly; do not
allocate another 2D matrix).

Run just this file:   python math_geometry/rotate_image.py
Run its tests:        pytest math_geometry/rotate_image.py -v
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """Do not return anything, modify matrix in-place instead."""
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


def test_example_2():
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    Solution().rotate(matrix)
    assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]


def test_single_cell():
    matrix = [[1]]
    Solution().rotate(matrix)
    assert matrix == [[1]]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(m)
    print(m)  # expected [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
