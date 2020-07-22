"""
This file contains code for the application "PyCalculator".
Author: CreativeCloudAppDev2020
"""


# Importing necessary libraries


import sys
from decimal import Decimal
import math

sys.modules['_decimal'] = None
import decimal
from decimal import *
getcontext().Emin = -10 ** 17
getcontext().Emax = 10 ** 17
getcontext().traps[Overflow] = 0
getcontext().traps[Underflow] = 0
getcontext().traps[DivisionByZero] = 0
getcontext().traps[InvalidOperation] = 0
getcontext().prec = 100

# Static variables for pi and e


PI = Decimal(math.pi)
e = Decimal(math.exp(1))


# Trigonometric functions


def sin(x):
    return Decimal(math.sin(x))


def cosec(x):
    return Decimal(1) / sin(x)


def cos(x):
    return Decimal(math.cos(x))


def sec(x):
    return Decimal(1) / cos(x)


def tan(x):
    return Decimal(math.tan(x))


def cot(x):
    return Decimal(1) / tan(x)


# Hyperbolic functions


def sinh(x):
    return Decimal(math.sinh(x))


def cosech(x):
    return Decimal(1) / sinh(x)


def cosh(x):
    return Decimal(math.cosh(x))


def sech(x):
    return Decimal(1) / cosh(x)
    

def tanh(x):
    return Decimal(math.tanh(x))


def coth(x):
    return Decimal(1) / tanh(x)


# Exponential function


def exp(x):
    return Decimal(math.exp(x))


def main():
    """
    This main function is used to run the application.
    """

    print("Welcome to 'PyCalculator' by 'CreativeCloudAppDev2020'.")
    print("This application can be used to do various types of calculations.")
    print("To use the mathematical value pi, type in PI.")
    print("To use the mathematical value e, type in e.")

    # Asking the user whether he/she wants to continue using this application or not.
    print("Enter 'Y' for yes.")
    print("Enter anything else for no.")
    continue_ask: str = input("Do you want to continue using 'PyCalculator'? ")
    while continue_ask == "Y":
        # Asking the user to input an equation
        equation: str = input("Please enter an equation: ")
        result: Decimal

        # Evaluating the equation
        try:
            result = Decimal(eval(equation))
        except: 
            result = Decimal("nan")
        print(str(equation) + " = " + str(result))
        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_ask = input("Do you want to continue using 'PyCalculator'? ")

    sys.exit()


if __name__ == '__main__':
    main()