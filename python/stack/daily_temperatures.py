"""
LeetCode 739. Daily Temperatures (Medium)
https://leetcode.com/problems/daily-temperatures/

Given an array of daily temperatures, return an array answer where
answer[i] is the number of days you have to wait after day i to get a
warmer temperature. If there is no future warmer day, answer[i] = 0.

Run just this file:   python stack/daily_temperatures.py
Run its tests:        pytest stack/daily_temperatures.py -v
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1, 1, 4, 2, 1, 1, 0, 0
    ]


def test_example_2():
    assert Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]


def test_example_3():
    assert Solution().dailyTemperatures([30, 60, 90]) == [1, 1, 0]


def test_single_day():
    assert Solution().dailyTemperatures([50]) == [0]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # expected [1,1,4,2,1,1,0,0]
