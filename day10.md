#迭代器iterator和生成器generator

##迭代器iterator
+ 是指用iter(可迭代对象)函数返回的对象（示例）
+ 迭代器可以用next(it)函数获取可迭代对象的数据

###迭代器函数
+ iter(iterable)  从可迭代对象中返回一个迭代器，iterable必须是一个能提供迭代器的可迭代对象
+ next(iterator)  从迭代器iterator中获取下一条记录，如果无法获取下一条记录，则触发StopIteration异常

**说明**

+ 迭代器是访问可迭代对象的一种方式
+ 迭代器只能向前取值，不会后退
+ 用iter函数可以返回一个可迭代对象的迭代器

**示例**
```python
#用while语句循环访问列表
L = [2, 3, 5, 7]
it = iter(L)  #用L生成一个迭代器
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        print("迭代结束")
        break
```

##生成器 Generator(python2.5以后有)

生成器是能够动态提供数据的对象，生成器对象也是可迭代对象（实例）

**两种生成器**

+ 1.生成器函数
+ 2.生成器表达式


###生成器函数

含有 **yield**语句的函数是生成器函数，此函数被调用时将返回一个生成器对象

**yield语句**
```python
yield 表达式
```
+ yield用于def函数中,目的是将此函数作为生成器函数使用
+ yield用来生成数据，共迭代器next(it)函数使用

**示例**
```python
def myyield():
    '''此函数为生成器函数'''
    print("即将生成2") #只有next才会执行
    yield 2  #生成2
    print("即将生成3")
    yield 3  #生成3
    print("即将生成5")
    yield 5  #生成5
    print("myyield函数返回")  
#用for 语句访问myyield函数

for x in myyield():
    print(x)

gen = myyield()
it = iter(gen)
next(it)
```

**生成器函数说明**

+ 生成器函数的调用将返回一个生成器对象，生成器对象是一个可迭代对象
+ 在生成器函数调用return时会生成一个StopIteration异常来通知next(it)函数不再能提供数据

###生成器表达式

**语法**
```python
(表达式 for 变量 in 可迭代对象 [if 真值表达式])
```

**作用**

用推导式的形式生成一个新的生成器

**示例**
```python
gen = (x**2 for x in range(1,5))
it = iter(gen)
next(it) #1
next(it) #4
next(it) #9
next(it) #16
next(it) #StopIteration
```
**优点**

不占用内存空间


**列表推导式与生成器表达式区别**
```python
L = [1,2,3,4]
gen = (x for x in L) #gen 绑定生成器
lst = [x for x in L] #lst 绑定列表
L[1] = 222  #改变原列表的第二个元素
for x in lst:
    print(x)  #1,2,3,4不变

for x in gen:
    print(x)  #1,222,3,4,第二个数是222
```

##迭代工具函数

迭代工具函数的作用是生成一个个性化的可迭代对象

+ zip(iter1 [, iter2, iter3,...])

返回一个zip对象，此对象用于生成一个元组，此元组的个数由最小的可迭代对象决定

+ enumerate(iterable[, start])

生成带索引的枚举对象，返回迭代类型为索引-值对（index-value)对，默认索引从0开始，也可以使用start绑定

**示例zip**
```python
numbers = [10086, 10000, 10010, 95588]
names = ['中国移动','中国电信','中国联通']
for n, a in zip(numbers, names):
    print(a, '的客服号码是', n)
for x in zip(numbers, names):
    print x
#zip生成一个字典
d = dict(zip(names, numbers)    #zip对象
```

**示例enumerate**
```python
names = ['中国移动','中国电信','中国联通']
for x in enumerate(names):
    print(x)
    #索引-元素
    index, element = x
    print('索引',index,'对应的元素是',element)

#索引从100开始
for x in enumerate(names, start = 100):
    print(x)
```

##字节串bytes和字节数组bytearray

###字节串bytes

**作用**

存储以字节为单位的数据

+ 字节串是不可变的字节序列
+ 字节是0~255之间的整数

**创建空字节串的字面值**

+ b''
+ b""
+ b''''''
+ b""""""
+ B''
+ B""
+ B''''''
+ B""""""

**非空字节串的字面值**

+ b'ABCD'
+ b'\x41\x41'


**字节串的构造函数**

+ bytes()　生成一个空的字节串，等同于b''
+ bytes(整型可迭代对象)  用可迭代对象初始化一个字节串
+ bytes(整数n)  生成n个值为零的字节串
+ bytes(字符串，encoding='utf-8')  用字符串的转换编码生成一个字节串

**字节串的运算**

+, +=, *,*=

<,<=,>,>=,==,!=

in,not in

索引/切片

**示例**

```python
b = b'abc' + b'123' #b = b'abc123'
b += b'ABC'         #b=b'abc123ABC'
b'ABD'>b'ABC'       #True

b = b'ABCD'
65 in b            #True
b'A' in b          #True

b= b'ABCD'
b[-1]              #68
```

**用于序列函数**

len,max,min,sum,all,any

**bytes与str区别**

+ bytes 存储字节（0~255）
+ str存储Unicode字符（0~65535）

**bytes与str的转换**

+ str -----编码(encode)------bytes  \ b=s.encode('utf-8')

+ bytest -----解码(decode)-----str  \ s = b.decode('utf-8')

###字节数组bytearray

可变的字节序列

**构造函数**
 
+ bytearray() 创建空的字节数组
+ bytearray(整数)
+ bytearray(整数可迭代对象)
+ bytearray(字符串,encoding='utf-8')

以上参数等同于字节串

**字节数组的运算**

+, +=, *,*=

<,<=,>,>=,==,!=

in,not in

索引/切片

**bytearray的相关方法**
+ b.clear()         清空字节数组
+ b.append(n)       追加一个字节
+ b.remove(value)   删除第一个出现的字节，如果没有出现，则产生ValueError错误
+ b.reverse()       字节顺序进行反转
+ b.decode(encoding='utf-8')      解码
+ b.find(sub[, start[,end]])      查找