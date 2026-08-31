"""
LeetCode 11. Container With Most Water (Medium)
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n; the i-th line goes from
(i, 0) to (i, height[i]). Find two lines that together with the x-axis form
a container holding the most water, and return that maximum amount
(area = width * min of the two heights). You may not slant the container.

Run just this file:   python two_pointers/container_with_most_water.py
Run its tests:        pytest two_pointers/container_with_most_water.py -v
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # Lines at indices 1 (h=8) and 8 (h=7): width 7 * min(8, 7) = 49.
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example_2():
    assert Solution().maxArea([1, 1]) == 1


def test_increasing_heights():
    # Best pair is indices 1 and 4: width 3 * min(2, 5) = 6 (ties with 2 and 4).
    assert Solution().maxArea([1, 2, 3, 4, 5]) == 6


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # expected 49
