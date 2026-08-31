"""
LeetCode 39. Combination Sum (Medium)
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target, return all
unique combinations of candidates that sum to target. The same number may
be chosen an unlimited number of times. Return combinations in any order.

Run just this file:   python backtracking/combination_sum.py
Run its tests:        pytest backtracking/combination_sum.py -v
"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def _norm(res: list[list[int]]) -> list[list[int]]:
    # Order doesn't matter (outer or inner) — normalize before comparing.
    return sorted(map(sorted, res))


def test_example_1():
    expected = [[2, 2, 3], [7]]
    assert _norm(Solution().combinationSum([2, 3, 6, 7], 7)) == _norm(expected)


def test_example_2():
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert _norm(Solution().combinationSum([2, 3, 5], 8)) == _norm(expected)


def test_example_3():
    assert Solution().combinationSum([2], 1) == []


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))  # expected [[2,2,3],[7]] in any order
