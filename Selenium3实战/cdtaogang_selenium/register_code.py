from PIL import Image
from selenium import webdriver
import time, random, json
from find_element import FindElement


class RegisterFunc(object):
    def __init__(self, url, i):
        self.driver = self.get_driver(url, i)

    def get_driver(self, url, i):
        '''浏览器初始化'''
        if i == 0:
            driver = webdriver.Chrome()
        elif i == 1:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Ie()
        driver.get(url)
        # driver.maximize_window()
        return driver

    def send_user_info(self, key, data):
        '''获取元素'''
        self.get_user_element(key).send_keys(data)

    def get_user_element(self, key):
        """获取用户元素"""
        fe = FindElement(self.driver)
        user_element = fe.get_element(key)
        return user_element

    def get_range_user(self):
        """随机生成用户名"""
        str = '1234567890abcdefghijklmnopqrstuvwsyz'
        user_info = ''.join(random.sample(str, 8))
        return user_info

    def get_range_email(self):
        """随机生成邮箱名"""
        user_info = self.get_range_user()
        print(type(user_info))
        if not user_info[0:1].isdigit():
            email = ''.join(user_info) + '@163.com'
        else:
            user_info = random.choice('abcdefghijklmnopqrstuvwsyz') + user_info[1:]
            email = ''.join(user_info) + '@163.com'
        return email

    def get_captcha_image(self, file_name):
        """裁剪验证码图片"""
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element('captcha_image')
        x = code_element.location['x']
        y = code_element.location['y']
        width = code_element.size['width'] + x
        height = code_element.size['height'] + y
        im = Image.open(file_name)
        img = im.crop((x, y, width, height))  # 裁剪图片
        img.save(file_name)

    def get_captcha_image_code(self, file_name):
        """解析验证码图片"""
        pass

    def main(self):
        """运行主程序"""
        file_name = './data/captcha_1.png'
        user_email = self.get_range_email()
        user_name = self.get_range_user()
        captcha_code = self.get_captcha_image_code(file_name)
        self.send_user_info('user_email', user_email)
        self.send_user_info('user_name', user_name)
        self.send_user_info('password', '123456')
        self.send_user_info('captcha_code', captcha_code)
        self.get_user_element('register_button').click()
        code_error = self.get_user_element('captcha_code_error')
        if code_error is None:
            print('注册成功')
        else:
            print('注册失败')
            self.driver.save_screenshot('./data/code_error.png')
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    for i in range(3):
        RegisterFunc('http://www.5itest.cn/register', i).main()
