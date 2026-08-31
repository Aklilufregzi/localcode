"""
LeetCode 76. Minimum Window Substring (Hard)
https://leetcode.com/problems/minimum-window-substring/

Given strings s and t, return the minimum window substring of s that contains
every character of t (including duplicates). If there is no such substring,
return the empty string "". The answer is guaranteed to be unique.

Run just this file:   python sliding_window/minimum_window_substring.py
Run its tests:        pytest sliding_window/minimum_window_substring.py -v
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"


def test_example_2():
    assert Solution().minWindow("a", "a") == "a"


def test_example_3():
    # t needs two 'a's but s has only one.
    assert Solution().minWindow("a", "aa") == ""


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))  # expected "BANC"
    print(s.minWindow("a", "aa"))               # expected ""
