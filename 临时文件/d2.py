import random


def create(total, sp="■", barLen=50):
    ans = []
    for i in range(1, 1 + total):
        ans.append(random.random())
        percent = i * 100 / total
        # print(f"\r{int(percent / 100 * barLen) * sp} 已完成{percent:.2f}%任务|生成{i}个随机数", end="")
        print(f"\r{int(percent / 100 * barLen) * sp} 已完成{percent:.4f}%任务|生成{i}个随机数", end="\n")


create(500000)
