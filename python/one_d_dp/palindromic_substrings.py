"""
LeetCode 647. Palindromic Substrings (Medium)
https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.
Substrings with different start/end positions count separately even
if they are equal as strings.

Run just this file:   python one_d_dp/palindromic_substrings.py
Run its tests:        pytest one_d_dp/palindromic_substrings.py -v
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().countSubstrings("abc") == 3


def test_example_2():
    assert Solution().countSubstrings("aaa") == 6


def test_single_char():
    assert Solution().countSubstrings("a") == 1


def test_mixed():
    # "abba": a, b, b, a, bb, abba -> 6
    assert Solution().countSubstrings("abba") == 6


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.countSubstrings("abc"))  # expected 3
    print(s.countSubstrings("aaa"))  # expected 6
