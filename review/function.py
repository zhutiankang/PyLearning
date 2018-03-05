def function(arg1, arg2):
    return "Something"


def fahrenheit_converter(C):
    fahrenheit = C * 9 / 5 + 32
    return str(fahrenheit) + 'F'

C2F = fahrenheit_converter(35)
print(C2F)

def weight_converter(G):
    weight = G / 1000
    return str(weight) + "kg"

weight = weight_converter(2000)
print(weight)

from math import sqrt
def hypotenuse_converter(cathetusOne,cathetusTwo):
    hypotenuse = sqrt(cathetusOne * cathetusOne + cathetusTwo * cathetusTwo)
    # 'The right triangle third side\'s length is ' + str(hypotenuse)
    # 两种方式
    return "The right triangle third side's length is"  + str(hypotenuse)

print(hypotenuse_converter(3,4))