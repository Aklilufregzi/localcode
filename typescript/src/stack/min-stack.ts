/**
 * LeetCode 155. Min Stack (Medium)
 * https://leetcode.com/problems/min-stack/
 *
 * Design a stack that supports push, pop, top, and retrieving the minimum
 * element, each in O(1) time. Implement the MinStack class with
 * push(val), pop(), top(), and getMin().
 *
 * Run just this file:   npx tsx src/stack/min-stack.ts
 * Run its tests:        npx vitest run src/stack/min-stack.test.ts
 */

export class MinStack {
  constructor() {
    // TODO: implement
  }

  push(val: number): void {
    // TODO: implement
    throw new Error("Not implemented");
  }

  pop(): void {
    // TODO: implement
    throw new Error("Not implemented");
  }

  top(): number {
    // TODO: implement
    throw new Error("Not implemented");
  }

  getMin(): number {
    // TODO: implement
    throw new Error("Not implemented");
  }
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  const st = new MinStack();
  st.push(-2);
  st.push(0);
  st.push(-3);
  console.log(st.getMin()); // expected -3
  st.pop();
  console.log(st.top()); // expected 0
  console.log(st.getMin()); // expected -2
}
