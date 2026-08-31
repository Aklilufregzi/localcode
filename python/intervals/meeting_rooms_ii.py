"""
LeetCode 253. Meeting Rooms II (Medium) — premium; NeetCode statement/signature
https://leetcode.com/problems/meeting-rooms-ii/  (https://neetcode.io/problems/meeting-schedule-ii)

Given an array of meeting time intervals [start, end], return the minimum
number of conference rooms required to hold all meetings. A meeting ending
at t and another starting at t can share a room.

Run just this file:   python intervals/meeting_rooms_ii.py
Run its tests:        pytest intervals/meeting_rooms_ii.py -v
"""


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # (0,40) overlaps (5,10) and (15,20), which don't overlap each other.
    assert Solution().minMeetingRooms([[0, 40], [5, 10], [15, 20]]) == 2


def test_example_2():
    assert Solution().minMeetingRooms([[4, 9]]) == 1


def test_all_overlapping():
    assert Solution().minMeetingRooms([[1, 10], [2, 10], [3, 10]]) == 3


def test_back_to_back():
    # A meeting ending at t and one starting at t can reuse the room.
    assert Solution().minMeetingRooms([[0, 5], [5, 10]]) == 1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.minMeetingRooms([[0, 40], [5, 10], [15, 20]]))  # expected 2
