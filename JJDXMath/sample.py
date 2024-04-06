from functools import cache
from math import sqrt


@cache
def E_X(args: list[float], n: int):
    """期望 E(X^n),n为正整数"""
    assert n > 0
    assert len(args) > 0
    e_x = 0
    for i in args:
        e_x += i ** n
    e_x /= len(args)
    return e_x


def S2(args):
    """样本方差 S^2=sum((xi-_x)^2) / (n-1)"""
    e_x = E_X(args, 1)
    s2 = 0
    for i in args:
        s2 += (i - e_x) ** 2
    s2 /= len(args) - 1
    return s2


def D_X(e_x, e_x2):
    """方差 D(X)=E(X^2)-E(X)^2"""
    return e_x2 - e_x ** 2


def D_X_byArgs(args):
    """方差 D(X)=E(X^2)-E(X)^2"""
    e_x1 = E_X(args, 1)
    e_x2 = E_X(args, 2)
    return e_x2 - e_x1 ** 2



