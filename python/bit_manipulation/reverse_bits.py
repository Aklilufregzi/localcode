"""
LeetCode 190. Reverse Bits (Easy)
https://leetcode.com/problems/reverse-bits/

Reverse the bits of a given 32-bit unsigned integer and return the
resulting unsigned integer.

Run just this file:   python bit_manipulation/reverse_bits.py
Run its tests:        pytest bit_manipulation/reverse_bits.py -v
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # 00000010100101000001111010011100 -> 00111001011110000010100101000000
    assert Solution().reverseBits(43261596) == 964176192


def test_example_2():
    # 11111111111111111111111111111101 -> 10111111111111111111111111111111
    assert Solution().reverseBits(4294967293) == 3221225471


def test_zero():
    assert Solution().reverseBits(0) == 0


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.reverseBits(43261596))  # expected 964176192
