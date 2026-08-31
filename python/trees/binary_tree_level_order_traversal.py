"""
LeetCode 102. Binary Tree Level Order Traversal (Medium)
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its
nodes' values (i.e. from left to right, level by level).

Run just this file:   python trees/binary_tree_level_order_traversal.py
Run its tests:        pytest trees/binary_tree_level_order_traversal.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import TreeNode, tree_from_list


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    root = tree_from_list([3, 9, 20, None, None, 15, 7])
    assert Solution().levelOrder(root) == [[3], [9, 20], [15, 7]]


def test_example_2():
    assert Solution().levelOrder(tree_from_list([1])) == [[1]]


def test_example_3_empty():
    assert Solution().levelOrder(None) == []


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.levelOrder(tree_from_list([3, 9, 20, None, None, 15, 7])))  # expected [[3], [9, 20], [15, 7]]
