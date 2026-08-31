"""
LeetCode 332. Reconstruct Itinerary (Hard)
https://leetcode.com/problems/reconstruct-itinerary/

Given a list of airline tickets [from, to], reconstruct the itinerary in order
starting from "JFK", using every ticket exactly once. If multiple valid
itineraries exist, return the one with the smallest lexical order when read as
a single string.

Run just this file:   python advanced_graphs/reconstruct_itinerary.py
Run its tests:        pytest advanced_graphs/reconstruct_itinerary.py -v
"""


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    assert Solution().findItinerary(tickets) == ["JFK", "MUC", "LHR", "SFO", "SJC"]


def test_example_2():
    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    # ["JFK","SFO","ATL","JFK","ATL","SFO"] is also valid but lexically larger.
    assert Solution().findItinerary(tickets) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]


def test_single_ticket():
    assert Solution().findItinerary([["JFK", "SFO"]]) == ["JFK", "SFO"]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    # expected ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
