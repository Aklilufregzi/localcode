"""
LeetCode 20. Valid Parentheses (Easy)
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just '(', ')', '{', '}', '[' and ']', determine
if the input string is valid: open brackets must be closed by the same type
of bracket and in the correct order.

Run just this file:   python stack/valid_parentheses.py
Run its tests:        pytest stack/valid_parentheses.py -v
"""


class Solution:
    def isValid(self, s: str) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().isValid("()") is True


def test_example_2():
    assert Solution().isValid("()[]{}") is True


def test_example_3():
    assert Solution().isValid("(]") is False


def test_wrong_nesting_order():
    assert Solution().isValid("([)]") is False


def test_single_open_bracket():
    assert Solution().isValid("(") is False


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.isValid("()[]{}"))  # expected True
    print(s.isValid("(]"))      # expected False
