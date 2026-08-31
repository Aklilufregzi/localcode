"""
LeetCode 261. Graph Valid Tree (Medium) — premium
https://leetcode.com/problems/graph-valid-tree/
https://neetcode.io/problems/valid-tree

Given n nodes (labeled 0..n-1) and a list of undirected edges, return True
if the edges form a valid tree: connected and acyclic (exactly n-1 edges,
all nodes reachable).

Run just this file:   python graphs/graph_valid_tree.py
Run its tests:        pytest graphs/graph_valid_tree.py -v
"""


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True


def test_example_2_cycle():
    assert Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False


def test_single_node_no_edges():
    assert Solution().validTree(1, []) is True


def test_disconnected():
    assert Solution().validTree(4, [[0, 1], [2, 3]]) is False


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))  # expected True
    print(s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))  # expected False
