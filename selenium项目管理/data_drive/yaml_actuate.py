import yaml

# # yaml文件读取操作
# file = open('../data/data1.yaml', encoding='utf-8')
# result = yaml.load(file, Loader=yaml.FullLoader)
# print(result)
# file.close()


# yaml文件读取并自动关闭
with open('../data/data1.yaml', encoding='utf-8') as f:
    result = yaml.load(f, Loader=yaml.FullLoader)
    print(result)