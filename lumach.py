"""
test_module.py
==============

This is a test module for Read the Docs documentation generation.
It contains simple functions and classes to demonstrate how Sphinx
generates documentation.

.. moduleauthor:: Your Name <your.email@example.com>
"""

def add(a, b):
    """
    Add two numbers.

    :param a: The first number to add.
    :param b: The second number to add.
    :return: The sum of the two numbers.
    :rtype: int

    **Example:**

    >>> add(2, 3)
    5
    """
    return a + b


class Calculator:
    """
    A simple calculator class.

    This class provides methods for basic arithmetic operations.

    **Example:**

    >>> calc = Calculator()
    >>> calc.multiply(2, 3)
    6
    """

    def multiply(self, a, b):
        """
        Multiply two numbers.

        :param a: The first number to multiply.
        :param b: The second number to multiply.
        :return: The product of the two numbers.
        :rtype: int

        **Example:**

        >>> calc = Calculator()
        >>> calc.multiply(3, 4)
        12
        """
        return a * b
