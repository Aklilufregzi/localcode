"""
LeetCode 239. Sliding Window Maximum (Hard)
https://leetcode.com/problems/sliding-window-maximum/

You are given an integer array nums and a window of size k sliding from the
very left to the very right, moving one position at a time. Return an array
of the maximum value in each window position.

Run just this file:   python sliding_window/sliding_window_maximum.py
Run its tests:        pytest sliding_window/sliding_window_maximum.py -v
"""


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_example_2():
    assert Solution().maxSlidingWindow([1], 1) == [1]


def test_window_covers_whole_array():
    assert Solution().maxSlidingWindow([4, 2, 12], 3) == [12]


def test_decreasing():
    assert Solution().maxSlidingWindow([5, 4, 3, 2], 2) == [5, 4, 3]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # expected [3, 3, 5, 5, 6, 7]
