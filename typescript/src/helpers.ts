/**
 * Shared data structures and builders for linked-list, tree, and graph problems.
 *
 * Usage from a problem file:
 *   import { ListNode, arrayToList, listToArray } from "../helpers.ts";
 */

export class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val = 0, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

/** Build a linked list from an array: [1,2,3] -> 1->2->3. */
export function arrayToList(values: number[]): ListNode | null {
  const dummy = new ListNode();
  let cur = dummy;
  for (const v of values) {
    cur.next = new ListNode(v);
    cur = cur.next;
  }
  return dummy.next;
}

/** Convert a linked list back to an array (limit guards against cycles). */
export function listToArray(head: ListNode | null, limit = 10_000): number[] {
  const out: number[] = [];
  let cur = head;
  while (cur && out.length < limit) {
    out.push(cur.val);
    cur = cur.next;
  }
  return out;
}

export class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

/** Build a binary tree from a LeetCode level-order array, e.g. [3,9,20,null,null,15,7]. */
export function treeFromArray(values: (number | null)[]): TreeNode | null {
  if (values.length === 0 || values[0] == null) return null;
  const root = new TreeNode(values[0]);
  const queue: TreeNode[] = [root];
  let i = 1;
  while (queue.length > 0 && i < values.length) {
    const node = queue.shift()!;
    if (i < values.length) {
      const v = values[i++];
      if (v != null) {
        node.left = new TreeNode(v);
        queue.push(node.left);
      }
    }
    if (i < values.length) {
      const v = values[i++];
      if (v != null) {
        node.right = new TreeNode(v);
        queue.push(node.right);
      }
    }
  }
  return root;
}

/** Inverse of treeFromArray: level-order array with trailing nulls trimmed. */
export function treeToArray(root: TreeNode | null): (number | null)[] {
  const out: (number | null)[] = [];
  const queue: (TreeNode | null)[] = [root];
  while (queue.length > 0) {
    const node = queue.shift()!;
    if (node == null) {
      out.push(null);
    } else {
      out.push(node.val);
      queue.push(node.left);
      queue.push(node.right);
    }
  }
  while (out.length > 0 && out[out.length - 1] == null) out.pop();
  return out;
}

/** LeetCode's `Node` for graph problems (e.g. Clone Graph). */
export class GraphNode {
  val: number;
  neighbors: GraphNode[];
  constructor(val = 0, neighbors: GraphNode[] = []) {
    this.val = val;
    this.neighbors = neighbors;
  }
}

/** Build a connected undirected graph from a LeetCode adjacency list (1-indexed nodes). */
export function graphFromAdjList(adj: number[][]): GraphNode | null {
  if (adj.length === 0) return null;
  const nodes = adj.map((_, i) => new GraphNode(i + 1));
  adj.forEach((neighbors, i) => {
    nodes[i]!.neighbors = neighbors.map((j) => nodes[j - 1]!);
  });
  return nodes[0]!;
}

/** Inverse of graphFromAdjList: adjacency list of a connected graph (1-indexed). */
export function graphToAdjList(node: GraphNode | null): number[][] {
  if (node == null) return [];
  const seen = new Map<number, GraphNode>();
  const queue: GraphNode[] = [node];
  while (queue.length > 0) {
    const cur = queue.shift()!;
    if (seen.has(cur.val)) continue;
    seen.set(cur.val, cur);
    for (const n of cur.neighbors) {
      if (!seen.has(n.val)) queue.push(n);
    }
  }
  return [...seen.keys()]
    .sort((a, b) => a - b)
    .map((v) => seen.get(v)!.neighbors.map((n) => n.val));
}
