"""
LeetCode 295. Find Median from Data Stream (Hard)
https://leetcode.com/problems/find-median-from-data-stream/

Design MedianFinder: addNum(num) adds an integer from a data stream, and
findMedian() returns the median of all elements so far (the mean of the two
middle values when the count is even).

Run just this file:   python heap/find_median_from_data_stream.py
Run its tests:        pytest heap/find_median_from_data_stream.py -v
"""

import pytest


class MedianFinder:
    def __init__(self):
        ...  # TODO: implement

    def addNum(self, num: int) -> None:
        ...  # TODO: implement

    def findMedian(self) -> float:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_official_example():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == pytest.approx(1.5)
    mf.addNum(3)
    assert mf.findMedian() == pytest.approx(2.0)


def test_single_element():
    mf = MedianFinder()
    mf.addNum(5)
    assert mf.findMedian() == pytest.approx(5.0)


def test_unsorted_stream_with_negatives():
    mf = MedianFinder()
    for num in [6, -1, 3, 0]:
        mf.addNum(num)
    assert mf.findMedian() == pytest.approx(1.5)  # sorted: [-1, 0, 3, 6]
    mf.addNum(10)
    assert mf.findMedian() == pytest.approx(3.0)  # sorted: [-1, 0, 3, 6, 10]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # expected 1.5
    mf.addNum(3)
    print(mf.findMedian())  # expected 2.0
