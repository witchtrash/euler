import inspect
from pathlib import Path


def get_problem_input(strip: bool = True) -> str:
    """
    Get problem input automagically, solution file is inferred from the call stack

    Input files are located in the `solutions/inputs` folder

    Note that input files have to be named {problem_number}.txt
    """

    caller_file = inspect.stack()[1].filename

    problem_number = Path(caller_file).stem.split(".")[0]
    input_path = Path(caller_file).parent / "inputs" / f"{problem_number}.txt"

    with open(input_path) as f:
        content = f.read()

    if strip:
        content = content.strip()

    return content
