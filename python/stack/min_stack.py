"""
LeetCode 155. Min Stack (Medium)
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum
element, each in O(1) time. Implement the MinStack class with
push(val), pop(), top(), and getMin().

Run just this file:   python stack/min_stack.py
Run its tests:        pytest stack/min_stack.py -v
"""


class MinStack:
    def __init__(self):
        ...  # TODO: implement

    def push(self, val: int) -> None:
        ...  # TODO: implement

    def pop(self) -> None:
        ...  # TODO: implement

    def top(self) -> int:
        ...  # TODO: implement

    def getMin(self) -> int:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_official_example():
    st = MinStack()
    st.push(-2)
    st.push(0)
    st.push(-3)
    assert st.getMin() == -3
    st.pop()
    assert st.top() == 0
    assert st.getMin() == -2


def test_min_updates_after_pops():
    st = MinStack()
    st.push(5)
    st.push(1)
    st.push(3)
    assert st.getMin() == 1
    st.pop()  # removes 3
    assert st.getMin() == 1
    st.pop()  # removes 1
    assert st.getMin() == 5
    assert st.top() == 5


def test_duplicate_minimums():
    st = MinStack()
    st.push(2)
    st.push(2)
    st.push(3)
    st.pop()
    assert st.getMin() == 2
    st.pop()
    assert st.getMin() == 2


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    st = MinStack()
    st.push(-2)
    st.push(0)
    st.push(-3)
    print(st.getMin())  # expected -3
    st.pop()
    print(st.top())     # expected 0
    print(st.getMin())  # expected -2
