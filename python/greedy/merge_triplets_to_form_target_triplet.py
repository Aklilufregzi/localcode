"""
LeetCode 1899. Merge Triplets to Form Target Triplet (Medium)
https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

Given triplets[i] = [a, b, c] and a target triplet [x, y, z], you may
repeatedly pick two triplets and replace one with their element-wise max.
Return True if target can be made equal to some triplet, False otherwise.

Run just this file:   python greedy/merge_triplets_to_form_target_triplet.py
Run its tests:        pytest greedy/merge_triplets_to_form_target_triplet.py -v
"""


class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]) is True


def test_example_2():
    assert Solution().mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]) is False


def test_example_3():
    assert Solution().mergeTriplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]) is True


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]))  # expected True
