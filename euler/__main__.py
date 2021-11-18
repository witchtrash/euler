import importlib
from typing import cast

import typer

from euler.solver import Solver


def main(problem: int, test: bool = False) -> None:
    try:
        solution = cast(Solver, importlib.import_module(f"euler.solutions.{problem}"))
        solution.test() if test else solution.solve()
    except ModuleNotFoundError:
        print(f"No solution for problem #{problem}!")


if __name__ == "__main__":
    typer.run(main)
