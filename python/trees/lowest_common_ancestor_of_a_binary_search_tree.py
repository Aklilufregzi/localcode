"""
LeetCode 235. Lowest Common Ancestor of a Binary Search Tree (Medium)
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a BST and two of its nodes p and q, return their lowest common
ancestor: the deepest node that has both p and q as descendants (a node
counts as a descendant of itself).

Run just this file:   python trees/lowest_common_ancestor_of_a_binary_search_tree.py
Run its tests:        pytest trees/lowest_common_ancestor_of_a_binary_search_tree.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import TreeNode, tree_from_list


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def _find(root: TreeNode | None, val: int) -> TreeNode:
    """Locate the node with the given value in the built tree."""
    assert root is not None
    if root.val == val:
        return root
    return _find(root.left if val < root.val else root.right, val)


def test_example_1():
    root = tree_from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    lca = Solution().lowestCommonAncestor(root, _find(root, 2), _find(root, 8))
    assert lca.val == 6


def test_example_2():
    # A node can be a descendant of itself.
    root = tree_from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    lca = Solution().lowestCommonAncestor(root, _find(root, 2), _find(root, 4))
    assert lca.val == 2


def test_example_3():
    root = tree_from_list([2, 1])
    lca = Solution().lowestCommonAncestor(root, _find(root, 2), _find(root, 1))
    assert lca.val == 2


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    root = tree_from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(Solution().lowestCommonAncestor(root, _find(root, 2), _find(root, 8)))  # expected TreeNode(6)
