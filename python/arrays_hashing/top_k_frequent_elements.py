"""
LeetCode 347. Top K Frequent Elements (Medium)
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent
elements. The answer is guaranteed unique; return it in any order.

Run just this file:   python arrays_hashing/top_k_frequent_elements.py
Run its tests:        pytest arrays_hashing/top_k_frequent_elements.py -v
Run everything:       pytest
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    # Order doesn't matter — compare as sorted lists.
    assert sorted(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]


def test_example_2():
    assert sorted(Solution().topKFrequent([1], 1)) == [1]


def test_k_equals_distinct_count():
    assert sorted(Solution().topKFrequent([4, 4, 5, 5, 6], 3)) == [4, 5, 6]


if __name__ == "__main__":
    # Quick manual run / debugging playground — set breakpoints here.
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # expected [1, 2] in any order
