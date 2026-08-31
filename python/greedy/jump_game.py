"""
LeetCode 55. Jump Game (Medium)
https://leetcode.com/problems/jump-game/

You start at index 0 of nums; nums[i] is your maximum jump length from
index i. Return True if you can reach the last index, False otherwise.

Run just this file:   python greedy/jump_game.py
Run its tests:        pytest greedy/jump_game.py -v
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().canJump([2, 3, 1, 1, 4]) is True


def test_example_2():
    assert Solution().canJump([3, 2, 1, 0, 4]) is False


def test_single_element():
    assert Solution().canJump([0]) is True


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))  # expected True
    print(s.canJump([3, 2, 1, 0, 4]))  # expected False
