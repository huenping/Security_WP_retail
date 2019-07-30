import os
import sys

# 获取当前路径
currPath= \
    os.path.split(os.path.realpath(__file__))[0]

proPath = \
readConfig.getConfValue(os.path.join(currPath,'config.ini'),'project','project_path')

# 获取日志路径
logPath= \
os.path.join(proPath,'retail','report','Log')