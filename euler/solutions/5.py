import math
from functools import reduce

problem_input = range(2, 21)
test_input = range(2, 11)


def solve(nums: range) -> int:
    return reduce(math.lcm, nums, 1)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
