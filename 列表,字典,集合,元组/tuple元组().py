# 创建元组
t = ('a', 'b', 'c')  # 括号可省略，如果只有一个元素，则不能省略，写成t=（a,)或t=tuple((a,b,c))
# -----------------------------------------------------------------------
# 空元组
t1 = ()
t2 = tuple()
# -----------------------------------------------------------------------
# 元组为不可变序列，列表和字典为可变
# 元组的遍历
for item in t :
    print(item, end='')  # abc
