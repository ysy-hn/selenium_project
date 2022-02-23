"""
封装元素定位方法：
    1、构造浏览器对象
    2、元素定位方法
    3、输入方法
    4、点击方法
    5、访问url
    6、强制等待
    7、退出浏览器方法
"""
from selenium import webdriver
from time import sleep


def open_browser(txt):
    """构造浏览器对象"""
    try:
        driver = getattr(webdriver, txt)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class Key:

    def __init__(self, txt):
        self.driver = open_browser(txt)

    # driver = webdriver.Chrome()

    def locator(self, name, value):
        """元素定位"""
        return self.driver.find_element(name, value)

    def click(self, name, value):
        """点击方法"""
        self.locator(name, value).click()

    def input(self, name, value, txt):
        """输入方法"""
        self.locator(name, value).send_keys(txt)

    def open(self, txt):
        """访问url"""
        self.driver.get(txt)

    def sleep(self, txt):
        """强制停止5s"""
        sleep(txt)

    def quit(self):
        """关闭浏览器"""
        self.driver.quit()


class A:
    def __init__(self, x):
        self.x = x

    def hello(self):
        return 'hello func'


if __name__ == '__main__':
    a = A(10)
    print(getattr(a, 'x'))  # 相当于a.x
    print(getattr(a, 'y', 20))  # 相当于a.y，因为a.y并不存在，所以返回第三个参数作为默认值
    print(getattr(a, 'hello')())  # 相当于a.hello()
    print(getattr(A, 'a'))  # 相当于A.a
