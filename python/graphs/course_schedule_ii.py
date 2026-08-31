"""
LeetCode 210. Course Schedule II (Medium)
https://leetcode.com/problems/course-schedule-ii/

There are numCourses courses labeled 0..numCourses-1. prerequisites[i] =
[a, b] means you must take course b before course a. Return ANY valid order
to take all courses, or [] if it is impossible (the graph has a cycle).

Run just this file:   python graphs/course_schedule_ii.py
Run its tests:        pytest graphs/course_schedule_ii.py -v
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------
# Any valid topological order is accepted — assert validity, not one answer.

def _assert_valid_order(order: list[int], num_courses: int, prerequisites: list[list[int]]) -> None:
    assert sorted(order) == list(range(num_courses)), "must be a permutation of all courses"
    pos = {course: i for i, course in enumerate(order)}
    for a, b in prerequisites:
        assert pos[b] < pos[a], f"course {b} must come before course {a}"


def test_example_1():
    _assert_valid_order(Solution().findOrder(2, [[1, 0]]), 2, [[1, 0]])


def test_example_2():
    prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
    _assert_valid_order(Solution().findOrder(4, prereqs), 4, prereqs)


def test_example_3_single_course():
    _assert_valid_order(Solution().findOrder(1, []), 1, [])


def test_cycle_returns_empty():
    assert Solution().findOrder(2, [[1, 0], [0, 1]]) == []


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    # expected: any valid order, e.g. [0, 1, 2, 3] or [0, 2, 1, 3]
