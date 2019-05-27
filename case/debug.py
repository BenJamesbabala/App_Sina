# Author: SH
# Data: 2019/5/16
# Status 
# Comment:

import os
print(os.path.abspath(os.path.join(os.getcwd(),'../'))) #获取上一级目录
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.realpath(__file__)))  # 当前文件所属目录