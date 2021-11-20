from typing import List

from euler.lib.prime import prime_factorize

problem_input = 600851475143
test_input = 13195


def solve(n: int) -> List[int]:
    return prime_factorize(n)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
