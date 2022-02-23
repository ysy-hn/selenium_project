# # 运算符
# # 逻辑：and、or、not
# # 成员：in、not in
# # 身份：is、is not
# # 三目：表达式1 if 判断 else 表达式2，若真，则1，反之2；可嵌套，a if a>b else c if c>d else d
# #
# #
# # 函数与模块
# # 函数嵌套，一般简单的认为是在函数中调用其他函数，和装饰器相似
# # 函数递归，一般简单的任务是在函数中调用自己，形成递归
# # 匿名函数：lambda [arg1 [,arg2,.....argn]]:expression（lambda 参数列表：return [表达式] 变量）
# # 值传递简单的认为使用一个值作为函数的实参；
# # 引用传递简单的认为传了一个变量作为函数的实参
# # os模块：
# #   1、os模块是Python内置的与操作系统功能和文件系统相关的模块，该模块中的语句的执行结果通常与操作系统有关，在不同的操作系统上运行，得到的结果可能不一样
# #   2、os模块与os.path模块用于对目录或文件进行操作
# # json模块：对json文件的读写等操作
# # jsonpath模块：解决多层嵌套的复杂字典以及其它场景使用(类似正则表达式），安装第三方库
# import json
# from jsonpath import jsonpath
# with open('数据.json', encoding='utf-8') as f:
#     a = json.load(f)
# print(jsonpath(a, '$..author'))  # 将所有author的字典值提取
#
#
# # 面向对象编程
#
#
# # 反射机制：反射机制就是在运行时，动态的确定对象的类型，并可以通过字符串调用对象属性、方法、导入模块，是一种基于字符串的事件驱动。
# # 反射就是通过字符串的形式，导入模块；通过字符串的形式，去模块寻找指定函数，并执行。利用字符串的形式去对象（模块）中操作（查找/获取/删除/添加）成员，一种基于字符串的事件驱动！
# # getattr()、setattr()、delattr()、exec()、eval()、__import__，这些函数都可以执行字符串。
# # eval：计算指定表达式的值，只能执行单个表达式，不能是复杂的代码逻辑，不能是赋值表达式。
# # exec：执行复杂表达式，可以动态运行代码段，返回值永远都是None。
# # 虽然我们可以使用eval和exec来执行，假如这个属性是不存在的，那么这种调用就会报错。
# # hasattr(object, name)：判断对象object是否包含名为name的特性（hasattr是通过调用getattr(ojbect, name)是否抛出异常来实现的）
# # getattr(对象，对象属性，默认属性（选填）),返回一个对象属性值，没有属性并且无默认属性报错。
# # setattr(对象，对象属性，默认属性（选填)) ,对应函数 getattr()，用于设置属性值，该属性不一定是存在的。
# # delattr(对象，对象属性)函数用于删除属性,delattr(x, 'foobar') 相等于 del x.foobar。
# # __import__() 函数用于动态加载类和函数,如果一个模块经常变化就可以使用__import__()来动态载入。
# imp = input("请输入模块:")
# dd = __import__(imp)  # 等价于import imp
# inp_func = input("请输入要执行的函数：")
# f = getattr(dd, inp_func, None)  # 作用:从导入模块中找到你需要调用的函数inp_func,然后返回一个该函数的引用.没有找到就烦会None
# f()  # 执行该函数
#
#
# # 自动化相关
# # 全局配置INI配置文件处理（configparser模块:增删读写）：
# # 1、读取ini文件
# import configparser
# # import os
# # os.chdir('E:\You\G\python\python_自动化测试\Selenium3自动化测试实战\项目试点\笔记')
# cf = configparser.ConfigParser()
# filename = cf.read("test.ini", encoding='utf-8')
# print(filename)
# sec = cf.sections()  # sections() 得到所有的section，以列表形式返回
# print(sec)
# opt = cf.options("mysql")  # options(section) 得到section下的所有option
# print(opt)
# value = cf.items("mysql")  # items 得到section的所有键值对
# print(value)
# mysql_host = cf.get("mysql", "host")  # get(section,option) 得到section中的option值，返回string/int类型的结果
# mysql_password = cf.getint("mysql", "password")
# print(mysql_host, mysql_password)
# # cf.read(filename)：读取文件内容
# # cf.sections()：得到所有的section（章节），并且以列表形式返回
# # cf.options(section)：得到section下所有的option（选项）
# # cf.items(option)：得到该section所有的键值对
# # cf.get(section,option)：得到section中option的值，返回string类型的结果
# # cf.getint(section,option)：得到section中option的值，返回int类型的结果
#
# # 2、写ini文件
# import configparser
# import os
# os.chdir('E:\You\G\python\python_自动化测试\Selenium3自动化测试实战\项目试点\笔记')
# cf = configparser.ConfigParser()
# cf.add_section('mq')
# cf.set('mq', 'user', 'laozhang')
# cf.add_section('用户')
# cf.set('用户', '账号', '密码')
# with open('test1.ini', 'w', encoding='utf-8')as f:
#     cf.write(f)
# # cf.write(filename)：将configparser对象写入.ini类型的文件
# # add_section()：添加一个新的section
# # add_set(section,option,value)：对section中的option信息进行写入
#
# # 3、修改ini文件
# import configparser
# import os
# os.chdir('E:\You\G\python\python_自动化测试\Selenium3自动化测试实战\项目试点\笔记')
# cf = configparser.ConfigParser()
# cf.read('test1.ini', encoding='utf-8')
# cf.remove_section('mq')
# cf.remove_option('用户', '账号')
# with open('test1.ini', 'w+', encoding='utf-8')as f:
#     cf.write(f)
# # cf.read(filename)：读取文件（这里需要注意的是：一定要先读取文件，再进行修改）
# # cf.remove_section(section)：删除文件中的某个section的数值
# # cf.remove_option(section,option)：删除文件中某个section下的option的数值
# #
# # 外部数据源Mysql数据库操作（Mysqldb、实现CURD（增读更删）、事务机制）：
# # 事务机制可以确保数据一致性。
# # 事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。
# # 原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
# # 一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
# # 隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
# # 持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。
# # import MySQLdb
# # host = "localhost"
# # port = 3306
# # user = "root"
# # passwd = "pass"
# # db = "my_test_db"
# # conn = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db = db) # 打开数据库连接
# # cur = conn.cursor() # 使用cursor()方法获取操作游标
# # try:
# #     sql = "insert into test values('str',1,-1)"
# #     cur.execute(sql)
# #     sql = "insert into te1st values('str',2,-2)" # 这是一条错误的sql，因为事务机制，所以上1条sql语句也不会执行
# #     cur.execute(sql)
# #     conn.commit() # 提交到数据库执行
# # except:
# #     conn.rollback() # 发生错误时回滚
# # sql = "select * from test"
# # cur.execute(sql)
# # print(cur.fetchall())
# # sql = "insert into test values('str',3,-3)" # 一条正确的插入语句
# # cur.execute(sql)
# # conn.commit() # 提交到数据库执行
# # sql = "select * from test"
# # cur.execute(sql)
# # print(cur.fetchall())
# # conn.close() # 关闭数据库连接，一定要关闭，连接开太多会出问题
#
#
# # 闭包函数：
# # 又称闭合函数，其实和前面讲的嵌套函数类似，不同之处在于，闭包中外部函数返回的不是一个具体的值，而是一个函数。
# # 一般情况下，返回的函数会赋值给一个变量，这个变量可以在后面被继续执行调用。
# # 一个函数和它的环境变量合在一起，就构成了一个闭包(closure)。所谓的闭包是一个包含有环境变量取值的函数对象。环境变量取值被保存在函数对象的__closure__属性中。
# # 闭包比普通的函数多了一个__closure__属性，该属性记录着自由变量的地址。当闭包被调用时，系统就会根据该地址找到对应的自由变量，完成整体的函数调用。
# # 创建一个闭包可以归结为以下三点：
# # 1、闭包函数必须有内嵌函数
# # 2、内嵌函数需要引用该嵌套函数上一级中的变量
# # 3、闭包函数必须返回内嵌函数
# def closureFun(a):
#     def add(x):        # 1 闭包函数必须有内嵌函数
#         return x + a   # 内嵌函数需要引用该嵌套函数上一级中的变量 a
#     return add         # 闭包函数必须返回内嵌函数
# c = closureFun(5)   # 实例化函数 closureFun  返回 函数add
# print(c(6))  # 调用add ,并传参 ，此时返回 x + a = 6 + 5 = 11
# print(c.__closure__)
# print(c.__closure__[0].cell_contents)
# print(c.__name__)
#
#
# # requests模块使用
# # response.status_code   # 打印状态码
# # response.url           # 打印请求url
# # response.headers       # 打印头信息
# # response.cookies       # 打印cookie信息
# # response.encoding      # 当前编码
# # response.text          # 以文本形式打印网页源码
# # response.content       # 以字节流形式（二进制）返回

# import requests
# response = requests.get('http://img.ivsky.com/img/tupian/pre/201708/30/kekeersitao-002.jpg')
# b = response.content
# with open('E:\You\G\python\python_自动化测试\Selenium3自动化测试实战\项目试点\笔记\\1.jpg','wb') as f:
#     f.write(b)

# # HTTP请求类型
# # import requests
# # requests.get('http://httpbin.org/get')
# # requests.get参数：params：查询参数，该方法会自动对params字典编码,然后和url拼接
# # timeout：超过等待时间则报错
# # auth：web客户端验证参数，1、针对于需要web客户端用户名密码认证的网站；2、auth = ('username','password')
# # verify：SSl证书认证参数，1、适用网站: https类型网站但是没有经过 证书认证机构 认证的网站；2、适用场景: 抛出 SSLError 异常则考虑使用此参数
# # proxies：代理参数，1、定义: 代替你原来的IP地址去对接网络的IP地址；2、作用: 隐藏自身真实IP,避免被封。
# # requests.post('http://httpbin.org/post')
# # requests.put('http://httpbin.org/put')
# # requests.delete('http://httpbin.org/delete')
# # requests.head('http://httpbin.org/get')
# # requests.options('http://httpbin.org/get')

# # 获取响应内容
# print(r.content)  # 以字节的方式去显示，中文显示为字符
# print(r.text)  # 以文本的方式去显示
#
# # URL传递参数
# payload = {'keyword': '香港', 'salecityid': '2'}
# r = requests.get("http://m.ctrip.com/webapp/tourvisa/visa_list", params=payload)
# print(r.url)  # 示例为http://m.ctrip.com/webapp/tourvisa/visa_list?salecityid=2&keyword=香港
#
# # 获取/修改网页编码
# r = requests.get('https://github.com/timeline.json')
# print(r.encoding)
#
#
# # json处理
# r = requests.get('https://github.com/timeline.json')
# print(r.json()) # 需要先import json
#
# # 定制请求头
# url = 'http://m.ctrip.com'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'
#     }
# r = requests.post(url, headers=headers)
# print(r.request.headers)
#
# # 复杂post请求
# url = 'http://m.ctrip.com'
# payload = {'some': 'data'}
# r = requests.post(url, data=json.dumps(payload))  # 如果传递的payload是string而不是dict，需要先调用dumps方法格式化一下
#
# # post多部分编码文件
# url = 'http://m.ctrip.com'
# files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=files)
#
# # 响应状态码
# r = requests.get('http://m.ctrip.com')
# print(r.status_code)
#
# # 响应头
# r = requests.get('http://m.ctrip.com')
# print(r.headers)
# print(r.headers['Content-Type'])
# print(r.headers.get('content-type'))  # 访问响应头部分内容的两种方式
#
# # Cookies
# url = 'http://example.com/some/cookie/setting/url'
# r = requests.get(url)
# r.cookies['example_cookie_name']  # 读取cookies
#
# url = 'http://m.ctrip.com/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)  # 发送cookies
#
# # 设置超时时间
# r = requests.get('http://m.ctrip.com', timeout=0.001)
#
# # 设置访问代理
# proxies = {
# "http": "http://10.10.1.10:3128",
# "https": "http://10.10.1.100:4444",
# }
# r = requests.get('http://m.ctrip.com', proxies=proxies)
#
# # 如果代理需要用户名和密码，则需要这样：
# proxies = {
# "http": "http://user:pass@10.10.1.10:3128/",
# }
#
# # get请求
# import requests
# ret = requests.get('https://www.cnblogs.com/lanyinhao/p/9634742.html')
# print(ret.url)
# print(ret.text)
# payload = {'key1': 'value1', 'key2': 'value2'}
# ret = requests.get("http://httpbin.org/get", params=payload)
# print(ret.url)
# print(ret.text)
#
# # Post请求
# # 1、基本POST实例
# import requests
# payload = {'key1': 'value1', 'key2': 'value2'}
# ret = requests.post("http://httpbin.org/post", data=payload)
# print(ret.text)
# print(1)
# # 2、发送请求头和数据实例
# import requests
# import json
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# headers = {'content-type': 'application/json'}
# ret = requests.post(url, data=json.dumps(payload), headers=headers)
# print(ret.text)
# print(2)
# print(ret.cookies)
#
# # Xml请求
# import requests
# class url_request():
#     def __init__(self):
#         """init"""
# if __name__ == '__main__':
#     heards = {'Content-type': 'text/xml'}
#     XML = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><Request xmlns="http://tempuri.org/"><jme><JobClassFullName>WeChatJSTicket.JobWS.Job.JobRefreshTicket,WeChatJSTicket.JobWS</JobClassFullName><Action>RUN</Action><Param>1</Param><HostIP>127.0.0.1</HostIP><JobInfo>1</JobInfo><NeedParallel>false</NeedParallel></jme></Request></soap:Body></soap:Envelope>'
#     url = 'http://jobws.push.mobile.xxxxxxxx.com/RefreshWeiXInTokenJob/RefreshService.asmx'
#     r = requests.post(url=url, headers=heards, data=XML)
#     data = r.text
#     print(data)
#
# # 状态异常处理
# import requests
# URL = 'http://ip.taobao.com/service/getIpInfo.php'  # 淘宝IP地址库API
# try:
#     r = requests.get(URL, params={'ip': '8.8.8.8'}, timeout=5)
#     r.raise_for_status()
# except requests.RequestException as e:
#     print('异常报错：{}'.format(e))
# else:
#     result = r.json()
#     print(type(result), result, sep='\n')
#
# # 上传文件
# import requests
# url = 'http://127.0.0.1:8080/upload'
# files = {'file': open('/home/rxf/test.jpg', 'rb')}
# # files = {'file': ('report.jpg', open('/home/lyb/sjzl.mpg', 'rb'))}     #显式的设置文件名
# r = requests.post(url, files=files)
# print(r.text)
#
# # 把字符串当作文件进行上传
# import requests
# url = 'http://127.0.0.1:8080/upload'
# files = {'file': ('test.txt', b'Hello Requests.')}  # 必需显式的设置文件名
# r = requests.post(url, files=files)
# print(r.status_code)
# print(r.text)
#
# # 身份验证
# import requests
# from requests.auth import HTTPBasicAuth
# r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=HTTPBasicAuth('user', 'passwd'))
# # r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=('user', 'passwd'))    # 简写
# print(r.json())
#
# # Cookies与会话对象
# import requests
# r = requests.get('http://www.google.com.hk/')
# print(r.cookies['NID'])
# print(tuple(r.cookies))
#
# # 发送cookies到服务器，可以使用 cookies 参数
# import requests
# url = 'http://httpbin.org/cookies'
# cookies = {'testCookies_1': 'Hello_Python3', 'testCookies_2': 'Hello_Requests'}
# # 在Cookie Version 0中规定空格、方括号、圆括号、等于号、逗号、双引号、斜杠、问号、@，冒号，分号等特殊符号都不能作为Cookie的内容。
# r = requests.get(url, cookies=cookies)
# print(r.json())
#
# import requests
# headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#            'Accept-Encoding': 'gzip, deflate, compress',
#            'Accept-Language': 'en-us;q=0.5,en;q=0.3',
#            'Cache-Control': 'max-age=0',
#            'Connection': 'keep-alive',
#            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
#            }
# s = requests.Session()
# s.headers.update(headers)
# # s.auth = ('superuser', '123')
# s.get('https://www.kuaipan.cn/account_login.htm')
# _URL = 'http://www.kuaipan.cn/index.php'
# s.post(_URL, params={'ac': 'account', 'op': 'login'},
#        data={'username': '****@foxmail.com', 'userpwd': '********', 'isajax': 'yes'})
# r = s.get(_URL, params={'ac': 'zone', 'op': 'taskdetail'})
# print(r.json())
# s.get(_URL, params={'ac': 'common', 'op': 'usersign'})
#
# import requests
# '''requests模块抓取网页源码并保存到文件示例'''
# html = requests.get("http://www.baidu.com")
# with open('test.txt', 'w', encoding='utf-8') as f:
#     f.write(html.text)
#
# '''读取一个txt文件，每次读取一行，并保存到另一个txt文件中的示例'''
# ff = open('test2.txt', 'w', encoding='utf-8')
# with open('test.txt', encoding="utf-8") as f:
#     for line in f:
#         ff.write(line)
# ff.close()
#
# # 自动登录，方式一，不推荐
# import requests
# # # 1、登录页面获取cookie
# i1 = requests.get(url="http://dig.chouti.com/help/service")
# i1_cookies = i1.cookies.get_dict()
# # # 2、用户登陆，携带上一次的cookie，后台对cookie中的 gpsd 进行授权
# i2 = requests.post(
#     url="http://dig.chouti.com/login",
#     data={
#         'phone': "8615131255089",
#         'password': "xxooxxoo",
#         'oneMonth': ""
#     },
#     cookies=i1_cookies
# )
# # # 3、点赞（只需要携带已经被授权的gpsd即可）
# gpsd = i1_cookies['gpsd']
# i3 = requests.post(
#     url="http://dig.chouti.com/link/vote?linksId=8589523",
#     cookies={'gpsd': gpsd}
# )
# print(i3.text)
#
# # 自动登录，方式二，推荐
# import requests
# session = requests.Session()  # 会话对象让你能够跨请求保持某些参数，最方便的是在同一个Session实例发出的所有请求之间保持cookies
# i1 = session.get(url="http://dig.chouti.com/help/service")
# i2 = session.post(
#     url="http://dig.chouti.com/login",
#     data={
#         'phone': "8615131255089",
#         'password': "xxooxxoo",
#         'oneMonth': ""
#     }
# )
# i3 = session.post(
#     url="http://dig.chouti.com/link/vote?linksId=8589523"
# )
# print(i3.text)
#
# # 知乎登录
# # import time
# # import requests
# # from bs4 import BeautifulSoup
# # session = requests.Session()
# # i1 = session.get(
# #     url='https://www.zhihu.com/#signin',
# #     headers={
# #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
# #     }
# # )
# # soup1 = BeautifulSoup(i1.text, 'lxml')
# # xsrf_tag = soup1.find(name='input', attrs={'name': '_xsrf'})
# # xsrf = xsrf_tag.get('value')
# # current_time = time.time()
# # i2 = session.get(
# #     url='https://www.zhihu.com/captcha.gif',
# #     params={'r': current_time, 'type': 'login'},
# #     headers={
# #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
# #     })
# # with open('zhihu.gif', 'wb') as f:
# #     f.write(i2.content)
# # captcha = input('请打开zhihu.gif文件，查看并输入验证码：')
# # form_data = {
# #     "_xsrf": xsrf,
# #     'password': 'xxooxxoo',
# #     "captcha": 'captcha',
# #     'email': '424662508@qq.com'
# # }
# # i3 = session.post(
# #     url='https://www.zhihu.com/login/email',
# #     data=form_data,
# #     headers={
# #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
# #     }
# # )
# # i4 = session.get(
# #     url='https://www.zhihu.com/settings/profile',
# #     headers={
# #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
# #     }
# # )
# # soup4 = BeautifulSoup(i4.text, 'lxml')
# # tag = soup4.find(id='rename-section')
# # nick_name = tag.find('span',class_='name').string
# # print(nick_name)
#
#
#
#
#
