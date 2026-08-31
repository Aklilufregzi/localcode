/**
 * LeetCode 125. Valid Palindrome (Easy)
 * https://leetcode.com/problems/valid-palindrome/
 *
 * Given a string s, return true if it is a palindrome after converting all
 * uppercase letters to lowercase and removing all non-alphanumeric
 * characters, and false otherwise.
 *
 * Run just this file:   npx tsx src/two-pointers/valid-palindrome.ts
 * Run its tests:        npx vitest run src/two-pointers/valid-palindrome.test.ts
 */

export function isPalindrome(s: string): boolean {
  // TODO: implement
 console.log("hello")
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(isPalindrome("A man, a plan, a canal: Panama")); // expected true
  console.log(isPalindrome("race a car")); // expected false
}
