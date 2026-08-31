"""
LeetCode 90. Subsets II (Medium)
https://leetcode.com/problems/subsets-ii/

Given an array nums that may contain duplicates, return all possible
subsets (the power set) without duplicate subsets, in any order.

Run just this file:   python backtracking/subsets_ii.py
Run its tests:        pytest backtracking/subsets_ii.py -v
"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def _norm(res: list[list[int]]) -> list[list[int]]:
    # Order doesn't matter (outer or inner) — normalize before comparing.
    return sorted(map(sorted, res))


def test_example_1():
    expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    assert _norm(Solution().subsetsWithDup([1, 2, 2])) == _norm(expected)


def test_example_2():
    expected = [[], [0]]
    assert _norm(Solution().subsetsWithDup([0])) == _norm(expected)


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))  # expected [[],[1],[1,2],[1,2,2],[2],[2,2]] any order
