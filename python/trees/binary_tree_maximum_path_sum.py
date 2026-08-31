"""
LeetCode 124. Binary Tree Maximum Path Sum (Hard)
https://leetcode.com/problems/binary-tree-maximum-path-sum/

A path is any node sequence where adjacent nodes are connected by an edge;
a node appears at most once and the path need not pass through the root.
Return the maximum sum of node values over all non-empty paths.

Run just this file:   python trees/binary_tree_maximum_path_sum.py
Run its tests:        pytest trees/binary_tree_maximum_path_sum.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import TreeNode, tree_from_list


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().maxPathSum(tree_from_list([1, 2, 3])) == 6


def test_example_2():
    assert Solution().maxPathSum(tree_from_list([-10, 9, 20, None, None, 15, 7])) == 42


def test_single_negative_node():
    assert Solution().maxPathSum(tree_from_list([-3])) == -3


def test_all_negative():
    # Best path is the single least-negative node.
    assert Solution().maxPathSum(tree_from_list([-2, -1])) == -1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.maxPathSum(tree_from_list([-10, 9, 20, None, None, 15, 7])))  # expected 42
