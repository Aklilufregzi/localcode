"""
LeetCode 746. Min Cost Climbing Stairs (Easy)
https://leetcode.com/problems/min-cost-climbing-stairs/

cost[i] is the cost of stepping on stair i; after paying you may climb
1 or 2 steps. You may start at index 0 or 1. Return the minimum cost
to reach the top of the floor (one past the last stair).

Run just this file:   python one_d_dp/min_cost_climbing_stairs.py
Run its tests:        pytest one_d_dp/min_cost_climbing_stairs.py -v
"""


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().minCostClimbingStairs([10, 15, 20]) == 15


def test_example_2():
    assert Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


def test_two_stairs():
    assert Solution().minCostClimbingStairs([5, 3]) == 3


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.minCostClimbingStairs([10, 15, 20]))  # expected 15
    print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # expected 6
