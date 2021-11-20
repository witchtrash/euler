from typing import List

from euler.lib.prime import prime_factorize

problem_input = 600851475143
test_input = 13195


def solve(n: int) -> List[int]:
    return prime_factorize(n)


def test() -> None:
    print(solve(test_input))


def run() -> None:
    print(solve(problem_input))
