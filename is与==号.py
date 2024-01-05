"""
基本数据类型:==与is都比较值
非基本数据类型:==号调用eq方法进行比较,is比较地址值
"""

a = 1000029
b = 1000029
hash_a = a.__hash__()
hash_b = b.__hash__()
print(hash_a, hash_b)
print(a == b, a is b)  # True True
print(id(a), id(b))  # 2730751343472 2730751343472
a = a + 1
print(a, b, id(a), id(b))  # 1000030 1000029 2730753710832 2730751343472


class AAA:
    name = None
    value = None

    def __init__(self):
        pass

    def __eq__(self, other):
        return True

    def __hash__(self):
        return 10


print("-----------1--------------------")
c = AAA()
d = AAA()
print(hash(c), hash(d))
print(c == d, c is d)  # True False

f = [1]
g = [1]
print(f == g, f is g)  # True False

h = {"a": 1}
i = {"a": 1}
print(h == i, h is i)  # True False
