"""
LeetCode 51. N-Queens (Hard)
https://leetcode.com/problems/n-queens/

Place n queens on an n x n chessboard so that no two queens attack each
other. Return all distinct solutions; each solution is a board of strings
where 'Q' marks a queen and '.' an empty square.

Run just this file:   python backtracking/n_queens.py
Run its tests:        pytest backtracking/n_queens.py -v
"""


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------
# The list of boards may come back in any order (each board's rows stay
# ordered) — sort only the outer list before comparing.

def test_example_1():
    expected = [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ]
    assert sorted(Solution().solveNQueens(4)) == sorted(expected)


def test_example_2():
    assert Solution().solveNQueens(1) == [["Q"]]


def test_no_solution_for_n_3():
    assert Solution().solveNQueens(3) == []


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    for board in s.solveNQueens(4):  # expected 2 solutions
        print("\n".join(board))
        print()
