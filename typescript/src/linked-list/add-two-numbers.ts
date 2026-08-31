/**
 * LeetCode 2. Add Two Numbers (Medium)
 * https://leetcode.com/problems/add-two-numbers/
 *
 * Two non-empty linked lists represent two non-negative integers with
 * digits stored in REVERSE order. Add the two numbers and return the sum
 * as a linked list, also in reverse order.
 *
 * Run just this file:   npx tsx src/linked-list/add-two-numbers.ts
 * Run its tests:        npx vitest run src/linked-list/add-two-numbers.test.ts
 */

import { ListNode, arrayToList, listToArray } from "../helpers.ts";

export function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(listToArray(addTwoNumbers(arrayToList([2, 4, 3]), arrayToList([5, 6, 4])))); // expected [7, 0, 8]
}
