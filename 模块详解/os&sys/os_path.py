import os
path = "/test1/test2/test3.txt"
print(__file__)  # 打印当前脚本所在的路径,包含文件名
# os.path-------------------------------------------------------
# 判断语句
os.path.isfile("path")  # 检验是否为一个文件
os.path.isdir("path")  # 检验是否为一个目录
os.path.isabs("path")  # 检验是否为绝对路径
os.path.exists("path")  # 检验路径是否存在
#
os.path.split("/test1/test2/test3.txt")  # 返回目录名和文件名("/test1/test2/","test3.txt")
os.path.splitext("/test1/test2/test3.txt")  # 分离拓展名("/test1/test2/test3",".txt")
os.path.dirname("/test1/test2/test3.txt")  # 返回所有上级目录"/test1/test2"
os.path.abspath("path")  # 返回相对路径的绝对路径
os.path.basename("/test1/test2/test3.txt")  # 获取最后一级目录或文件名"test3.txt"
os.path.getsize("file")#获取文件大小
os.path.join("dir","file")#拼接目录和文件名
