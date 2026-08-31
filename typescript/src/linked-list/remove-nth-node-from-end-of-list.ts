/**
 * LeetCode 19. Remove Nth Node From End of List (Medium)
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 *
 * Given the head of a linked list, remove the nth node from the END of
 * the list and return the head.
 *
 * Run just this file:   npx tsx src/linked-list/remove-nth-node-from-end-of-list.ts
 * Run its tests:        npx vitest run src/linked-list/remove-nth-node-from-end-of-list.test.ts
 */

import { ListNode, arrayToList, listToArray } from "../helpers.ts";

export function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(listToArray(removeNthFromEnd(arrayToList([1, 2, 3, 4, 5]), 2))); // expected [1, 2, 3, 5]
}
