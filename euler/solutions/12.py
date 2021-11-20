# https://primes.utm.edu/glossary/page.php?sort=tau
from itertools import groupby

from euler.lib.prime import prime_factorize

problem_input = 500
test_input = 5


def solve(x: int) -> int:
    triangle = 3
    n = 3

    while True:
        divisors = 1
        prime_factors = [list(j) for _, j in groupby(prime_factorize(triangle))]

        for p in prime_factors:
            divisors *= len(p) + 1

        if divisors > x:
            return triangle

        triangle += n
        n += 1


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
