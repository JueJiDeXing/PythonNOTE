a = 4
match a:
    case 1:
        print(1)  # 不需要break语句,没有case穿透
    case 2:
        print(2)
    case 3 | 4 | 5:  # 同时匹配多个情况
        print("3或4或5")
    case 6, 7:
        print("元组(6,7)")
    case _:  # default
        print("ERROR")
