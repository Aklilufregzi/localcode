"""
LeetCode 134. Gas Station (Medium)
https://leetcode.com/problems/gas-station/

There are n gas stations on a circle; gas[i] is fuel available at station
i and cost[i] is fuel needed to drive to station i+1. Starting empty,
return the index of the station from which you can travel the full circuit
once clockwise, or -1 if impossible. If a solution exists it is unique.

Run just this file:   python greedy/gas_station.py
Run its tests:        pytest greedy/gas_station.py -v
"""


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3


def test_example_2():
    assert Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1


def test_single_station():
    assert Solution().canCompleteCircuit([5], [4]) == 0


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # expected 3
