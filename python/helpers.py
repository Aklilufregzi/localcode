"""
Shared data structures and builders for linked-list, tree, and graph problems.

Usage from a problem file (works for both `python file.py` and `pytest`):

    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from helpers import ListNode, TreeNode, list_to_linked, linked_to_list, tree_from_list, tree_to_list
"""
from __future__ import annotations

from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def list_to_linked(values: list[int]) -> ListNode | None:
    """Build a linked list from a Python list: [1,2,3] -> 1->2->3."""
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def linked_to_list(head: ListNode | None, limit: int = 10_000) -> list[int]:
    """Convert a linked list back to a Python list (limit guards against cycles)."""
    out: list[int] = []
    while head and len(out) < limit:
        out.append(head.val)
        head = head.next
    return out


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def tree_from_list(values: list[int | None]) -> TreeNode | None:
    """Build a binary tree from a LeetCode level-order list, e.g. [3,9,20,None,None,15,7]."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.left = TreeNode(v)
                queue.append(node.left)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.right = TreeNode(v)
                queue.append(node.right)
    return root


def tree_to_list(root: TreeNode | None) -> list[int | None]:
    """Inverse of tree_from_list: level-order list with trailing Nones trimmed."""
    out: list[int | None] = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


class GraphNode:
    """LeetCode's `Node` for graph problems (e.g. Clone Graph)."""

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"GraphNode({self.val})"


def graph_from_adj_list(adj: list[list[int]]) -> GraphNode | None:
    """Build a connected undirected graph from a LeetCode adjacency list (1-indexed nodes)."""
    if not adj:
        return None
    nodes = [GraphNode(i + 1) for i in range(len(adj))]
    for i, neighbors in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0]


def graph_to_adj_list(node: GraphNode | None) -> list[list[int]]:
    """Inverse of graph_from_adj_list: adjacency list of a connected graph (1-indexed)."""
    if node is None:
        return []
    seen: dict[int, GraphNode] = {}
    queue = deque([node])
    while queue:
        cur = queue.popleft()
        if cur.val in seen:
            continue
        seen[cur.val] = cur
        for n in cur.neighbors:
            if n.val not in seen:
                queue.append(n)
    return [[n.val for n in seen[i].neighbors] for i in sorted(seen)]
