# 字符串格式化表达式

## 运算符 %

**作用：**

生成一定格式的字符串

**语法：**

-   格式字符串% 参数值
-   格式字符串% (参数值1,参数值2,...)...

格式字符串中的%为占位符，占位符的位置将用参数值替换

## 格式化字符串中的占位符和类型码
- 占位符            意义
- %s              字符串，使用str函数转换
- %r              字符串，使用repr函数转换
- %c              整数转为单字符
- %d              十进制整数
- %o              八进制整数
- %x              十六进制整数（a-f小写）
- %X              十六进制整数（A-F大写）
- %e              指数型浮点数（e小写）如2.9e+10
- %E              指数型浮点数（E小写）如2.9E+10
- %f,%F           浮点十进制形式
- %g,%G           十进制形式浮点或指数浮点数自动转换
- %%              等同于一个%字符

## 占位符和类型码之间的格式语法
- %[格式语法] 类型码

**格式语法：**

-    -左对齐
-    +显示正号
-    0补零
-    宽度（整数）
-    宽度.精度（整数）

**示例：**

-   '%10d' % 123   #'       123'
-   '%-10d' % 123  #'123       '
-   '%10s' % 'abc' #'       abc'
-   '%-5s' % 'abc' #'abc  '
-   '%05d' % 123   #'00123'
-   '%7.3f' % 3.1415926   #'003.141'

## while 语句

**作用**

根据一定条件，重复执行一条语句或多条语句

**语法**
```python
while  真值表达式：
   语句块
else:
   语句块
```

**语法说明：**
- 先执行真值表达式，判断True/False
- 如果为True则执行语句块1，然后跳转到第1步
- 如果为False则执行else子句部分的语句块2.然后结束此while语句的执行
  如果没有else子句，则直接结束while语句
- else子句部分可以省略（同if语句）

**while注意事项：**
- 要控制真值表达式来访问死循环
- 通常用真值表达式的变量来控制循环条件
- 通常要在循环语句块内改变循环变量来控制循环的次数和变量的走向


## while语句嵌套

while语句本身是语句，和其他语句一样，可以放在其他复合语句的内部

**while语句嵌套示意：**

```python
while 真值表达式：
   ...
   while 真值表达式：
      ...
   else:
      ...
   ...
else:
   ...
```

   
## break 语句

**作用：**

用于循环语句（while,for语句）中，用来终止当前循环语句的执行

**break语句说明**

- 当break语句执行后，此循环语句break之后的语句将不再执行
- break语句通常和if语句组合使用
- break语句终止循环时，循环语句的else子语句的语句将不会执行
- break语句只能终止当前循环语句的执行，如果有循环嵌套时，不会跳出嵌套的外重循环
- break语句只能在循环语句（while,for）内部使用

## 死循环

死循环是指循环条件一直成立的循环，死循环通常用break语句来终止循环

死循环的else子句永远不会执行


## for 语句

**作用：**

- 用来遍历可迭代对象的数据元素
- 可迭代对象是指能依次获取数据元素的对象
+ 可迭代对象包括：
  +  字符串 str
  +  列表   list
  +  元祖   tuple
  +  字典   dict
  +  集合   set
  +  ...

**for语句语法**
```python
   for 变量列表  in  可迭代对象：
       语句块1
   else:
       语句块2
```

**for语句语法说明**

+ 可迭代对象每次提供一个元素依次赋值给变量列表中的变量，赋值完毕后执行语句块1，重复执行此步骤，直到可迭代对象不能提供数据为止
+ 可迭代对象提供完所有元素后，执行else子句部分的语句块2，然后推出此for语句
+ else子句部分可以省略（同while语句类似）
+ 当循环内部使用break终止循环时，else子句部分语句不会执行。

## range函数
格式见：
```python
help(range)
```

**函数：**

+ range(stop)  

   + 从零开始，每次生成一个整数后加1操作，直到stop为止（不包括stop）

+ range(start, stop[, step])

   + 从start开始，每次生成一个整数后移动step，直到stop为止（不包括stop，且step可以是负整数）

**作用**

用来创建一个生成一系列整数的可迭代对象（也叫整数序列生成器）

**说明**

range返回的对象是可迭代对象，可以用于for语句中

**示例：**

+ range(4)            #0,1,2,3
+ range(3,6)          #3,4,5
+ range(1,10,2)       #1,3,5,7,9
+ range(5,0,-2)       #5,3,1

## for语句嵌套

for语句内部可以放任意语句，包括for语句和while语句

**示例：**

```python
for x in "ABC":
    for y in '123':
        print(x + y)
```
 
       
## continue 语句

**作用：**

用于循环语句当中（while,for）不在执行本次循环内continue之后的语句，重新开始一次新的循环

**说明：**

+ while语句中，执行continue语句将会直接跳到while语句的真值表达式处重新判断循环条件
+ for语句中，执行continue语句，将会从可迭代对象中取下一个元素，绑定变量后再次进行循环

**示例：**
```python
for x in range(5):
    if x == 2:
        continue
    print(x)
```

    
    
## 循环总结

+ while语句
+ for语句
   +   -字符串
   +   -range函数
+ break语句
+ continue语句

## 列表 list

+ 列表由一系列特定元素组成的，元素与元素之间没有任何关联关系，但他们之间有先后顺序关系
+ 列表是一种容器
+ 列表是序列的一种
+ 列表是可以被改变的序列

**python中的序列类型简介（sequence）**

+ 字符串str
+ 列表 list
+ 元组 tuple
+ 字节串 bytes
+ 字节数组bytearray

**创建空列表的字面值：**

+    L = []  #L绑定空列表

**创建非空列表：**

+    L = [1, 2, 3, 4]
+    L = ["北京","上海", "重庆"]
+    L = [1, 'two', 3, '四']
+    L = [1, 2, [3.1, 3.2, 3.3], 4]

**列表的构造函数list**

+ list() 生成一个空的列表，等同于[]
+ list(iterable) 用可迭代对象创建一个列表

**示例：**

+    L = list()   #L为空列表
+    L = list("ABCD") # L -> ['A','B','C','D']
+    L = list(range(1, 20, 2))
   
**列表的运算**

+  用于拼接列表
  + x = [1, 3]
  + y = [2, 4]
  + z = x + y             #用于原列表与右侧可迭代对象进行拼接，生产新的列表
  +  x  = [1, 2, 3]
  +  x += [4, 5, 6]
  +  x += 'ABC'           #右侧是可迭代对象皆可
   
+  生成重复的列表
  +  x = [1,2,3] * 2

+  *= 用于生成重复的列表，同时用变量绑定新列表

+    x = [1, 2]
+    x *= 3


**列表的比较运算符**

运算符:

+ < <= > >= == !=
+ x = [1,2,3]
+ y = [2,3,4]
+ x != y                      #True
+ x > [1, 2]                  #True
+ x < y                       #True
+ [1, 3, 2] > [1, 2, 3]       #True
+ ['AB', 'CD'] >['AC', 'BD']  #False
+ [1, 'two'] > ['two', 1]     #TypeError