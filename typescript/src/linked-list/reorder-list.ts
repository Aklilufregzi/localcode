/**
 * LeetCode 143. Reorder List (Medium)
 * https://leetcode.com/problems/reorder-list/
 *
 * Given the head of a list L0 -> L1 -> ... -> Ln-1 -> Ln, reorder it
 * IN PLACE to L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
 * Only node pointers may be changed, not node values. Returns nothing.
 *
 * Run just this file:   npx tsx src/linked-list/reorder-list.ts
 * Run its tests:        npx vitest run src/linked-list/reorder-list.test.ts
 */

import { ListNode, arrayToList, listToArray } from "../helpers.ts";

export function reorderList(head: ListNode | null): void {
  // TODO: implement (modify head in place)
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  const head = arrayToList([1, 2, 3, 4, 5]);
  reorderList(head);
  console.log(listToArray(head)); // expected [1, 5, 2, 4, 3]
}
