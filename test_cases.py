"""Unit tests for CFG/PDA case studies."""

import unittest

from balanced_parentheses import is_balanced
from arithmetic_expression import is_valid_expression
from palindrome_checker import is_palindrome_npda


class TestBalancedBracketsPDA(unittest.TestCase):
    def test_accepted(self):
        for value in ["", "()", "([]{})", "((x+y)*z)", "{[()]}"]:
            with self.subTest(value=value):
                self.assertTrue(is_balanced(value))

    def test_rejected(self):
        for value in ["(", ")", "([)]", "(()", "{]", "([{}))"]:
            with self.subTest(value=value):
                self.assertFalse(is_balanced(value))


class TestArithmeticCFG(unittest.TestCase):
    def test_accepted(self):
        for value in ["1", "a+b", "a+b*c", "(a+b)*12", "-x/3", "foo_2 + 17"]:
            with self.subTest(value=value):
                self.assertTrue(is_valid_expression(value))

    def test_rejected(self):
        for value in ["", "a+", "*a", "(a+b", "a b", "2**3", "a//b", "()"]:
            with self.subTest(value=value):
                self.assertFalse(is_valid_expression(value))


class TestPalindromeNPDA(unittest.TestCase):
    def test_accepted(self):
        for value in ["", "a", "b", "aa", "aba", "abba", "aabbaa", "baab"]:
            with self.subTest(value=value):
                self.assertTrue(is_palindrome_npda(value))

    def test_rejected(self):
        for value in ["ab", "aab", "abab", "abb", "abc", "aabbab"]:
            with self.subTest(value=value):
                self.assertFalse(is_palindrome_npda(value))


if __name__ == "__main__":
    unittest.main(verbosity=2)
