problem_input = 1000
test_input = 5


def solve(x: int) -> int:
    numerals = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand",
    }

    numeral_keys = list(numerals.keys())[::-1]
    letters = 0

    for i in range(1, x + 1):
        number = i
        numeral: list[str] = []

        for n in numeral_keys:
            if number >= n:
                if number >= 100:
                    numeral.append(numerals[number // n])
                    numeral.append(numerals[n])

                    if number % 100 != 0:
                        numeral.append("and")

                    number -= (number // n) * n
                else:
                    numeral.append(numerals[n])
                    number -= n

        letters += sum([len(x) for x in numeral])

    return letters


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
