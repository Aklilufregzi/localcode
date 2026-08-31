"""
LeetCode 226. Invert Binary Tree (Easy)
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree (swap every node's left
and right children) and return its root.

Run just this file:   python trees/invert_binary_tree.py
Run its tests:        pytest trees/invert_binary_tree.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import TreeNode, tree_from_list, tree_to_list


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    root = tree_from_list([4, 2, 7, 1, 3, 6, 9])
    assert tree_to_list(Solution().invertTree(root)) == [4, 7, 2, 9, 6, 3, 1]


def test_example_2():
    root = tree_from_list([2, 1, 3])
    assert tree_to_list(Solution().invertTree(root)) == [2, 3, 1]


def test_example_3_empty():
    assert tree_to_list(Solution().invertTree(None)) == []


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(tree_to_list(s.invertTree(tree_from_list([4, 2, 7, 1, 3, 6, 9]))))  # expected [4, 7, 2, 9, 6, 3, 1]
