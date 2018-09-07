# 元组 tuple 和字典 dict

## 元祖
**定义**

元组是不可改变的序列，同list一样，元组可以存放任意类型的元素，一旦元组生成，则它不可以改变。

**表示方式**

用小括号（）括起来，单个元素括起来用','区分是单个对象还是元组

**空元组创建**

t = ()

**非空元组的字面值**

- t = 200,
- t = (20,)
- t = (1, 2, 3)

## 元组的构造函数

tuple()生成一个空的元组， 等同于() \
tuple(iterable)用于可迭代对象生成一个元组

**示例：**
```python
t = tuple()
t = tuple(range(10))
t = tuple('hello')
t = tuple([1,2,3,4])
```

## 元组的算术运算
- ‘+’ ‘+=’ ‘*’ ‘*=’  \
   用法同列表一致
   
- '<' '<=' '>=' '==' '!=' \
   规则与列表完全相同

- in/not in
- 索引取值
- 切片取值 \
  规则与列表完全相同

**区别**

元组是不可改变对象，不支持索引赋值和切片赋值

**元组方法**

- help(tuple)
- T.index
- T.count

**用于序列的函数**

len, max, min , sum, all , any

**三个构造函数**

用于创建相应的对象
- str(obj)
- list(iterable)
- tuple(iterable)

**其他函数**

- reversed(seq) \
  返回反向顺序的可迭代对象
- sorted(iterable, reversed=False) \
  返回已排序的列表

**示例：**
```python
for x in reversed("ABCD"):
    print(x)  #D B C A
    
L = [8, 6, 3, 5, 7]
L2 = sorted(L)
print(L2)  #[3, 5, 6, 7, 8]

L3 = sorted(L, reversed = True)
print(L3)  #[8, 7, 6, 5, 3]

print(L) #保持不变
```

## 字典 dict
- 字典是一种可变的容器，可以存储任意类型的数据
- 字典的每个数据用‘键’key进行索引，而不像序列可以用下标来进行索引
- 字典的数据没有先后顺序关系，字典的存储是无序的
- 字典的数据以键key-值value进行映射存储
- 字典的键不能重复，且只能用不可变类型作为字典的键

**字典的字面表示方式：**

用{}括起来，以冒号（：）分隔键-值对，各键值对用分号隔开


**创建空字典:**

```python
d = {}
```

**创建非空的字典：**
```python
d = {'name': 'tarena'; 'age': 15}
d = {'姓名':'张三'}
d = {1:'壹', 2:'贰'}
d = {'a' : {1:'one', 2:'two'}}
d = { (2008,8,8): '北京奥运会'}
```
**字典的构造函数 dict**

- dict() 创建一个空字典，等同于{}
- dict(iterable) 用可迭代对象初始化一个字典
- dict(**kwargs) 关键字传参形式生成一个字典

**示例：**

```python
d = dict()
d = dict([('name','tarena'), ('age', 15)]) #列表是可迭代对象
d = dict(name= 'tarena', age = 15)
d = dict(('AB', 'CD'))
d = dict(('AB', 'CD',[1,2],(3,4)))
```
**可以作为键的**

- 不可变类型：

int,float,complex,bool,str,tuple,frozenset(固定集合)，bytes(字节串)

- 不可以作为键的可变类型

list, dict, set(集合), bytearray(字节数组)


**字典的键索引**

用[]运算符可以获取字典内‘键’所对应的‘值’

+ 语法：

```python
字典[键]
```
+ 获取数据元素

```python
d = dict([('name','tarena'), ('age', 15)]) 
print(d['age'])  #15
```
+ 添加/修改字典元素
   + 字典[键] = 表达式 
   
```python
d = {}

d['name'] = 'tarena' #创建一个新的键值对
d['age'] = 15   #创建键值对
d['age'] = 12   #修改键值对
```
**del 语句删除字典元素**

del 字典[键]

```python
d = {'name': 'china', 'pos':'asia'}
del d['pos']
print(d)

del d['name']
print(d)  #{}
```

**字典的in /not in 运算符**

可以用in 运算符来判断一个‘键’是否存在于字典中，如果存在则返回True,否则返回False

not in 与 in 返回值相反

示例：
```python
d = {'a':1, 'b':2}
'a' in d      #True
1 in d        #False
100 not in d  #True
2 not in d    #True
```
**字典的迭代访问：**

字典是可迭代对象，字典只能对键进行迭代访问
```python
d = {'name': 'tarena', (2002,1,1):'生日'}
for x in d :
   print(x)
```   

**用于字典的内建函数**

- len(x)  返回字典键-值对的个数
- max(x)  返回字典的键的最大值
- min(x)  返回字典键的最小值
- sum(x)  返回字典所有键的和
- any(x)  真值测试，只对键测试，如果一个键为True，结果为True
- all(x)  真值测试，全部键为True，返回True

**字典的方法：**

见： /dict.html


##字典推导式

字典推导式是用可迭代对象依次生成字典内元素的表达式

**语法**
```python
{键表达式:值表达式 for 变量 in 可迭代对象 [if 真值表达式]}
```
注：[]的内容代表可以省略

**示例：**
```python
d = {x : x**2 for x in range(10)}
```

