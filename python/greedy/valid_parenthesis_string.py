"""
LeetCode 678. Valid Parenthesis String (Medium)
https://leetcode.com/problems/valid-parenthesis-string/

Given a string s containing '(', ')' and '*', where '*' can be treated as
a single '(' or ')' or an empty string, return True if s can be made a
valid parenthesis string.

Run just this file:   python greedy/valid_parenthesis_string.py
Run its tests:        pytest greedy/valid_parenthesis_string.py -v
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().checkValidString("()") is True


def test_example_2():
    assert Solution().checkValidString("(*)") is True


def test_example_3():
    assert Solution().checkValidString("(*))") is True


def test_star_then_open_is_invalid():
    assert Solution().checkValidString("*(") is False


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.checkValidString("(*))"))  # expected True
    print(s.checkValidString("*("))   # expected False
