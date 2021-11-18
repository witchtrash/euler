from typing import Protocol


class Solver(Protocol):
    def test(self) -> None:
        pass

    def solve(self) -> None:
        pass
