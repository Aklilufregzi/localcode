"""
LeetCode 46. Permutations (Medium)
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all possible
permutations, in any order.

Run just this file:   python backtracking/permutations.py
Run its tests:        pytest backtracking/permutations.py -v
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------
# Outer order doesn't matter; each inner list IS a permutation, so only
# the outer list is sorted before comparing.

def test_example_1():
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert sorted(Solution().permute([1, 2, 3])) == sorted(expected)


def test_example_2():
    expected = [[0, 1], [1, 0]]
    assert sorted(Solution().permute([0, 1])) == sorted(expected)


def test_example_3():
    assert Solution().permute([1]) == [[1]]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.permute([1, 2, 3]))  # expected all 6 permutations, any order
