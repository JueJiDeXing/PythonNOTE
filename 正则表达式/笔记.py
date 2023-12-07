import re

r'''
# 一、支持普通字符匹配

# 二、元字符匹配

\d 匹配数字0~9  大写表示除...以外,如\D匹配除0-9以外的字符
\w 数字、字母、下划线（0-9，a-z，A-Z）

[] 匹配[]中列举的所有字符  [abc]匹配a,b,c
^  除...外      [^abc]除了a,b,c
.  匹配到除换行符之外的任意字符

# 三、量词

我今天赚了500块，花了2块
+ 表示匹配一次或多次  \d+匹配所有连续数字           (匹配到2处)500 2
* 表示0次或多次      \d*没有数字时匹配到了没有返回值 (匹配到12处)        500     2
? 表示0次或一次      \d?                        (匹配到14处)        5 0 0    2    

# 四、惰性匹配

玩儿吃鸡游戏,晚上一起上游戏,打游戏
玩儿.*游戏      匹配到   玩儿 吃鸡游戏,晚上一起上游戏,打 游戏
玩儿.*?游戏     匹配到   玩儿 吃鸡 游戏
.*?为惰性匹配,匹配到距离...最近的内容
'''
# 五、内置函数

text = "今天我有100块,花了2块"
# findall查找所有
result1 = re.findall(r"\d+", text)
print(result1)  # ['100','2']

# search搜索
result2 = re.search(r"\d+", text)  # <re.Match object; span=(4,7), match='100'>
print(result2.group())  # 100   search拿到第一个结果就返回

# finditer迭代
result3 = re.finditer(r"\d+", text)  # <callable_iterator object at 0x0000012ECF7DA240>
for i in result3:
    print(i)  # <_sre.SRE_Match object; span=(4, 7), match='100'><_sre.SRE_Match object; span=(11, 12), match='2'>
    print(i.group())  # 100 2

# 预加载
obj = re.compile(r"\d+")  # 提取写好正则,这样在循环里就不用每次创造新的正则了
obj.findall(text)

# 六、分组
result4 = re.finditer(r"(?P<shu>\d+)", text)  # 加括号(),?P<>,里面填组名
for i in result4:
    print(i)  # <_sre.SRE_Match object; span=(4, 7), match='100'><_sre.SRE_Match object; span=(11, 12), match='2'>
    print(i.group('shu'))  # 100 2

# ---------------------------------------------------------------
# *号
info = "1234560000"
rett = re.match("[1-9*]", info)
# print(rett)  # 123456
'''
*表示多个
1-9*表示把1到9的数字都取出来进行匹配
'''
# .*
line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
print("", matchObj.group())
'''
.点表示可以匹配到除换行符之外的任意字符
()括号就表示这两个正则符号需要连接起来使用
.*表示的意思就是可以匹配除换行符之外的任意多个字符,也就是基本上匹配所有字符串
'''
