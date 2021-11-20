import math

problem_input = 0
test_input = 0


def solve(x: int) -> int:
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = a ** 2 + b ** 2
            cs = math.isqrt(c)
            if c == cs ** 2:
                if a + b + cs == 1000:
                    return a * b * cs

    return 0


def test() -> str:
    return str("No test case")


def run() -> str:
    return str(solve(problem_input))
