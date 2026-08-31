"""
LeetCode 22. Generate Parentheses (Medium)
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, generate all combinations of
well-formed parentheses.

Run just this file:   python stack/generate_parentheses.py
Run its tests:        pytest stack/generate_parentheses.py -v
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------
# Output order doesn't matter — compare sorted.

def test_example_1():
    assert sorted(Solution().generateParenthesis(3)) == sorted(
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
    )


def test_example_2():
    assert sorted(Solution().generateParenthesis(1)) == ["()"]


def test_n_2():
    assert sorted(Solution().generateParenthesis(2)) == sorted(["(())", "()()"])


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.generateParenthesis(3))  # expected ["((()))","(()())","(())()","()(())","()()()"] in any order
