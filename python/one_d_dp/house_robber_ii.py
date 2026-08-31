"""
LeetCode 213. House Robber II (Medium)
https://leetcode.com/problems/house-robber-ii/

Same as House Robber, but the houses are arranged in a circle: the
first and last houses are adjacent. Return the max amount you can rob
without robbing two adjacent houses.

Run just this file:   python one_d_dp/house_robber_ii.py
Run its tests:        pytest one_d_dp/house_robber_ii.py -v
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().rob([2, 3, 2]) == 3


def test_example_2():
    assert Solution().rob([1, 2, 3, 1]) == 4


def test_example_3():
    assert Solution().rob([1, 2, 3]) == 3


def test_single_house():
    assert Solution().rob([7]) == 7


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.rob([2, 3, 2]))     # expected 3
    print(s.rob([1, 2, 3, 1]))  # expected 4
