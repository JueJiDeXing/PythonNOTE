z = '10086'


# ---------------------------------------------------
def function1():
    z = '你好'
    print('Inside myFunction(): ', z)


function1()
print('Outside myFunction(): ', z)


# 函数内输出'你好',外输出'10086',z为局部变量，没有带到函数外部

# ---------------------------------------------------
def Function2():
    global z
    z = '你好'
    print('Inside myFunction(): ', z)


Function2()
print('Outside myFunction(): ', z)
# 均输出'你好',z为全局变量,在函数内部被赋值
# ----------------------------------------------------#
