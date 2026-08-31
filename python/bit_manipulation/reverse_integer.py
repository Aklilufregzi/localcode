"""
LeetCode 7. Reverse Integer (Medium)
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing causes the value to go outside [-2^31, 2^31 - 1], return 0.
Assume the environment does not allow storing 64-bit integers.

Run just this file:   python bit_manipulation/reverse_integer.py
Run its tests:        pytest bit_manipulation/reverse_integer.py -v
"""


class Solution:
    def reverse(self, x: int) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().reverse(123) == 321


def test_example_2():
    assert Solution().reverse(-123) == -321


def test_example_3():
    assert Solution().reverse(120) == 21


def test_overflow_returns_zero():
    # reversed 1534236469 -> 9646324351 > 2^31 - 1
    assert Solution().reverse(1534236469) == 0


def test_negative_overflow_returns_zero():
    # reversed -2147483648 -> -8463847412 < -2^31
    assert Solution().reverse(-2147483648) == 0


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.reverse(123))  # expected 321
    print(s.reverse(1534236469))  # expected 0
