from euler.lib.prime import generate_primes


def solve() -> int:
    primes = set(generate_primes(1_000_000))

    max_primes = 0
    coefficients = (0, 0)

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            prime_count = 0
            while True:
                p = n ** 2 + a * n + b
                if p in primes:
                    prime_count += 1
                else:
                    if prime_count > max_primes:
                        max_primes = prime_count
                        coefficients = (a, b)
                    break
                n += 1

    return coefficients[0] * coefficients[1]


def test() -> str:
    return "No test case"


def run() -> str:
    return str(solve())
