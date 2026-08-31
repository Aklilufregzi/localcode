"""
LeetCode 1584. Min Cost to Connect All Points (Medium)
https://leetcode.com/problems/min-cost-to-connect-all-points/

You are given points on a 2D plane. The cost of connecting two points is their
Manhattan distance |xi - xj| + |yi - yj|. Return the minimum total cost to make
all points connected (i.e. the weight of a minimum spanning tree).

Run just this file:   python advanced_graphs/min_cost_to_connect_all_points.py
Run its tests:        pytest advanced_graphs/min_cost_to_connect_all_points.py -v
"""


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20


def test_example_2():
    assert Solution().minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18


def test_single_point():
    assert Solution().minCostConnectPoints([[0, 0]]) == 0


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))  # expected 20
