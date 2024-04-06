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
    value = None

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


print("--------------------------------")
c = AAA(1)
d = AAA(1)
print(c == d, c is d)  # True False

f = [1]
g = [1]
print(f == g, f is g)  # True False

h = {"a": 1}
i = {"a": 1}
print(h == i, h is i)  # True False
