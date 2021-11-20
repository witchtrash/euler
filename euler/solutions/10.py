from euler.lib.prime import generate_primes

problem_input = 2_000_000
test_input = 10


def solve(x: int) -> int:
    return sum(generate_primes(x))


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
