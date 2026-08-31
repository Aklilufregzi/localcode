"""
LeetCode 743. Network Delay Time (Medium)
https://leetcode.com/problems/network-delay-time/

Given directed weighted edges times[i] = (u, v, w) meaning a signal takes w
time to travel u -> v, n nodes labeled 1..n, and a start node k: return the
time for the signal sent from k to reach ALL nodes, or -1 if impossible.

Run just this file:   python advanced_graphs/network_delay_time.py
Run its tests:        pytest advanced_graphs/network_delay_time.py -v
"""


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2


def test_example_2():
    assert Solution().networkDelayTime([[1, 2, 1]], 2, 1) == 1


def test_example_3_unreachable():
    assert Solution().networkDelayTime([[1, 2, 1]], 2, 2) == -1


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # expected 2
