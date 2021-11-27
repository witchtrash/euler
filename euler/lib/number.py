import math
from typing import List


def divisors(n: int) -> List[int]:
    """Get the proper divisors of a number n"""

    limit = int(math.sqrt(n)) + 1
    proper_divisors = {1}

    for i in range(2, limit):
        if n % i == 0:
            proper_divisors.add(n // i)
            proper_divisors.add(i)

    return list(proper_divisors)
