"""
LeetCode 70. Climbing Stairs (Easy)
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase with n steps. Each time you can climb
either 1 or 2 steps. In how many distinct ways can you reach the top?

Run just this file:   python one_d_dp/climbing_stairs.py
Run its tests:        pytest one_d_dp/climbing_stairs.py -v
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().climbStairs(2) == 2


def test_example_2():
    assert Solution().climbStairs(3) == 3


def test_single_step():
    assert Solution().climbStairs(1) == 1


def test_larger():
    assert Solution().climbStairs(10) == 89


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.climbStairs(2))  # expected 2
    print(s.climbStairs(3))  # expected 3
