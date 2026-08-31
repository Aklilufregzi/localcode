"""
LeetCode 207. Course Schedule (Medium)
https://leetcode.com/problems/course-schedule/

There are numCourses courses labeled 0..numCourses-1. prerequisites[i] =
[a, b] means you must take course b before course a. Return True if you can
finish all courses (i.e. the prerequisite graph has no cycle).

Run just this file:   python graphs/course_schedule.py
Run its tests:        pytest graphs/course_schedule.py -v
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().canFinish(2, [[1, 0]]) is True


def test_example_2_cycle():
    assert Solution().canFinish(2, [[1, 0], [0, 1]]) is False


def test_no_prerequisites():
    assert Solution().canFinish(3, []) is True


def test_longer_cycle():
    assert Solution().canFinish(4, [[1, 0], [2, 1], [3, 2], [1, 3]]) is False


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.canFinish(2, [[1, 0]]))          # expected True
    print(s.canFinish(2, [[1, 0], [0, 1]]))  # expected False
