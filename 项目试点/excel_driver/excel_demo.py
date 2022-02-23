import openpyxl
from web_key.key import Key

excel = openpyxl.load_workbook(r'../data/data.xlsx')
sheets = excel.sheetnames
for name in sheets:
    sheet = excel[name]
    print("********{}********".format(name))
    for values in sheet.values:
        if type(values[0]) is int:
            """
            提取内容：
                1、操作行为
                2、对应参数
            """
            data = {}
            data['name'] = values[2]
            data['value'] = values[3]
            data['txt'] = values[4]
            # 将参数的none值去除
            for key1 in list(data.keys()):
                if data[key1] is None:
                    del data[key1]
            # print(data)
            print("正在执行：{}".format(values[5]))
            # 基于关键字行为进行测试执行
            if values[1] == 'open_browser':
                key = Key(**data)
            else:
                getattr(key, values[1])(**data)
# 单星号 * 用于对列表LIST或元组tuple中的元素进行取出（unpacke）
# 双星号 ** 可将字典里的“值”取出