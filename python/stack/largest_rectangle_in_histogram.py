"""
LeetCode 84. Largest Rectangle in Histogram (Hard)
https://leetcode.com/problems/largest-rectangle-in-histogram/

Given an array of bar heights (each bar has width 1), return the area of
the largest rectangle that fits inside the histogram.

Run just this file:   python stack/largest_rectangle_in_histogram.py
Run its tests:        pytest stack/largest_rectangle_in_histogram.py -v
"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # Rectangle of height 5 spanning bars [5, 6] -> area 10.
    assert Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10


def test_example_2():
    assert Solution().largestRectangleArea([2, 4]) == 4


def test_single_bar():
    assert Solution().largestRectangleArea([7]) == 7


def test_increasing_then_decreasing():
    # Best is height 3 spanning the middle three bars -> 9.
    assert Solution().largestRectangleArea([1, 3, 5, 3, 1]) == 9


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # expected 10
