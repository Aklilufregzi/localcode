"""
LeetCode 1. Two Sum (Easy)
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of
the two numbers such that they add up to target.

Run just this file:   python arrays_hashing/two_sum.py
Run its tests:        pytest arrays_hashing/two_sum.py -v
Run everything:       pytest
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [seen[complement], i]
            seen[n] = i
        return []


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_example_2():
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]


def test_same_number_twice():
    assert Solution().twoSum([3, 3], 6) == [0, 1]


if __name__ == "__main__":
    # Quick manual run / debugging playground — set breakpoints here.
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # expected [0, 1]
    print(s.twoSum([3, 2, 4], 6))       # expected [1, 2]
