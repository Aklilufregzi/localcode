"""
LeetCode 238. Product of Array Except Self (Medium)
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer where answer[i] is the
product of all elements of nums except nums[i]. Run in O(n) without using
the division operation.

Run just this file:   python arrays_hashing/product_of_array_except_self.py
Run its tests:        pytest arrays_hashing/product_of_array_except_self.py -v
Run everything:       pytest
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_example_2():
    assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_two_elements():
    assert Solution().productExceptSelf([2, 5]) == [5, 2]


def test_two_zeros():
    assert Solution().productExceptSelf([0, 4, 0]) == [0, 0, 0]


if __name__ == "__main__":
    # Quick manual run / debugging playground — set breakpoints here.
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))       # expected [24, 12, 8, 6]
    print(s.productExceptSelf([-1, 1, 0, -3, 3]))  # expected [0, 0, 9, 0, 0]
