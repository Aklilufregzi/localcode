import { describe, expect, it } from "vitest";
import { Trie } from "./implement-trie-prefix-tree.ts";

describe("Trie", () => {
  it("official example", () => {
    const trie = new Trie();
    trie.insert("apple");
    expect(trie.search("apple")).toBe(true);
    expect(trie.search("app")).toBe(false);
    expect(trie.startsWith("app")).toBe(true);
    trie.insert("app");
    expect(trie.search("app")).toBe(true);
  });

  it("prefix is not a word", () => {
    const trie = new Trie();
    trie.insert("car");
    expect(trie.search("ca")).toBe(false);
    expect(trie.startsWith("ca")).toBe(true);
    expect(trie.startsWith("card")).toBe(false);
  });

  it("single letter word", () => {
    const trie = new Trie();
    trie.insert("a");
    expect(trie.search("a")).toBe(true);
    expect(trie.startsWith("a")).toBe(true);
    expect(trie.search("b")).toBe(false);
  });
});
