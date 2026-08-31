/**
 * LeetCode 150. Evaluate Reverse Polish Notation (Medium)
 * https://leetcode.com/problems/evaluate-reverse-polish-notation/
 *
 * Evaluate an arithmetic expression given in Reverse Polish Notation.
 * Valid operators are +, -, * and /. Division between two integers
 * truncates toward zero. Operands may be integers or other expressions.
 *
 * Run just this file:   npx tsx src/stack/evaluate-reverse-polish-notation.ts
 * Run its tests:        npx vitest run src/stack/evaluate-reverse-polish-notation.test.ts
 */

export function evalRPN(tokens: string[]): number {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(evalRPN(["2", "1", "+", "3", "*"])); // expected 9
  console.log(evalRPN(["4", "13", "5", "/", "+"])); // expected 6
}
