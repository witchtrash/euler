from typing import List

from euler.lib.util import get_problem_input

problem_input = get_problem_input()
test_input = """3
7 4
2 4 6
8 5 9 3"""


def solve(s: str) -> int:
    tree: List[List[int]] = []
    for row in s.split("\n"):
        tree.append([int(x) for x in row.split()])

    tree = tree[::-1]

    for i in range(1, len(tree)):
        current_row = tree[i]
        next_row = tree[i - 1]
        max_row = []

        for j in range(len(current_row)):
            max_row.append(
                max(current_row[j] + next_row[j], current_row[j] + next_row[j + 1])
            )
        tree[i] = max_row

    return tree[len(tree) - 1][0]


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
