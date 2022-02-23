from email_demo import Mail


mail = Mail('Chrome')
mail.window_size('1000', '1000')
mail.open_url('http://www.126.com')
mail.login('username', 'password')
mail.sleep_time(2)
mail.logout()



