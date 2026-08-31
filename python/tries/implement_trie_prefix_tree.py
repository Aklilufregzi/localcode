"""
LeetCode 208. Implement Trie (Prefix Tree) (Medium)
https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert(word), search(word) returning whether the exact
word was inserted, and startsWith(prefix) returning whether any inserted word
has the given prefix. Words consist of lowercase English letters.

Run just this file:   python tries/implement_trie_prefix_tree.py
Run its tests:        pytest tries/implement_trie_prefix_tree.py -v
"""


class Trie:
    def __init__(self):
        ...  # TODO: implement

    def insert(self, word: str) -> None:
        ...  # TODO: implement

    def search(self, word: str) -> bool:
        ...  # TODO: implement

    def startsWith(self, prefix: str) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_official_example():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True


def test_prefix_is_not_a_word():
    trie = Trie()
    trie.insert("car")
    assert trie.search("ca") is False
    assert trie.startsWith("ca") is True
    assert trie.startsWith("card") is False


def test_single_letter_word():
    trie = Trie()
    trie.insert("a")
    assert trie.search("a") is True
    assert trie.startsWith("a") is True
    assert trie.search("b") is False


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))     # expected True
    print(trie.search("app"))       # expected False
    print(trie.startsWith("app"))   # expected True
