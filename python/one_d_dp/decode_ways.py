"""
LeetCode 91. Decode Ways (Medium)
https://leetcode.com/problems/decode-ways/

A message of letters A-Z is encoded as digits "1"-"26". Given a digit
string s, return the number of ways to decode it ("0" alone or a leading
zero in a pair is invalid).

Run just this file:   python one_d_dp/decode_ways.py
Run its tests:        pytest one_d_dp/decode_ways.py -v
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().numDecodings("12") == 2


def test_example_2():
    assert Solution().numDecodings("226") == 3


def test_example_3():
    assert Solution().numDecodings("06") == 0


def test_leading_zero():
    assert Solution().numDecodings("0") == 0


def test_ten():
    assert Solution().numDecodings("10") == 1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.numDecodings("12"))   # expected 2
    print(s.numDecodings("226"))  # expected 3
