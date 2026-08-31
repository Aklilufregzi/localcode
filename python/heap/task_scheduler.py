"""
LeetCode 621. Task Scheduler (Medium)
https://leetcode.com/problems/task-scheduler/

Given CPU tasks labeled A-Z and a cooling interval n, the same task must be
at least n intervals apart; the CPU may idle. Return the minimum number of
intervals required to finish all tasks.

Run just this file:   python heap/task_scheduler.py
Run its tests:        pytest heap/task_scheduler.py -v
"""


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8


def test_example_2():
    assert Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6


def test_example_3():
    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    assert Solution().leastInterval(tasks, 2) == 16


def test_single_task():
    assert Solution().leastInterval(["A"], 100) == 1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # expected 8
    print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 0))  # expected 6
