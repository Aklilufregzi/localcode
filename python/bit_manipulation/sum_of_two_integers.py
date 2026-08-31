"""
LeetCode 371. Sum of Two Integers (Medium)
https://leetcode.com/problems/sum-of-two-integers/

Given two integers a and b, return their sum without using the operators
+ and - (use bitwise operations instead).

Run just this file:   python bit_manipulation/sum_of_two_integers.py
Run its tests:        pytest bit_manipulation/sum_of_two_integers.py -v
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().getSum(1, 2) == 3


def test_example_2():
    assert Solution().getSum(2, 3) == 5


def test_negative_cancels():
    assert Solution().getSum(-1, 1) == 0


def test_negative_result():
    assert Solution().getSum(-2, -3) == -5


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.getSum(1, 2))  # expected 3
    print(s.getSum(-2, -3))  # expected -5
