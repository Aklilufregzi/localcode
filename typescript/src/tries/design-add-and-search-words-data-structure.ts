/**
 * LeetCode 211. Design Add and Search Words Data Structure (Medium)
 * https://leetcode.com/problems/design-add-and-search-words-data-structure/
 *
 * Design a data structure supporting addWord(word) and search(word), where
 * search may contain '.' wildcards that match any single letter. All other
 * characters are lowercase English letters.
 *
 * Run just this file:   npx tsx src/tries/design-add-and-search-words-data-structure.ts
 * Run its tests:        npx vitest run src/tries/design-add-and-search-words-data-structure.test.ts
 */

export class WordDictionary {
  constructor() {
    // TODO: implement
  }

  addWord(word: string): void {
    throw new Error("Not implemented");
  }

  search(word: string): boolean {
    throw new Error("Not implemented");
  }
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  const wd = new WordDictionary();
  wd.addWord("bad");
  wd.addWord("dad");
  wd.addWord("mad");
  console.log(wd.search("pad")); // expected false
  console.log(wd.search("bad")); // expected true
  console.log(wd.search(".ad")); // expected true
  console.log(wd.search("b..")); // expected true
}
