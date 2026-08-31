"""
LeetCode 230. Kth Smallest Element in a BST (Medium)
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree and an integer k, return the kth
smallest value (1-indexed) of all the values of the nodes in the tree.

Run just this file:   python trees/kth_smallest_element_in_a_bst.py
Run its tests:        pytest trees/kth_smallest_element_in_a_bst.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import TreeNode, tree_from_list


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().kthSmallest(tree_from_list([3, 1, 4, None, 2]), 1) == 1


def test_example_2():
    assert Solution().kthSmallest(tree_from_list([5, 3, 6, 2, 4, None, None, 1]), 3) == 3


def test_k_is_size():
    assert Solution().kthSmallest(tree_from_list([3, 1, 4, None, 2]), 4) == 4


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.kthSmallest(tree_from_list([3, 1, 4, None, 2]), 1))  # expected 1
