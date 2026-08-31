"""
LeetCode 49. Group Anagrams (Medium)
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together.
Return the answer in any order (group order and in-group order are free).

Run just this file:   python arrays_hashing/group_anagrams.py
Run its tests:        pytest arrays_hashing/group_anagrams.py -v
Run everything:       pytest
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def normalize(groups: list[list[str]]) -> list[list[str]]:
    # Order doesn't matter (neither group order nor order within a group).
    return sorted(sorted(g) for g in groups)


def test_example_1():
    result = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert normalize(result) == normalize(expected)


def test_example_2():
    result = Solution().groupAnagrams([""])
    assert normalize(result) == [[""]]


def test_example_3():
    result = Solution().groupAnagrams(["a"])
    assert normalize(result) == [["a"]]


if __name__ == "__main__":
    # Quick manual run / debugging playground — set breakpoints here.
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # expected (any order): [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
