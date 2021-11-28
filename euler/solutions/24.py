import itertools


def solve() -> str:
    permutations = sorted(list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))

    return "".join(map(str, permutations[999_999]))


def test() -> str:
    return "No test case"


def run() -> str:
    return solve()
