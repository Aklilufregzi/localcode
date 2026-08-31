"""
LeetCode 416. Partition Equal Subset Sum (Medium)
https://leetcode.com/problems/partition-equal-subset-sum/

Given an array nums of positive integers, return True if it can be
partitioned into two subsets whose sums are equal.

Run just this file:   python one_d_dp/partition_equal_subset_sum.py
Run its tests:        pytest one_d_dp/partition_equal_subset_sum.py -v
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().canPartition([1, 5, 11, 5]) is True


def test_example_2():
    assert Solution().canPartition([1, 2, 3, 5]) is False


def test_single_element():
    assert Solution().canPartition([1]) is False


def test_pair():
    assert Solution().canPartition([4, 4]) is True


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.canPartition([1, 5, 11, 5]))  # expected True
    print(s.canPartition([1, 2, 3, 5]))   # expected False
