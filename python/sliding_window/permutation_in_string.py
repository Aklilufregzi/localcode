"""
LeetCode 567. Permutation in String (Medium)
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1
as a substring, and false otherwise (i.e. some window of s2 is an anagram
of s1).

Run just this file:   python sliding_window/permutation_in_string.py
Run its tests:        pytest sliding_window/permutation_in_string.py -v
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # s2 contains "ba", a permutation of "ab".
    assert Solution().checkInclusion("ab", "eidbaooo") is True


def test_example_2():
    assert Solution().checkInclusion("ab", "eidboaoo") is False


def test_s1_longer_than_s2():
    assert Solution().checkInclusion("abc", "ab") is False


def test_exact_match():
    assert Solution().checkInclusion("adc", "dcda") is True


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo"))  # expected True
    print(s.checkInclusion("ab", "eidboaoo"))  # expected False
