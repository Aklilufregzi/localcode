"""
LeetCode 286. Walls and Gates (Medium) — premium; NeetCode calls it "Islands and Treasure"
https://leetcode.com/problems/walls-and-gates/
https://neetcode.io/problems/islands-and-treasure

Given a grid where -1 is a wall, 0 is a gate (treasure chest), and
2147483647 (INF) is an empty room, fill each empty room IN PLACE with the
distance to its nearest gate. Leave a room as INF if no gate is reachable.

Run just this file:   python graphs/walls_and_gates.py
Run its tests:        pytest graphs/walls_and_gates.py -v
"""

INF = 2147483647


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        """Do not return anything, modify grid in-place instead."""
        ...  # TODO: implement


# ---------------------------- tests ----------------------------
# In-place problem: call islandsAndTreasure(), then assert on the mutated grid.

def test_example_1():
    grid = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]
    Solution().islandsAndTreasure(grid)
    assert grid == [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]


def test_example_2():
    grid = [
        [0, -1],
        [INF, INF],
    ]
    Solution().islandsAndTreasure(grid)
    assert grid == [
        [0, -1],
        [1, 2],
    ]


def test_unreachable_room_stays_inf():
    grid = [
        [0, -1, INF],
    ]
    Solution().islandsAndTreasure(grid)
    assert grid == [
        [0, -1, INF],
    ]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    grid = [
        [0, -1],
        [INF, INF],
    ]
    s.islandsAndTreasure(grid)
    print(grid)  # expected [[0, -1], [1, 2]]
