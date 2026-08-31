"""
LeetCode 494. Target Sum (Medium)
https://leetcode.com/problems/target-sum/

Given an integer array nums and an integer target, assign '+' or '-' before
each number so the resulting expression evaluates to target. Return the
number of different expressions that do so.

Run just this file:   python two_d_dp/target_sum.py
Run its tests:        pytest two_d_dp/target_sum.py -v
"""


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # -1+1+1+1+1, +1-1+1+1+1, +1+1-1+1+1, +1+1+1-1+1, +1+1+1+1-1
    assert Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5


def test_example_2():
    assert Solution().findTargetSumWays([1], 1) == 1


def test_unreachable_target():
    assert Solution().findTargetSumWays([1], 2) == 0


def test_with_zero():
    # +0+1 and -0+1 both reach 1
    assert Solution().findTargetSumWays([0, 1], 1) == 2


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))  # expected 5
    print(s.findTargetSumWays([1], 1))              # expected 1
