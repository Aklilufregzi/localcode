"""
LeetCode 1851. Minimum Interval to Include Each Query (Hard)
https://leetcode.com/problems/minimum-interval-to-include-each-query/

Given intervals [left, right] and queries, answer each query q with the
size (right - left + 1) of the smallest interval containing q
(left <= q <= right), or -1 if no such interval exists.

Run just this file:   python intervals/minimum_interval_to_include_each_query.py
Run its tests:        pytest intervals/minimum_interval_to_include_each_query.py -v
"""


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------
# Answers must line up with the queries in their given order.

def test_example_1():
    assert Solution().minInterval(
        [[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]
    ) == [3, 3, 1, 4]


def test_example_2():
    assert Solution().minInterval(
        [[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]
    ) == [2, -1, 4, 6]


def test_no_interval_matches():
    assert Solution().minInterval([[5, 10]], [1, 11]) == [-1, -1]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]))  # expected [3, 3, 1, 4]
