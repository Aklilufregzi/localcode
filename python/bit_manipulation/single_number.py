"""
LeetCode 136. Single Number (Easy)
https://leetcode.com/problems/single-number/

Every element in nums appears twice except for one, which appears once.
Find that single one. Must run in O(n) time and O(1) extra space.

Run just this file:   python bit_manipulation/single_number.py
Run its tests:        pytest bit_manipulation/single_number.py -v
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().singleNumber([2, 2, 1]) == 1


def test_example_2():
    assert Solution().singleNumber([4, 1, 2, 1, 2]) == 4


def test_example_3():
    assert Solution().singleNumber([1]) == 1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.singleNumber([4, 1, 2, 1, 2]))  # expected 4
