"""
LeetCode 198. House Robber (Medium)
https://leetcode.com/problems/house-robber/

Given an array of money in each house along a street, return the max
amount you can rob without robbing two adjacent houses.

Run just this file:   python one_d_dp/house_robber.py
Run its tests:        pytest one_d_dp/house_robber.py -v
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().rob([1, 2, 3, 1]) == 4


def test_example_2():
    assert Solution().rob([2, 7, 9, 3, 1]) == 12


def test_single_house():
    assert Solution().rob([5]) == 5


def test_two_houses():
    assert Solution().rob([2, 10]) == 10


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.rob([1, 2, 3, 1]))     # expected 4
    print(s.rob([2, 7, 9, 3, 1]))  # expected 12
