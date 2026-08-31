"""
LeetCode 1448. Count Good Nodes in Binary Tree (Medium)
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

A node X is "good" if on the path from the root to X there are no nodes
with a value greater than X's. Return the number of good nodes.

Run just this file:   python trees/count_good_nodes_in_binary_tree.py
Run its tests:        pytest trees/count_good_nodes_in_binary_tree.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import TreeNode, tree_from_list


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().goodNodes(tree_from_list([3, 1, 4, 3, None, 1, 5])) == 4


def test_example_2():
    assert Solution().goodNodes(tree_from_list([3, 3, None, 4, 2])) == 3


def test_example_3_single_node():
    assert Solution().goodNodes(tree_from_list([1])) == 1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.goodNodes(tree_from_list([3, 1, 4, 3, None, 1, 5])))  # expected 4
