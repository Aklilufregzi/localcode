"""
LeetCode 78. Subsets (Medium)
https://leetcode.com/problems/subsets/

Given an array nums of unique integers, return all possible subsets
(the power set). The solution set must not contain duplicate subsets;
return it in any order.

Run just this file:   python backtracking/subsets.py
Run its tests:        pytest backtracking/subsets.py -v
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def _norm(res: list[list[int]]) -> list[list[int]]:
    # Order doesn't matter (outer or inner) — normalize before comparing.
    return sorted(map(sorted, res))


def test_example_1():
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert _norm(Solution().subsets([1, 2, 3])) == _norm(expected)


def test_example_2():
    expected = [[], [0]]
    assert _norm(Solution().subsets([0])) == _norm(expected)


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.subsets([1, 2, 3]))  # expected all 8 subsets of {1,2,3}, any order
