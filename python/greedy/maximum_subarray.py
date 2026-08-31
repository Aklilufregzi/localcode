"""
LeetCode 53. Maximum Subarray (Medium)
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the subarray (contiguous, non-empty)
with the largest sum, and return its sum.

Run just this file:   python greedy/maximum_subarray.py
Run its tests:        pytest greedy/maximum_subarray.py -v
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_example_2():
    assert Solution().maxSubArray([1]) == 1


def test_example_3():
    assert Solution().maxSubArray([5, 4, -1, 7, 8]) == 23


def test_all_negative():
    assert Solution().maxSubArray([-3, -2, -5]) == -2


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expected 6
