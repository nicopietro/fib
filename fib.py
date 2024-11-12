import argparse
from functools import cache

def fibonacci(n: int):
    if n < 0:
        raise ValueError("n must be greater or equal to zero.")
    if n < 2:
        return n
    n0 = 0
    n1 = 1
    for _ in range(n - 1):
        nth = n0 + n1
        n0 = n1
        n1 = nth
    return nth

@cache
def fibonacci_recursive(n: int):
    if n < 0:
        raise ValueError("n must be greater or equal to zero.")
    if n < 2:
        return n
    nth = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return nth


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('nth', type=int, help='Numero de repeticiones')

    args = parser.parse_args()

    r = fibonacci(args.nth)
    print(r)
