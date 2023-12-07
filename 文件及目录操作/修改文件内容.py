# 修改文件:只能将⽂件中的内容先读取出来,将信息修改完毕,然后将源⽂件删除,将新⽂件的名字改成老⽂件的名字
# 文件修改
import os

# 读取原文件,写入新文件，再把文件名替换
with open("file/dog", mode="r", encoding="utf-8") as f1, open("file/dog_new", mode="w", encoding="utf-8") as f2:
    for line in f1:
        line_new = line.replace("哈", "嘻")
        f2.write(line_new)

os.remove("file/dog")
os.rename("file/dog_new", "file/dog")

# 关闭文件---------------------------------------------------------------
file.close()  # 释放文件句柄
# 使用with语句可以不写关闭
with open(file_path, mode="r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 其他操作---------------------------------------------------------------
file.seek(n, type)  # 光标移动到第n个字节位置,向type处读取(不写type则不读取),因为我们大部分是采用utf-8的编码格式,所以一般n取得都是3的倍数.
# t y p e: 取 0,1,2
# 0:指相对开头偏移1:指相对本身位置进行偏移2:指相对结尾偏移
file.tell()  # 帮助我们获取当前光标位置，返回的值也是以字节为单位进行度量的。
f.truncate(n)  # 有n则从开头删除n个字节内容,不写n删掉光标后⾯的所有内容
