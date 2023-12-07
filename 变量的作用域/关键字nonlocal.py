count1 = 1


def test1():
    print(count1)  # 全局变量可读不可写(字典可写)


def test2():
    count = count + 1  # 当在赋值操作时,默认为局部变量
    print(count)


def test3():
    global count1
    count1 = count1 + 1
    print(count1)


# --------------------------------
def test4():
    count2 = 2

    def test41():
        global count2  # 未定义
        count2 = count2 + 1
        print(count2)


def test5():
    count3 = 2

    def test51():
        nonlocal count3
        # count2不是定义在函数闭包外的全局变量,所以使用nonlocal
        count3 = count3 + 1
        print(count3)
