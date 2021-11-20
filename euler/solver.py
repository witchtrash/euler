from typing import Protocol


class Solver(Protocol):
    def test(self) -> str:
        pass

    def run(self) -> str:
        pass
