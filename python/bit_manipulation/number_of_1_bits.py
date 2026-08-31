"""
LeetCode 191. Number of 1 Bits (Easy)
https://leetcode.com/problems/number-of-1-bits/

Given a positive integer n, return the number of set bits (1s) in its
binary representation (the Hamming weight).

Run just this file:   python bit_manipulation/number_of_1_bits.py
Run its tests:        pytest bit_manipulation/number_of_1_bits.py -v
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().hammingWeight(11) == 3  # 1011


def test_example_2():
    assert Solution().hammingWeight(128) == 1  # 10000000


def test_example_3():
    assert Solution().hammingWeight(2147483645) == 30


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.hammingWeight(11))  # expected 3
