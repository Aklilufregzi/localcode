/**
 * LeetCode 22. Generate Parentheses (Medium)
 * https://leetcode.com/problems/generate-parentheses/
 *
 * Given n pairs of parentheses, generate all combinations of
 * well-formed parentheses.
 *
 * Run just this file:   npx tsx src/stack/generate-parentheses.ts
 * Run its tests:        npx vitest run src/stack/generate-parentheses.test.ts
 */

export function generateParenthesis(n: number): string[] {
  // TODO: implement
  throw new Error("Not implemented");
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(generateParenthesis(3)); // expected ["((()))","(()())","(())()","()(())","()()()"] in any order
}
