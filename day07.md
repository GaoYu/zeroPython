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




