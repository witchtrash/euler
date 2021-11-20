problem_input = 1000
test_input = 15


def solve(x: int) -> int:
    return sum([int(n) for n in str(2 ** x)])


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
