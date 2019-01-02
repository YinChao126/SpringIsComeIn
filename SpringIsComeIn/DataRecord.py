# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 15:41:20 2019

@author: yinchao
"""

import json
from datetime import datetime
class DataRecord:
    def __init__(self,f_name = 'example.json'):
        self.filename = f_name
        
    def record(self):
        '''
        根据填入的信息生成一个json格式的文件，用于之后系统统一读入
        返回值：成功->0 失败->-1
        '''
        date = "20190101"
        cash = "2.86"
        income = "20.1"
        credit_debt = "0.89"
        bond_value = "5.81"
        stock_value = "37.23"
        growth_value = "30.55"
        cur_invest = "1.5"      
        big_cost = [{"eat":"0.1"},{"sleep":"1.2"}]  
        new_debt = []
        udf_asset = [{"get money":"0.2"}]
        
        record_data = {
                "date":date,
                "cash":cash,
                "income":income,
                "credit_debt":credit_debt,
                "bond_value":bond_value,
                "stock_value":stock_value,
                "growth_value":growth_value,
                "cur_invest":cur_invest,
                "big_cost":big_cost,
                "new_debt":new_debt,
                "udf_asset":udf_asset,
                }
#        print(record_data)
        json_str = json.dumps(record_data, indent=4)
        print(self.filename)
        with open(self.filename, 'w') as json_file:
            json_file.write(json_str)    
            print('record success')
            return 0
        return -1

if __name__ == '__main__':
    base = 'C:\\Program Files\\SpringCome\\'
    user = 'yinchao'
    day = '20190101'
    fname = base + user + '\\monthly_record\\' + day + '.json'
    test = DataRecord(fname)
    test.record()