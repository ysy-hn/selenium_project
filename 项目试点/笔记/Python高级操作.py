# # 1、*args与**kwargs的使用，*是必须的，名字非必须
# # *args:可在函数中传入多个参数列表
# # **kwargs：可在函数中传入多个不定长度的键值对
#
#
# # 2、生成器（generators）
# # 一个迭代器在遍历并读取一个容器的数据元素时，并不会执行一个迭代。
# # 可迭代对象(Iterable)：能提供迭代器的任意对象；定义了可以返回一个迭代器的__iter__方法，或者定义了可以支持下标索引的__getitem__方法
# # 迭代器(Iterator)：只要定义了next(Python2) 或者__next__方法。
# # 迭代(Iteration)：从某个地方（比如一个列表）取出一个元素的过程。当我们使用一个循环来遍历某个东西时，这个过程本身就叫迭代。
# #
# # 生成器也是一种迭代器，但是你只能对其迭代一次。这是因为它们并没有把所有的值存在内存中，而是在运行时生成值。
# # 你通过遍历来使用它们，要么用一个“for”循环，要么将它们传递给任意可以进行迭代的函数和结构。
# # 大多数时候生成器是以函数来实现的。然而，它们并不返回一个值，而是yield(暂且译作“生出”)一个值。
# #
# # 生成器最佳应用场景是：你不想同一时间将所有计算出来的大量结果集分配到内存当中，特别是结果集里还包含循环。分配到内存中会消耗大量资源。
# # 简单的说有yield的都是生成器，使用next可以获取yield序列的下一个元素，yield完所有的值后再yield会触发StopIteration的异常。
# # 对于一个可迭代对象，而不是迭代器，可使用iter来实施迭代，并使用生成器的next来获取值,next较为繁琐，可使用for循环来取值
# a = 'yan'
# b = iter(a)
# print(next(b), next(b))
# print(next(a))
#
#
# # 3、map、filter、reduce
# # lambda 参数:操作(参数)；lambda 参数1,参数2,...: 表达式,入参（可选）；
# # Map：会将一个函数映射到一个输入列表的所有元素上;不仅用于一列表的输入，我们甚至可以用于一列表的函数;
# # map(function_to_apply, list_of_inputs)
# a = [1, 2, 3, 4, 5]
# b = list(map(lambda x: x**2, a))  # lambda:匿名函数
# print(b)
#
# def multiply(x):
#     return (x*x)
# def add(x):
#     return (x + x)
# funcs = [multiply, add]
# for i in range(5):
#     value = map(lambda x: x(i), funcs)
#     print(list(value))
#
# # filter：过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，符合要求即函数映射到该元素时返回值为True.
# a = range(-5, 5)
# b = filter(lambda x: x < 0, a)
# print(list(b))
#
# # Reduce：当需要对一个列表进行一些计算并返回结果时，Reduce 是个非常有用的函数
# from functools import reduce
# a = reduce(lambda x, y: x*y, [1, 2, 3, 4])
# print(a)
#
#
# # 4、set集合数据结构，与list行为类似，但不能有重复的值,有重复的会去重
# a = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# b = set(a)
# c = set([x for x in a if a.count(x) > 1])
# print(b, c)
# # 交集：intersection；set中使用，其它数据不可
# # 差集：difference；set中使用，其它数据不可
# a = ['yellow', 'red', 'blue', 'green', 'black']
# b = set(a)
# c = ['red', 'brown']
# d = set(c)
# print(b.intersection(d), b.difference(d))
#
#
# # 5 、高级语法
# #     1、x**2（参数） for x in L;参数 for循环
# #     2、x for x in a if a.count(x) > 1；参数 for循环 if判断
# #     3、x + y for x in 'ab' for y in 'jk'；参数 for循环 for循环嵌套
# #     4、(x，y) for x in X [if condition]  for y in Y [if condition]；参数 for循环[if判断] for循环[if判断]...
# #     5、[x, x+1, x+2] for x in [1, 4, 7]；列表推导式
# #     6、[x, x+1, x+2] for x in (1, 4, 7)；生成器表达式
# #     7、[x, x+1, x+2] for x in {1, 4, 7}；集合推导式
# #     8、value: key for key, value in 表达式；字典推导式
# #     9、如果列表中的数据量比较大的情况下，内存消耗是比较严重的在某些情况下，
# #     我们只需要使用列表中的一部分数据，后面的数据并不是特别关心，使用列表动态构建器
# lix = (2*x + 1 for x in range(1, 101))
# print(next(lix), next(lix))
#
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b  # 生成器标志，最终会不走return运行；没有就走return运行
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# f = fib(6)
# print(list(f))
#
# # 6、三元运算符通常在Python里被称为条件表达式，这些表达式基于真(true)/假(not)的条件判断
# # condition_is_true if condition else condition_is_false；真的结果 if 判读条件 else 假的结果
# a = True
# b = "fat" if a else "not fat"
# print(b)
# # (if_test_is_false, if_test_is_true)[test]；(假的结果，真的结果)[判读条件]
# fat = True
# fitness = ("skinny", "fat")[fat]
# print("Ali is ", fitness)
#
# # 7、装饰器(Decorators)，修改其他函数的功能的函数;简单说将不同的函数进行调用修改功能。
# # 在函数中定义函数，在函数中返回函数，在函数中调用函数。
# def a_new_decorator(a_func):
#
#     def wrapTheFunction():
#         print("1")
#         a_func()
#         print("2")
#     return wrapTheFunction
#
# def a_function_requiring_decoration():
#     print("3")
#
# a = a_new_decorator(a_function_requiring_decoration)()
#
# from functools import wraps  # @wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能
# def decorator_name(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         if not can_run:
#             return "Function will not run"
#         return f(*args, **kwargs)
#     return decorated
#
# @decorator_name
# def func():
#     return("Function is running")
#
# can_run = True
# print(func())
# can_run = False
# print(func())
#
# # 装饰器能有助于检查某个人是否被授权（Authorization）去使用一个web应用的端点(endpoint)。
# # from functools import wraps
# #
# # def requires_auth(f):
# #     @wraps(f)
# #     def decorated(*args, **kwargs):
# #         auth = request.authorization
# #         if not auth or not check_auth(auth.username, auth.password):
# #             authenticate()
# #         return f(*args, **kwargs)
# #     return decorated
# #
# # 日志是装饰器运用的另一个亮点
# from functools import wraps
#
# def logit(func):
#     @wraps(func)
#     def with_logging(*args, **kwargs):
#         print(func.__name__ + ' was called')
#         return func(*args, **kwargs)
#     return with_logging
#
# @logit
# def addition_func(x):
#     return x+x
#
# result = addition_func(4)
# print(result)
#
# # 在函数中嵌入装饰器
# from functools import wraps
#
# def logit(logfile='out1.log'):
#     def logging_decorator(func):
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             log_string = func.__name__ + " was called"
#             print(log_string)
#             # 打开logfile，并写入内容
#             with open(logfile, 'a') as opened_file:
#                 # 现在将日志打到指定的logfile
#                 opened_file.write(log_string + '\n')
#             return func(*args, **kwargs)
#         return wrapped_function
#     return logging_decorator
#
# @logit()
# def myfunc1():
#     print('myfunc1--1')
# myfunc1()
#
# @logit(logfile='func2.log')
# def myfunc2():
#     print('myfunc2--2')
# myfunc2()
#
# # 装饰器类
# from functools import wraps
#
# class logit(object):
#     def __init__(self, logfile='out2.log'):
#         self.logfile = logfile
#
#     def __call__(self, func):
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             log_string = func.__name__ + " was called"
#             print(log_string)
#             # 打开logfile并写入
#             with open(self.logfile, 'a') as opened_file:
#                 # 现在将日志打到指定的文件
#                 opened_file.write(log_string + '\n')
#             # 现在，发送一个通知
#             self.notify()
#             return func(*args, **kwargs)
#         return wrapped_function
#
#     def notify(self):
#         print(1)
#
# @logit()
# def myfunc1():
#     print(2)
# myfunc1()
#
#
# # 8、Global和return
# # Global：全局的,将函数中的变量变成全局变量，慎用；使用return即可。
#
#
# # 9、对象变动（mutation），可变(mutable)与不可变(immutable)的数据类型，不可变(immutable)的意思是“常量(constant)”。
#
#
# # 10、__slots__魔法，减轻内存负担；__slots__来告诉Python不要使用字典，而且只给一个固定集合的属性分配空间。
# class MyClass(object):
#     __slots__ = ['name', 'identifier']  # 需要设置新属性的变量
#     def __init__(self, name, identifier):
#         self.name = name
#         self.identifier = identifier
#         self.set_up()
#
#
# # 11、虚拟环境(virtualenv)，使用virtualenv！针对每个程序创建独立（隔离）的Python环境，而不是在全局安装所依赖的模块。
# # 安装：pip install virtualenv
# # 创建：virtualenv myproject  # 不使用全局模块
# # 激活：source bin/activate
# # 创建使用系统全局模块：virtualenv --system-site-packages mycoolproject
# # 退出：deactivate
# # 先决定virtualenv是否使用系统全局的模块，默认情况下，virtualenv不会使用系统全局模块。
# # smartcd工具：帮助你管理你的环境，当你切换目录时，它可以帮助你激活（activate）和退出（deactivate）你的virtualenv。
#
#
# # 12、容器(Collections)模块功能较多，比较实用，可以多了解。
# # defaultdict：dict类型时，key不存在会报错；defaultdict不会报错；需要先导入collections类
# from collections import defaultdict
# colours = (
#     ('Yasoob', 'Yellow'),
#     ('Ali', 'Blue'),
#     ('Arham', 'Green'),
#     ('Ali', 'Black'),
#     ('Yasoob', 'Red'),
#     ('Ahmed', 'Silver'),
# )
# favourite_colours = defaultdict(list)
#
# # counter：Counter是一个计数器，它可以帮助我们针对某项数据进行计数。需要先导入collections类，统计方面经常用到，
# from collections import Counter
# colours = (
#     ('Yasoob', 'Yellow'),
#     ('Ali', 'Blue'),
#     ('Arham', 'Green'),
#     ('Ali', 'Black'),
#     ('Yasoob', 'Red'),
#     ('Ahmed', 'Silver'),
# )
# favs = Counter(name for name, colour in colours)
# print(favs)
#
# # deque：提供了一个双端队列，你可以从头/尾两端添加或删除元素。需要先导入collections类
# # 也可以限制这个列表的大小，当超出你设定的限制时，数据会从对队列另一端被挤出去(pop)。
# from collections import deque
# a = list(range(5))
# print(a)
# b = deque(a, maxlen=4)
# print(b)
# b.popleft()  # 最左边取出
# b.pop()      # 最右边取出
# print(b)
# b.extendleft([0])  # 最左边添加
# b.extend([6,7,8])  # 最右边添加
# print(b)
#
# # namedtuple：把元组变成一个针对简单任务的容器，不必使用整数索引来访问一个namedtuples的数据；可以像字典一样访问namedtuples，但namedtuples是不可变的。
# # 好处：
# # 1、元组名称和字段名称，使你的代码更易理解，元组直接有相应的名称；
# # 2、namedtuple的每个实例没有对象字典，所以它们很轻量，与普通的元组比，并不需要更多的内存，这使得它们比字典更快。
# # 3、可以将命名元组转换为字典
# from collections import namedtuple
# Animal = namedtuple('Animal', 'name age type')
# perry = Animal(name="Perry", age=31, type="cat")
# print(perry._asdict())
#
# # enum.Enum：枚举对象,一个变量有多重属性，如幼小的、小猫，Enums(枚举类型)基本上是一种组织各种东西的方式，导入enum类
# from collections import namedtuple
# from enum import Enum
# class Species(Enum):
#     cat = 1
#     dog = 2
#     horse = 3
#     aardvark = 4
#     butterfly = 5
#     owl = 6
#     platypus = 7
#     dragon = 8
#     unicorn = 9
#     kitten = 1  # (译者注：幼小的猫咪)
#     puppy = 2   # (译者注：幼小的狗狗)
# Animal = namedtuple('Animal', 'name age type')
# perry = Animal(name="Perry", age=31, type=Species.cat)
# drogon = Animal(name="Drogon", age=4, type=Species.dragon)
# tom = Animal(name="Tom", age=75, type=Species.cat)
# charlie = Animal(name="Charlie", age=2, type=Species.kitten)
# print(perry)
# print(drogon)
# print(tom)
# print(charlie)
# print(Species(1), Species['cat'], Species.cat)
#
#
# # 13、枚举(enumerate)是Python内置函数，允许我们遍历数据并自动计数，可选参数允许我们定制从哪个数字开始枚举。
# my_list = ['apple', 'banana', 'grapes', 'pear']
# for c, value in enumerate(my_list, 2):
#     print(c, value)
#
# my_list = ['apple', 'banana', 'grapes', 'pear']
# counter_list = list(enumerate(my_list, 1))
# print(counter_list)
#
#
# # 14、对象自省，自省(introspection)，在计算机编程领域里，是指在运行时来判断一个对象的类型的能力。
# # dir,返回一个列表，列出了一个对象所拥有的属性和方法.
# # type,返回一个对象的类型
# # id,返回任意不同种类对象的唯一ID.
# # inspect模块也提供了许多有用的函数，来获取活跃对象的信息:
# # getmembers:查看一个对象的成员.
# import inspect
# print(inspect.getmembers(str))
#
#
# # 15、异常
# # try/except从句：可能触发异常产生的代码会放到try语句块里，而处理异常的代码会在except语句块里实现。
# # except EOFError as e：处理单个异常，或多个异常，后面再加其他异常
# # except (IOError, EOFError) as e：使用元组将多个异常放在一起
# # except Exception:处理所有异常
#
# # try/except/finally从句,finally中的代码不管异常是否触发都将会被执行。这可以被用来在脚本执行之后做清理工作。
#
# # try/except/else/finally从句,else从句只会在没有异常的情况下执行，而且它会在finally语句之前执行。
#
#
# # 16、zip，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# # *zipped，与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# a = [1,2,3]
# b = [4,5,6]
# c = [4,5,6,7,8]
# d = zip(a,b)     # 打包为元组的列表
# print(list(d))
# zip(*d)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# print(list(zip(a,c)))   # 元素个数与最短的列表一致
#
#
# # 17、使用c扩展
# # CTypes模块，将C文件编译为.so文件(windows下为DLL)；下面操作会生成adder.so文件。
# # linux：gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c
# # mac：gcc -shared -Wl,-install_name,adder.so -o adder.so -fPIC add.c
# from ctypes import *
# adder = CDLL('./adder.so')
# # 一开始先导入ctypes模块，然后使用CDLL函数来加载我们创建的库文件。
#
#
# # 18、兼容python2和3
# # 1、Future模块导入，导入__future__模块。它可以帮你在Python2中导入Python3的功能。
# # 什么模块不支持，使用from __future__ import 模块名
# # ps：from __future__ import print_function
# # 2、模块重命名，import foo as foo，可以将功能不同但名字相同的模块重命名，这样都支持。
#
#
# # 19、协程，协程和生成器很相似但又稍有不同，生成器是数据的生产者 协程则是数据的消费者
# # 协程中包含的生成器并不是立刻执行，而是通过next()方法来响应send()方法。
# # 通过调用close()方法来关闭一个协程
# def grep(pattern):
#     print("1：", pattern)
#     while True:
#         line = (yield)
#         if pattern in line:
#             print(line)
# search = grep('coroutine')
# next(search)
# search.send("3")
# search.send("4")
# search.send("I love coroutine instead!")
# earch = grep('6')
# next(earch)
# search.close()
#
#
# # 20、函数缓存(Function caching)，函数缓存允许我们将一个函数对于给定参数的返回值缓存起来。
# # 当一个I/O密集的函数被频繁使用相同的参数调用的时候，函数缓存可以节约时间。
# # lru_cache的装饰器，允许我们将一个函数的返回值快速地缓存或取消缓存。
# from functools import lru_cache
# @lru_cache(maxsize=32)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)
# print([fib(n) for n in range(10)])
# fib.cache_clear()  # 清除缓存
#
#
# # 21、上下文管理器(Context managers)，上下文管理器允许你在有需要的时候，精确地分配和释放资源。
# # 使用上下文管理器最广泛的案例就是with语句了；
# # 想象下你有两个需要结对执行的相关操作，然后还要在它们中间放置一段代码。上下文管理器就是专门让你做这种事情的。
# # 上下文管理器的一个常见用例，是资源的加锁和解锁，以及关闭已打开的文件。
# with open('some_file', 'w') as opened_file:
#     opened_file.write('Hola!')
#
# # 基于类的实现，一个上下文管理器的类，最起码要定义__enter__和__exit__方法。
# class File(object):
#     def __init__(self, file_name, method):
#         self.file_obj = open(file_name, method)
#     def __enter__(self):
#         return self.file_obj
#     def __exit__(self, type, value, traceback):  # __exit__函数接受三个参数
#         self.file_obj.close()
# with File('demo.txt', 'w') as opened_file:
#     opened_file.write('Hola!')
# # 底层发送的过程
# # 1、with语句先暂存了File类的__exit__方法
# # 2、然后它调用File类的__enter__方法
# # 3、__enter__方法打开文件并返回给with语句
# # 4、打开的文件句柄被传递给opened_file参数
# # 5、我们使用.write()来写文件
# # 6、with语句调用之前暂存的__exit__方法
# # 7、__exit__方法关闭了文件
#
# # 处理异常，__exit__方法的这三个参数：type, value和traceback。
# # 在第4步和第6步之间，如果发生异常，Python会将异常的type,value和traceback传递给__exit__方法。
# # 当异常发生时，with语句会采取哪些步骤。
# # 1. 它把异常的type,value和traceback传递给__exit__方法
# # 2. 它让__exit__方法来处理异常
# # 3. 如果__exit__返回的是True，那么这个异常就被优雅地处理了。
# # 4. 如果__exit__返回的是True以外的任何东西，那么这个异常将被with语句抛出。
# # __exit__方法返回的是None(如果没有return语句那么方法会返回None)。因此，with语句抛出了那个异常。
#
# # 基于生成器的实现，可以用装饰器(decorators)和生成器(generators)来实现上下文管理器；contextlib模块专门用于这个目的。
# from contextlib import contextmanager
# @contextmanager
# def open_file(name):
#     f = open(name, 'w')
#     yield f
#     f.close()
# # 1. Python解释器遇到了yield关键字。因为这个缘故它创建了一个生成器而不是一个普通的函数。
# # 2. 因为这个装饰器，contextmanager会被调用并传入函数名（open_file）作为参数。
# # 3. contextmanager函数返回一个以GeneratorContextManager对象封装过的生成器。
# # 4. 这个GeneratorContextManager被赋值给open_file函数，我们实际上是在调用GeneratorContextManager对象。
# # 可以用这个新生成的上下文管理器了：
# with open_file('some_file') as f:
#     f.write('hola!')
#
#
#
# # 22、多线程类似于同时执行多个不同程序，多线程运行有如下优点：
# # 使用线程可以把占据长时间的程序中的任务放到后台去处理。
# # 用户界面可以更加吸引人，比如用户点击了一个按钮去触发某些事件的处理，可以弹出一个进度条来显示处理的进度。
# # 程序的运行速度可能加快。
# # 在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程就比较有用了。
# # 每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口
#
# # threading 模块
# # Python中使用线程有两种方式：函数或者用类来包装线程对象。
# # threading.currentThread(): 返回当前的线程变量。
# # threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# # threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
# # run(): 用以表示线程活动的方法。
# # start():启动线程活动。
# # join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
# # isAlive(): 返回线程是否活动的。
# # getName(): 返回线程名。
# # setName(): 设置线程名。
#
# import threading
# import time
# exitFlag = 0
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print('开始线程：' + self.name)
#         print_time(self.name, self.counter, 5)
#         print("退出线程：" + self.name)
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print("%s: %s"%(threadName, time.ctime(time.time())))
#         counter -= 1
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("退出主线程")
#
#
# # 23、JSON操作
# # json.dumps(): 对数据进行编码。
# # json.loads(): 对数据进行解码。
# # json.dump(): 对json文件进行编码。
# # json.load(): 对json文件进行解码。
#
#
# # 24、日期和时间， time 和 calendar 模块可以用于格式化日期和时间。
# # time模块
# # time:时间戳
# # localtime:获取当前时间，以时间元组的形式
# # asctime：获取格式化的时间
# # strftime(format,t):格式化日期，format格式化格式，t时间
# # strptime(t,format)：根据fmt的格式把一个时间字符串解析为时间元组。
# # time.mktime():转换为时间戳
# # time.mktime(strptime(t,format)):将格式字符串转换为时间戳
# # time.perf_counter()：返回系统运行时间
# # time.process_time():返回进程运行时间
# # sleep():推迟调用线程的运行，简单说睡眠时间
# # time.clock()：浮点数秒数，用于衡量不同程序的耗时，前后两次调用的时间差
#
# import time
# ticks = time.time()
# print ("当前时间戳为:", ticks)
# localtime = time.localtime(time.time())
# print ("本地时间为 :", localtime)
# localtime = time.asctime( time.localtime(time.time()))
# print("本地时间为 :", localtime)
# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# a = "Sat Mar 28 22:24:24 2016"
# print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
#
# import time  # 进度条
# scale = 50
# print("执行开始".center(scale//2,"-"))  # .center() 控制输出的样式，宽度为 25//2，即 22，汉字居中，两侧填充 -
# start = time.perf_counter() # 调用一次 perf_counter()，从计算机系统里随机选一个时间点A，计算其距离当前时间点B1有多少秒。当第二次调用该函数时，默认从第一次调用的时间点A算起，距离当前时间点B2有多少秒。两个函数取差，即实现从时间点B1到B2的计时功能。
# for i in range(scale+1):
#     a = '*' * i             # i 个长度的 * 符号
#     b = '.' * (scale-i)  # scale-i） 个长度的 . 符号。符号 * 和 . 总长度为50
#     c = (i/scale)*100  # 显示当前进度，百分之多少
#     dur = time.perf_counter() - start    # 计时，计算进度条走到某一百分比的用时
#     print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')  # \r用来在每次输出完成后，将光标移至行首，这样保证进度条始终在同一行输出，即在一行不断刷新的效果；{:^3.0f}，输出格式为居中，占3位，小数点后0位，浮点型数，对应输出的数为c；{}，对应输出的数为a；{}，对应输出的数为b；{:.2f}，输出有两位小数的浮点数，对应输出的数为dur；end=''，用来保证不换行，不加这句默认换行。
#     time.sleep(0.1)     # 在输出下一个百分之几的进度前，停止0.1秒
# print("\n"+"执行结果".center(scale//2,'-'))
#
# # Calendar 模块有很广泛的方法用来处理年历和月历
# # calendar.calendar(year,w=2,l=1,c=6)：返回年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
# # calendar.month(year,month,w=2,l=1)：返回月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
# # calendar.isleap(year)：是闰年返回 True，否则为 false。
# # calendar.weekday(year,month,day)：返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
#
# import calendar
# cal = calendar.month(2016, 1)
# print("以下输出2016年1月份的日历:" + cal)
#
#
# # 25、内置函数
# setattr(object, name, value)：设置属性值，该属性不一定是存在的。
# getattr(object, name[, default])：返回一个对象属性值，没有时触发AttributeError错误。反射机制
#
# all()：判断给定的可迭代参数iterable中的所有元素是否都为TRUE，如果是返回 True，否则返回 False。
# 元素除了是 0、空、None、False 外都算 True；空元组、空列表返回值为True。
# any(iterable)：如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true。
#
# next(iterable[, default])：返回迭代器的下一个项目，第二个参数可选防止触发异常。
# iter(object[, sentinel])：生成迭代器，将可迭代的对象转换为Iterator迭代对象。
#
# sort（iterable, key=None, reverse=False）：对列表进行排序，reverse = True 降序 ， reverse = False 升序（默认）
# sorted(iterable, key=None, reverse=False)：对所有可迭代的对象进行排序操作；reverse = True 降序 ， reverse = False 升序（默认）
#
# ascii(object)：ascii() 函数类似 repr() 函数, 返回一个表示对象的字符串, 但是对于字符串中的非 ASCII 字符则返回通过 repr() 函数使用 \x, \u 或 \U 编码的字符。
# repr(object)：将对象转化为供解释器读取的形式，返回一个对象的 string 格式。

# slice(start, stop[, step])：实现切片对象，主要用在切片操作函数里的参数传递。
# divmod(a, b)：返回一个包含商和余数的元组(a // b, a % b)。
# id([object])：获取对象的内存地址。
# enumerate(sequence, [start=0])：枚举，将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# python staticmethod：返回函数的静态方法。
# class C(object):
#     @staticmethod
#     def f():
#         print('runoob')
# C.f()  # 静态方法无需实例化
# cobj = C()
# cobj.f()  # 也可以实例化后调用

# eval(expression[, globals[, locals]])：执行一个字符串表达式，并返回表达式的值。
# exec(object[, globals[, locals]])：执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码。

# isinstance(object, classinfo)：判断一个对象是否是一个已知的类型，类似 type()。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
# type() 不会认为子类是一种父类类型，不考虑继承关系；一个参数返回对象类型, 三个参数，返回新的类型对象。
# type(object)/type(name, bases, dict)

# # bin()：返回一个整数 int 或者长整数 long int 的二进制表示。
# # hex()：将一个指定数字转换为 16 进制数。
# # oct()：将一个整数转换成 8 进制字符串，8 进制以 0o 作为前缀表示。
# ord(c)：是 chr() 函数（对于 8 位的 ASCII 字符串）的配对函数，它以一个字符串（Unicode 字符）作为参数，
# 返回对应的 ASCII 数值，或者 Unicode 数值。返回值是对应的十进制整数。
# chr(i)：返回一个对应的字符；i -- 可以是 10 进制也可以是 16 进制的形式的数字，数字范围为 0 到 1,114,111 (16 进制为0x10FFFF)。
# bytearray([source[, encoding[, errors]]])：返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
# 如果 source 为整数，则返回一个长度为 source 的初始化数组；
# 如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
# 如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
# 如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
# 如果没有输入任何参数，默认就是初始化数组为0个元素。
# class bytes([source[, encoding[, errors]]])：返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。它是 bytearray 的不可变版本。

# map(function, iterable, ...)：根据提供的函数对指定序列做映射；第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
# filter(function, iterable)：参数1：函数:2：序列；过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象
# Reduce：当需要对一个列表进行一些计算并返回结果时，Reduce 是个非常有用的函数

# pow(x, y[, z])：计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z

# super(type[, object-or-type])：调用父类(超类)的一个方法
# callable()：检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功。
# issubclass(class, classinfo)：判断参数 class 是否是类型参数 classinfo 的子类。
# property()：是在新式类中返回属性值。
# class C(object):
#     def __init__(self):
#         self._x = None
#     def getx(self):
#         return self._x
#     def setx(self, value):
#         self._x = value
#     def delx(self):
#         del self._x
#     x = property(getx, setx, delx, "I'm the 'x' property.")

# frozenset()：返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
# 在集合的关系中，有集合的中的元素是另一个集合的情况，但是普通集合（set）本身是可变的，
# 那么它的实例就不能放在另一个集合中（set中的元素必须是不可变类型）。

# vars()：返回对象object的属性和属性值的字典对象。

# classmethod 修饰符，类似装饰器，对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，
# 可以来调用类的属性，类的方法，实例化对象等。

# locals():会以字典类型返回当前位置的全部局部变量。
# 对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
# globals():会以字典类型返回当前位置的全部全局变量。

# zip，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# *zipped，与 zip 相反，*zipped 可理解为解压，返回二维矩阵式

# compile(source, filename, mode[, flags[, dont_inherit]])：将一个字符串编译为字节代码。
# source -- 字符串或者AST（Abstract Syntax Trees）对象。。
# filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
# mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
# flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
# flags和dont_inherit是用来控制编译源码时的标志
# str = "3 * 4 + 5"
# a = compile(str,'','eval')
# print(a, eval(a))

# reversed(seq):返回一个反转的迭代器。seq -- 要转换的序列，可以是 tuple, string, list 或 range。
# seqString = 'Runoob'
# print(list(reversed(seqString)))

# __import__(name[, globals[, locals[, fromlist[, level]]]]):动态加载类和函数;如果一个模块经常变化就可以使用 __import__() 来动态载入。















#
#
# # 26、MySql
# mysql - connector驱动器来连接使用MySQL；python -m pip install mysql-connector
# import mysql.connector，导入检测是否安装成功

#
# # 27、OS操作


# # 28、正则表达式、线程、CGI编程、网络编程、SMTP发送邮件、XML解析


# # 

















