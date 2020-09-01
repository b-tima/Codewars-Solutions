from math import floor

def zero(operator=lambda x: x):
    return operator(0)
def one(operator=lambda x: x):
    return operator(1)
def two(operator=lambda x: x):
    return operator(2)
def three(operator=lambda x: x):
    return operator(3)
def four(operator=lambda x: x):
    return operator(4)
def five(operator=lambda x: x):
    return operator(5)
def six(operator=lambda x: x):
    return operator(6)
def seven(operator=lambda x: x):
    return operator(7)
def eight(operator=lambda x: x):
    return operator(8)
def nine(operator=lambda x: x):
    return operator(9)

def plus(value):
    return lambda x: floor(x + value)
def minus(value):
    return lambda x: floor(x - value)
def times(value):
    return lambda x: floor(x * value)
def divided_by(value):
    return lambda x: floor(x / value)