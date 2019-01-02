# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 16:06:14 2019

@author: yinchao
"""
import json
import os,stat
import shutil

class User:
    '''
    管理用户配置信息、登陆、文件系统
    '''
    def __init__(self, user, passwd):
        self.user = user
        self.passwd = passwd
        self.base = "C:\\Program Files\\SpringCome\\" #默认的数据根目录
    
    def config_info(self,item):
        '''
        获取所需的配置信息
        '''
        filename = '../config.json'
        
        with open(filename,'r') as fh:
            content = fh.read()
        result = json.loads(content)
        return result[item]
    
    def register(self, user, passwd):
        '''
        新用户注册，生成对应的用户数据文件夹和配置文件
        如果是首次创建，则必须手动创建C:\\Program Files\\SpringCome\\根目录，并添加权限
        判断是否已经有user的文件夹，如果有，则直接返回
        '''
        self.base = self.config_info('default_dir')
        user_dir = self.base + user
        print(user_dir)
        if os.path.exists(user_dir):
            print('用户已存在')
        else:
            print('没有该文件夹')
            os.mkdir(user_dir)
            os.mkdir(user_dir+'\\monthly_record')
            '''
            添加用户信息到self.base+account.csv文件中（DataFrame格式）
            id  user     passwd    record_time  login_time
            0   yinchao  123456    12           33
            '''
            
            
    def del_user(self, user):
        '''
        彻底删除该用户的所有信息
        '''
        self.base = self.config_info('default_dir')
        user_dir = self.base + user
        print(user_dir)
        result = input('你确定要删除%s的所有信息吗？(y/n)' % user)    
        if result == 'y':
            shutil.rmtree(user_dir)
            print('悲剧了，永世找不到这个人的资料了')
        
    def login(self):
        '''
        登陆逻辑：
        1.判断是否已经存在用户的文件夹
        2.判断文件夹中的用户信息和登陆信息是否匹配
        @返回值： 成功->True 失败->False
        '''
        
        
if __name__ == '__main__':
    test = User('lili','123456')
    test.register('lili','123456')
    test.del_user('lili')