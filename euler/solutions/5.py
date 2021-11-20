import math
from functools import reduce

problem_input = range(2, 21)
test_input = range(2, 11)


def solve(nums: range) -> int:
    return reduce(math.lcm, nums, 1)


def test() -> None:
    print(solve(test_input))


def run() -> None:
    print(solve(problem_input))
