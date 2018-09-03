# 元组 tuple

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
