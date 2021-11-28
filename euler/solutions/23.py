from euler.lib.number import divisors


def solve() -> int:
    total = 0
    upper_limit = 28_123
    abundant_sums: set[int] = set()
    abundant_numbers: list[int] = []

    for i in range(1, upper_limit + 1):
        if sum(divisors(i)) > i:
            abundant_numbers.append(i)

    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sums.add(abundant_numbers[i] + abundant_numbers[j])

    for i in range(1, upper_limit + 1):
        if i not in abundant_sums:
            total += i

    return total


def test() -> str:
    return "No test case"


def run() -> str:
    return str(solve())
