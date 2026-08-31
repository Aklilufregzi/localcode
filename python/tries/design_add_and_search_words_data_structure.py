"""
LeetCode 211. Design Add and Search Words Data Structure (Medium)
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure supporting addWord(word) and search(word), where
search may contain '.' wildcards that match any single letter. All other
characters are lowercase English letters.

Run just this file:   python tries/design_add_and_search_words_data_structure.py
Run its tests:        pytest tries/design_add_and_search_words_data_structure.py -v
"""


class WordDictionary:
    def __init__(self):
        ...  # TODO: implement

    def addWord(self, word: str) -> None:
        ...  # TODO: implement

    def search(self, word: str) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_official_example():
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True


def test_wildcard_length_must_match():
    wd = WordDictionary()
    wd.addWord("bad")
    assert wd.search("b.") is False
    assert wd.search("b...") is False
    assert wd.search("...") is True


def test_all_wildcards_empty_dictionary():
    wd = WordDictionary()
    assert wd.search(".") is False
    wd.addWord("a")
    assert wd.search(".") is True


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(wd.search("pad"))  # expected False
    print(wd.search("bad"))  # expected True
    print(wd.search(".ad"))  # expected True
    print(wd.search("b.."))  # expected True
