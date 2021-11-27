import datetime


def solve() -> int:
    month = 1
    year = 1901
    sundays = 0

    while year < 2001:
        date = datetime.date(year=year, month=month, day=1)
        if date.weekday() == 6:
            sundays += 1

        month += 1
        if month == 13:
            month = 1
            year += 1

    return sundays


def test() -> str:
    return "No test case"


def run() -> str:
    return str(solve())
