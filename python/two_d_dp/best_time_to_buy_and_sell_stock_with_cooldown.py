"""
LeetCode 309. Best Time to Buy and Sell Stock with Cooldown (Medium)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Given daily stock prices, maximize profit with as many transactions as you
like, but after selling you must cool down one day before buying again,
and you may not hold more than one share at a time.

Run just this file:   python two_d_dp/best_time_to_buy_and_sell_stock_with_cooldown.py
Run its tests:        pytest two_d_dp/best_time_to_buy_and_sell_stock_with_cooldown.py -v
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # buy day0(1), sell day1(2), cooldown, buy day3(0), sell day4(2) -> 3
    assert Solution().maxProfit([1, 2, 3, 0, 2]) == 3


def test_example_2():
    assert Solution().maxProfit([1]) == 0


def test_decreasing_prices():
    assert Solution().maxProfit([5, 4, 3, 2, 1]) == 0


def test_two_days():
    assert Solution().maxProfit([1, 5]) == 4


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))  # expected 3
    print(s.maxProfit([1]))              # expected 0
