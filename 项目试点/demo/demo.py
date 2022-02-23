from web_key.key import Key


key = Key('sa')
key.open('http://www.baidu.com')
key.input('id', 'kw', '虚竹')
key.click('id', 'su')
key.sleep(5)
key.quit()





