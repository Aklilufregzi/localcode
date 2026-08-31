"""
LeetCode 269. Alien Dictionary (Hard, premium — NeetCode version)
https://leetcode.com/problems/alien-dictionary/
https://neetcode.io/problems/foreign-dictionary

There is a foreign language that uses the latin alphabet, but with an unknown
letter order. You get a list of words sorted lexicographically by that order.
Return a string of the language's letters sorted in its order (any valid order
if several exist). Return "" if the ordering is invalid / contradictory.

Run just this file:   python advanced_graphs/alien_dictionary.py
Run its tests:        pytest advanced_graphs/alien_dictionary.py -v
"""


class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def _is_valid_order(order: str, words: list[str]) -> bool:
    """True iff `order` contains each letter of `words` exactly once and is
    consistent with every adjacent word pair (multiple valid orders exist)."""
    letters = {c for w in words for c in w}
    if not isinstance(order, str) or len(order) != len(letters) or set(order) != letters:
        return False
    rank = {c: i for i, c in enumerate(order)}
    for w1, w2 in zip(words, words[1:]):
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if rank[c1] > rank[c2]:
                    return False
                break
        else:
            if len(w1) > len(w2):  # prefix rule violated by the input itself
                return False
    return True


def test_example_1():
    words = ["z", "o"]
    assert _is_valid_order(Solution().foreignDictionary(words), words)


def test_example_2():
    words = ["hrn", "hrf", "er", "enn", "rfnn"]
    assert _is_valid_order(Solution().foreignDictionary(words), words)


def test_cycle_is_invalid():
    assert Solution().foreignDictionary(["z", "x", "z"]) == ""


def test_prefix_violation_is_invalid():
    # "abc" before its own prefix "ab" is impossible in any letter order.
    assert Solution().foreignDictionary(["abc", "ab"]) == ""


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.foreignDictionary(["z", "o"]))                            # expected "zo"
    print(s.foreignDictionary(["hrn", "hrf", "er", "enn", "rfnn"]))   # expected "hernf"
    print(s.foreignDictionary(["z", "x", "z"]))                       # expected ""
