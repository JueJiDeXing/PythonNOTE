from functools import cache

import random
import ProgressBar

Number = float | int


def estimate_pi(points_total):
    points_in_circle = 0
    print("开始计算pi")
    print(" " * 10 + "|", end="")
    for i in range(points_total):
        ProgressBar.printBar1(i, points_total)
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        if x ** 2 + y ** 2 <= 1:
            points_in_circle += 1

    return 4 * points_in_circle / points_total


pi = estimate_pi(50000000)
print("pi=", pi)


def abs(n: Number) -> Number:
    """绝对值"""
    return n if n > 0 else -n


def sqrt(n: Number, degree=1e-6) -> Number:
    """开平方根"""
    if n < 0:
        raise Exception("负数不能开平方根")
    if n == 0:
        return 0
    t = n / 2
    while abs(t * t - n) > degree:
        print(t)
        t = (t + n / t) / 2
    return t


@cache
def factorial(n: int) -> int:
    """阶乘"""
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def radians(n: Number) -> Number:
    """将角度转换为弧度"""
    return n / 180 * pi


def sin(x, terms=50):
    """sin(x)"""
    x = radians(x)
    res = 0
    for n in range(terms):
        # 泰勒公式 sinx通项为 (-1)^n * x^(2n+1) / (2n+1)!
        sign = 1 if n % 2 == 0 else -1
        num = x ** (2 * n + 1)
        den = factorial(2 * n + 1)
        res += sign * (num / den)
    return res


print(sin(90))
