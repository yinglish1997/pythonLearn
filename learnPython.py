#encoding:utf-8
# created by YingYing

# 一、python初探
'''
动态语言（能够在运行时修改自身程序结构的语言），是一种很高级的语言，抽象程度高。
冒号：表示代码头和接下来即将是代码块。分号；表示一个语句的结束。
'''
''''''
a = 9
b = 2
a, b = b, a
print a, b  # 2 9

# python以缩进识别代码块。
n = 4
if n > 3:
    print "bigger"
    print "really bigger"
else:
    print "smalleer"

if n > 7:
    print "bigger"
print "anyway, this sentence will appear"


# 二、python基本数据类型
# 序列：成员是有序排序，并且可以通过下标偏移量访问它的成员。包括：字符串，列表，元组
# 2.1字符串
# 创建
aString = 'hello word'
bString = "tomorrow"
listString = str(range(4)) # range(x):1~ x-1
print listString
# [0, 1, 2, 3]

# 截取：单个截取和切片。负号表示从右边开始数
print aString[1]
print aString[-1]
print bString[1:5]
print bString[-3:-2] # -3 -3
print aString[0:6] + bString

# 转义字符\
print 'he said \'nice to meet you\''

print '\"I have a dream\"'

print '\\'
# 用r''表示''内部的字符串默认不转义
print r'"I hope you all can learn""have a good time"'


# 成员操作符：in/not in
if 'you' in 'iloveyou':
    print 'yes'

# 格式化，%也称占位符。%s表示用字符串替换，%d表示用整数替换
print 'hi, %s' % 'Mike'
print '%s told %s to wash the cloth' % ('lily', 'Mike')

# 常见字符串函数
print len('nothingToSay')
print 'what'.upper()
print 'OK'.lower()
print 'I am you'.replace('I', 'He')


# 2.2列表list

# 创建：中括号来定义，或者工厂方法。相比于数组，列表允许其中元素类型不一。
aList = ['multiplied', 12, 'to', [1, 2], 'will get what']
print aList
print list('name')  # ['n', 'a', 'm', 'e']

# 访问，同字符串一样，可以通过下标和切片取值
print aList[1]
print aList[2:]
print aList[3][1]

# 修改。！列表是可变序列！可以直接指定下标修改，可以用append()追加，可以用insert
aList[0] = 'add'
print aList
aList.append([13, 14])
print aList
aList.insert(1, 8)
print aList

# del(index) remove(element)
del aList[1]
print aList
aList.remove('to')
print aList

# 连接操作符+：注意只能连接相同类型的对象，比如说我们不能通过加号为列表添加一个字符串
firstList = ['cool']
secondList = ['wonderful']
print firstList + secondList

# 重复操作符*
print [1, 2, 3] * 2

# 序列类型函数
numList =[8,2,1,5]
print sorted(numList)
print min(numList)
print max(numList)
for i in reversed(numList):
    print i,

# 2.3元组
'''
元组和列表最大的区别就是，元组是不可变类型。同时元组用小括号括起来表示。
和列表一样，元组可以通过直接和工厂方式创建，通过下标和切片访问，通过加号连接，乘号重复其数据
但是要注意，由于元组是不可变的，所以它不存在排序，替换，添加方法。我们也不可能通过切片进行右边
赋值。
元组的不可变性是为了数据的安全性。
'''
tuple = (123, 'abc', 4.33, ['inner', 'tuple'])
# 注意!如果元组里面只有一个元素，要加逗号，不然会被当做普通数据类型
oneElement = (123,)
if 123 in tuple:
    print 'yes'


# 2.4字典
'''
映射类型：不要求用数字做索引从一个容器获取对应的数据项。数据项呈“键值对”的形式。
键可以是数字，字符串，元组。键一定是不可变对象。（前面讲到的列表就属于可变对象）
键是唯一的，值可以重复。
'''
# 创建
items = [('name', 'Mike'), ('age', '20')]
itemDict = dict(items)

list = ([20, 'age'], ['Mike', 'name'])
ddict = dict(list)

dict = {'name': 'YingYing', 'password': 233}

emptyDict = {}
# 内建函数fromkeys，提供键，创建具有相同值的字典，默认情况下其值为none
fDict = {}.fromkeys(('id', 'score'))
print fDict
formDict = {}.fromkeys(('x', 'y'), (-1, -2))
print formDict
# {'score': None, 'id': None} {'y': (-1, -2), 'x': (-1, -2)}

# 访问 通过keys()或者values()可以取到所有键或者值
for key in dict.keys():
    print key
    for value in dict.values():
        print value

if 'name' in ddict.values():
    print 'name in ddict'
# has_key也可以判断键是否在字典中，但是，当然啦，只能检查键而不能检查值
print ddict.has_key(20)

# 通过键取值
print itemDict['name']
print itemDict.get('name')
# 修改，键是唯一的，值可以重复或者改变，删除一个键值对用del，删除字典中所有项用.clear()
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除。不支持连接和重复操作
itemDict['name'] = 'Lily'
del itemDict['name']
itemDict.clear()

# 格式化
dict = {'name': 'shaBi', 'age': 20}
print 'I have a friend named %(name)s, he is %(age)s years old' % dict

# 2.5集合set
'''
set与dict相似，也是一组键的集合，但是它不存储值。相当与我们数学中的无序不重复集合.
所以它会有集合的交并差操作。
如果放入相同的键，会自动去重。
基本功能包括关系测试和去重。
'''

# 创建
print set('abcd')  # set(['a', 'c', 'b', 'd'])
print set(['nice', 'to', 'meet', 'to'])

# 修改 add remove
# 取交集 &； 取并集 |；做差 -
firstSet = set(1, 2, 3)
secondSet = set(3, 4, 5)
print firstList & secondList
print firstList | secondList
print firstList - secondList

# 三、基本语法
'''

'''
num = 9
# 3.1 if语句
if num < 10:
    print 'num is smaller than ten'

# 3.2 while循环
while num > 5:
    print num,
    num = num - 1
print ''

# 3.3 for循环和range()内建函数
for word in ['python', 'is', 'cool']:
    print word,
print

for num in range(5):
    print num,
print

# 列表解析：可以在列表中做复杂筛选
print [x * x for x in range(4)]
print [x + 2 for x in range(6) if x % 2]

# break跳出当前循环
for k in range(5):
    if k == 2:
        break
    else:
        print k,
    k = k -1
print  # 0 1

# continue跳出本层循环
for k in range(5):
    if k == 2:
        continue
    else:
        print k,
    k = k -1
print  # 0 1 3 4

# pass标识可以暂时不进行操作的部分
if 8 > 9:
    pass

# 3.4 函数
# 函数是对程序逻辑进行结构化或者过程化的一种编程方法

# 3.4.1内置函数：
print abs(-2)
# cmp(a, b) if a<b,return -1, if a>b,return 1, if a=b, return 0
print cmp(1, 2),cmp(2, 1),cmp(3, 3)
# 强制类型转换int() float() bool() str()
print int("123")

# 3.4.2 定义函数：用def定义，依次写函数名，括号，括号内参数和冒号，在缩进块中写函数体，return返回值
def my_abs(a, b):
    if a > b:
        return 1
    else:
        if a < b:
            return -1
        else:
            return 0
print my_abs(7, -4)

# 3.4.3 函数参数：默认参数
def power(x, n =2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s
# 默认情况下n为2，除非显式传入值。
print power(2), power(2, 4)
# 如果有多个默认参数，如需赋值，一般按照参数顺序设置。如果只要赋给个别默认参数，写上参数名
def register(name, pwd, city='GuangZhou', level='member'):
    print name, city, level

register('Mike', '123', level='senior')

# 可变参数：即传入的参数个数可变，在变量名前加*。函数内部把这些可变参数做元组处理
def calc(*number):
    sum = 0
    for n in number:
        sum += n
    return sum
print calc(1,2,3), calc(4,5,6,7)

# 关键字参数：允许传入0或任意个含参数名的参数，这些参数在函数内部自动组装成一个dict
def person(name, age, **otherInformation):
    print 'name is ', name, ', aged ', age, ', other: ', otherInformation.keys(), ':',otherInformation.values();

person('xiaoMing', 18, local='GuangZhou')

# 可以传入任意个键值对。同时，下面这个例子也说明，可以把字典转化为关键字参数传入
kw = {'love':'july', 'salary': 30000}
person('Mike', 30, love = kw['love'], salary = kw['salary'])
# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

# 闭包
# 先来看一段简单的代码
def add():
    a = 2
    b = 5
    def func(c):
        return a*c + b
    return func
a = add()
print a  # <function func at 0xb6f2e374>
a(5)
print a(5)  # 15
'''
在函数func里面用到了外面的参数a, b（称为函数的环境变量）。像这样，函数与其环境变量就构成了闭包。
简单地理解呢，就是嵌套函数。
当我们调用外层函数时，返回内层函数，并不立刻马上进行计算啊操作啊等等。只要我们再调用一次，才会操作。
所以当我们调用add()时，返回给a的是一个function，只有向a传递参数时才执行func()函数
'''

# 装饰器
'''
好了，了解闭包后我们就可以涉及一下装饰器了。所谓装饰器就是实现一些小功能（比如在函数操作前后输出打印点什么），
又能不让代码嵌入其中。通常我们用＠语法把装饰器，就是实现小功能的函数放在另一个函数的上一行。
'''
def log(func):
    def wrapper():
        print 'call %s()' % func.func_name
        return func()
    return wrapper

@log
def now():
    now.func_name = 'now'
    print '2017-4-22'

now()

# 3.5类
# 简要讲解面向对象编程
class student():  # 类定义：类名通常首字母大写
    def __init__(self, name, score):  # 定义构造器
        self.name = name
        self.score = score
    def printIntroduction(self):  # 定义方法
        print 'student ', self.name, '\'s score is ', self.score

st = student('Mike', 90)  # 实例化
st.printIntroduction()  # 调用方法

# 访问权限：如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
class user():
    def __init__(self, userName, usePwd):
        self.userName = userName
        self.__userPwd = usePwd
    def getPwd(self):
        return self.__userPwd

aUser = user('Mike', 345)
print aUser.userName
print aUser.getPwd()
# 由此也引出了面向对象编程的第一个特性：封装。封装就是将抽象得到的数据和行为相结合，形成一个有机的整体，即类。
# 封装的目的是增强安全性和简化编程，使用者不必了解具体的实现细节，而只是要通过外部接口，一特定的访问权限来使用类的成员。

# 用下面的代码演示继承和多态。
# 继承：子类衍生于父类，父类也称基类/超类。子类可以使用父类的方法。
# 多态：最常见的一种形式就是，子类中存在与父类一样的方法（方法名和参数列表都一样），初始化的是子类，则调用子类的方法。
class people():
    def __init__(self, name, hair, height):
        self.name = name
        self.hair = hair
        self.height = height
    def printName(self):
        print 'my name is ', self.name
    def printHair(self):
        print 'I have hair'
    def printHeight(self):
        print 'I have height'

Mike = people('Mike', 'short', 'tall')
Mike.printName()

class boy(people):
    '''
    def printName(self):
        print 'I have my own name, my name is ', self.name    
    '''

Mike = boy('Mike', 'short', 'tall')
Mike.printName()


# 四、高级操作
# 4.1异常处理
'''
高级语言一般都内置有try...except...finally...的错误处理方法
当我们任务某些代码可能有错时，可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，
而是直接跳转至错误处理代码，即except语句块，执行完except后，
如果有finally语句块，则执行finally语句块，至此，执行完毕。
如果不确定是什么错误，可以这样写：
    except Exception as e:
        print e.message
'''
def division():
    try:
        x = input('Enter the first number: ')
        y = input('the second one: ')
        print x/y
    except ZeroDivisionError:
        print "The second number cannot be zero!"
    finally:
        print 'whatever success or fail, this sentence will appear'

division()

'''
try语句块中异常点之后的代码是不会被执行到的，一旦出现错误，就会在本函数中查找差错处理方法。
如果在本函数中找不到，那么异常就会移交给上一个调用者。如下面的例子中，division()中有自己的处理，
则进行自我处理，否则，将会调用user()的差错处理
'''
def user():
    try:
        division()
    except Exception as e:
        print 'user()'
        print e.message

user()

# 4.2文件读写

# 4.2.1读文件 r means 'read'
file = open('/home/yingying/桌面/jsFile.java', 'r')
for line in file.read():
    print line

# read() 一次读取整个文件，将文件内容放到字符串变量中
# readline() 一次只读取一行
# readlines() 一次读取整个文件，将文件内容分析成行的列表，可以通过for..in...打印出一行一行
print '0:',file[0], ', 2:', file[2], ', -1:', file[-1]  # file[-1]='\n' 每一行的结尾都是有一个换行符的存在的
print file.readline()  #
print file.readlines()  # ['first line\n', 'second line\n', 'third line\n', 'fouth line\n']
# with语句：可以省略file.close()
with open('pathToFile') as file:
   for line in file.readlines():
       print line.strip()  # 去除掉换行符


# 4.2.2写文件 w means 'write'
# success 将会覆盖原文件内容，如果想要的是在原内容上追加而不是覆盖，用'a'(means append)
# open中其他的模式参数还包括 b二进制模式，'rb''wb'; + 读/写模式，'r+'可读的同时也是可写的
with open('/home/yingying/桌面/jsFile.java', 'w') as writeFile:
    writeFile.write('success')


# 五、python相关包
'''
python-pip: 安装和管理python包的工具。 安装：http://www.ttlsa.com/python/how-to-install-and-use-pip-ttlsa/
结巴分词jieba： 安装使用：https://github.com/fxsjy/jieba
Numpy：是Python的一个科学计算的库，提供了矩阵运算的功能  
     安装：http://www.cnblogs.com/zhizhan/p/4605538.html
     使用：http://old.sebug.net/paper/books/scipydoc/numpy_intro.html
'''
# import numpy as np

# 六、github的使用：实践
'''
git和github的关系就像本地的百度云盘和云盘。
首先在自己的机子上安装git：
sudo apt-get install git
接着配置：
git config --global user.name "yinglish1997"
git config --global user.email "yinglish@foxmail.com"
这些设置可以在配置文件中找到：
sudo gedit  ~/.gitconfig
在github的网页上创建一个仓库MovieGraph
复制到本地机上来：
git clone http://github.com/yinglish1997/MovieGraph
这样在自己的机子上就会一个文件夹MovieGraph，然后把想要放上去的代码文件拷贝过去，拷贝完后还有add
cd MovieGraph/
git add CreateGraph.java
git add MovieGraph.java
git add ReadGraph.java
通过git add 命令将文件放入暂存区，再通过 git commit 提交
git commit -m "备注"
最后push一下，github上的仓库就会被刷新
git push
然后会被问一下用户名和密码
'''

# 七、代码规范性
'''
1、记住python以缩进识别代码块。四个空格为准，不要空格和制表符混用
2、分号划分句子。但是最好不要把两个句子放在同一行然后用分号划分。行尾无需用分号。
3、注释，单行注释，代码外和代码内。多行注释
4、空格：括号内，逗号、分号、冒号前不要加空格。（习惯）
5、二元操作符（比如等号赋值，比较，布尔）两边都加空格
6、。。。。
http://www.runoob.com/w3cnote/google-python-styleguide.html
'''








