"""
LeetCode 167. Two Sum II - Input Array Is Sorted (Medium)
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given a 1-indexed array of integers numbers sorted in non-decreasing order,
find two numbers that add up to a specific target. Return their 1-indexed
positions [index1, index2] with index1 < index2. Exactly one solution exists;
you may not use the same element twice. Use only constant extra space.

Run just this file:   python two_pointers/two_sum_ii_input_array_is_sorted.py
Run its tests:        pytest two_pointers/two_sum_ii_input_array_is_sorted.py -v
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]


def test_example_2():
    assert Solution().twoSum([2, 3, 4], 6) == [1, 3]


def test_example_3():
    assert Solution().twoSum([-1, 0], -1) == [1, 2]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # expected [1, 2]
    print(s.twoSum([2, 3, 4], 6))       # expected [1, 3]
