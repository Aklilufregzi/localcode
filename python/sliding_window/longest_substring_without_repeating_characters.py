"""
LeetCode 3. Longest Substring Without Repeating Characters (Medium)
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring (contiguous)
without duplicate characters.

Run just this file:   python sliding_window/longest_substring_without_repeating_characters.py
Run its tests:        pytest sliding_window/longest_substring_without_repeating_characters.py -v
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # "abc" has length 3.
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3


def test_example_2():
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1


def test_example_3():
    # "wke" has length 3 ("pwke" is a subsequence, not a substring).
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3


def test_empty_string():
    assert Solution().lengthOfLongestSubstring("") == 0


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))  # expected 3
    print(s.lengthOfLongestSubstring("pwwkew"))    # expected 3
