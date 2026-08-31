"""
LeetCode 5. Longest Palindromic Substring (Medium)
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Run just this file:   python one_d_dp/longest_palindromic_substring.py
Run its tests:        pytest one_d_dp/longest_palindromic_substring.py -v
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------
# Multiple valid answers are possible — assert membership in the valid set.

def test_example_1():
    assert Solution().longestPalindrome("babad") in {"bab", "aba"}


def test_example_2():
    assert Solution().longestPalindrome("cbbd") == "bb"


def test_single_char():
    assert Solution().longestPalindrome("a") == "a"


def test_whole_string_palindrome():
    assert Solution().longestPalindrome("racecar") == "racecar"


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.longestPalindrome("babad"))  # expected "bab" or "aba"
    print(s.longestPalindrome("cbbd"))   # expected "bb"
