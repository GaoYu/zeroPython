---
output:
  html_document: default
  word_document: default
---
#面向对象编程
##异常(高级)
**回顾异常相关的语句:**
 
+ try-except    用来捕获异常通知
+ try-finally   用来做一定要做的事情
+ raise         用来发生异常通知
+ assert  用来根据条件来发出AssertionError类型的异常通知

###with 语句
**语法:**
```python
with 表达式1 [as 变量1], 表达式2 [as 变量2]:
    语句块
```
**作用:**

使用于对资源进行访问的场合,确保使用过程中不管是否发生异常,都会执行必须的'清理'操作,并释放资源。如: 文件使用后自动关闭, 线程中锁的自动获取和释放等
  
**示例见:**

01_with.py

**说明:**

能够用于with语句进行管理的对象必须是环境管理器

###环境管理器:
+ 1. 类内有__enter__ 和 __exit__实例方法的类被称为环境管理器
+ 2. 能够用with语句管理的对象必须是环境管理器
+ 3. __enter__方法将在进入with语句时被调用,并返回由 as变量管理的对象
+ 4. __exit__将在离开with语句时被调用,且可以用参数来判断在离开with语句时是否有异常发生并做出相应的处理

**示例:**
```python
class A:
   def __enter__(self):
      print("已进入with语句")
      return self  # 返回的对象将由 as绑定
   def __exit__(self, exc_type, exc_val, exc_tb):
      print("已离开with语句")
```      
**详见:**

03_context.py

###对象的属性管理函数

+ getattr(obj, name[, default])	从一个对象得到对象的属性；getattr(x, 'y') 等同于x.y; 当属性不存在时,如果给出default参数,则返回default,如果没有给出default则产生一个AttributeError错误
+ hasattr(obj, name)	用给定的name返回对象obj是否有此属性,此种做法可以避免在getattr(obj, name)时引发错误
+ setattr(obj, name, value)	给对象obj的名为name的属性设置相应的值value, set(x, 'y', v) 等同于 x.y = v
+ delattr(obj, name)	删除对象obj中的name属性, delattr(x, 'y') 等同于 del x.y

###运算符的重载

让自定义的类生成的对象能够使用运算符进行操作

**作用**

+ 让自定义的类的实例对象像内建对象一样运行运算符操作
+ 让程序简洁易读
+ 对自定义的对象，将运算符赋予新的运算规则


**算术运算符的重载**

```python
  __add__(self, rhs)        self + rhs   加法
  __sub__(self, rhs)        self - rhs   减法
  __mul__(self, rhs)        self * rhs   乘法
  __truediv__(self, rhs)    self / rhs   除法
  __floordiv__(self, rhs)   self // rhs  地板除法
  __mod__(self, rhs)        self % rhs   求余
  __pow__(self, rhs)        self ** rhs  冪
```

**示例**

06_mynumber.py

###反向算术运算符的重载

当左手边的类型为内建类型，右手边为自定义类型时，用以下方法重载

```python
  __radd__(self, lhs)        lhs + self   加法
  __rsub__(self, lhs)        lhs - self   减法
  __rmul__(self, lhs)        lhs * self   乘法
  __rtruediv__(self, lhs)    lhs / self   除法
  __rfloordiv__(self, lhs)   lhs // self  地板除法
  __rmod__(self, lhs)        lhs % self   求余
  __rpow__(self, lhs)        lhs ** self  冪

```

**示例见:**

  07_mylist.py

###复合赋值算术运算符的重载
```python
  __iadd__(self, rhs)        self += rhs   加法
  __isub__(self, rhs)        self -= rhs   减法
  __imul__(self, rhs)        self *= rhs   乘法
  __itruediv__(self, rhs)    self /= rhs   除法
  __ifloordiv__(self, rhs)   self //= rhs  地板除法
  __imod__(self, rhs)        self %= rhs   求余
  __ipow__(self, rhs)        self **= rhs  冪
```

**示例见:**

  08_mylist.py


**如下:**
```python
L = [1,2,3]
# 问题1
def f1():
   global L  # 为什么这里必须加global L
   L = L + [4,5,6]　　# 等同于 L = L.__add__([4,5,6])
f1()
print(L)
# 问题2
def f2():
   # 为什么以下就不加 global　L
   L += [4,5, 6]  # L.__iadd__([4,5,6])
f2()
print(L)
```

###比较运算符的重载
```python
  __lt__(self, rhs)     self <  rhs   小于
  __le__(self, rhs)     self <= rhs   小于等于
  __gt__(self, rhs)     self >  rhs   大于
  __ge__(self, rhs)     self >= rhs   大于等于
  __eq__(self, rhs)     self == rhs   等于
  __ne__(self, rhs)     self != rhs   不等于
```
**注:**

  比较运算符通常返回True或False

###位运算符重载
```python
__invert__(self)       　 ~ self   　　　　取反(一元运算符)
__and__(self, rhs)       self & 　rhs  位与
__or__(self, rhs)        self | 　rhs  位或
__xor__(self, rhs)       self ^ 　rhs  位异或
__lshift__(self, rhs)    self << rhs  左移
__rshift__(self, rhs)    self >> rhs  右移
```
###反向位运算符重载
```python
  __rand__(self, lhs)       lhs & 　self  位与
  __ror__(self, lhs)        lhs | 　self  位或
  __rxor__(self, lhs)       lhs ^ 　self  位异或
  __rlshift__(self, lhs)    lhs << self  左移
  __rrshift__(self, lhs)    lhs >> self  右移
```
###复合赋值位运算符重载
```python
  __iand__(self, rhs)       self &= 　rhs  位与
  __ior__(self, rhs)        self |= 　rhs  位或
  __ixor__(self, rhs)       self ^= 　rhs  位异或
  __ilshift__(self, rhs)    self <<= rhs  左移
  __irshift__(self, rhs)    self >>= rhs  右移
```

###一元运算符的重载
```python
  __neg__(self)        - self   负号
  __pos__(self)　　　　　　　　+ self   正号
  __invert__(self)     ~ self   取反
````
###一元运算符的重载方法:
```python
  class 类名:
      def __xxx__(self):
          ...
```
**示例见:**

  09_mylist.py

###运算符重载说明
+ **运算符重载不能改变运算符的优先级**
+ **python命名最好用驼峰命名法**
    + MyList 大驼峰
    + getStudentAge 小驼峰

###in / not in 运算符的重载

**重载方法**
```python
def __contains__(self, e)   e in self    成员运算
```

###索引和切片运算符的重载

```python
__getitem__(self, i)     x = self[i]  索引/切片取值
__setitem__(self, i, v)  self[i] = v  索引/切片赋值
__delitem__(self, i)     del self[i] del语句删除索引等
```

**作用**

让自定义的类型的对象能够支持索引和切片操作

**示例**

11_mylist.py


###slice构造函数

**作用**

用于创建一个slice切片对象，此对象存储一个节片的起始值，终止值和步长信息

```python
slice(start, stop= None, step= None) 
```

**slice的对象属性**

+ s.start 切片起始值，默认为None
+ s.stop  切片终止值，默认为None
+ s.step  切片步长，  默认为None

**示例**

12_mylist_slice.py