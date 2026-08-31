"""
LeetCode 15. 3Sum (Medium)
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, j != k, and
nums[i] + nums[j] + nums[k] == 0. The solution set must not contain
duplicate triplets. Answer may be returned in any order.

Run just this file:   python two_pointers/three_sum.py
Run its tests:        pytest two_pointers/three_sum.py -v
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def _normalize(triplets: list[list[int]]) -> list[list[int]]:
    # Output order doesn't matter (outer or inner) — sort both for comparison.
    return sorted(sorted(t) for t in triplets)


def test_example_1():
    result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    assert _normalize(result) == _normalize([[-1, -1, 2], [-1, 0, 1]])


def test_example_2():
    assert Solution().threeSum([0, 1, 1]) == []


def test_example_3():
    assert _normalize(Solution().threeSum([0, 0, 0])) == [[0, 0, 0]]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))  # expected [[-1, -1, 2], [-1, 0, 1]] (any order)
