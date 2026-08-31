"""
LeetCode 543. Diameter of Binary Tree (Easy)
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of its diameter — the
number of edges on the longest path between any two nodes in the tree.
The path may or may not pass through the root.

Run just this file:   python trees/diameter_of_binary_tree.py
Run its tests:        pytest trees/diameter_of_binary_tree.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import TreeNode, tree_from_list


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().diameterOfBinaryTree(tree_from_list([1, 2, 3, 4, 5])) == 3


def test_example_2():
    assert Solution().diameterOfBinaryTree(tree_from_list([1, 2])) == 1


def test_single_node():
    assert Solution().diameterOfBinaryTree(tree_from_list([1])) == 0


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.diameterOfBinaryTree(tree_from_list([1, 2, 3, 4, 5])))  # expected 3
