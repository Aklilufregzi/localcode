"""
LeetCode 268. Missing Number (Easy)
https://leetcode.com/problems/missing-number/

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Run just this file:   python bit_manipulation/missing_number.py
Run its tests:        pytest bit_manipulation/missing_number.py -v
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().missingNumber([3, 0, 1]) == 2


def test_example_2():
    assert Solution().missingNumber([0, 1]) == 2


def test_example_3():
    assert Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_single_zero_missing():
    assert Solution().missingNumber([1]) == 0


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.missingNumber([3, 0, 1]))  # expected 2
