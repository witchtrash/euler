import math

from euler.lib.prime import generate_primes

problem_input = 10_001
test_input = 6


def solve(n: int) -> int:
    # Estimate the upper bound using the prime number theorem
    guess_prime = 2 * math.ceil(n * math.log(n))

    # Generate primes up to the upper bound
    primes = generate_primes(guess_prime)

    return primes[n - 1]


def test() -> None:
    print(solve(test_input))


def run() -> None:
    print(solve(problem_input))
