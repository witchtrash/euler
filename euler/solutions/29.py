problem_input = 100
test_input = 5


def solve(x: int) -> int:
    terms: set[int] = set()

    for a in range(2, x + 1):
        for b in range(2, x + 1):
            terms.add(a ** b)

    return len(terms)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
