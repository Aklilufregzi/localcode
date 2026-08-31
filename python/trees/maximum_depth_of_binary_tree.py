"""
LeetCode 104. Maximum Depth of Binary Tree (Easy)
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth — the number of
nodes along the longest path from the root down to the farthest leaf.

Run just this file:   python trees/maximum_depth_of_binary_tree.py
Run its tests:        pytest trees/maximum_depth_of_binary_tree.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import TreeNode, tree_from_list


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().maxDepth(tree_from_list([3, 9, 20, None, None, 15, 7])) == 3


def test_example_2():
    assert Solution().maxDepth(tree_from_list([1, None, 2])) == 2


def test_empty():
    assert Solution().maxDepth(None) == 0


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.maxDepth(tree_from_list([3, 9, 20, None, None, 15, 7])))  # expected 3
