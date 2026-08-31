"""
LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal (Medium)
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder — the preorder and inorder
traversals of the same binary tree (unique values) — construct and return
the binary tree.

Run just this file:   python trees/construct_binary_tree_from_preorder_and_inorder_traversal.py
Run its tests:        pytest trees/construct_binary_tree_from_preorder_and_inorder_traversal.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import TreeNode, tree_to_list


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    root = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert tree_to_list(root) == [3, 9, 20, None, None, 15, 7]


def test_example_2():
    assert tree_to_list(Solution().buildTree([-1], [-1])) == [-1]


def test_left_only_chain():
    assert tree_to_list(Solution().buildTree([3, 2, 1], [1, 2, 3])) == [3, 2, None, 1]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(tree_to_list(s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))  # expected [3, 9, 20, None, None, 15, 7]
