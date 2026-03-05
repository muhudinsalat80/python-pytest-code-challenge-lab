import pytest
from lib.palindrome import longest_palindromic_substring


# ----------------------
# Basic Cases
# ----------------------

def test_basic_case_babad():
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]


def test_even_palindrome():
    assert longest_palindromic_substring("cbbd") == "bb"


# ----------------------
# Edge Cases
# ----------------------

def test_single_character():
    assert longest_palindromic_substring("a") == "a"


def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_no_long_palindrome():
    result = longest_palindromic_substring("abcde")
    assert len(result) == 1