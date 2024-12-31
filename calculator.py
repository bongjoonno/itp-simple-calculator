import math
from math import *
def add(x, y):
    return x + y

def subtract(x, y):
    return x-y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'You cannot divide by zero'

def multiply(x, y):
    return x*y
    
def square(x):
    x**2

def power(x, y):
    x**y

def sqrt(x):
    return sqrt(x)
