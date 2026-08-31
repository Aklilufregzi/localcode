"""
LeetCode 100. Same Tree (Easy)
https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, return true if they are the
same tree: structurally identical with equal node values.

Run just this file:   python trees/same_tree.py
Run its tests:        pytest trees/same_tree.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import TreeNode, tree_from_list


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().isSameTree(tree_from_list([1, 2, 3]), tree_from_list([1, 2, 3])) is True


def test_example_2():
    assert Solution().isSameTree(tree_from_list([1, 2]), tree_from_list([1, None, 2])) is False


def test_example_3():
    assert Solution().isSameTree(tree_from_list([1, 2, 1]), tree_from_list([1, 1, 2])) is False


def test_both_empty():
    assert Solution().isSameTree(None, None) is True


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.isSameTree(tree_from_list([1, 2, 3]), tree_from_list([1, 2, 3])))  # expected True
    print(s.isSameTree(tree_from_list([1, 2]), tree_from_list([1, None, 2])))  # expected False
