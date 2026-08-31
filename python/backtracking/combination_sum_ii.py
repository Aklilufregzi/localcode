"""
LeetCode 40. Combination Sum II (Medium)
https://leetcode.com/problems/combination-sum-ii/

Given a list of candidates (may contain duplicates) and a target, return
all unique combinations where the candidates sum to target. Each candidate
may be used at most once; the result must not contain duplicate combinations.

Run just this file:   python backtracking/combination_sum_ii.py
Run its tests:        pytest backtracking/combination_sum_ii.py -v
"""


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def _norm(res: list[list[int]]) -> list[list[int]]:
    # Order doesn't matter (outer or inner) — normalize before comparing.
    return sorted(map(sorted, res))


def test_example_1():
    expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    assert _norm(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)) == _norm(expected)


def test_example_2():
    expected = [[1, 2, 2], [5]]
    assert _norm(Solution().combinationSum2([2, 5, 2, 1, 2], 5)) == _norm(expected)


def test_no_combination():
    assert Solution().combinationSum2([3, 5], 2) == []


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))  # expected [[1,1,6],[1,2,5],[1,7],[2,6]] any order
