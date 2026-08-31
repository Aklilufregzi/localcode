"""
LeetCode 846. Hand of Straights (Medium)
https://leetcode.com/problems/hand-of-straights/

Given an array hand of card values and an integer groupSize, return True
if the cards can be rearranged into groups of exactly groupSize
consecutive cards, False otherwise.

Run just this file:   python greedy/hand_of_straights.py
Run its tests:        pytest greedy/hand_of_straights.py -v
"""


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) is True


def test_example_2():
    assert Solution().isNStraightHand([1, 2, 3, 4, 5], 4) is False


def test_group_size_one():
    assert Solution().isNStraightHand([8, 10, 12], 1) is True


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))  # expected True
