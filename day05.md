# 集合set

- 集合是可变的容器
- 集合内的数据对像是唯一的（不能重复多次）
- 集合是无序的存储结构，集合中的数据没有先后关系
- 集合内的元素是不可变对象
- 集合是可迭代的
- 集合相当于只有键没有值的字典（键是集合的数据）

**创建空的集合**
```python
s = set()
```

**创建非空集合**
```python
s = {1, 2, 3}  #集合中的三个整数
```

**集合的构造函数**

- set()  创建空集合
- set(iterable)  用可迭代对象创建一个集合对象

**示例**
```python
s = set("ABC")
s = set("ABCCBA")
s = set({1:"一", 2:"二", 5:"五"})
s = set([1, 3.14, False])
s = set((2, 3, 5, 7))

s = set([1, 3.14, [1, 1], 4])  #错误示例
```

**集合的运算**

交集、并集、补集、子集、超集

- '&' 生成两个集合的交集
```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 & s2    #{2, 3}
```

- '|' 生成两个集合的并集
```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2    #{1,2,3,4}
```

- '-' 生成两个集合的补集
```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 - s2    #{1}
```

- '^' 生成两个集合的对称补集
```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 ^ s2    #{1, 4}
#等同于s3 = (s1 - s2) | (s2 - s1)
```

- '<' 判断一个集合是另一个集合的子集;'>' 判断一个集合是两一个集合的超集
```python
s1 = {1, 2, 3}
s2 = {2, 3}
s1 > s2    # 判断超集True
s2 < s1    # 判读子集True
```
- "==" "!=" 判断集合是否相同
```python
s1 = {1, 2, 3}
s2 = {2, 3, 1}
s1 == s2    #True
s1 != s2    #False
```
- s1 = s1 | s2 不等同于 s1 |= s2
```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s = s1
if True:
   s1 = s1 | s2 #对可变对象，不等同于s1 += s2
   print(s)  #{1,2,3}
else:
   s1 |= s2
   print(s)     #{1,2,3,4}
```

- in / not in 
等同于字典，in 运算符用于集合中，当某个值存在于集合中则为真，否则假
```python
s = {1, 'two', 3.14}
1 in s  #True
2 in s  # False
3.14 not in s #False
4 not in s #True
```

**用于集合的函数**

len(x) max(x) min(x) sum(x) any(x) all(x)

**集合是可迭代对象**
```python
s = {1, 2, 3}
for x in s:
    print(x)
```  

**集合的方法**

见： ..../set.html
```python
s = set()
s.add(100)        #添加元素
s.add(200)

s.remove(200)     #删除元素（元素不存在时报错）
s.discard(100)    #删除元素（元素不存在不报错）

s.clear()         #清空集合元素

s = {1, 2, 3, 4}
s2 = s.copy()     #将集合进行浅拷贝
s.clear()     

s = {2, 3, 5, 7, 11}
s.pop()           #随机从集合中删除一个元素
s.pop()           #空集合时会报错

s.update(s2)      #用s与s2得到新的集合
```


**集合推导式**

用可迭代对象来创建集合的表达式

- **语法：**
```python
{表达式 for 变量 in 可迭代对象 [if 真值表达式]}
```
“[]”表示可以省略

- **示例：**
```python
L = [2, 3, 5, 7, 3, 5, 7, 11]
s = {x**2 for x in L}   #s={4，9，25，49，121}
```

- **集合推导式的嵌套**
```python
{x + y for x in 'ABC' for y in '123'}
```

**固定集合 frozenset**

固定集合是不可变的，无序的，含有唯一元素的集合

- **作用：**

固定集合可以作为字典的键，也可以作为集合的值

- **创建固定集合：**
```python
fs = frozenset()
fs = frozenset([2, 3, 5, 7])
```
- **构造函数：**
```python
frozenset()
frozenset(可迭代对象)   #同set函数一致，返回固定集合
```

+ **固定集合的运算：**
  + ‘&’
  + ‘|’
  + ‘-’
  + ‘^’
  + '> >= < <= == !='
  + in / not in

- **固定集合的方法**

相当于集合的全部方法去掉修改集合的方法。


