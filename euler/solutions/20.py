import math

problem_input = 100
test_input = 10


def solve(x: int) -> int:
    n = math.factorial(x)

    return sum([int(c) for c in str(n)])


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
