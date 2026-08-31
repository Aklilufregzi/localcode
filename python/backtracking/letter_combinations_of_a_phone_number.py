"""
LeetCode 17. Letter Combinations of a Phone Number (Medium)
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits 2-9, return all possible letter
combinations the number could represent on a phone keypad
(2=abc, 3=def, ..., 9=wxyz), in any order.

Run just this file:   python backtracking/letter_combinations_of_a_phone_number.py
Run its tests:        pytest backtracking/letter_combinations_of_a_phone_number.py -v
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------
# Combinations may come back in any order — sort before comparing.

def test_example_1():
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sorted(Solution().letterCombinations("23")) == sorted(expected)


def test_example_2():
    assert Solution().letterCombinations("") == []


def test_example_3():
    assert sorted(Solution().letterCombinations("2")) == ["a", "b", "c"]


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.letterCombinations("23"))  # expected ["ad","ae","af","bd","be","bf","cd","ce","cf"] any order
