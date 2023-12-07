import os
# os.environ环境变量----------------------------------------
# 是一个环境变量的字典
os.getenv(key="HOME")  # 读取操作系统环境变量HOME的值
os.environ.get(k="HOME")
os.environ.keys()  # 获取所有环境变量的key
'''
os.environ['HOMEPATH']:当前用户主目录。
os.environ['TEMP']:临时目录路径。
os.environ["PATHEXT"]:可执行文件。
os.environ['SYSTEMROOT']:系统主目录。
os.environ['LOGONSERVER']:机器名。
os.environ['PROMPT']:设置提示符.
'''
# 设置
os.environ['环境变量名称']='环境变量值' #其中key和value均为string类型
os.putenv('环境变量名称', '环境变量值')
os.environ.setdefault('环境变量名称', '环境变量值')
# 修改
os.environ['环境变量名称']='新环境变量值'
# 获取
os.environ['环境变量名称']
os.getenv('环境变量名称')
os.environ.get('环境变量名称', '默认值')	#默认值可给可不给，环境变量不存在返回默认值
# 删除
del os.environ['环境变量名称']
del(os.environ['环境变量名称'])
# 判断
if '环境变量值' in os.environ:pass   # 存在返回 True，不存在返回 False
