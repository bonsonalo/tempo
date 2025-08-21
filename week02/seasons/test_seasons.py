import pytest
from datetime import date
import sys
from seasons import parse_date, calculate_minutes, number_to_words


# parse_date tests
def test_parse_date_valid():
    assert parse_date("2000-01-01") == date(2000, 1, 1)


def test_parse_date_invalid_format():
    with pytest.raises(SystemExit):
        parse_date("01-2000-01")  # wrong format


def test_parse_date_non_numeric():
    with pytest.raises(SystemExit):
        parse_date("abcd-ef-gh")  # letters, not numbers


# calculate_minutes tests
def test_calculate_minutes():
    dob = date(2000, 1, 1)
    today = date(2000, 1, 2)
    assert calculate_minutes(dob, today) == 1440  # 1 day = 1440 minutes


def test_calculate_minutes_multiple_days():
    dob = date(2000, 1, 1)
    today = date(2000, 1, 11)  # 10 days later
    assert calculate_minutes(dob, today) == 14400


# number_to_words tests 
def test_number_to_words_simple():
    assert number_to_words(1440) == "One thousand four hundred forty"


def test_number_to_words_large_number():
    result = number_to_words(1000000)
    assert "million" in result.lower()
