# Example of indentation (4 spaces)
def example_function():
    if True:
        print("PEP 8 is great!")


# Example of line length (maximum 79 characters)
def function_with_long_name(
        long_argument1, long_argument2, long_argument3):
    """Function with a long name and multiple arguments."""
    pass


# Example of blank lines
class MyClass:
    def method_one(self):
        """First method in class."""
        pass

    def method_two(self):
        """Second method in class."""
        pass


# Example of imports (in the correct order)
import os
import sys

import requests

# Example of whitespace usage
# Correct usage of whitespace in expressions and statements
x = 1
y = x**2 + 5  # No extraneous whitespace

# Correct usage of whitespace around operators and in expressions
x = (1 + 2) * (3 - 4)


# Example of naming conventions
def calculate_total():
    """Calculate and return the total."""
    pass


class MyClassExample:
    """Example class using CamelCase convention."""
    pass


MAX_SIZE = 100


# Example of docstrings and comments
def add(x, y):
    """Add two numbers and return the result."""
    return x + y


# Example of an inline comment
x = 5  # Inline comment explaining the variable

# Main executable code example using __main__
def main():
    """Main function that executes script functionality."""
    print("Hello, PEP 8!")


if __name__ == "__main__":
    main()
