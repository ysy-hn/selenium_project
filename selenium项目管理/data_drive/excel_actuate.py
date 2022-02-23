# # ！/usr/bin/python3
# -*- coding: utf-8 -*-
# 当前项目名称：Selenium3自动化测试实战
# 文件名称： excel_actuate
# 登录用户名： yanshaoyou
# 作者： 闫少友
# 邮件： 2395969839@qq.com
# 电话：17855503800
# 创建时间： 2021/12/9  13:52
import openpyxl
from test_case.Test_web import TestWeb

excel = openpyxl.load_workbook('../data/data1.xlsx')
sheets = excel.sheetnames
for name in sheets:
    sheet = excel[name]
    print("********{}********".format(name))
    for value in sheet.values:
        if type(value[0]) is int:
            data = {}
            data['name'] = value[2]
            data['value'] = value[3]
            data['txt'] = value[4]
            for key1 in list(data.keys()):
                if data[key1] is None:
                    del data[key1]
            # print(data)
            print("正在执行：{}".format(value[5]))
            if value[1] == 'open_browser':
                key = TestWeb('as')
            else:
                getattr(key, value[1])(**data)
