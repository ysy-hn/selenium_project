import yagmail


def send_email(attachment):
    # 发出邮件账号，密码，邮箱网址
    yag = yagmail.SMTP(user='2395969839@qq.com', password='123456', host='qq.com')
    # 主题
    subject = 'unittest 和 email 测试'
    # 正文
    contents = '详情请查看正文附件'
    # # 发送的附件
    # file1 = '../log/log.log'
    # file2 = '../Report_integration/2022-01-04 14_23_16report.html'
    # attachment_list = [file1, file2]
    # 收件人账号
    recipients_list = ['', '']
    # 发送
    yag.send(recipients_list, subject, contents, attachment)
    print('邮件发送成功！')


if __name__ == '__main__':
    pass
