problem_input = range(1, 101)
test_input = range(1, 11)


def solve(nums: range) -> int:
    sum_of_squares = sum([x ** 2 for x in nums])
    square_of_sum = sum(nums) ** 2

    return square_of_sum - sum_of_squares


def test() -> None:
    print(solve(test_input))


def run() -> None:
    print(solve(problem_input))
