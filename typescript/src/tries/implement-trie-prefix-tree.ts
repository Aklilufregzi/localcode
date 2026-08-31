/**
 * LeetCode 208. Implement Trie (Prefix Tree) (Medium)
 * https://leetcode.com/problems/implement-trie-prefix-tree/
 *
 * Implement a trie with insert(word), search(word) returning whether the exact
 * word was inserted, and startsWith(prefix) returning whether any inserted
 * word has the given prefix. Words consist of lowercase English letters.
 *
 * Run just this file:   npx tsx src/tries/implement-trie-prefix-tree.ts
 * Run its tests:        npx vitest run src/tries/implement-trie-prefix-tree.test.ts
 */

export class Trie {
  constructor() {
    // TODO: implement
  }

  insert(word: string): void {
    throw new Error("Not implemented");
  }

  search(word: string): boolean {
    throw new Error("Not implemented");
  }

  startsWith(prefix: string): boolean {
    throw new Error("Not implemented");
  }
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === `file://${process.argv[1]}`) {
  const trie = new Trie();
  trie.insert("apple");
  console.log(trie.search("apple")); // expected true
  console.log(trie.search("app")); // expected false
  console.log(trie.startsWith("app")); // expected true
}
