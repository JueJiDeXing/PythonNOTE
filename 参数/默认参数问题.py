from _datetime import datetime


def fun(a=(), b=[]):
    a += (1,)
    b.append(1)
    return a, b


fun()
a, b = fun()
print(a, b)  # (1,) [1,1]


# 执行一次fun之后,默认参数b为列表(可变类型)默认值变为[1]
# 而a因为是元组(不可变类型),开辟了新的内存存储数据(1,),其默认值不变仍为()
# 在定义函数时会存储默认参数！


def time(a=datetime.now()):  # datetime.now()返回现在的时间
    return a


print(time())
print(time())  # 输出结果一样,因为在定义函数时已经存储a,第二次执行时没有改变默认值
