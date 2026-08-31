"""
LeetCode 202. Happy Number (Easy)
https://leetcode.com/problems/happy-number/

Repeatedly replace n by the sum of the squares of its digits. n is "happy" if
this process reaches 1 (it otherwise falls into a cycle that never includes 1).
Return True iff n is a happy number.

Run just this file:   python math_geometry/happy_number.py
Run its tests:        pytest math_geometry/happy_number.py -v
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # 19 -> 82 -> 68 -> 100 -> 1
    assert Solution().isHappy(19) is True


def test_example_2():
    assert Solution().isHappy(2) is False


def test_one():
    assert Solution().isHappy(1) is True


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.isHappy(19))  # expected True
    print(s.isHappy(2))   # expected False
