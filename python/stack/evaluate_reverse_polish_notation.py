"""
LeetCode 150. Evaluate Reverse Polish Notation (Medium)
https://leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate an arithmetic expression given in Reverse Polish Notation.
Valid operators are +, -, * and /. Division between two integers
truncates toward zero. Operands may be integers or other expressions.

Run just this file:   python stack/evaluate_reverse_polish_notation.py
Run its tests:        pytest stack/evaluate_reverse_polish_notation.py -v
"""


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # (2 + 1) * 3 = 9
    assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9


def test_example_2():
    # 4 + (13 / 5) = 4 + 2 = 6
    assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6


def test_example_3():
    # ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22 (division truncates toward zero)
    assert Solution().evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    ) == 22


def test_single_token():
    assert Solution().evalRPN(["18"]) == 18


def test_negative_division_truncates_toward_zero():
    # -7 / 2 truncates to -3, not -4
    assert Solution().evalRPN(["-7", "2", "/"]) == -3


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.evalRPN(["2", "1", "+", "3", "*"]))   # expected 9
    print(s.evalRPN(["4", "13", "5", "/", "+"]))  # expected 6
