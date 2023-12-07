import os
import signal

path = "/test1/test2/test3.txt"

# os---------------------------------------------------------
os.getcwd()  # 返回当前工作目录current-work-dir
os.chdir("dir")  # 改变当前目录change-dir

os.listdir("/test1/test2")  # 返回指定目录下的所有文件和目录名test3.txt
os.mkdir("test")  # 创建单个目录
os.makedirs("")  # 创建多级目录

os.remove("file")  # 移除文件
os.removedirs(r"C:\test")  # 移除目录
# 重命名
os.replace("file1", "file2")  # 若file2已存在,则先删除file2,再将file1重命名为file2
os.rename("file1", "file2")  # Window下,若file2已存在,会报错

seq = os.linesep  # 给出当前平台使用的行终止符,Windows使用’\r\n’，Linux使用’\n’而Mac使用’\r’。
name = os.name  # 指示当前使用平台,Window为'nt',Linux为'posix'
os.get_terminal_size()  # 获取当前终端的大小
os.kill(__pid=10884, __signal=signal.SIGINT)  # 杀死进程
