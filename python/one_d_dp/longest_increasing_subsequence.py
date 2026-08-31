"""
LeetCode 300. Longest Increasing Subsequence (Medium)
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly
increasing subsequence (elements keep their relative order but need
not be contiguous).

Run just this file:   python one_d_dp/longest_increasing_subsequence.py
Run its tests:        pytest one_d_dp/longest_increasing_subsequence.py -v
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_example_2():
    assert Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4


def test_example_3():
    assert Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1


def test_single_element():
    assert Solution().lengthOfLIS([42]) == 1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # expected 4
    print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))            # expected 4
