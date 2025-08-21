from datetime import date
import sys
import inflect  # pip install inflect


def main():
    dob_str = input("Date of Birth (YYYY-MM-DD): ")
    dob = parse_date(dob_str)
    today = date.today()
    minutes = calculate_minutes(dob, today)
    print(number_to_words(minutes), "minutes")


def parse_date(dob_str):
    """Parse user input into a date object. Exit if invalid format."""
    try:
        year, month, day = map(int, dob_str.split("-"))
        return date(year, month, day)
    except Exception:
        sys.exit("Invalid date format, must be YYYY-MM-DD")


def calculate_minutes(dob: date, today):
    """Calculate total minutes lived since dob until today."""
    delta = today - dob
    return round(delta.days * 24 * 60)


def number_to_words(n):
    """Convert a number into words (without 'and')."""
    p = inflect.engine()
    words = p.number_to_words(n, andword="")
    return words.capitalize()


if __name__ == "__main__":
    main()
