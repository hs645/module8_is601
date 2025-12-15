# app/operations.py

"""
Module: operations.py

This module contains basic arithmetic functions that perform addition, subtraction,
multiplication, and division of two numbers. These functions are foundational for
building more complex applications, such as calculators or financial tools.

Functions:
- add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]: Returns the sum of a and b.
- subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]: Returns the difference when b is subtracted from a.
- multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]: Returns the product of a and b.
- divide(a: Union[int, float], b: Union[int, float]) -> float: Returns the quotient when a is divided by b. Raises ValueError if b is zero.

Usage:
These functions can be imported and used in other modules or integrated into APIs
to perform arithmetic operations based on user input.
"""

from typing import Union  # Import Union for type hinting multiple possible types

# Define a type alias for numbers that can be either int or float
Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """
    Add two numbers and return the result.

    Parameters:
    from typing import Union  # Import Union for type hinting multiple possible types

    # Define a type alias for numbers that can be either int or float
    Number = Union[int, float]

    def add(a: Number, b: Number) -> Number:
        result = a + b
        return result

    def subtract(a: Number, b: Number) -> Number:
        result = a - b
        return result

    def multiply(a: Number, b: Number) -> Number:
        result = a * b
        return result

    def divide(a: Number, b: Number) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        return result
    - b (int or float): The number to subtract.
