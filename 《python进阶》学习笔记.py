# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 22:55:20 2018

@author: Administrator
"""
# =============================================================================
# *args 和 **kwargs
# =============================================================================
#其实并不是必须写成*args 和**kwargs。 只有变量前面的 *(星号)才是必须的. 
#你也可以写成*var 和**vars. 而写成*args 和**kwargs只是一个通俗的命名约定。 
def test_args_kwargs(*args,**kwargs ):
    print("arg:", args)
    print("kwargs:", kwargs)

def another_test_args_kwargs(*var,**vars):
    print("var:", var)
    print("vars:", vars)
# 这两种写法是一样的
 test_args_kwargs(test, name = 'xxx')
 another_test_args_kwargs(test, name = 'xxx')
 # 两种写法运行效果完全一样，所以以后你不用纠结*args 和 **kwargs了


# =============================================================================
# *args 的用法
# =============================================================================
# *args是用来发送一个非键值对的可变数量的参数列表给一个函数.
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')

# =============================================================================
# **kwargs 的用法
# =============================================================================
# 允许你将不定数量的键值对, 作为参数传递给一个函数。
# 如果你想要在一个函数里处理带名字的参数, 你应该使用**kwargs。
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))

greet_me(name="yasoob")
greet_me(name="yasoob",age=3) # 因为不定数量的，你也可以给两个，也能传进去

# =============================================================================
# #使用 *args 和 **kwargs 来调用函数
# =============================================================================
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
    
# 你可以使用*args或**kwargs来给这个小函数传递参数。
args = ("two", 3, 5)
test_args_kwargs(*args)

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)

# 标准参数与*args、**kwargs在使用时的顺序
some_func(fargs, *args, **kwargs) # 你可以在函数里里面同时使用这三种参数

# =============================================================================
# map函数 ：Map会将一个函数映射到一个输入列表的所有元素上。
# =============================================================================
# 计算list每个元素的平方：
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

# map还能对多个函数列表进行映射
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)
def three(x):
    return (x*3)

funcs = [multiply, add,three]
for i in range(5):
    value = map(lambda x: x(i), funcs) #将i同时映射到3个函数里进行运算
    print(list(value))
    
# =============================================================================
# Filter：过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表
# =============================================================================
number_list = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, number_list)
print(list(less_than_zero))  

# =============================================================================
# reduce()函数: 会对参数序列中元素进行累积。先对集合中的第 1、2 个元素进行操作，
# 得到的结果再与第三个数据用 function 函数运算，直到最后得到一个结果
# ==============================================================================
from functools import reduce
product = reduce( (lambda x, y: x * y), [1, 2, 3, 4] )

# =============================================================================
# 条件表达式（三元运算符）
# =============================================================================
# 格式如下：condition_is_true if condition else condition_is_false
is_fat = True
state = "fat" if is_fat else "not fat"

condition = True
print(2 if condition else 1/0)

# =============================================================================
# 装饰器（Decorators）
# =============================================================================

# 在理解装饰器之前先要具备一些函数进阶知识：
def hi(name="yasoob"):  # 定义一个带默认参数的函数
    return "hi " + name
hi()

# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi 
greet()     # greet()的执行效果和hi()是一样的

del hi  # 然后删除hi()
hi()    # 执行hi()报错了，因为已经删除
greet() # 但是greet()还是能执行
del greet

# 函数嵌套：在函数里定义函数
def hi(name="yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")

hi()
greet()     
welcome()   #但是你不能执行greet() 和 welcome()因为他们是函数内定义的函数

# 从函数中返回函数
def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome    
a = hi()
print(a)    # 可以看到a是函数greet
a()     #a是可以执行的，a()表示运行a

a = hi(name = "ali")    # 换个name参数看什么效果 
print(a)    # 可以看到，因为 name = ali，所以返回了函数 welcome
a() 

hi()()   #还能玩出花样
         #第一次执行，因为name默认值是'yasoob',所以返回了函数greet，
         # 第二个圆括号表示：执行函数greet，输出'now you are in the greet() function'

# 将函数作为参数传给另一个函数
def hi():
    return "hi yasoob!"

def doSomethingBeforeHi(func):      # 函数的参数是一个函数
    print("I am doing some work before executing hi()") 
    print(func())       # 执行输入函数，打印结果

doSomethingBeforeHi(hi)


# 现在你已经具备所有必需知识，来进一步学习装饰器真正是什么了。
# 装饰器让你在一个函数的前后去执行代码。
def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs decoration")

a_function_requiring_decoration()   # 未经装饰的函数
# 装饰一下
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration) 
a_function_requiring_decoration()   # 装饰过的函数，执行效果不一样了

# 装饰器语法糖
@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print('I am the function which needs  decoration!')

a_function_requiring_decoration() # 执行显示函数也被装饰过了
print(a_function_requiring_decoration.__name__) # 但是连函数名字也变成装饰器的名字了，

# functools.wraps：将原函数的参数拷贝过来，避免被装饰器修改掉
from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func) # 将原函数的参数拷贝过来
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print('I am the function which needs decoration')

print(a_function_requiring_decoration.__name__) # 这次没错了

# 一个规范的装饰器写法：
from functools import wraps

def decorator_name(f): # 这是一个判断函数是否能够运行的装饰器
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
func()

can_run = False
func()

# 装饰器的使用场景1：授权(Authorization)
from functools import wraps

def requires_auth(f):  # 检查某个人是否被授权去使用一个web应用
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated

# 装饰器的使用场景2：日志(Logging)
from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x

result = addition_func(4)

# 装饰器的使用场景3：在函数中嵌入装饰器
from functools import wraps

def logit(logfile=r'D:\out.log'):  # 运行函数并记录log 
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()


# 类装饰器

#类也可以用来构建装饰器
from functools import wraps

class logit(object):    # 运行函数并记录log，也可以附件一些邮件通知等功能
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        # logit只保存日志，不做别的，所以这里不写了，当然也可以添加功能
        pass

@logit()
def myfunc1():
    pass
myfunc1()

# 下面如果要实现邮件通知的功能，可以重新写一个子类
class email_logit(logit): #子类从logit类继承
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''
    def __init__(self,email='admin@myproject.com',*args,**kwargs,):
        self.email = email
        super(email_logit, self).__init__(*args,**kwargs)

    def notify(self):
        print('发送邮件给self.email')

@email_logit()
def myfunc1():
    pass
myfunc1()


# =============================================================================
# 可变对象(Mutation) 
# =============================================================================
def add_to(num, target=[]):
    target.append(num)
    return target
add_to(1)
add_to(2)
add_to(3)   # 怎么返回[1, 2, 3]，target=[]不是被默认为空了吗？
# 在Python中当函数被定义时，默认参数只会运算一次，而不是每次被调用时都会重新运算。
# 永远不要定义可变类型的默认参数(诸如list之类)

def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target
add_to(42)
add_to(42)
add_to(42) # 当你运行add_to()不传入target参数是，targert就是None，空列表就会被创建

# =============================================================================
#  容器 (Collections)
# =============================================================================

#defaultdict
from collections import defaultdict
colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)
favourite_colours = defaultdict(list)
for name, colour in colours:
    favourite_colours[name].append(colour)
print(favourite_colours)

some_dict = {}
some_dict['colours']['favourite'] = "yellow"    # 嵌套赋值导致dict报错

import collections
tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"
import json
print(json.dumps(some_dict))

# counter
from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)    # 每个人喜欢集中颜色 
print(favs)

favs = Counter(colour for name, colour in colours)   # 每种颜色出现了几次
print(favs)

with open('filename', 'rb') as f:   # 统计文件行数
    line_count = Counter(f)
print(line_count)

# deque ：双向队列，你可以从头/尾两端添加或删除元素。
from collections import deque
d = deque()     # 它的用法就像python的list
d.append('1')
d.append('2')
d.append('3')

d = deque(range(5))
print(d)
d.popleft()     # 从右侧删除元素
d.pop()     # 从右侧删除元素
print(d)
d = deque(maxlen=10)  # 可以限制这个列表的大小，当超出限制，数据会从对队列另一端被挤出去pop
d.extend([1,2,3,4])
d.extendleft([0])
d.extend([5,6,7,8,9])
print(d)
d.append(10)
print(d)    # 0被从左边挤出去了
d.appendleft(0)
print(d)    # 这次10被从右边挤出去了

# namedtuple :可以像字典(dict)一样访问namedtuples，但namedtuples是不可变的。
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry)
print(perry.name)

perry.age = 42      # 报错，元组的元素是不可修改的

print(perry[0])     # 命名元组又是后向兼容元组的
print(perry[1])

print(perry._asdict())  # 另外他可以直接转成字典

# =============================================================================
# enumerate （枚举） ：接收一个可迭代对象，返回它的序号和元素组成的二元组
# =============================================================================

my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 2):  # 第二个数字参数是可选的，表示序号从几开始
    print(c, value) 

my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))   # 可以创建一个元组list
print(counter_list)  

# =============================================================================
#  对象自省
# =============================================================================

# dir :列出了一个对象所拥有的属性和方法
dir(my_list)
help(my_list.append)    # 通常我们会和help一起使用，获取相应方法的帮助
help(my_list.sort)

# type和id 返回对象的类型，内存地址
print(type(''))
print(type([]))
print(type({}))
print(type(dict))
name = "Yasoob"
print(id(name))

# inspect模块：提供了许多有用的函数，来获取活跃对象的信息
import inspect
print(inspect.getmembers(str))      # 查看一个对象的成员

# =============================================================================
# 推导式 Comprehension
# =============================================================================

# 列表(list)推导式 ：简明的方法来创建列表

multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)

squared = []    # 创建一个平方列表
for x in range(10):
    squared.append(x**2)

squared = [x**2 for x in range(10)]     #推导式写法更简洁易读


# 字典（dict）推导式

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}   # 合并字典中的大小写key

new_dict = {v:k for k,v in mcase.items()}  #键值快速互换

# 集合(set)推导式 

squared = {x**2 for x in [1, 1, 2]}     # 与列表基本相同，使用大括号
print(squared)

# =============================================================================
# 异常处理 ：try/except 语句
# =============================================================================

try:     # 处理一个IOError的异常
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))    
    

try:  # 处理多个异常
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # 这里的代码只会在try语句里没有触发异常时运行,
    # 但是这里的异常将 *不会* 被捕获
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')
    
# =============================================================================
# 一行式
# =============================================================================

# 文件夹共享
# 在文件夹目录下执行
python -m http.server    

# 漂亮的打印
from pprint import pprint
my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
pprint(my_dict)

# 从文件打印出json数据
cat file.json | python -m json.tool

# 脚本性能分析
python -m cProfile my_script.py

# CSV转换为json
# csv_file.csv为你要转换的文件
python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"

# 列表碾平
# 使用itertools包中的itertools.chain.from_iterable
import itertools
a_list = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a_list)))

print(list(itertools.chain(*a_list))) # 这里的*表示解压缩


# =============================================================================
# For - Else 语句
# =============================================================================

# for循环还有一个else从句,else从句会在循环正常结束没有遇到任何break时执行。
for item in container:  # 从一个迭代器里面找某个元素，如果找到就中断，找不到就执行另一个操作 
    if search_something(item):
        # Found it!
        process(item)
        break
else:
    # Didn't find anything..
    not_found_in_container()

# 找出2-10之间的数字的因数
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', int(n/x))
            break    
# 我们可以加上一个附加的else语句块，来抓住质数
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', int(n/x))
            break    
    else:
        # 当循环正常结束还找找不到满足条件的因数，则这个数就是质数
        print(n, 'is a prime number')           

# =============================================================================
# open函数
# =============================================================================
f = open('photo.jpg', 'r+')
jpgdata = f.read()
f.close()   # 只有在read成功的情况下close才会被执行

with open('photo.jpg', 'r+',encoding = 'utf-8' ) as f:  # 正确的写法
    jpgdata = f.read()
# 如果你想读取文件，传入r
# 如果你想读取并写入文件，传入r+
# 如果你想覆盖写入文件，传入w  
# 如果你想在文件末尾附加内容，传入a    

# 读取一个文件，检测它是否是JPG（提示：这些文件头部以字节FF D8开始）
import io
with open('photo.jpg', 'rb') as inf:
    jpgdata = inf.read()

if jpgdata.startswith(b'\xff\xd8'):
    text = u'This is a JPEG file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

with io.open('summary.txt', 'w', encoding='utf-8') as outf:
    outf.write(text % len(jpgdata))
    

