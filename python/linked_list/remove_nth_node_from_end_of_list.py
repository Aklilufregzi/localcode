"""
LeetCode 19. Remove Nth Node From End of List (Medium)
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the END of
the list and return the head.

Run just this file:   python linked_list/remove_nth_node_from_end_of_list.py
Run its tests:        pytest linked_list/remove_nth_node_from_end_of_list.py -v
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import ListNode, list_to_linked, linked_to_list


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    head = list_to_linked([1, 2, 3, 4, 5])
    assert linked_to_list(Solution().removeNthFromEnd(head, 2)) == [1, 2, 3, 5]


def test_example_2_single_node():
    head = list_to_linked([1])
    assert Solution().removeNthFromEnd(head, 1) is None


def test_example_3_remove_last():
    head = list_to_linked([1, 2])
    assert linked_to_list(Solution().removeNthFromEnd(head, 1)) == [1]


def test_remove_head():
    head = list_to_linked([1, 2])
    assert linked_to_list(Solution().removeNthFromEnd(head, 2)) == [2]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(linked_to_list(s.removeNthFromEnd(list_to_linked([1, 2, 3, 4, 5]), 2)))  # expected [1, 2, 3, 5]
