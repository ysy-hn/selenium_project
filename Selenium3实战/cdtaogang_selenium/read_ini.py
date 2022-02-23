import configparser


# cf = configparser.ConfigParser()
# cf.read('../config/LocalElement.ini')
# print(cf.get('RegisterElement', 'user_email'))

class ReadIni(object):
    """读取ini配置文件数据"""
    def __init__(self, filename=None, node=None):
        if filename == None:
            self.filename = '../config/LocalElement.ini'
        if node == None:
            self.node = 'RegisterElement'
        else:
            self.node = node
        self.cf = self.load_ini(self.filename)

    def load_ini(self, filename):
        cf = configparser.ConfigParser()
        cf.read(filename)
        return cf

    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data


if __name__ == '__main__':
    print(ReadIni().get_value('user_name'))
