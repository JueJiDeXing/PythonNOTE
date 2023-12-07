class Hello:

    def __init__(self, name):
        self.name = name

    def showInfo(self):
        print(self.name)


h = Hello(name='张三')  # Hello()是往__init__里传参数
h.showInfo()
