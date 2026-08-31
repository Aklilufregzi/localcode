"""
LeetCode 217. Contains Duplicate (Easy)
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least
twice in the array, and false if every element is distinct.

Run just this file:   python arrays_hashing/contains_duplicate.py
Run its tests:        pytest arrays_hashing/contains_duplicate.py -v
Run everything:       pytest
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().containsDuplicate([1, 2, 3, 1]) is True


def test_example_2():
    assert Solution().containsDuplicate([1, 2, 3, 4]) is False


def test_example_3():
    assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True


def test_single_element():
    assert Solution().containsDuplicate([7]) is False


if __name__ == "__main__":
    # Quick manual run / debugging playground — set breakpoints here.
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))  # expected True
    print(s.containsDuplicate([1, 2, 3, 4]))  # expected False
