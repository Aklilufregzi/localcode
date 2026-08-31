"""
LeetCode 1046. Last Stone Weight (Easy)
https://leetcode.com/problems/last-stone-weight/

Repeatedly smash the two heaviest stones x <= y together: if x == y both are
destroyed, otherwise y becomes y - x. Return the weight of the last remaining
stone, or 0 if none remain.

Run just this file:   python heap/last_stone_weight.py
Run its tests:        pytest heap/last_stone_weight.py -v
"""


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1


def test_example_2():
    assert Solution().lastStoneWeight([1]) == 1


def test_all_stones_destroyed():
    assert Solution().lastStoneWeight([2, 2]) == 0


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))  # expected 1
    print(s.lastStoneWeight([1]))                 # expected 1
