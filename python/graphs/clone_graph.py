"""
LeetCode 133. Clone Graph (Medium)
https://leetcode.com/problems/clone-graph/

Given a reference to a node in a connected undirected graph, return a deep
copy of the graph. Each node has a val and a list of neighbors. Node values
are 1-indexed and unique (node.val == its 1-based index in the adjacency list).

Run just this file:   python graphs/clone_graph.py
Run its tests:        pytest graphs/clone_graph.py -v
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from helpers import GraphNode, graph_from_adj_list, graph_to_adj_list


class Solution:
    def cloneGraph(self, node: GraphNode | None) -> GraphNode | None:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def _collect_nodes(node: GraphNode | None) -> list[GraphNode]:
    """All nodes reachable from `node` (for identity checks)."""
    if node is None:
        return []
    seen: dict[int, GraphNode] = {}
    stack = [node]
    while stack:
        cur = stack.pop()
        if id(cur) in seen:
            continue
        seen[id(cur)] = cur
        stack.extend(cur.neighbors)
    return list(seen.values())


def _assert_deep_copy(adj: list[list[int]]) -> None:
    original = graph_from_adj_list(adj)
    clone = Solution().cloneGraph(original)
    # Same structure via adjacency-list round trip...
    assert graph_to_adj_list(clone) == adj
    # ...but none of the returned nodes are the same objects as the input's.
    original_ids = {id(n) for n in _collect_nodes(original)}
    for n in _collect_nodes(clone):
        assert id(n) not in original_ids, f"node {n.val} was not cloned"


def test_example_1():
    _assert_deep_copy([[2, 4], [1, 3], [2, 4], [1, 3]])


def test_example_2_single_node_no_neighbors():
    _assert_deep_copy([[]])


def test_example_3_empty_graph():
    assert Solution().cloneGraph(None) is None


def test_two_connected_nodes():
    _assert_deep_copy([[2], [1]])


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    original = graph_from_adj_list([[2, 4], [1, 3], [2, 4], [1, 3]])
    clone = s.cloneGraph(original)
    print(graph_to_adj_list(clone))  # expected [[2, 4], [1, 3], [2, 4], [1, 3]]
    print(clone is original)  # expected False
