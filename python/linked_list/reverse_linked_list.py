"""
LeetCode 206. Reverse Linked List (Easy)
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list and return
the new head.

Run just this file:   python linked_list/reverse_linked_list.py
Run its tests:        pytest linked_list/reverse_linked_list.py -v
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import ListNode, list_to_linked, linked_to_list


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    head = list_to_linked([1, 2, 3, 4, 5])
    assert linked_to_list(Solution().reverseList(head)) == [5, 4, 3, 2, 1]


def test_example_2():
    head = list_to_linked([1, 2])
    assert linked_to_list(Solution().reverseList(head)) == [2, 1]


def test_example_3_empty():
    assert Solution().reverseList(None) is None


def test_single_node():
    head = list_to_linked([7])
    assert linked_to_list(Solution().reverseList(head)) == [7]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(linked_to_list(s.reverseList(list_to_linked([1, 2, 3, 4, 5]))))  # expected [5, 4, 3, 2, 1]
