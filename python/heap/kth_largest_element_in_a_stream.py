"""
LeetCode 703. Kth Largest Element in a Stream (Easy)
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class that, initialized with k and an initial list of scores nums,
supports add(val) which inserts val into the stream and returns the kth
largest element seen so far (with duplicates counted).

Run just this file:   python heap/kth_largest_element_in_a_stream.py
Run its tests:        pytest heap/kth_largest_element_in_a_stream.py -v
"""


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        ...  # TODO: implement

    def add(self, val: int) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_official_example():
    kth = KthLargest(3, [4, 5, 8, 2])
    assert kth.add(3) == 4
    assert kth.add(5) == 5
    assert kth.add(10) == 5
    assert kth.add(9) == 8
    assert kth.add(4) == 8


def test_starts_with_fewer_than_k_elements():
    # nums may start with fewer than k elements; k exist once we add.
    kth = KthLargest(2, [1])
    assert kth.add(2) == 1
    assert kth.add(3) == 2
    assert kth.add(10) == 3


def test_k_equals_one():
    kth = KthLargest(1, [7])
    assert kth.add(3) == 7
    assert kth.add(9) == 9


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    kth = KthLargest(3, [4, 5, 8, 2])
    print(kth.add(3))   # expected 4
    print(kth.add(5))   # expected 5
    print(kth.add(10))  # expected 5
    print(kth.add(9))   # expected 8
    print(kth.add(4))   # expected 8
