"""
LeetCode 518. Coin Change II (Medium)
https://leetcode.com/problems/coin-change-ii/

Given coin denominations and an amount, return the number of combinations
of coins that make up that amount (infinite supply of each coin). Return 0
if the amount cannot be made up.

Run just this file:   python two_d_dp/coin_change_ii.py
Run its tests:        pytest two_d_dp/coin_change_ii.py -v
"""


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # 5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1
    assert Solution().change(5, [1, 2, 5]) == 4


def test_example_2():
    assert Solution().change(3, [2]) == 0


def test_example_3():
    assert Solution().change(10, [10]) == 1


def test_zero_amount():
    # One way to make 0: use no coins.
    assert Solution().change(0, [7]) == 1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.change(5, [1, 2, 5]))  # expected 4
    print(s.change(3, [2]))        # expected 0
