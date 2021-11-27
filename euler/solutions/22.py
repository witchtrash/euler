from euler.lib.util import get_problem_input


def solve() -> int:
    names = sorted(get_problem_input().replace('"', "").split(","))
    total = 0

    for i in range(len(names)):
        name = names[i]
        alphabetical_value = 0

        for c in name:
            alphabetical_value += ord(c) - 64
        total += alphabetical_value * (i + 1)

    return total


def test() -> str:
    return "No test case"


def run() -> str:
    return str(solve())
