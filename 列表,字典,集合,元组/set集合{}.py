"""
+:add添加、update更新
-:remove去除、discard丢弃、pop随机删除一个
集合运算:intersection交集&、union并集|、different差集-、symmetric_difference对称差集^
"""
# 创建集合
s1 = {1, 1, 0}
s2 = set(range(6))
s3 = set([3, 3, 3])
s4 = set((4, 8, 4, 8))
s5 = set('abcde')
s6 = set({6, 6, "d", "s"})
print(s1, s2, s3, s4, s5, s6)
s1 = {0, 1}  # 互异性，相同的数只输出一个
s2 = {0, 1, 2, 3, 4, 5}
s3 = {3}
s4 = {8, 4}
s5 = {'b', 'c', 'a', 'd', 'e'}  # 无序性，输出排序会变
s6 = {'s', 'd', 6}
# -----------------------------------------------------------------------
# 空集合
s = set()
print(type(s))  # <class 'set'>
# -----------------------------------------------------------------------
# 添加元素
s.add('绝')  # 一个
print(s)
s = {'绝'}
# ---------------------------------------------
s.update('绝迹的星')  # 至少一个
print(s)
s = {'星', '的', '绝', '迹'}
# -----------------------------------------------------------------------
# 删除元素
s.remove('的')  # 一个，元素不存在KeyError
print(s)
s = {'星', '绝', '迹'}
# ---------------------------------------------
s.discard('星')  # 一个，元素不存在不报错
print(s)
s = {'绝', '迹'}
# ---------------------------------------------
s.pop()  # 随机删除一个元素，不能添加参数
print(s)
s = {'迹'}
# ---------------------------------------------
s.clear()  # 清除元素
print(s)
s = set()
# -----------------------------------------------------------------------
# 集合的运算
s1 = {1, 2, 3, 4, 5, 6}
s2 = {0, 1, 2, 3}
s3 = {7, 8, 9}

s4 = s1 & s2  # 交集
print(s4)
s4 = {1, 2, 3}
# --------------------------------------------
s5 = s1 | s3  # 并集
print(s5)
s5 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# --------------------------------------------
s6 = s1 - s2  # 差集
s7 = s2 - s1  # 不同的减法结果不一样
print(s6, s7)
s6 = {4, 5, 6}
s7 = {0}
# ---------------------------------------------
s8 = s1 ^ s2  # 对称差集，减去共有部分
print(s8)
s8 = {0, 4, 5, 6}

# 集合是没有value的字典
