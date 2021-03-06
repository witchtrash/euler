problem_input = 999
test_input = 9


def div_sum(limit: int, n: int) -> int:
    p = limit // n
    return n * (p * (p + 1)) // 2


def solve(limit: int) -> int:
    return div_sum(limit, 3) + div_sum(limit, 5) - div_sum(limit, 15)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
