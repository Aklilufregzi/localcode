"""
LeetCode 252. Meeting Rooms (Easy) — premium; NeetCode statement/signature
https://leetcode.com/problems/meeting-rooms/  (https://neetcode.io/problems/meeting-schedule)

Given an array of meeting time intervals [start, end], determine if a
person could attend all meetings (no two meetings overlap). Meetings that
only touch, e.g. (0,8) and (8,10), do NOT overlap.

Run just this file:   python intervals/meeting_rooms.py
Run its tests:        pytest intervals/meeting_rooms.py -v
"""


class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # (0,30) overlaps both (5,10) and (15,20).
    assert Solution().canAttendMeetings([[0, 30], [5, 10], [15, 20]]) is False


def test_example_2():
    assert Solution().canAttendMeetings([[5, 8], [9, 15]]) is True


def test_touching_meetings():
    # Back-to-back meetings do not overlap.
    assert Solution().canAttendMeetings([[0, 8], [8, 10]]) is True


def test_no_meetings():
    assert Solution().canAttendMeetings([]) is True


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))  # expected False
    print(s.canAttendMeetings([[5, 8], [9, 15]]))             # expected True
