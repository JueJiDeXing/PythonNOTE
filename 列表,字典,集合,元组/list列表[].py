"""
range范围
index索引
+:append追加、extend延伸、insert插入
-:remove去除、pop指定位置去除、clear清除、del删除
排序:sort排序、sorted重排、reverse=True/False颠倒
"""
# 创建列表：###############################################################
lst = []
lst = [1, 8, 3, 9, 7, 8, 8, 7, 5, 0, 6]
# -----------------------------------------------------------------------
# 获取索引
a = lst.index(8, 4)  # (元素，star，stop),star默认为1，stop默认到最后，存在n个相同元素，只返回第一个
print(a)  # 从第4+1位开始，第一个元素8的索引为5
a = 5
# -----------------------------------------------------------------------
# 获取元素
b = lst[4]  # [索引],可为负数
print(b)  # lst中索引为4的元素是7
b = 7
# -----------------------------------------------------------------------
# 切片
lst2 = lst[2::2]  # [star：stop：step],不写默认为(开始,最后,1),step为负数会倒着切,左闭右开,不会切到stop
print(lst2)  # 从第2+1位开始，步长为2切取列表
lst2 = [3, 7, 8, 5, 6]
# -----------------------------------------------------------------------
# 列表元素增加操作：
lst2.append(2)  # 在列表末尾添加一个元素,还是原列表,没有创建新列表
print(lst2)
lst2 = [3, 7, 8, 5, 6, 2]
# ---------------------------------------------------
lst3 = [1, 1, 0]
lst2.append(lst3)  # 把列表当做一个元素添加到末尾
print(lst2)
lst2 = [3, 7, 8, 5, 6, 2, [1, 1, 0]]
# ---------------------------------------------------
lst2.extend(lst3)  # 在一个列表末尾添加另一个列表的所有元素
print(lst2)
lst2 = [3, 7, 8, 5, 6, 2, [1, 1, 0], 1, 1, 0]
# ---------------------------------------------------
lst2.insert(6, 'p')  # (索引,元素)在索引位置插入元素,index=-1无法插入到最后一位,因为它是向前插入的
print(lst2)
lst2 = [3, 7, 8, 5, 6, 2, 'p', [1, 1, 0], 1, 1, 0]
# --------------------------------------------------
lst2[5:] = lst2  # 切掉列表x后面的所有元素，并添加列表2的所有元素
print(lst2)
lst2 = [3, 7, 8, 5, 6, 3, 7, 8, 5, 6, 2, 'p', [1, 1, 0], 1, 1, 0]
# -----------------------------------------------------------------------
# 列表元素删除操作：
lst2.remove(3)  # (元素)移除列表里第一个指定元素
print(lst2)
lst2 = [7, 8, 5, 6, 3, 7, 8, 5, 6, 2, 'p', [1, 1, 0], 1, 1, 0]
# -----------------------------------------------
lst2.pop(-4)  # (索引)移除元素,如果不写索引，则移除最后一个元素
print(lst2)
lst2 = [7, 8, 5, 6, 3, 7, 8, 5, 2, 6, 'p', 1, 1, 0]
# -----------------------------------------------
lst2[2:] = []  # [star:stop:step]切除列表片段
print(lst2)
lst2 = [7, 8]
# -----------------------------------------------
lst2.clear()  # 清除元素
print(lst2)
lst2 = []
# ------------------------------------------------
del lst2  # 删除列表
# print(lst2) #name 'lst2' is not defined
# -----------------------------------------------------------------------
# 列表元素修改和排序操作
lst3 = [1, 1, 0]
lst3[2] = 6  # [索引]＝元素,修改元素
print(lst3)
lst3 = [1, 1, 6]
# -----------------------------------------
lst3[1:2] = [0, 0, 8]  # 替换片段
print(lst3)  # 列表名[star:stop]＝[a，b，c……]
lst3 = [1, 0, 0, 8, 6]
# -----------------------------------------------------------------------
# 排序
lst3.sort()  # 小到大，升序排序
print(lst3)
lst3 = [0, 0, 1, 6, 8]
# -----------------------------------------
lst3.sort(reverse=True)  # 大到小，降序
print(lst3)
lst3 = [8, 6, 1, 0, 0]
# ------------------------------------------
lst4 = sorted(lst3)  # 升序新列表
print(lst4)
lst4 = [0, 0, 1, 6, 8]
# -------------------------------------------
lst5 = sorted(lst3, reverse=True)  # 降序新列表
print(lst5)
lst5 = [8, 6, 1, 0, 0]
# -----------------------------------------
lst6 = [i ** 2 for i in range(1, 6)]  # [表达式 for 变量 in range()]生成列表
print(lst6)
lst6 = [1, 4, 9, 16, 25]
# -----------------------------------------------------------------------
# 判断
print(9 in lst6)  # True,9存在于lst6中
# -----------------------------------------------------------------------
# 拷贝
lst7 = lst6.copy()  # 修改lst7,6不会变
# -----------------------------------------------------------------------
# 循环创建多个列表
for k in range(10,20):
    exec(f'lst{k}=2*k')
print(lst15)  # 30


