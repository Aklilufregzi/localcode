/**
 * LeetCode 21. Merge Two Sorted Lists (Easy)
 * https://leetcode.com/problems/merge-two-sorted-lists/
 *
 * Given the heads of two sorted linked lists list1 and list2, merge them
 * into one sorted list by splicing together their nodes, and return the
 * head of the merged list.
 *
 * Run just this file:   npx tsx src/linked-list/merge-two-sorted-lists.ts
 * Run its tests:        npx vitest run src/linked-list/merge-two-sorted-lists.test.ts
 */

import { ListNode, arrayToList, listToArray } from "../helpers.ts";

export function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(listToArray(mergeTwoLists(arrayToList([1, 2, 4]), arrayToList([1, 3, 4])))); // expected [1, 1, 2, 3, 4, 4]
}
