# enumerate()同时获取可迭代对象的索引和值,可指定起始索引
# 适用于字符串和列表
# 一般配合for循环使用
s = '651986151'
s = [7, 8, 2, 4, 5]
for index, value in enumerate(s,2):
    print(index,value)
'''
2 7
3 8
4 2
5 4
6 5
'''