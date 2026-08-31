"""
LeetCode 704. Binary Search (Easy)
https://leetcode.com/problems/binary-search/

Given a sorted (ascending) array of distinct integers and a target,
return the index of target if it exists, otherwise -1.
Must run in O(log n) time.

Run just this file:   python binary_search/binary_search.py
Run its tests:        pytest binary_search/binary_search.py -v
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4


def test_example_2():
    assert Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1


def test_single_element_found():
    assert Solution().search([5], 5) == 0


def test_single_element_not_found():
    assert Solution().search([5], -5) == -1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 9))  # expected 4
    print(s.search([-1, 0, 3, 5, 9, 12], 2))  # expected -1
