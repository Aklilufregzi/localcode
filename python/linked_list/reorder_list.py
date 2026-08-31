"""
LeetCode 143. Reorder List (Medium)
https://leetcode.com/problems/reorder-list/

Given the head of a list L0 -> L1 -> ... -> Ln-1 -> Ln, reorder it
IN PLACE to L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
Only node pointers may be changed, not node values. Returns nothing.

Run just this file:   python linked_list/reorder_list.py
Run its tests:        pytest linked_list/reorder_list.py -v
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import ListNode, list_to_linked, linked_to_list


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        ...  # TODO: implement (modify head in place)


# ---------------------------- tests ----------------------------

def test_example_1():
    head = list_to_linked([1, 2, 3, 4])
    Solution().reorderList(head)
    assert linked_to_list(head) == [1, 4, 2, 3]


def test_example_2():
    head = list_to_linked([1, 2, 3, 4, 5])
    Solution().reorderList(head)
    assert linked_to_list(head) == [1, 5, 2, 4, 3]


def test_two_nodes():
    head = list_to_linked([1, 2])
    Solution().reorderList(head)
    assert linked_to_list(head) == [1, 2]


def test_single_node():
    head = list_to_linked([1])
    Solution().reorderList(head)
    assert linked_to_list(head) == [1]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    head = list_to_linked([1, 2, 3, 4, 5])
    Solution().reorderList(head)
    print(linked_to_list(head))  # expected [1, 5, 2, 4, 3]
