"""
LeetCode 215. Kth Largest Element in an Array (Medium)
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element
in the array (in sorted order, duplicates counted). Solve without fully
sorting if you can.

Run just this file:   python heap/kth_largest_element_in_an_array.py
Run its tests:        pytest heap/kth_largest_element_in_an_array.py -v
"""


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5


def test_example_2():
    assert Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


def test_single_element():
    assert Solution().findKthLargest([1], 1) == 1


def test_k_equals_length():
    assert Solution().findKthLargest([7, 6, 5], 3) == 5


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))           # expected 5
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # expected 4
