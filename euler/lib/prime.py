import math
from itertools import cycle
from typing import List, Optional


def generate_primes(n: int) -> List[int]:
    """
    Generate a list of primes smaller than n
    """

    if n < 3:
        return [] if n < 2 else [False, False, True]

    integers = [True] * n
    integers[0] = False
    integers[1] = False

    for i in range(2, int(math.sqrt(n) + 1)):
        if integers[i]:
            for j in range(i ** 2, n, i):
                integers[j] = False

    primes = []
    for i, p in enumerate(integers):
        if p:
            primes.append(i)

    return primes


def is_prime(n: int) -> bool:
    """
    Determine if a number is prime using wheel factorization
    with a 2, 3, 5 wheel
    """

    # Special cases, 2, 3 and 5 are prime
    if n in [2, 3, 5]:
        return True
    # 2 is the smallest prime
    if n < 2:
        return False
    # Check divisibility with 2, 3 and 5
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False

    # Start checking at 7
    k = 7
    wheel = cycle([4, 2, 4, 2, 4, 6, 2, 6])
    limit = math.ceil(math.sqrt(n))

    for x in wheel:
        if k > limit:
            break

        if n % k == 0:
            return False

        k += x

    return True


def prime_factorize(n: int, primes: Optional[list[int]]) -> List[int]:
    """
    Prime factorize a positive number greater than 1, returning a list of prime factors.
    """

    if n < 2:
        raise ValueError("Only numbers greater than 1 have a prime factorization.")

    if is_prime(n):
        return [n]

    if primes is None:
        primes = generate_primes(n // 2 + 1)
    factors: List[int] = []

    for p in primes:
        if p > n:
            break

        while n % p == 0:
            factors.append(p)
            n //= p

    return factors
