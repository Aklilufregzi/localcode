import { describe, expect, it } from "vitest";
import { WordDictionary } from "./design-add-and-search-words-data-structure.ts";

describe("WordDictionary", () => {
  it("official example", () => {
    const wd = new WordDictionary();
    wd.addWord("bad");
    wd.addWord("dad");
    wd.addWord("mad");
    expect(wd.search("pad")).toBe(false);
    expect(wd.search("bad")).toBe(true);
    expect(wd.search(".ad")).toBe(true);
    expect(wd.search("b..")).toBe(true);
  });

  it("wildcard length must match", () => {
    const wd = new WordDictionary();
    wd.addWord("bad");
    expect(wd.search("b.")).toBe(false);
    expect(wd.search("b...")).toBe(false);
    expect(wd.search("...")).toBe(true);
  });

  it("all wildcards, empty then non-empty dictionary", () => {
    const wd = new WordDictionary();
    expect(wd.search(".")).toBe(false);
    wd.addWord("a");
    expect(wd.search(".")).toBe(true);
  });
});
