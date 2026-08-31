"""
LeetCode 121. Best Time to Buy and Sell Stock (Easy)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a stock on the
i-th day. Choose a single day to buy and a later day to sell to maximize
profit. Return the maximum profit, or 0 if no profit is possible.

Run just this file:   python sliding_window/best_time_to_buy_and_sell_stock.py
Run its tests:        pytest sliding_window/best_time_to_buy_and_sell_stock.py -v
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # Buy on day 2 (price 1), sell on day 5 (price 6): profit 5.
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5


def test_example_2():
    # Prices only fall — no profitable transaction.
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0


def test_single_day():
    assert Solution().maxProfit([5]) == 0


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # expected 5
    print(s.maxProfit([7, 6, 4, 3, 1]))     # expected 0
