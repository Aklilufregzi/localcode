import { describe, expect, it } from "vitest";
import { groupAnagrams } from "./group-anagrams.ts";

// Order doesn't matter (neither group order nor order within a group) —
// normalize both sides before comparing.
function normalize(groups: string[][]): string[][] {
  return groups
    .map((g) => [...g].sort())
    .sort((a, b) => (a.join(",") < b.join(",") ? -1 : 1));
}

describe("groupAnagrams", () => {
  it("example 1", () => {
    const result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]);
    const expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]];
    expect(normalize(result)).toEqual(normalize(expected));
  });

  it("example 2", () => {
    expect(normalize(groupAnagrams([""]))).toEqual([[""]]);
  });

  it("example 3", () => {
    expect(normalize(groupAnagrams(["a"]))).toEqual([["a"]]);
  });
});
