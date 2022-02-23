from business.register_business import RegisterBusiness
from selenium import webdriver


class FirstCase(object):
    def __init__(self):
        driver = webdriver.Chrome()
        driver.get('http://www.5itest.cn/register')
        self.reg_business = RegisterBusiness(driver)

    def test_register_email_error(self):
        email_error = self.reg_business.register_email_error('2839ssa31@qq.com', 'laowang', '123456', 'he7h1')
        if email_error:
            print('注册成功， 此条case执行失败')
        else:
            print('注册失败， 此条case执行成功')

    def test_register_username_error(self):
        username_error = self.reg_business.register_username_error('2839ssa31@qq.com', 'lao', '123456', 'he7h1')
        if username_error:
            print('注册成功， 此条case执行失败')
        else:
            print('注册失败， 此条case执行成功')

    def test_register_password_error(self):
        password_error = self.reg_business.register_password_error('2839ssa31@qq.com', 'laowang', '123456', 'he7h1')
        if password_error:
            print('注册成功， 此条case执行失败')
        else:
            print('注册失败， 此条case执行成功')

    def test_register_captcha_error(self):
        captcha_error = self.reg_business.register_captcha_error('2839ssa31@qq.com', 'laowang', '123456', 'he7h1')
        if captcha_error:
            print('注册成功， 此条case执行失败')
        else:
            print('注册失败， 此条case执行成功')

    def test_register_success(self):
        self.reg_business.user_common('2839ssa31@qq.com', 'laowang', '123456', 'he7h1')
        if self.reg_business.register_success():
            print('注册失败')
        else:
            print('注册成功')


def main():
    fc = FirstCase()
    fc.test_register_email_error()
    fc.test_register_username_error()
    fc.test_register_password_error()
    fc.test_register_captcha_error()
    fc.test_register_success()


if __name__ == '__main__':
    main()