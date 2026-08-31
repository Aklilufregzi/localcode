/**
 * LeetCode 138. Copy List with Random Pointer (Medium)
 * https://leetcode.com/problems/copy-list-with-random-pointer/
 *
 * A linked list of length n where each node has an extra `random` pointer
 * to any node in the list (or null). Return a DEEP COPY of the list:
 * brand-new nodes with the same val/next/random structure, sharing no
 * nodes with the original.
 *
 * Run just this file:   npx tsx src/linked-list/copy-list-with-random-pointer.ts
 * Run its tests:        npx vitest run src/linked-list/copy-list-with-random-pointer.test.ts
 */

export class _Node {
  val: number;
  next: _Node | null;
  random: _Node | null;
  constructor(val = 0, next: _Node | null = null, random: _Node | null = null) {
    this.val = val;
    this.next = next;
    this.random = random;
  }
}

export function copyRandomList(head: _Node | null): _Node | null {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  const a = new _Node(7);
  const b = new _Node(13);
  a.next = b;
  b.random = a;
  const copy = copyRandomList(a);
  console.log(copy?.val, copy?.next?.val, copy?.next?.random === copy); // expected 7 13 true
}
