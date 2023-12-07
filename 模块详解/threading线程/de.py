import threading

a = 1


def text1(a):
    for _ in range(5):
        a += 1
        print("text1" + str(a))


def text2():
    for _ in range(5):
        print("text2")


t1 = threading.Thread(target=text1, args=(a,))  # 函数名,传参
t2 = threading.Thread(target=text2)
t2.start()  # 线程开始运行
t1.start()
t1.join()  # 等待线执行完再执行主线程
print("主线程")
