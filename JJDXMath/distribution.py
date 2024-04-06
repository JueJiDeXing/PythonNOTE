from math import sqrt
import sympy


def E_X(T, var, fun, range_down, range_up):
    """
    E(T),T为关于var的表达式
    E(T)=∫ {a} {b} {T*fun} d{var}
    """
    return sympy.integrate(T * fun, (var, range_down, range_up))


def D_X(E_T2, E_T1):
    """
    D(T)=E(T^2)-(E(T))^2
    """
    return E_T2 - E_T1 ** 2


def D_X_(T, var, fun, range_down, range_up):
    """
    D(T)=E(T^2)-(E(T))^2
    """
    return E_X(T ** 2, var, fun, range_down, range_up) - E_X(T, var, fun, range_down, range_up) ** 2


def Cov_xy_byE(E_xy, E_x, E_y):
    """协方差"""
    return E_xy - E_x * E_y


def p_xy(Cov_xy, D_x, D_y):
    """相关系数"""
    return Cov_xy / (sqrt(D_x * D_y))


def __dis__():
    x = sympy.Symbol("x")
    y = x ** 2
    f = 1
    a = 0
    b = 1
    print(E_X(y, x, f, a, b))
