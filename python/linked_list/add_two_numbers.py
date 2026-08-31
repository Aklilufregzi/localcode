"""
LeetCode 2. Add Two Numbers (Medium)
https://leetcode.com/problems/add-two-numbers/

Two non-empty linked lists represent two non-negative integers with
digits stored in REVERSE order. Add the two numbers and return the sum
as a linked list, also in reverse order.

Run just this file:   python linked_list/add_two_numbers.py
Run its tests:        pytest linked_list/add_two_numbers.py -v
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import ListNode, list_to_linked, linked_to_list


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # 342 + 465 = 807
    result = Solution().addTwoNumbers(list_to_linked([2, 4, 3]), list_to_linked([5, 6, 4]))
    assert linked_to_list(result) == [7, 0, 8]


def test_example_2():
    result = Solution().addTwoNumbers(list_to_linked([0]), list_to_linked([0]))
    assert linked_to_list(result) == [0]


def test_example_3():
    # 9999999 + 9999 = 10009998
    result = Solution().addTwoNumbers(
        list_to_linked([9, 9, 9, 9, 9, 9, 9]), list_to_linked([9, 9, 9, 9])
    )
    assert linked_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]


def test_carry_extends_length():
    # 5 + 5 = 10
    result = Solution().addTwoNumbers(list_to_linked([5]), list_to_linked([5]))
    assert linked_to_list(result) == [0, 1]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(linked_to_list(s.addTwoNumbers(list_to_linked([2, 4, 3]), list_to_linked([5, 6, 4]))))  # expected [7, 0, 8]
