"""
LeetCode 138. Copy List with Random Pointer (Medium)
https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list of length n where each node has an extra `random` pointer
to any node in the list (or None). Return a DEEP COPY of the list:
brand-new nodes with the same val/next/random structure, sharing no
nodes with the original.

Run just this file:   python linked_list/copy_list_with_random_pointer.py
Run its tests:        pytest linked_list/copy_list_with_random_pointer.py -v
"""


class Node:
    def __init__(self, x: int, next: "Node | None" = None, random: "Node | None" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node | None") -> "Node | None":
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def _build(pairs: list[tuple[int, int | None]]) -> "Node | None":
    """Build a list from [(val, random_index_or_None), ...]."""
    nodes = [Node(v) for v, _ in pairs]
    for i, node in enumerate(nodes):
        node.next = nodes[i + 1] if i + 1 < len(nodes) else None
        ri = pairs[i][1]
        node.random = nodes[ri] if ri is not None else None
    return nodes[0] if nodes else None


def _nodes_of(head: "Node | None") -> list:
    out, cur = [], head
    while cur:
        out.append(cur)
        cur = cur.next
    return out


def _to_pairs(head: "Node | None") -> list[tuple[int, int | None]]:
    """Inverse of _build: [(val, random_index_or_None), ...]."""
    nodes = _nodes_of(head)
    index = {id(n): i for i, n in enumerate(nodes)}
    pairs = []
    for n in nodes:
        assert n.random is None or id(n.random) in index, "random points outside the list"
        pairs.append((n.val, index[id(n.random)] if n.random is not None else None))
    return pairs


def test_example_1():
    pairs = [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)]
    original = _build(pairs)
    copy = Solution().copyRandomList(original)
    assert _to_pairs(copy) == pairs
    # Deep copy: no node may be shared with the original.
    original_ids = {id(n) for n in _nodes_of(original)}
    assert all(id(n) not in original_ids for n in _nodes_of(copy))
    # Original must be left intact.
    assert _to_pairs(original) == pairs


def test_example_2():
    pairs = [(1, 1), (2, 1)]
    copy = Solution().copyRandomList(_build(pairs))
    assert _to_pairs(copy) == pairs


def test_example_3():
    pairs = [(3, None), (3, 0), (3, None)]
    copy = Solution().copyRandomList(_build(pairs))
    assert _to_pairs(copy) == pairs


def test_empty():
    assert Solution().copyRandomList(None) is None


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    head = _build([(7, None), (13, 0), (11, 4), (10, 2), (1, 0)])
    print(_to_pairs(Solution().copyRandomList(head)))  # expected [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)]
