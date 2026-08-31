"""
LeetCode 684. Redundant Connection (Medium)
https://leetcode.com/problems/redundant-connection/

A tree with n nodes (labeled 1..n) had one extra edge added. Given the
resulting graph as a list of n edges, return the edge that can be removed so
the graph is a tree again. If multiple answers exist, return the one that
occurs LAST in the input.

Run just this file:   python graphs/redundant_connection.py
Run its tests:        pytest graphs/redundant_connection.py -v
"""


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]


def test_example_2():
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    assert Solution().findRedundantConnection(edges) == [1, 4]


def test_cycle_is_whole_graph():
    assert Solution().findRedundantConnection([[1, 2], [2, 3], [3, 1]]) == [3, 1]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # expected [2, 3]
