"""
key关键词、value值
大小写:upper大写、lower小写、swapcase大小写转换、capitalize首字母大写、title首字母大写
"""
# 创建字典#################################################################
dic = {"name": "绝迹的星", "age": 20}  # {key:value}
# 空字典
d = {}
d = dict({"name": "绝迹的星", "age": 20})
# -----------------------------------------------------------------------
# 获取字典元素
print(dic["name"])  # 如果name不存在会报错KeyError
print(dic.get("name"))  # 不存在输出None
print(dic.get("name", "value"))  # 不存在时输出value
# -----------------------------------------------------------------------
# 添加元素
dic["birthday"] = 12.25  # [key]=value,修改元素也是同样的
print(dic)
dic = {'name': '绝迹的星', 'age': 20, 'birthday': 12.25}
# -----------------------------------------------------------------------
# 修改元素
dic2 = {'age': 3}
dic.update(dic2)  # dic.update(age=3)或者dic[age]=3
print(dic)
dic = {'name': '绝迹的星', 'age': 3, 'birthday': 12.25}
# -----------------------------------------------------------------------
# 删除元素
del dic['birthday']
print(dic)
dic = {'name': '绝迹的星', 'age': 20}
# -----------------------------------------------------------------------
# 清除元素
dic.clear()
print(dic)
dic = {}
# -----------------------------------------------------------------------
# 获取字典视图
dic = {"name": "绝迹的星", "age": 20}
A = dic.keys()  # 输出[key]
B = dic.values()  # 输出[value]
C = dic.items()  # 输出[(keys，values)]
print(A, B, C)
A = ['name', 'age']
B = ['绝迹的星', 20]
C = [('name', '绝迹的星'), ('age', 20)]
# -----------------------------------------------------------------------
# zip字典生成
items = ["name", "age"]
prices = ["绝迹的星", "20"]
dic = {item.title(): price for item, price in zip(items, prices)}
print(dic)
dic = {'Name': '绝迹的星', 'Age': '20'}
# -----------------------------------------------------------------------
# 判断
print("Age" in dic)  # True
# -----------------------------------------------------------------------
# 排序
'''
list = sorted(iterable, key=None, reverse=False)
iterable 指定的序列,key 自定义排序规则,reverse 默认为False从小到大
sorted() 函数会返回一个排好序的列表
'''
dic = {'b': 3, 'a': 5, 'c': 4}
import operator

list = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
print(list)  # 输出[('a', 5),('c':4),('b', 3)]
# 其中key作用是取出key-value元组中下标为1的元素,即取出了dic里的value,改为0可按key排序
# 排序后reverse,按从大到小排序
