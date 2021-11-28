from euler.lib.number import number_of_digits
from euler.lib.sequence import fibonacci

problem_input = 1000
test_input = 3


def solve(x: int) -> int:
    fibonacci_generator = fibonacci()
    index = 1

    while True:
        n = next(fibonacci_generator)
        if number_of_digits(n) >= x:
            return index
        index += 1


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
