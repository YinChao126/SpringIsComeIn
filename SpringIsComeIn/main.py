# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 15:03:03 2019

@author: yinchao
"""
import DataRecord
import json
a = DataRecord.DataRecord()
a.record()

with open(base_dir+'test.txt','w') as fh:
    fh.write('hello,worldss')

class SpringCome:
    '''
    主函数
    1. 读取配置文件，提供整个系统工作所需的参数
    2. 打开登陆界面，等待用户输入
    3. 判断用户文件系统是否完整，并更新文件系统
    4. 弹出用户使用主界面
    5. 如果用户需要录入数据，则弹出录数据的界面（自动追加到文件中）
    6. 如果用户需要查看以往的结果，则图形化返回
    '''
    def __init__(self):
        self.user = 'yinchao'
        self.passwd = '123456'
        