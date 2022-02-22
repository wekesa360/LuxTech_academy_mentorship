"""
confirm if a number belongs to the fibonacci sequence.
"""
# import of a math module
import math

def is_perfect_square(n):
    """ a function that returns true if n
    is a perfect square"""

    value = int(math.sqrt(n))
    return (value * value == n)

def is_fibonacci(n):
    """ checks if n is a fibonacci number"""

    # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perfect square.
    return (is_perfect_square(5*n*n + 4) or
                is_perfect_square(5*n*n - 4))

number_input = int(input("Enter a number: "))
if (is_fibonacci(number_input)== True):
    print("The number {} is fibonacci".format(number_input))
else:
    print("The number {} is not fibonacci".format(number_input))
