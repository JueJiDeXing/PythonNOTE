class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"I'm, {self.name}")


if __name__ == "__main__":
    # 传统获取属性
    d = Dog('Mark', 6)
    print(d.age)  # 6
    d.age = 4
    print(d.age)  # 4

    # 动态获取属性
    s = 'age'
    print(getattr(d, s))  # 4
    setattr(d, 'age', 2)
    print(d.age)  # 2
    # 动态增加属性
    d.__setattr__('color', 'red')
    print(getattr(d, 'color'))

    # 动态调用方法
    getattr(d, 'bark')()  # I'm, Mark
