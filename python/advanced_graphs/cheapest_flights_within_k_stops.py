"""
LeetCode 787. Cheapest Flights Within K Stops (Medium)
https://leetcode.com/problems/cheapest-flights-within-k-stops/

There are n cities and flights [from, to, price]. Return the cheapest price
from src to dst with at most k stops (i.e. at most k intermediate cities),
or -1 if no such route exists.

Run just this file:   python advanced_graphs/cheapest_flights_within_k_stops.py
Run its tests:        pytest advanced_graphs/cheapest_flights_within_k_stops.py -v
"""


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    # 0 -> 1 -> 2 -> 3 costs 400 but uses 2 stops; with k=1 the best is 0 -> 1 -> 3 = 700.
    assert Solution().findCheapestPrice(4, flights, 0, 3, 1) == 700


def test_example_2():
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    assert Solution().findCheapestPrice(3, flights, 0, 2, 1) == 200


def test_example_3_zero_stops():
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    assert Solution().findCheapestPrice(3, flights, 0, 2, 0) == 500


def test_unreachable():
    assert Solution().findCheapestPrice(3, [[0, 1, 100]], 0, 2, 1) == -1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    print(s.findCheapestPrice(4, flights, 0, 3, 1))  # expected 700
