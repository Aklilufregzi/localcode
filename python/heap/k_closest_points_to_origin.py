"""
LeetCode 973. K Closest Points to Origin (Medium)
https://leetcode.com/problems/k-closest-points-to-origin/

Given a list of points [x, y] on a plane and an integer k, return the k points
closest to the origin (0, 0) by Euclidean distance. The answer is guaranteed
unique (except for order).

Run just this file:   python heap/k_closest_points_to_origin.py
Run its tests:        pytest heap/k_closest_points_to_origin.py -v
"""


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]


def test_example_2():
    # Output order doesn't matter — normalize by sorting.
    result = Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2)
    assert sorted(result) == sorted([[3, 3], [-2, 4]])


def test_k_equals_all_points():
    result = Solution().kClosest([[0, 1], [1, 0]], 2)
    assert sorted(result) == [[0, 1], [1, 0]]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.kClosest([[1, 3], [-2, 2]], 1))          # expected [[-2, 2]]
    print(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))  # expected [[3, 3], [-2, 4]] in any order
