"""
LeetCode 98. Validate Binary Search Tree (Medium)
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid BST: every
node's left subtree contains only values strictly less than the node, its
right subtree only values strictly greater, and both subtrees are BSTs.

Run just this file:   python trees/validate_binary_search_tree.py
Run its tests:        pytest trees/validate_binary_search_tree.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import TreeNode, tree_from_list


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().isValidBST(tree_from_list([2, 1, 3])) is True


def test_example_2():
    assert Solution().isValidBST(tree_from_list([5, 1, 4, None, None, 3, 6])) is False


def test_deep_violation():
    # 3 is in the left subtree of 5 but greater than the root's left bound check trap:
    # [5,4,6,None,None,3,7] — 3 sits under 6 (right subtree of 5) but 3 < 5.
    assert Solution().isValidBST(tree_from_list([5, 4, 6, None, None, 3, 7])) is False


def test_single_node():
    assert Solution().isValidBST(tree_from_list([1])) is True


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.isValidBST(tree_from_list([2, 1, 3])))  # expected True
    print(s.isValidBST(tree_from_list([5, 1, 4, None, None, 3, 6])))  # expected False
