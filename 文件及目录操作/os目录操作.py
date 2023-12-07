import os

os.mkdir('path')  # 创建目录
os.makedirs('path')  # 当父目录不存在是会创建父目录   例如:'./text1/text2'如果text1也不存在,会创建text1
os.path.exists('path')  # 判断一个目录是否存在
