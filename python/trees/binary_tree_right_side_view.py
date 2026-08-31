"""
LeetCode 199. Binary Tree Right Side View (Medium)
https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, imagine standing on its right side:
return the values of the nodes you can see, ordered from top to bottom
(the rightmost node of each level).

Run just this file:   python trees/binary_tree_right_side_view.py
Run its tests:        pytest trees/binary_tree_right_side_view.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import TreeNode, tree_from_list


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    root = tree_from_list([1, 2, 3, None, 5, None, 4])
    assert Solution().rightSideView(root) == [1, 3, 4]


def test_example_2():
    assert Solution().rightSideView(tree_from_list([1, None, 3])) == [1, 3]


def test_example_3_empty():
    assert Solution().rightSideView(None) == []


def test_left_leaning():
    # Deeper left branch is visible below the shorter right branch.
    assert Solution().rightSideView(tree_from_list([1, 2, 3, 4])) == [1, 3, 4]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.rightSideView(tree_from_list([1, 2, 3, None, 5, None, 4])))  # expected [1, 3, 4]
