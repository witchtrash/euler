problem_input = 999
test_input = 99


def solve(n: int) -> int:
    mx = 0
    for a in range(n, n // 10 + 1, -1):
        for b in range(n, n // 10 + 1, -1):
            p = str(a * b)
            if p == p[::-1]:
                mx = max(mx, int(p))

    return mx


def test() -> None:
    print(solve(test_input))


def run() -> None:
    print(solve(problem_input))
