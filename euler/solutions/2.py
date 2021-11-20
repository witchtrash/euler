problem_input = 4_000_000


def solve(limit: int) -> int:
    a = 1
    b = 2
    even_sum = 0

    while True:
        if b > limit:
            return even_sum
        if b % 2 == 0:
            even_sum += b
        a, b = b, a + b


def test() -> None:
    pass


def run() -> None:
    print(solve(problem_input))
