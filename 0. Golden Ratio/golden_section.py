from math import sqrt
from turtle import circle, done, lt, fd

PHI = 2 / (sqrt(5) - 1)


def square(size):
    for _ in range(4):
        fd(size)
        lt(90)


def golden_spiral(n):
    size = 4
    for _ in range(n):
        circle(size, 90)
        size *= PHI


def print_fibonacci(n):
    a = 1
    b = 1
    for _ in range(n):
        r = b / a
        print(f'{a:15d}{b:15d}{r:25.16f}')
        a, b = b, a + b


print_fibonacci(40)
print(f'PHI = {PHI}')

golden_spiral(9)
done()
