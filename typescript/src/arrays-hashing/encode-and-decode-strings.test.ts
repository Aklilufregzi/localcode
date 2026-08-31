import { describe, expect, it } from "vitest";
import { Solution } from "./encode-and-decode-strings.ts";

// Encoded form is up to you — tests only check the round trip.
function roundtrip(strs: string[]): string[] {
  const s = new Solution();
  return s.decode(s.encode(strs));
}

describe("encode/decode", () => {
  it("example 1", () => {
    expect(roundtrip(["neet", "code", "love", "you"])).toEqual(["neet", "code", "love", "you"]);
  });

  it("example 2", () => {
    expect(roundtrip(["we", "say", ":", "yes"])).toEqual(["we", "say", ":", "yes"]);
  });

  it("strings containing '#'", () => {
    expect(roundtrip(["a#b", "#", "##", "c"])).toEqual(["a#b", "#", "##", "c"]);
  });

  it("empty strings", () => {
    expect(roundtrip(["", "", "a", ""])).toEqual(["", "", "a", ""]);
  });

  it("empty list", () => {
    expect(roundtrip([])).toEqual([]);
  });
});
