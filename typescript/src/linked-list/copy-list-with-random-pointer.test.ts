import { describe, expect, it } from "vitest";
import { _Node, copyRandomList } from "./copy-list-with-random-pointer.ts";

type Pair = [val: number, randomIndex: number | null];

/** Build a list from [val, randomIndexOrNull] pairs. */
function build(pairs: Pair[]): _Node | null {
  const nodes = pairs.map(([v]) => new _Node(v));
  pairs.forEach(([, ri], i) => {
    nodes[i]!.next = nodes[i + 1] ?? null;
    nodes[i]!.random = ri === null ? null : nodes[ri]!;
  });
  return nodes[0] ?? null;
}

function nodesOf(head: _Node | null): _Node[] {
  const out: _Node[] = [];
  for (let cur = head; cur !== null; cur = cur.next) out.push(cur);
  return out;
}

/** Inverse of build: [val, randomIndexOrNull] pairs. */
function toPairs(head: _Node | null): Pair[] {
  const nodes = nodesOf(head);
  return nodes.map((n) => {
    const ri = n.random === null ? null : nodes.indexOf(n.random);
    expect(ri).not.toBe(-1); // random must point inside the copied list
    return [n.val, ri] as Pair;
  });
}

describe("copyRandomList", () => {
  it("example 1: deep copy with correct random wiring", () => {
    const pairs: Pair[] = [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]];
    const original = build(pairs);
    const copy = copyRandomList(original);
    expect(toPairs(copy)).toEqual(pairs);
    // Deep copy: no node may be shared with the original.
    const originalNodes = new Set(nodesOf(original));
    for (const n of nodesOf(copy)) expect(originalNodes.has(n)).toBe(false);
    // Original must be left intact.
    expect(toPairs(original)).toEqual(pairs);
  });

  it("example 2", () => {
    const pairs: Pair[] = [[1, 1], [2, 1]];
    expect(toPairs(copyRandomList(build(pairs)))).toEqual(pairs);
  });

  it("example 3", () => {
    const pairs: Pair[] = [[3, null], [3, 0], [3, null]];
    expect(toPairs(copyRandomList(build(pairs)))).toEqual(pairs);
  });

  it("empty list", () => {
    expect(copyRandomList(null)).toBeNull();
  });
});
