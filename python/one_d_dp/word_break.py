"""
LeetCode 139. Word Break (Medium)
https://leetcode.com/problems/word-break/

Given a string s and a dictionary wordDict, return True if s can be
segmented into a space-separated sequence of one or more dictionary
words (words may be reused).

Run just this file:   python one_d_dp/word_break.py
Run its tests:        pytest one_d_dp/word_break.py -v
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().wordBreak("leetcode", ["leet", "code"]) is True


def test_example_2():
    assert Solution().wordBreak("applepenapple", ["apple", "pen"]) is True


def test_example_3():
    assert Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False


def test_single_word():
    assert Solution().wordBreak("a", ["a"]) is True


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]))  # expected True
    print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # expected False
