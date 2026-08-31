"""
LeetCode 1143. Longest Common Subsequence (Medium)
https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest
common subsequence (a sequence derived by deleting some or no characters
without changing the relative order of the rest). Return 0 if there is none.

Run just this file:   python two_d_dp/longest_common_subsequence.py
Run its tests:        pytest two_d_dp/longest_common_subsequence.py -v
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().longestCommonSubsequence("abcde", "ace") == 3


def test_example_2():
    assert Solution().longestCommonSubsequence("abc", "abc") == 3


def test_example_3():
    assert Solution().longestCommonSubsequence("abc", "def") == 0


def test_single_chars():
    assert Solution().longestCommonSubsequence("a", "a") == 1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.longestCommonSubsequence("abcde", "ace"))  # expected 3
    print(s.longestCommonSubsequence("abc", "def"))    # expected 0
