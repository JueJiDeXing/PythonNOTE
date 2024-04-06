def fun1(a, *args):
    print(args)  # fun1(1,2,3),输出(2,3)元组类型


fun1(1, 2, 3)  # a=1,args=(2,3)



def fun2(a, **kwargs):
    print(kwargs)  # fun2(1,z=2,k3='www'),输出{'z': 2, 'k3': 'www'}字典类型


fun2(1, z=2, k3='www')  # a=1,kwargs={'z': 2, 'k3': 'www'}

""" *args不定参 与 解包
*args无名的多个不定参数,可以不传,是元组类型(可迭代)
*号表示解包操作,解包示例:*[1,2,3] -> 1 2 3         *(1,2,3) -> 1 2 3
*args表示传递的参数是已被解包的

def test1(*args): # 函数调用test1(1,2,3), 则*args=1 2 3, 则args=(1,2,3)
    print(args)  # 输出(1,2,3)

def test2(a,b,c): # 函数调用test2(*[1,2,3]), 则a=1,b=2,c=3
    print(a,b,c)  # 输出1,2,3

# *kwargs为字典类型传参,key=value
def test3(*kwargs): # 函数调用test3(name="张三",age=18),则*kwargs=name="张三" age=18,kwargs={name="张三",age=18}
    print(kwargs["name"],kwargs["age"]) # 输出张三 18
"""
