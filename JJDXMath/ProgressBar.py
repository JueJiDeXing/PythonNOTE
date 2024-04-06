import random


def printBar1(var: int, total: int, show: str = "█", unshow: str = " ", barLen: int = 20) -> None:
    if var % int(random.uniform(1, 10)) == 0:
        percent = var / total
        message = (show * int(percent * barLen)) + unshow * int((1 - percent) * barLen) + "|" + str(var) + "/" + str(
            total)
        print("\r" + message, end="")


def printBar2(percent: float, show: str = "█", unshow: str = " ", barLen: int = 20) -> None:
    message = (show * int(percent * barLen)) + unshow * int((1 - percent) * barLen) + "|" + str(percent * 100) + "%"
    print("\r" + message, end="")
