problem_input = 1_000_000
test_input = 13


def solve(x: int) -> int:
    mx = 0
    start = 1
    memo: dict[int, int] = {}

    for i in range(x):
        n = i
        terms = 0
        while n > 1:
            if memo.get(n):
                terms += memo[n]
                break

            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1

            terms += 1

        memo[i] = terms

        if terms > mx:
            mx = terms + 1
            start = i

    return start


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
