n = 0
file_path = ' '
open(file_path, mode=' ')
# --------------------------------------------------------------
# file_path:文件路径，可使用绝对路径也可使用相对路径

# --------------------------------------------------------------
# mode:指定对文件进行的操作:

# ######r:read----------------######
file = open(file_path, mode="r")
file.read(n)  # 读取n个字节    第二次读取会从上一次读取到的地方开始读取
file.readline()  # 读取一行内容      数据末尾带\n,可以使用strip()来清除\n
file.readlines()  # 以每行数据为一个元素,放入列表中
# 循环读取:
for line in file:
    print(line)

# ######w:write---------------#######
file = open(file_path, mode="w")  # 没有文件创造文件,有文件会删掉原内容写入
file.write('写入内容')
file = open(file_path, mode="wb")  # wb不指定编码格式
file.write('写入内容'.encode('utf-8'))  # 写入内容时要将内容转换为指定的编码格式

# ######a:append---------------######
file = open(file_path, mode="a")  # 追加内容到文件末尾
file.write('追加内容')

# ######r+---------------######
file = open(file_path, mode="r+")  # 读写,没有文件则报错
content = file.read()
file.write('写入内容')
"""要先读，如果先写后读，写的内容会覆盖原有的部分内容，读会从写到的地方开始读取"""

# ######w+、w+b、a+、a+b---------------######
