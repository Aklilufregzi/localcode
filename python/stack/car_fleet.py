"""
LeetCode 853. Car Fleet (Medium)
https://leetcode.com/problems/car-fleet/

n cars at position[i] drive at speed[i] toward a destination at target
miles. A car cannot pass the car ahead; it catches up and travels at the
slower car's speed, forming a fleet. Return the number of fleets that
arrive at the destination (a fleet catching up exactly AT target counts as one).

Run just this file:   python stack/car_fleet.py
Run its tests:        pytest stack/car_fleet.py -v
"""


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3


def test_example_2():
    assert Solution().carFleet(10, [3], [3]) == 1


def test_example_3():
    # Cars starting at 0 and 2 merge at x=4; that fleet catches the car from 4 at x=6.
    assert Solution().carFleet(100, [0, 2, 4], [4, 2, 1]) == 1


def test_no_car_catches_up():
    assert Solution().carFleet(10, [6, 8], [3, 2]) == 2


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # expected 3
