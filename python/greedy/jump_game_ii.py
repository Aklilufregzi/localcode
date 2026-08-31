"""
LeetCode 45. Jump Game II (Medium)
https://leetcode.com/problems/jump-game-ii/

You start at index 0 of nums; nums[i] is your maximum jump length from
index i. Return the MINIMUM number of jumps to reach the last index.
Test cases are generated so the last index is always reachable.

Run just this file:   python greedy/jump_game_ii.py
Run its tests:        pytest greedy/jump_game_ii.py -v
"""


class Solution:
    def jump(self, nums: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().jump([2, 3, 1, 1, 4]) == 2


def test_example_2():
    assert Solution().jump([2, 3, 0, 1, 4]) == 2


def test_single_element():
    assert Solution().jump([0]) == 0


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))  # expected 2
