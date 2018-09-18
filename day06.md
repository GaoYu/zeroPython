## 函数

函数是可以重复执行的语句块，可以重复使用

**作用：**

+ 用于封装语句块，提高代码的重用性 \
+ 定义用户级别的函数

**函数定义语句 def 语句的语法：**
```python
def 函数名（形参列表）：
    语句块
```
**说明**

+ 函数的名字就是语句块的名称
+ 函数名的命名规则与变量名相同（函数名必须为标识符）
+ 函数有自己的名字空间，在函数外部不可以访问函数内部的变量，在函数内部可以访问函数外部的变量，通常让函数处理外部数据需要用参数给函数传入一些数据
+ 函数的参数列表可以为空
+ 语句部分不能为空。如果为空需要填充pass语句

```python
#def 定义函数
def say_hello():
    print("helllo world!")
    print("hello tarena!")
    print("hello everyone!!!")

#调用函数
say_hello()
```

**函数的调用**

函数名（实际调用传递参数列表）

注：实际调用传递参数以后称为实参

**说明**

+ 函数调用是一个表达式
+ 如果没有return语句，此函数执行完毕后返回None对象
+ 如果函数需要返回其他的对象需要用到return语句

##return 语句

**语法**

+ return [表达式] \n []代表可以省略

**作用**

+ 用于函数中，结束当前函数的执行，返回到调用该函数的地方，同时返回一个对象的引用关系
    
**说明**

+ return语句后跟的表达式可以省略，省略后相当于return None
+ 如果函数没有return语句，则函数执行完最后一条语句后返回None（相当于在最后加了一条return None语句）
+ 函数调用一定会返回一个对象的引用
    
    
##函数的参数传递

**传递方式**

    + 位置传递 \
        序列传参
    + 关键字传递 \
        字典关键字传参

**位置传参**

实际参数（实参）的对应关系与形式（形参）的对应关系是按照位置来依次对应的

示意：
    
```python
def myfun(a, b, c)
    pass
    
myfun(1, 2, 3)
```
说明： 
    
实际参数和形式参数通过位置进行传递的匹配，实参个数必须与形参个数相同


**序列传参**

序列传参是指在函数调用过程中，用“*”将序列拆解后按照位置传参的方式进行参数传递

示例

```python
def myfun(a, b, c):
    pass

s = [1, 2, 3]
myfun(*s)
s2 = "ABC"
myfun(*s2)
```

**关键字传参**

关键字传参是指传参时，按形参的名称给形参赋值，实参和形参按名称进行匹配

**示例**

```python
def myfun(a, b, c):
    pass

myfun(b = 22, c = 33, a = 11) 
```

**说明**

实参和形参可以不按位置匹配

**字典关键字传参**

是指实参为字典，将字典用"**"拆解后进行关键字传参

**示例**

```python
def myfun(a, b, c):
    pass
  
d = {'c' :33, 'b':22, 'a':11}
myfun(**d)
```

**说明**

+ 字典的键名和形参名必须一致
+ 字典键名必须为字符串
+ 字典键名要在形参中存在

**函数的综合传参**

函数传参方式，在能确定形参能唯一匹配到相应实参的情况下可以任意组合

**示例**
```python
def myfun(a, b, c):
    pass
    
myfun(100, *[200, 300])  #正确
myfun(*'AB', 300)        #正确
myfun(100, c = 300, b=200) #正确
myfun(1, **{'c':3, 'b':2}) #正确
myfun(**{'c':3, 'b':2}, a = 1) #正确

myfun(b = 2, c=3, 1)          #错误,不能确定1给谁
```



##函数形参

**函数的缺省形参**

**语法**

```python
def  myfun(形参名1=默认实参1,
           形参名2=默认实参2,
           ...)
```

**示例：**
```python
def info(name, age=1, address='未填写'):
    print(name, "今年",
          age, "岁,家庭地址是：", address)
          
info('tarena', 15)
info('小魏',20, '北京朝阳区')
info('小李')
```

**说明**

1.缺省参数必须自右至左依次存在，如果一个参数有缺省数，则其右侧的所有参数都必须有缺省参数

如：
```python
def test(a, b = 10, c):  #错误示例
    pass
```

2.缺省参数可以有0个或多个，甚至全部都有缺省参数。


##形参定义方式

- 位置形参
- 星号元组形参
- 命名关键字形参
- 双星号字典形参

**位置形参**

语法：
```python
def myfun(形参名1, 形参名2, ...);
    语句块
```

**星号元组形参：**

语法：
```python
def myfun(*元组形参名)：
    语句块
```

作用：

收集多余位置形参传参

说明：

元组形参名常用：“args”

**命名关键字形参：**

语法：

```python
def myfun(*, 命名关键字形参):
    语句
    
def myfun(*args, 命名关键字形参)：
    语句
```

作用：

要求传参时，所有的参数都必须用关键字传参或字典关键字传参

示例：

```python
def fn(*, d, e):
    print("d=", d)
    print("e=", e)

fn(d = 100, e = 200)  #合法
#fn(1, 2)             #不合法，不能用位置传参

def fn(a,b,*, d, e):
    pass
fn(1,2, d=100,e=200) 

def f1(a,b,*args, c, d):
    pass
f1(1,2,c=3,d=4)
```

**双星号字典形参：**

语法：

```python
def 函数名(**字典形参名):
    语句
```

作用：

收集多余的关键字形参

说明：

通常双星号字典形参（**kwargs)

```python

#此示例示意双星号字典形参kwargs收集多余的关键字传参
def func(**kwargs):
    print("关键字参数个数是：", len(kwargs))
    print("kwargs = ", kwargs)

func(name= 'tarena', age = 15)
```

**参数说明**

缺省参数、位置形参、星号元组形参、命名关键字形参和双星号字典形参可以混合使用

函数参数自左向右的顺序为：

+ 位置形参
+ 星号元组形参
+ 命名关键字形参
+ 双星号字典形参

```python
def f1(a, b, *args, c, **kwargs):
    print(args)
    print("kwargs是：",kwargs)
#f1(1, 2, 3, 4, d=6, c=5, e= 7)
f1(*"hello",d = 6, **{'c':5, 'e':7})
```

##函数的不定长参数
```python
def fn(*args, **kwargs):
    pass
    
    #可以接收任意的位置传参和关键字传参
def fn(*args, **kwargs):
    print(args)
    print(kwargs)
fn(1,2,3,a=4,b=5)
```

##全局变量和局部变量

**局部变量**

+ 定义在函数内部的变量成为局部变量（函数的形参也是局部变量）
+ 局部变量只能在函数内部使用
+ 局部变量在函数调用时才能被创建，在函数调用之后会自动销毁

**全局变量**

+ 定义在函数外部，模块内部的变量成为全局变量
+ 全局变量，所有的函数都可以直接访问（函数内部不能直接将其赋值）

**示例**
```python
a = 10
b = 20

def fy(c):
   d = 40
   a = 20        #创建局部变量a，不会修改全局变量a
   print(a, b, c, d)

print("--------------------")
fy(30)

print("a=", a)
````

**局部变量说明**

+ 在函数内首先对变量赋值是创建局部变量，再次为变量赋值是修改局部变量的绑定关系
+ 在函数内部的赋值语句不会对全局变量造成影响
+ 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个模块范围内访问

**globals和locals函数**

+ globals() 返回当前全局作用域内变量的字典
+ locals()  返回当前局部作用域内变量的字典

示例：

```python
a = 1
b = 2
c = 3
def f1(c, d):
    e = 300
    print("locals()返回：", locals())
    print("-------------------------")
    print("globals()返回：", globals())
    for k, v in globals().items():
        print(k, "-->", v)
        
    print(c)               #局部变量复制100
        
    print(globals()['c'])  #全局变量 3
f1(100, 200)
```

##函数变量

**函数名是变量，它在创建函数时绑定一个函数**

示例：
```python
def f1():
    print("f1被调用")
fx = f1
fx   #等同于f1()

del f1
fx   #同上
```
示例2
```python
def f1():
    print("hello")
def f2():
    print("world")
f1, f2 = f2, f1 #交换两个变量
f1()   #
```

**一个函数可以作为另一个函数的参数传递**

示例
```python
def f1():
    print("hello")
def f2():
    print("world")

def fx(fn):
    print(fn)
    fn()         #调用谁

###3个全局变量
fx(f1)           #此语句在做什么
fx(f2)
```

```python
def fx(a, fn):
    return fn(a)
  
L = [5, 9, 4, 6]
print('最大值：',  fx(L, max))
print('最小值：',  fx(L, min))
print('和是：',  fx(L, sum))
```

**函数作为返回值**
```python
def myadd(x, y): #计算两个数相加
    return x + y
def mymul(x, y): #计算两个数相乘
    return x * y

def get_op(s = "加"):  #s代表操作字符串：'加'，'乘'
    if s == '加' or s == '+':
        return myadd
    elif s == '乘' or s == '*':
        return mymul
    else:
        return "输入有误"


#主函数：
def main():
    while True:
        s = input('请输入计算公式：') #如：10 加 20
        L = s.split()
        a, s, b = L
        a, b = int(a), int(b)
        fn = get_op(s)
        print("结果是：", fn(a, b))  #结果是30
```

**函数的嵌套定义**

函数的嵌套定义是指一个函数里用def语句来创建其他的函数
```python
def fn_outer():
    print("fn_outer被调用！")
    def fn_inner():
        print("fn_innter被调用")
    fn_inner()
    fn_inner()
    print("fn_outer调用结束")
    return fn_inner
    
fn_outer()
#fn_inner() #此处报错

fx = fn_outer()
fx()         #调用fn_outer函数内部函数fn_inner
```

**python作用域**

作用域也叫名字空间，是访问变量时，查找变量名的范围空间

**python四种作用域 LEGB**

+ 局部作用域               Local function              L
+ 外部嵌套函数作用域       Enclosing Function Locals   E
+ 函数定义所在模块（文件）的作用域 Global（Mudule）    G
+ python内置模块的作用域           Builtin(python)     B

```python
#说明python的作用域
v = 100        #全局作用域
def fun1():
    v = 200    #外部嵌套函数的作用域
    print('fun1内的v=', v)
    def fun2():
        v = 300        #局部作用域
        print("fun2内的v=", v)
    fun2()
fun1()
print("v=", v)
```

变量名的查找规则：

L -->   E  --> G --> B

默认情况下，对变量名复制会创建或改变本作用域内的变量。

## global 语句

问题：
```python
v = 100
def f():
    v = 200  #希望此赋值语句操作全局变量v
f()
print(v)  #200 怎么办？
```
**作用：**

+ 告诉解释器， global语句声明的一个或多个变量，这些变量的作用域为模块级的作用域，也成为全局变量
+ 全局声明（global）将赋值变量映射到模块内部的作用域

**语法**
```python
global 变量1,　变量2
```
```python
v = 100
def f():
    global v
    v = 200  #希望此赋值语句操作全局变量v
f()
print(v)  #200 怎么办？
```
**global说明**

+ 全局变量如果要在函数内部被赋值，则必须经过全局声明（否则会被认为是局部变量）
+ 全局变量在函数内部不经过声明就可以直接访问
+ 不能先声明局部变量，再经过global声明为全局变量，此做法不符合规则
+ global变量列表里的变量不能出现在此作用域内的形参列表里面

示例：
```python
#不能先声明局部变量，再经过global声明为全局变量
def f1():
    #x = 100  #不能先声明局部变量再声明全局变量
    global x
    x = 100

f1()

#global变量列表里的变量不能出现在此作用域内的形参列表里面
v = 100
def f2(v):
    #global v   #形参列表中已经有v，global不能再次声明
    v = 300
f2(200)
print(v)
```

##nonlocal语句

**作用：**

告诉解释器，nonlocal声明的变量不是局部变量，也不是全局变量，而是外部嵌套函数内的变量

**语法：**

```python
nonlocal 变量名1, 变量名2
```

**说明：**

+ nonlocal语句只能在被嵌套函数内部使用
+ 访问nonlocal变量将对外面嵌套函数的作用域的变量进行操作
+ 当有两层或两层以上的函数嵌套时，访问nonlocal变量只对最近一层的变量进行操作
+ nonlocal语句的变量列表里的变量名，不能出现在此函数的参数列表中

##lambda表达式（匿名函数）:**

**作用:**
+ 创建一个匿名函数对象
+ 同 def 类似，但不提供函数名

**语法:**
```python
lambda [参数1, 参数2, ...]: 表达式
```
[] 里的内容可以省略
  
**示例:**
```python
def myadd(x, y):
    return x + y
    # 以上函数可以改写为:
    
myadd = lambda x, y: x + y
print('2 + 3 =', myadd(2, 3))
```    
**语法说明:**
+ lambda 只是一个表达式，它用来创建一个函数对象
+ 当lambda表达式调用时，先执行冒号后(:)的表达式，并返回表达式的结果的引用
+ lambda 表达式创建的函数只能包含一条"表达式"
+ lambda 比函数简单，且可以随时创建和销毁，有利于减少程序的偶合度


##eval()  和 exec()函数

**eval()  函数**

**格式:**
```python
eval(source, global=None, locals=None)
```
**作用:**

把一个字符串当成一个表达式来执行，返回表达式执行后的结果

**示例:**
```python
x = 100
y = 200
a = eval('x+y')
print(a)
```

**exec() 函数**

**作用:**

把一个字符串当成程序来执行

**格式:**
```python
exec(source, globals=None, locals=None)
```
**示例:**
```python
x = 100
y = 200
s = 'z = x+y; print(z); del z; print("删除成功"'
exec(s)  # 执行s绑定的语句
```

**eval 和 exec的两个参数globals 和 locals**

此两个参数是用来设置'表达式'或'程序'运行的全局变量和局部变量

**示例:**
```python
x = 100
y = 200
s = 'print(x, y, x + y)'
exec(s)  # 100 200, 300
exec(s, {'x': 10, 'y': 20})  # 10, 20, 30
exec(s, {'x': 10}, {'x': 1, 'y': 2})  # 1 2 3
exec(s, {'x': 10}, {'y': 2})  # 10 2 12
```




