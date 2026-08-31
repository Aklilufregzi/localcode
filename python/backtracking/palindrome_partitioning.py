"""
LeetCode 131. Palindrome Partitioning (Medium)
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition
is a palindrome. Return all possible palindrome partitionings of s.

Run just this file:   python backtracking/palindrome_partitioning.py
Run its tests:        pytest backtracking/palindrome_partitioning.py -v
"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------
# Outer order doesn't matter; each inner list is an ordered partition of s,
# so only the outer list is sorted before comparing.

def test_example_1():
    expected = [["a", "a", "b"], ["aa", "b"]]
    assert sorted(Solution().partition("aab")) == sorted(expected)


def test_example_2():
    assert Solution().partition("a") == [["a"]]


def test_all_same_letters():
    expected = [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
    assert sorted(Solution().partition("aaa")) == sorted(expected)


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.partition("aab"))  # expected [["a","a","b"],["aa","b"]] in any order
