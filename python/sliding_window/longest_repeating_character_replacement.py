"""
LeetCode 424. Longest Repeating Character Replacement (Medium)
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s of uppercase English letters and an integer k. You
can choose any character and change it to any other uppercase letter, at most
k times total. Return the length of the longest substring containing the same
letter you can get after performing the operations.

Run just this file:   python sliding_window/longest_repeating_character_replacement.py
Run its tests:        pytest sliding_window/longest_repeating_character_replacement.py -v
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # Replace the two 'A's (or the two 'B's) to get "BBBB" (or "AAAA").
    assert Solution().characterReplacement("ABAB", 2) == 4


def test_example_2():
    # Replace the middle 'B' to get "AABAAA" -> longest run "AAAA" of length 4.
    assert Solution().characterReplacement("AABABBA", 1) == 4


def test_no_replacements_needed():
    assert Solution().characterReplacement("AAAA", 0) == 4


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.characterReplacement("ABAB", 2))     # expected 4
    print(s.characterReplacement("AABABBA", 1))  # expected 4
