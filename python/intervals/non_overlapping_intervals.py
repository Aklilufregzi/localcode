"""
LeetCode 435. Non-overlapping Intervals (Medium)
https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals, return the minimum number of intervals you
must remove so that the rest are non-overlapping. Intervals that only
touch (e.g. [1,2] and [2,3]) are non-overlapping.

Run just this file:   python intervals/non_overlapping_intervals.py
Run its tests:        pytest intervals/non_overlapping_intervals.py -v
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1


def test_example_2():
    assert Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2


def test_example_3():
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 3]]) == 0


def test_single_interval():
    assert Solution().eraseOverlapIntervals([[1, 100]]) == 0


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # expected 1
