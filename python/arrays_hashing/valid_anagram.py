"""
LeetCode 242. Valid Anagram (Easy)
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s
(same characters with the same counts, rearranged), false otherwise.

Run just this file:   python arrays_hashing/valid_anagram.py
Run its tests:        pytest arrays_hashing/valid_anagram.py -v
Run everything:       pytest
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().isAnagram("anagram", "nagaram") is True


def test_example_2():
    assert Solution().isAnagram("rat", "car") is False


def test_different_lengths():
    assert Solution().isAnagram("a", "ab") is False


def test_same_letters_different_counts():
    assert Solution().isAnagram("aabb", "abbb") is False


if __name__ == "__main__":
    # Quick manual run / debugging playground — set breakpoints here.
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))  # expected True
    print(s.isAnagram("rat", "car"))          # expected False
