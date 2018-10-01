## 函数式编程
函数式编程是指用一系列函数解决问题

**函数是一等公民**

+ 函数本身可以赋值给变量，赋值后变量绑定函数
+ 允许函数本身作为参数传入另一个函数
+ 允许返回一个函数

**函数的可重入性**

可重入性是指一个函数传参一定，则结果一定

要求：

def定义的函数不要访问除局部变量以外的变量

示例：
```python
#以下是不可重入的函数
y = 200
def myadd(x):
    return x + y
print(myadd(10))  #210

#可重入的函数myadd
def myadd(x, y):
    return x + y
print(myadd(10,20))
```

##高阶函数

满足下列一个条件的函数

+ 函数接收一个或多个函数作为参数传入
+ 函数返回一个函数

###map函数

map(fun, *iterables)用函数和可迭代对象中的每一个元素作为参数计算出新的可迭代对象，当最短的一个可迭代对象不再提供数据时，此可迭代对象生成结束

**示例**
```python
def pow2(x):
    return x**2
for x in map(pow2, range(1,10)):
    print(x)
    
## 利用内建pow(x,y,z=Zone)
for x in map(pow, range(1,10), range(4,0,-1)):  #最短的可迭代对象不提供数据结束
    print(x)

for x in map(pow, [2,3,5,7],[4,3,2,1], range(5,10)):
    print(x)

    
```

###filter

**格式：**

filter(func, iterable)

**作用**

筛选可迭代对象iterable中的数据，返回一个可迭代对象，此可迭代对象将对Iterable进行筛选

**说明**

函数func将对每个元素进行求职，返回False则将此数据丢弃，返回True则保留此数据

**示例**

```python
def isodd(x):
    return x % 2 == 1
for x in filter(isodd, range(10)):
    print(x)
    
even = [x for x in filter(lambda x: x%2 ==0, range(10))]    
```

###sorted函数

**作用**

将原可迭代对象的数据顺序进行排序，生成排序后的列表

**格式**

sorted(iterable, key=None, reverse=False)

**说明**

+ iterable是可迭代对象
+ key函数是用来提供一个参考值，这个值作为排序的依据
+ reverse标志用来设置是否降序排序

**示例**

```python
L = [5,-2,-4,0,3,1]
L2 = sorted(L)
L2 = sorted(L, reverse = True)
L3 = sorted(L, Key=abs)
```

##递归函数

函数直接或间接的调用自身

**示例**
```python
#永远循环自身
import time
def story():
    time.sleep(5)
    print("从前有座山")
    print("山上有座庙")
    print("庙里有个老和尚讲故事：")
    story() #直接调用自身 
story()

#函数间调用自身递归
def fa():
    fb()
def fb():
    fa()
fa()
print("递归结束")
```
**说明**

+ 递归一定要控制递归的层数，当符合某一条件要终止递归
+ 几乎所有的递归都能用while循环来代替

**控制递归层数的示例：**
```python
def fx(n):
    print("递归进入第", n, "层")
    if n ==3:
        return
    fx(n + 1)
    print("递归退出第", n, '层')
fx(1)
print("程序结束")
```

**递归的优缺点**

+ 优点
     + 可以把问题简单化，让思路更为清晰，代码更简洁
+ 缺点
     + 递归受系统环境影响大，当递归深度太大时，可能会得到不可预知的结果
     
**递归函数的实现方法**

先假设函数已经实现

**示例**
```python
#求和 1 + 2 +...+98 + 99 + 100
def mysum(x):
    if x <= 1: #设置递归终止点
        return 1
    return x + mysum(x - 1)
    print(x)
mysum(100)

#  编写程序用递归求阶乘:
def myfac(x):
    if x == 1:
        return 1
    return x * myfac(x-1)

print(myfac(5))
print(myfac(4))

```


##闭包closure

将内嵌函数的语句和这些语句的执行环境打包在一起时，得到的对象称为闭包（closure）

**满足三个条件：**

+ 必须有一个内嵌函数
+ 内嵌函数必须引用外部函数中的变量
+ 外部函数返回值必须是内嵌函数
+ 闭包可以用来创建函数
**示例：**
```python
def make_power(y):
    def fx(arg):
        return arg **y
    return fx
```

## 装饰器decorators

**问题：**
```python
def say(x):
    print("您好：",x)
```
希望打印：\
开始问候：\
您好：老魏\
结束问候

**定义**
函数装饰器是指装饰的是一个函数，传入的是一个函数，返回的也是一个函数的函数

**函数装饰器的语法**
```python
def 装饰器函数名(参数)：
    语句块
    return 函数对象
```    

**被装饰器函数的语法**
```python
@装饰器函数名
def 函数名（形参列表）：
    语句块
```

**示例**
```python
#此示例示意函数装饰器的用法

#定义一个装饰器函数解决问题
def mydeco(fn):
    def fx():
        print('+++++++++++++++')
        fn()
        print('---------------')
    return fx

#定义函数的地方（小张写的）
@mydeco  #等同于myfunc = mydeco(myfunc)
def myfunc():
    print("myfunc被调用")
    
#调用函数部分是小李写的
myfunc()
myfunc()
#调用函数的地方可能是小王写的
myfunc()
```

##函数的文档字符串

函数内部，第一个没有赋值给任何变量的字符串为文档字符串

**语法**

```python
def 函数名(形参列表):
    '''
    函数的文档字符串
    '''
    函数语句块
```

**示例**

```python
def cba():
    '这是一块文档字符串...'
    pass
```

##函数的__doc__属性

用于绑定该函数的文档字符串

示例：

```python
def fx(a, b):
    '''
    这是函数的文档字符串
    这是第二行
    '''
print(fx.__doc__)
```

##函数的__name__属性

__name__属性用于绑定函数名的字符串

示例：

```python
def fx():
    pass
f1 = fx
print(f1.__name)
```

##函数定义语句（def语句的语法）

[@装饰器名1]
[@装饰器名2]
```python
def  函数名([位置形参], [*[元组形参名]], [命名关键字形参],
            [**字典形参])：
     '''文档字符串'''
     语句块
```
注：[]里的内容可以省略


不可重用的函数——python bug示例

```python
#面试题
L = [1,2,3]
def f(n, lst=[]):
    lst.append(n)
    print(lst)
f(4,L)
f(5,L)
f(100)
f(200)


#解决方法：
def f(n, lst=[]):
    if lst is None:
       lst = []
    lst.append(n)
    print(lst)
```
```
**说明**

默认参数

默认参数绑定在函数对象内部，随函数的生命一直存在






