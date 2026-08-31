/**
 * LeetCode 206. Reverse Linked List (Easy)
 * https://leetcode.com/problems/reverse-linked-list/
 *
 * Given the head of a singly linked list, reverse the list and return
 * the new head.
 *
 * Run just this file:   npx tsx src/linked-list/reverse-linked-list.ts
 * Run its tests:        npx vitest run src/linked-list/reverse-linked-list.test.ts
 */

import { ListNode, arrayToList, listToArray } from "../helpers.ts";

export function reverseList(head: ListNode | null): ListNode | null {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(listToArray(reverseList(arrayToList([1, 2, 3, 4, 5])))); // expected [5, 4, 3, 2, 1]
}
