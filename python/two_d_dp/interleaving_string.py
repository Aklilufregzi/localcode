"""
LeetCode 97. Interleaving String (Medium)
https://leetcode.com/problems/interleaving-string/

Given strings s1, s2, s3, return true if s3 is formed by an interleaving of
s1 and s2: s3 uses all characters of s1 and s2, keeping the relative order
within each source string.

Run just this file:   python two_d_dp/interleaving_string.py
Run its tests:        pytest two_d_dp/interleaving_string.py -v
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") is True


def test_example_2():
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") is False


def test_example_3_all_empty():
    assert Solution().isInterleave("", "", "") is True


def test_length_mismatch():
    assert Solution().isInterleave("a", "b", "abc") is False


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # expected True
    print(s.isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # expected False
