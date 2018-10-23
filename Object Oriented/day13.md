#面向对象编程
**用于类的函数**

issubclass(cls, class_or_tuple)

判读一个类是否继承自其他的类，如果此类cls是class或tuple中的一个派生子类则返回True，否则返回False

**示例**
```python
class A:
    pass
class B(A):
    pass
class C(B):
    pass
issubclass(C, (A, B))  #True
issubclass(C, (int, str)) #False
```
##封装 enclosure

封装是指隐藏类的实现细节，让使用者不用关心这些细节，封装的目的是让使用者尽可能少的对实例变量（属性）进行操作。

**私有属性**

python类中，以双下划线'__'开头，不以双下滑线结尾的标识符为私有成员，在类的外部无法直接访问

**示例**

01_enclosure.py


##多态 polymorphic

多种状态

多态是指在继承/派生关系的类中，调用基类对象的方法，实际能调用子类的覆盖版本方法的现象叫多态。

**说明**

+ 多态调用的方法与对象相关，不与类型相关
+ python的全部对象都只有“运行时状态(动态)”,没有“C++/java”里的“编译时状态（静态）”

**示例**

02_poly.py

##多继承 multiple inheritance

多继承是指一个子类继承自两个或两个以上的基类

###语法
```python
class 类名(基类名1, 基类名2, ...):
    语句块
```

**说明**

1.一个子类同时继承自多个父类，父类中的方法可以同时被继承下来

2.如果两个父类中有同名的方法，而在子类中又没有覆盖此方法时，调用结果难以确定

**示例**

03_multi_inherit.py

###多继承的缺陷

标识符(名字空间冲突问题)， 要谨慎使用多继承

**示例**

04_multi_inherit_bug.py

###继承的MRO(Method Resolution Order)问题

类内的__mro__属性用来记录继承方法的查找顺序

**示例**

05_mro.py

