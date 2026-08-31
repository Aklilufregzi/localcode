"""
LeetCode 125. Valid Palindrome (Easy)
https://leetcode.com/problems/valid-palindrome/

Given a string s, return true if it is a palindrome after converting all
uppercase letters to lowercase and removing all non-alphanumeric characters,
and false otherwise.

Run just this file:   python two_pointers/valid_palindrome.py
Run its tests:        pytest two_pointers/valid_palindrome.py -v
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") is True


def test_example_2():
    assert Solution().isPalindrome("race a car") is False


def test_example_3():
    # After removing non-alphanumerics, s is empty, which reads the same both ways.
    assert Solution().isPalindrome(" ") is True


def test_single_char():
    assert Solution().isPalindrome("a") is True


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))  # expected True
    print(s.isPalindrome("race a car"))                      # expected False
