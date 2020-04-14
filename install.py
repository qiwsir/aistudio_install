#!coding:utf-8
'''
如果需要进行持久化安装, 需要使用持久化路径, 如下方代码示例:

!mkdir /home/aistudio/external-libraries
!pip install beautifulsoup4 -t /home/aistudio/external-libraries

同时添加如下代码, 这样每次环境(kernel)启动的时候只要运行下方代码即可:

import sys
sys.path.append('/home/aistudio/external-libraries')
'''

import sys
import os

ds = os.listdir()
dire = '/home/aistudio/external-libraries'
if dire not in ds:
    os.mkdir(dire)

package_name = sys.argv[1]

cn_source = "-i https://pypi.tuna.tsinghua.edu.cn/simple/"
os.system("pip install " + package_name + " " + cn_source + " -t " + dire)

sys.path.append(dire)