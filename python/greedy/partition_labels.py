"""
LeetCode 763. Partition Labels (Medium)
https://leetcode.com/problems/partition-labels/

Partition the string s into as many parts as possible so that each letter
appears in at most one part; concatenating the parts in order must give s.
Return a list of the sizes of these parts.

Run just this file:   python greedy/partition_labels.py
Run its tests:        pytest greedy/partition_labels.py -v
"""


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]


def test_example_2():
    assert Solution().partitionLabels("eccbbbbdec") == [10]


def test_all_distinct():
    assert Solution().partitionLabels("abc") == [1, 1, 1]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))  # expected [9, 7, 8]
