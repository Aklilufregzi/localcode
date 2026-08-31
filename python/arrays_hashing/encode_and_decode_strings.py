"""
LeetCode 271. Encode and Decode Strings (Medium)
https://leetcode.com/problems/encode-and-decode-strings/  (premium — NeetCode version)

Design an algorithm to encode a list of strings to a single string, and
decode that single string back to the original list. Strings may contain
any characters (including '#') and may be empty.

Run just this file:   python arrays_hashing/encode_and_decode_strings.py
Run its tests:        pytest arrays_hashing/encode_and_decode_strings.py -v
Run everything:       pytest
"""


class Solution:
    def encode(self, strs: list[str]) -> str:
        ...  # TODO: implement

    def decode(self, s: str) -> list[str]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------
# Encoded form is up to you — tests only check the round trip.

def roundtrip(strs: list[str]) -> list[str]:
    s = Solution()
    return s.decode(s.encode(strs))


def test_example_1():
    assert roundtrip(["neet", "code", "love", "you"]) == ["neet", "code", "love", "you"]


def test_example_2():
    assert roundtrip(["we", "say", ":", "yes"]) == ["we", "say", ":", "yes"]


def test_strings_containing_hash():
    assert roundtrip(["a#b", "#", "##", "c"]) == ["a#b", "#", "##", "c"]


def test_empty_strings():
    assert roundtrip(["", "", "a", ""]) == ["", "", "a", ""]


def test_empty_list():
    assert roundtrip([]) == []


if __name__ == "__main__":
    # Quick manual run / debugging playground — set breakpoints here.
    s = Solution()
    encoded = s.encode(["neet", "code", "love", "you"])
    print(encoded)
    print(s.decode(encoded))  # expected ["neet", "code", "love", "you"]
