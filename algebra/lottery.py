from random import randint
from math import log10

CLASS_SIZE = 24

# Distribute `lottery tickets` to students.
# Students discuss their `winnings`.
# Students estimate the distribution heuristically.
# Classroom graphs the distribution exactly.


def lottery(func):
    data = [randint(0, 256) for _ in range(CLASS_SIZE)]
    data = map(func, data)
    for n in data:
        output(n)


def exponential(n):
    BASE = 1.1
    value = pow(BASE, n)
    return significant_figures(value)


def significant_figures(x):
    x = round(x, 1 - int(log10(x)))
    return int(x)


def output(n):
    print("$ " + format(n, ",d"))


if __name__ == "__main__":
    lottery(exponential)
