import re
from typing import Generator, Callable


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Generates float numbers from the input text that are clearly surrounded by spaces.

    Args:
        text (str): The input string containing potential float numbers.

    Yields:
        float: Each float number found in the text.
    """
    # Regex pattern to match float numbers surrounded by spaces
    pattern = r'(?<=\s)\d+\.\d+(?=\s)'
    for match in re.finditer(pattern, text):
        # Yield the matched number as a float
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Calculates the total profit by summing all float numbers extracted from the text.

    Args:
        text (str): The input string containing the numbers.
        func (Callable): A function that returns a generator of float numbers from text.

    Returns:
        float: The total sum of all float numbers found in the text.
    """
    # Use the provided function to extract numbers and calculate their sum
    return sum(func(text))

# Example usage
text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими надходженнями "
    "27.45 і 324.00 доларів."
)

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

