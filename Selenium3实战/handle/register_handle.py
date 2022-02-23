from page.register_page import RegisterPage

class RegisterHandle(object):
    def __init__(self, driver):
        self.reg_page = RegisterPage(driver)

    def send_user_email(self, email):
        """输入邮箱地址"""
        self.reg_page.get_email_element().send_keys(email)

    def send_user_name(self, name):
        """输入用户名"""
        self.reg_page.get_username_element().send_keys(name)

    def send_user_password(self, password):
        """输入密码"""
        self.reg_page.get_password_element().send_keys(password)

    def send_user_captcha(self, code):
        """输入验证码"""
        self.reg_page.get_captcha_element().send_keys(code)

    def get_error_msg(self, info, error_msg):
        """获取邮箱错误信息"""
        if info == 'email_error':
            text = self.reg_page.get_user_email_error_element().text
        elif info == 'username_error':
            text = self.reg_page.get_user_name_error_element().text
        elif info == 'password_error':
            text = self.reg_page.get_password_error_element().text
        else:
            text = self.reg_page.get_captcha_code_error_element().text
        return text

    def click_register(self):
        """点击注册"""
        self.reg_page.get_register_button_element().click()

    def get_register_button_text(self):
        return self.reg_page.get_register_button_element().text


