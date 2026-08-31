"""
LeetCode 152. Maximum Product Subarray (Medium)
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a contiguous non-empty subarray with
the largest product and return that product.

Run just this file:   python one_d_dp/maximum_product_subarray.py
Run its tests:        pytest one_d_dp/maximum_product_subarray.py -v
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().maxProduct([2, 3, -2, 4]) == 6


def test_example_2():
    assert Solution().maxProduct([-2, 0, -1]) == 0


def test_single_negative():
    assert Solution().maxProduct([-3]) == -3


def test_two_negatives_multiply():
    # -4 * -3 = 12 beats any single element.
    assert Solution().maxProduct([-4, -3]) == 12


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.maxProduct([2, 3, -2, 4]))  # expected 6
    print(s.maxProduct([-2, 0, -1]))    # expected 0
