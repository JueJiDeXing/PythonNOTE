import re

re.findall(pattern='',string='')
# pattern表达式表明需要的字符,string用于匹配的字符
# 在string中查找pattern
s = '-8498.w-849'
res = max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)
print(res)