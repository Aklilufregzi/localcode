"""
LeetCode 110. Balanced Binary Tree (Easy)
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced: for every node,
the heights of its left and right subtrees differ by at most 1.

Run just this file:   python trees/balanced_binary_tree.py
Run its tests:        pytest trees/balanced_binary_tree.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import TreeNode, tree_from_list


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().isBalanced(tree_from_list([3, 9, 20, None, None, 15, 7])) is True


def test_example_2():
    assert Solution().isBalanced(tree_from_list([1, 2, 2, 3, 3, None, None, 4, 4])) is False


def test_example_3_empty():
    assert Solution().isBalanced(None) is True


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.isBalanced(tree_from_list([3, 9, 20, None, None, 15, 7])))  # expected True
    print(s.isBalanced(tree_from_list([1, 2, 2, 3, 3, None, None, 4, 4])))  # expected False
