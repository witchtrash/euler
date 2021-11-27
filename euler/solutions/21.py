from euler.lib.number import divisors

problem_input = 10_000
test_input = 0


def solve(x: int) -> int:
    amicable_sum = 0
    found: set[int] = set()

    for i in range(1, x):
        amicable_a = sum(divisors(i))
        amicable_b = sum(divisors(amicable_a))

        if amicable_b == i and amicable_a != amicable_b:
            if amicable_a in found or amicable_b in found:
                continue

            found.add(amicable_a)
            found.add(amicable_b)
            amicable_sum += amicable_a + amicable_b

    return amicable_sum


def test() -> str:
    return "No test case"


def run() -> str:
    return str(solve(problem_input))
