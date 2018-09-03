# 列表

##列表的 in / not in
1.判断一个元素是否存在容器中，在返回True,否则返回False

2.not in 与 in运算符相反

示例：

x = [1, 'two', 3.14, '四'] \
1 in x           #True    \
3 not in x       #True

##列表的索引 index  /切片 slice

###列表的索引语法：
   列表[整数表达式]

###用法：
   列表的索引取值与字符串的索引取值规则完全相同
   
   列表的索引分为正向索引和反向索引

示例：   
  x = [1, 'two', 3.14, '四']
  
  print(x[1]) # 'two'
  
##列表的索引赋值
   列表是可变的序列，可以通过索引赋值改变列表的元素

###语法：
   列表[索引]  = 表达式

###示例：
   x = [1, 2, 3, 4]
   
   x[2] = 3.14  #改变第三个元素
   
   y = [1, 2, 3, 4]
   
   id(x) 
   
   id(y)          #id(x)不一致
   
   x[2] = 3.14
   
   id(x)          #id(x)没变化
   
   x += '123'     
   
   id(x)          #id(x)已经不一样了,'123'新建的
   
   x += [1,2,3,4] #id(x)没有变化,改变的是列表内值
   
   
##列表切片
   - 列表[:]
   - 列表的[::]
   - 列表的切片取值返回一个列表，规则等同于字符串的切片规则
   
 示例：
   - x = list(range(8))
   - y = x[1:9:2] # y = [1, 3, 5, 7]
   
   
##列表的切片赋值语法
   列表[切片] = 可迭代对象

###说明：
   切片复制的赋值运算符的右侧必须是一个可迭代对象

###示例：
  - L = [2, 3, 4]  # 0~2
  - L[0:1] =[1.1, 2.2]
  - L[3:3] = [5, 6]
   
###切片步长不为1
对于步长不为1的切片赋值，赋值运算符右侧的可迭代对象提供的元素的个数一定要等于切片的段数。

   - L = list(range(1,9))
   - L[1::2] = [2.2, 4.4, 6.6, 8.8]
   - print(L)

##del语句
用于删除列表元素

###语法
- del 列表[索引]
- del 列表[切片]

###示例：
- L = [1, 2, 3, 4, 5, 6]
- del L[0]
- del L[::2]  #L = [2, 4, 6]

##常见的序列函数
- len(x)
- max(x)
- min(x)
- sum(x)
- any(x) #真值测试，如果列表中一个值为真则为True,否则返回False。
- all(x) #真值测试，如果列表中所有制为真则返回True，只要一个为假则返回False

##列表的方法

help(list)

 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)  
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 
 
##字符串文本解析方法 split 和join

###S.split(sep=None) 
将字符串，使用sep作为分隔符分割S字符串，返回分割后的字符串列表，当不给定参数时，用空白字符作为分隔符进行分割
###S.join(iterable)
用可迭代对象中的字符串，返回一个中间用S进行分割的字符串

例：
- s = 'Beijing is capital'
- L = s.split(' ') #L = ['Beijing','is','capital']
- s1 = "-".join(L)
 
 
##深拷贝deep copy与浅拷贝 shallow copy

###浅拷贝
是指在复制过程中只复制一层变量，不会复制深层变量绑定的对象的复制过程。

浅拷贝可以共用同一个对象。

 - L = [3.1, 3.2]
 - L1 = [1, 2, L] #[1, 2, [3.1, 3.2]]
 - L2 = L1.copy() #[1, 2, [3.1, 3.2]]  
 - L2[2][0] = 3.14
 - print(L)      #[3.14, 3.2]
 - print(L1)     #[1, 2, [3.14, 3.2]]
 - print(L2)     #[1, 2, [3.14, 3.2]]

###深拷贝
只拷贝可变的部分变量，不可变对象不拷贝

- import copy            #导入copy模块
- L = [3.1, 3.2]
- L1 = [1, 2, L]
- L2 = copy.deepcopy(L1)  #深拷贝
- print(L1)   #[1, 2, [3.1, 3.2]]
- print(L2)   #[1, 2, [3.1, 3.2]]

- L2[2][0] = 3.14      #L1 ,L2 改变的部分不一致了
- print(L1)     #[1, 2, [3.1, 3.2]]
- print(L2)     #[1, 2, [3.14, 3.2]]


##列表推导式
列表推导式是用可迭代对象依次生成带有多个元素的列表的表达式

###作用：
   用简易的方法生产列表

###语法：
   - [表达式 for 变量 in 可迭代对象]
   
   - [表达式 for 变量 in 可迭代对象 if 真值表达式]
   
###示例：
   #生成一个数值为1~9的平方的列表
   
   - L = [X*X for x in range(1,10)]

##列表推导式的嵌套

###语法
[表达式1
  for 变量1 in 可迭代对象1 if 真值表达式1
    for 变量2 in 可迭代对象2 if 真值表达式2
      ...]
      
###示例
- L1 = [2, 3, 5]
- L2 = [7, 11, 13]

将L1 中的全部元素与L2中的全部元素依次相乘后放到L3列表中

L3 = [x * y  for x in L1 
         for y in L2]

print(L3)