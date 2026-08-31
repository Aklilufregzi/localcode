"""
LeetCode 127. Word Ladder (Hard)
https://leetcode.com/problems/word-ladder/

Given beginWord, endWord, and a wordList, return the number of words in the
SHORTEST transformation sequence from beginWord to endWord (each step changes
exactly one letter and must be in wordList; beginWord need not be). Return 0
if no such sequence exists.

Run just this file:   python graphs/word_ladder.py
Run its tests:        pytest graphs/word_ladder.py -v
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    # hit -> hot -> dot -> dog -> cog (5 words)
    assert Solution().ladderLength("hit", "cog", words) == 5


def test_example_2_end_word_missing():
    words = ["hot", "dot", "dog", "lot", "log"]
    assert Solution().ladderLength("hit", "cog", words) == 0


def test_one_step():
    assert Solution().ladderLength("a", "c", ["a", "b", "c"]) == 2


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # expected 5
