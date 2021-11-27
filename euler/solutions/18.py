from typing import List

problem_input = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
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
