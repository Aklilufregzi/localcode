"""
LeetCode 56. Merge Intervals (Medium)
https://leetcode.com/problems/merge-intervals/

Given an array of intervals, merge all overlapping intervals and return
an array of the non-overlapping intervals that cover all the input.

Run just this file:   python intervals/merge_intervals.py
Run its tests:        pytest intervals/merge_intervals.py -v
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------
# Result order isn't specified — sort before comparing.

def test_example_1():
    result = Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    assert sorted(result) == [[1, 6], [8, 10], [15, 18]]


def test_example_2():
    # [1,4] and [4,5] touch at 4 and are considered overlapping.
    assert sorted(Solution().merge([[1, 4], [4, 5]])) == [[1, 5]]


def test_single_interval():
    assert Solution().merge([[1, 4]]) == [[1, 4]]


def test_contained_interval():
    assert sorted(Solution().merge([[1, 10], [2, 3]])) == [[1, 10]]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # expected [[1, 6], [8, 10], [15, 18]]
