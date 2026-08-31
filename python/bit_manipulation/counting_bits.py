"""
LeetCode 338. Counting Bits (Easy)
https://leetcode.com/problems/counting-bits/

Given an integer n, return an array ans of length n + 1 where ans[i] is
the number of 1s in the binary representation of i.

Run just this file:   python bit_manipulation/counting_bits.py
Run its tests:        pytest bit_manipulation/counting_bits.py -v
"""


class Solution:
    def countBits(self, n: int) -> list[int]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().countBits(2) == [0, 1, 1]


def test_example_2():
    assert Solution().countBits(5) == [0, 1, 1, 2, 1, 2]


def test_zero():
    assert Solution().countBits(0) == [0]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.countBits(5))  # expected [0, 1, 1, 2, 1, 2]
