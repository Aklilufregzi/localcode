"""
LeetCode 572. Subtree of Another Tree (Easy)
https://leetcode.com/problems/subtree-of-another-tree/

Given the roots of two binary trees root and subRoot, return true if there
is a subtree of root with the same structure and node values as subRoot.

Run just this file:   python trees/subtree_of_another_tree.py
Run its tests:        pytest trees/subtree_of_another_tree.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import TreeNode, tree_from_list


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    root = tree_from_list([3, 4, 5, 1, 2])
    sub = tree_from_list([4, 1, 2])
    assert Solution().isSubtree(root, sub) is True


def test_example_2():
    root = tree_from_list([3, 4, 5, 1, 2, None, None, None, None, 0])
    sub = tree_from_list([4, 1, 2])
    assert Solution().isSubtree(root, sub) is False


def test_identical_trees():
    assert Solution().isSubtree(tree_from_list([1, 2, 3]), tree_from_list([1, 2, 3])) is True


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.isSubtree(tree_from_list([3, 4, 5, 1, 2]), tree_from_list([4, 1, 2])))  # expected True
