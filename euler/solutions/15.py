import math

problem_input = 20
test_input = 2


def solve(x: int) -> int:
    return math.comb(x * 2, x)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
