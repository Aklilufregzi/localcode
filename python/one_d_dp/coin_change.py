"""
LeetCode 322. Coin Change (Medium)
https://leetcode.com/problems/coin-change/

Given coin denominations and an amount, return the fewest number of
coins needed to make up that amount (unlimited supply of each coin),
or -1 if it cannot be made. amount == 0 needs 0 coins.

Run just this file:   python one_d_dp/coin_change.py
Run its tests:        pytest one_d_dp/coin_change.py -v
"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().coinChange([1, 2, 5], 11) == 3


def test_example_2():
    assert Solution().coinChange([2], 3) == -1


def test_example_3():
    assert Solution().coinChange([1], 0) == 0


def test_greedy_fails():
    # Greedy would pick 4+1+1 (3 coins); optimal is 3+3 (2 coins).
    assert Solution().coinChange([1, 3, 4], 6) == 2


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))  # expected 3
    print(s.coinChange([2], 3))         # expected -1
