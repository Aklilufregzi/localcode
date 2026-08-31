"""
LeetCode 42. Trapping Rain Water (Hard)
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it can trap after raining.

Run just this file:   python two_pointers/trapping_rain_water.py
Run its tests:        pytest two_pointers/trapping_rain_water.py -v
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_example_2():
    assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9


def test_no_water():
    # Monotonic elevation traps nothing.
    assert Solution().trap([1, 2, 3]) == 0


def test_single_bar():
    assert Solution().trap([5]) == 0


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # expected 6
    print(s.trap([4, 2, 0, 3, 2, 5]))                     # expected 9
