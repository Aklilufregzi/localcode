"""
LeetCode 128. Longest Consecutive Sequence (Medium)
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted integer array nums, return the length of the longest run
of consecutive integers (values, not positions). Must run in O(n) time.

Run just this file:   python arrays_hashing/longest_consecutive_sequence.py
Run its tests:        pytest arrays_hashing/longest_consecutive_sequence.py -v
Run everything:       pytest
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # 1, 2, 3, 4
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4


def test_example_2():
    # 0..8
    assert Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_example_3():
    # duplicates don't extend the run: 0, 1, 2
    assert Solution().longestConsecutive([1, 0, 1, 2]) == 3


def test_empty():
    assert Solution().longestConsecutive([]) == 0


if __name__ == "__main__":
    # Quick manual run / debugging playground — set breakpoints here.
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))  # expected 4
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # expected 9
