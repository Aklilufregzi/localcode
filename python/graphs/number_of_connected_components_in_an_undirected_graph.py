"""
LeetCode 323. Number of Connected Components in an Undirected Graph (Medium) — premium
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
https://neetcode.io/problems/count-connected-components

Given n nodes (labeled 0..n-1) and a list of undirected edges, return the
number of connected components in the graph.

Run just this file:   python graphs/number_of_connected_components_in_an_undirected_graph.py
Run its tests:        pytest graphs/number_of_connected_components_in_an_undirected_graph.py -v
"""


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().countComponents(3, [[0, 1], [0, 2]]) == 1


def test_example_2():
    assert Solution().countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]) == 2


def test_no_edges():
    assert Solution().countComponents(4, []) == 4


def test_single_node():
    assert Solution().countComponents(1, []) == 1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]))  # expected 2
