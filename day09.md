##系统模块sys

https://docs.python.org/3/library/sys.html?highlight=sys#module-sys

##自定义模块

参考 mymod1.py  \
     test_mymod1.py

```python
#此模块是用户自定义模块
#假设小张写了此模块

def myfun1():
    print('正在调用mymod1里面的myfun1()')

def myfun2():
    print('正在调用mymod1里面的myfun2()')

name1 = 'audi'

name2 = 'tesla'
```
```python
import mymod1#导入模块mymod1.py
mymod1.myfun1()#调用mymod1里的myfun1()函数
print(mymod1.name1)

from mymod1 import name2
print("mymod1里的name2为：", name2)
from mymod1 import *
myfun2()

```

自定义模块的模块名必须符合“标识符”的命名规则（同变量名）

**模块有各自独立的作用域**     


**模块化编程优点**

+ 利于多人合作开发
+ 使代码更易于维护
+ 提高代码的复用率
+ 有利于解决变量名冲突问题

##模块的导入与加载

###import语句 搜索模块的路径顺序
+ 1.搜索程序运行时的路径
+ 2.sys.path 提供的路径
+ 3.搜索内置模块

**sys.path是一个存储模块搜索的列表**

+ 1.把自定义模块放在相应的路径下，可以导入
+ 2.可以把自定义模块的路径添加在sys.path列表中（sys.path.append）

###模块的加载过程

+ 模块导入时，模块的所有语句会执行
+ 如果一个模块已经导入，则再次导入时不会重新执行模块内的语句

**模块的重新加载**
```python
import mymod3
import  imp
imp.reload(mymod3)#重新加载
```

###模块导入和执行的过程

+ 先搜索相关的路径找模块（.py文件）
+ 判断是否有此模块对应的.pyc文件，如果存在pyc文件且比.py文件新，则直接加载.pyc文件
+ 否则用.py文件直接生成.pyc后再进行加载

**pyc模块的编译文件**

mymod1.py  ----编译-------mymod1.pyc ------解释执行------python3


###模块的属性

**属性的实质是模块内的全局变量**

**模块内预置的属性**

+ __doc__属性
    + 用来绑定模块的文档字符串（模块内第一个没有赋值给任何变量的字符串为模块的文档字符串）

+ __file__属性
    + 用来绑定模块对应的文档路径名
    + 对于内建模块，不绑定路径（没有__file__属性）
    + 对于其他模块，绑定路径名的字符串

+ __name__属性
    + 用来记录模块的自身名字（记录模块名）
    + 用来判断是否为主模块（最先运行的模块）
    + 当此模块为主模块是，__name__绑定‘__main__’
    + 当此模块不是主模块时，此属性绑定模块名
    
+ __all__列表
    + 用来存放可导出属性的字符串列表
    + 当用from import *语句导入时，只导入__all__列表内的属性
    
    
**模块的隐藏属性**

模块中以'_'开头的属性，在from import * 语句导入时，将不被导入，通常称这些属性为隐藏属性

**随机模块random**

      用于模拟或生成随机输出的模块 \
  
      python_base_docs_html/随机模块random.html

**二分查找**

##包（模块包） package

将模块以文件夹的组织形式进行分组管理的方法，有利于防止命名冲突，可以在需要时加载一部分模块而不是全部模块。

**示例**

+ mypack/ 
    + __init__.py
    + menu.py
    + games/
        + __init__.py
        + contra.py
        + supermario.py
        + tanks.py
    + office/
        + __init__.py
        + excel.py
        + word.py
        

**"__init__"文件**        

+ 常规包中必须存在的文件    
+ '__init__.py'会在包加载时被自动调用

+ 编写此包的内容
+ 在内部填写文档字符串
+ 在__init__.py内可以加载此包所依赖的一些其他模块

**包的导入**

三条import语句可以导入包（同模块的导入规则）

```python
import 包名 [as 包别名]
import 包名.模块名[as 模块新名]
import 包名.子包名.模块名

from 包名 import 模块名[as 模块新名] 
from 包名.子包名 import 模块名[as 模块新名] 
from 包名.子包名.模块名 import 属性名[as 属性新名]

from 包名 import *
from 包名.模块名 import * 
```

**包的__init__.py内的__all__列表**

+ 用来记录此包内哪些包或模块在用from  包 import *语句导入时是否被调用
+ 只对from import *语句起作用

##包的相对导入

是值包内模块的相互导入

**语法**
```python
from 相对路径包或模块 import 属性或模块名

from 相对路径包或模块 import *
```
**相对路径**

+ . 代表当前目录
+ ..代表上一级目录
+ ...代表上二级目录
+ .....依次类推

相对导入时不能超出包的外部

##包的加载路径

同模块的加载路径相同

+ 档期那文件夹
+ sys.path给出的路径


##异常exception

**错误**

+ 错误是指由于逻辑或语句等导致一个程序无法正常执行的问题
+ 有些错误是无法预知的

**异常**

+ 异常时程序出错时标识的一种状态
+ 当异常发生时，程序不会再向下执行，而转去调用此函数的地方，待处理此错误并恢复正常状态
  
+ 通知上层调用者有错误产生需要处理
+ 用作信号通知


###try 语句

+ try - except语句
+ try - finally语句

**try - except**

尝试捕捉异常，将程序转为正常状态并继续执行
```python
try:
    可能触发异常的语句
except 错误类型1[as 变量1]:
    异常处理语句1
except 错误类型2[as 变量2]:
    异常处理语句2
except (错误类型3,错误类型4,...)[as 变量3]:
    异常处理语句3
...
exept:
    异常处理语句other
else:
    未发生异常时执行的语句
finally:
    最终执行的语句
```    

**语法说明**

+ as  子句用于绑定错误对象的变量，可以省略不写
+ except 子句可以有一个或多个，但至少要有一个
+ else 子句最多只能有一个，也可以省略不写
+ finally 子句最多只能有一个，也可以省略不写

**try - finally**

```python
try:
    可能触发异常的语句
finally:
    最终语句
```

+ finally 子句不可以省略
+ 一定不存在except子句
+ 通常try-finally语句用来做触发异常时必须要处理的事情，无论异常是否发生，finally子句都会被执行
+ try-finally语句不会改变程序的（正常/异常）状态



###raise语句

触发一个错误，让程序进入异常状态

```python
raise 异常类型

raise 异常对象
```

###assert语句（断言语句）

**语法**

```python
assert 真值表达式，错误数据（通常是字符串）
```

当真值表达式为False时，用错误数据创建一个AssertionError类型的错误，并进入异常状态

**类似于**
```python
if 真值表达式 == False:
    raise AssertionError(错误数据)
```    

**为什么要用异常处理机制**

+ 在程序调用层数较深时，向调主函数传递错误信息需要用return语句层层传递比较麻烦，所以用异常处理机制

参考built_house.py




   
