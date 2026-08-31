"""
LeetCode 297. Serialize and Deserialize Binary Tree (Hard)
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Design an algorithm to serialize a binary tree to a string and deserialize
that string back to the original tree structure. Any format works as long
as deserialize(serialize(root)) reconstructs the tree.

Run just this file:   python trees/serialize_and_deserialize_binary_tree.py
Run its tests:        pytest trees/serialize_and_deserialize_binary_tree.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import TreeNode, tree_from_list, tree_to_list


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        """Encodes a tree to a single string."""
        ...  # TODO: implement

    def deserialize(self, data: str) -> TreeNode | None:
        """Decodes your encoded data to tree."""
        ...  # TODO: implement


# ---------------------------- tests ----------------------------
# The encoded format is up to you — tests only check the round trip.

def _round_trip(values: list[int | None]) -> list[int | None]:
    codec = Codec()
    return tree_to_list(codec.deserialize(codec.serialize(tree_from_list(values))))


def test_example_1():
    assert _round_trip([1, 2, 3, None, None, 4, 5]) == [1, 2, 3, None, None, 4, 5]


def test_example_2_empty():
    assert _round_trip([]) == []


def test_single_node():
    assert _round_trip([1]) == [1]


def test_negative_and_multi_digit_values():
    assert _round_trip([-10, 9, 20, None, None, 15, 7]) == [-10, 9, 20, None, None, 15, 7]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    codec = Codec()
    data = codec.serialize(tree_from_list([1, 2, 3, None, None, 4, 5]))
    print(data)
    print(tree_to_list(codec.deserialize(data)))  # expected [1, 2, 3, None, None, 4, 5]
