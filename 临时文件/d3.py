def display(func):
    def fun(x, y):
        funName = func.__str__().split(" ")[1]
        if funName == "add":
            return print(f"{x} + {y} = {x + y}")
        elif funName == "sub":
            return print(f"{x} - {y} = {x - y}")
        elif funName == "mul":
            return print(f"{x} * {y} = {x * y}")
        elif funName == "div":
            return print(f"{x} / {y} = {x / y}")

    return fun


@display
def add(x, y):
    return x + y


@display
def sub(x, y):
    return x - y


@display
def mul(x, y):
    return x * y


@display
def div(x, y):
    return x / y


add(2, 3)
sub(2, 3)
div(5, 2)
mul(4, 3)
