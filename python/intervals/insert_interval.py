"""
LeetCode 57. Insert Interval (Medium)
https://leetcode.com/problems/insert-interval/

Given non-overlapping intervals sorted by start, insert newInterval into
intervals so the result is still sorted and non-overlapping (merge where
necessary), and return it.

Run just this file:   python intervals/insert_interval.py
Run its tests:        pytest intervals/insert_interval.py -v
"""


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]


def test_example_2():
    assert Solution().insert(
        [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
    ) == [[1, 2], [3, 10], [12, 16]]


def test_empty_intervals():
    assert Solution().insert([], [5, 7]) == [[5, 7]]


def test_insert_before_all():
    assert Solution().insert([[3, 5], [12, 15]], [1, 2]) == [[1, 2], [3, 5], [12, 15]]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.insert([[1, 3], [6, 9]], [2, 5]))  # expected [[1, 5], [6, 9]]
