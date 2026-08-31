"""
LeetCode 21. Merge Two Sorted Lists (Easy)
https://leetcode.com/problems/merge-two-sorted-lists/

Given the heads of two sorted linked lists list1 and list2, merge them
into one sorted list by splicing together their nodes, and return the
head of the merged list.

Run just this file:   python linked_list/merge_two_sorted_lists.py
Run its tests:        pytest linked_list/merge_two_sorted_lists.py -v
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import ListNode, list_to_linked, linked_to_list


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    merged = Solution().mergeTwoLists(list_to_linked([1, 2, 4]), list_to_linked([1, 3, 4]))
    assert linked_to_list(merged) == [1, 1, 2, 3, 4, 4]


def test_example_2_both_empty():
    assert Solution().mergeTwoLists(None, None) is None


def test_example_3_one_empty():
    merged = Solution().mergeTwoLists(None, list_to_linked([0]))
    assert linked_to_list(merged) == [0]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(linked_to_list(s.mergeTwoLists(list_to_linked([1, 2, 4]), list_to_linked([1, 3, 4]))))  # expected [1, 1, 2, 3, 4, 4]
