from handle.register_handle import RegisterHandle


class RegisterBusiness(object):
    def __init__(self, driver):
        self.reg_handle = RegisterHandle(driver)

    def user_common(self, email, name, password, code):
        self.reg_handle.send_user_email(email)
        self.reg_handle.send_user_name(name)
        self.reg_handle.send_user_password(password)
        self.reg_handle.send_user_captcha(code)
        self.reg_handle.click_register()

    def register_email_error(self, email, name, password, code):
        self.user_common(email, name, password, code)
        if self.reg_handle.get_error_msg('email_error', '请输入有效的电子邮件地址') == None:
            print('注册邮箱错误信息检验不成功')
            return True
        else:
            return False

    def register_username_error(self, name, email, password, code):
        self.user_common(email, name, password, code)
        if self.reg_handle.get_error_msg('username_error', '字符长度必须大于等于4，一个中文字算2个字符') == None:
            print('注册用户名误信息检验不成功')
            return True
        else:
            return False

    def register_password_error(self, name, email, password, code):
        self.user_common(email, name, password, code)
        if self.reg_handle.get_error_msg('password_error', '最少输入5个字符') == None:
            print('注册密码错误信息检验不成功')
            return True
        else:
            return False

    def register_captcha_error(self, name, email, password, code):
        self.user_common(email, name, password, code)
        if self.reg_handle.get_error_msg('captcha_error', '验证码错误') == None:
            print('注册验证码误信息检验不成功')
            return True
        else:
            return False

    def register_success(self):
        if self.reg_handle.get_register_button_text():
            return True
        else:
            return False
