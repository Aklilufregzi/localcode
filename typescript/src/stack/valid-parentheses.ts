/**
 * LeetCode 20. Valid Parentheses (Easy)
 * https://leetcode.com/problems/valid-parentheses/
 *
 * Given a string s containing just '(', ')', '{', '}', '[' and ']', determine
 * if the input string is valid: open brackets must be closed by the same type
 * of bracket and in the correct order.
 *
 * Run just this file:   npx tsx src/stack/valid-parentheses.ts
 * Run its tests:        npx vitest run src/stack/valid-parentheses.test.ts
 */

export function isValid(s: string): boolean {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(isValid("()[]{}")); // expected true
  console.log(isValid("(]")); // expected false
}
