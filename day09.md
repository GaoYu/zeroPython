##ϵͳģ��sys

https://docs.python.org/3/library/sys.html?highlight=sys#module-sys

##�Զ���ģ��

�ο� mymod1.py  \
     test_mymod1.py

```python
#��ģ�����û��Զ���ģ��
#����С��д�˴�ģ��

def myfun1():
    print('���ڵ���mymod1�����myfun1()')

def myfun2():
    print('���ڵ���mymod1�����myfun2()')

name1 = 'audi'

name2 = 'tesla'
```
```python
import mymod1#����ģ��mymod1.py
mymod1.myfun1()#����mymod1���myfun1()����
print(mymod1.name1)

from mymod1 import name2
print("mymod1���name2Ϊ��", name2)
from mymod1 import *
myfun2()

```

�Զ���ģ���ģ����������ϡ���ʶ��������������ͬ��������

**ģ���и��Զ�����������**     


**ģ�黯����ŵ�**

+ ���ڶ��˺�������
+ ʹ���������ά��
+ ��ߴ���ĸ�����
+ �����ڽ����������ͻ����

##ģ��ĵ��������

###import��� ����ģ���·��˳��
+ 1.������������ʱ��·��
+ 2.sys.path �ṩ��·��
+ 3.��������ģ��

**sys.path��һ���洢ģ���������б�**

+ 1.���Զ���ģ�������Ӧ��·���£����Ե���
+ 2.���԰��Զ���ģ���·��������sys.path�б��У�sys.path.append��

###ģ��ļ��ع���

+ ģ�鵼��ʱ��ģ�����������ִ��
+ ���һ��ģ���Ѿ����룬���ٴε���ʱ��������ִ��ģ���ڵ����

**ģ������¼���**
```python
import mymod3
import  imp
imp.reload(mymod3)#���¼���
```

###ģ�鵼���ִ�еĹ���

+ ��������ص�·����ģ�飨.py�ļ���
+ �ж��Ƿ��д�ģ���Ӧ��.pyc�ļ����������pyc�ļ��ұ�.py�ļ��£���ֱ�Ӽ���.pyc�ļ�
+ ������.py�ļ�ֱ������.pyc���ٽ��м���

**pycģ��ı����ļ�**

mymod1.py  ----����-------mymod1.pyc ------����ִ��------python3


###ģ�������

**���Ե�ʵ����ģ���ڵ�ȫ�ֱ���**

**ģ����Ԥ�õ�����**

+ __doc__����
    + ������ģ����ĵ��ַ�����ģ���ڵ�һ��û�и�ֵ���κα������ַ���Ϊģ����ĵ��ַ�����

+ __file__����
    + ������ģ���Ӧ���ĵ�·����
    + �����ڽ�ģ�飬����·����û��__file__���ԣ�
    + ��������ģ�飬��·�������ַ���

+ __name__����
    + ������¼ģ����������֣���¼ģ������
    + �����ж��Ƿ�Ϊ��ģ�飨�������е�ģ�飩
    + ����ģ��Ϊ��ģ���ǣ�__name__�󶨡�__main__��
    + ����ģ�鲻����ģ��ʱ�������԰�ģ����
    
+ __all__�б�
    + ������ſɵ������Ե��ַ����б�
    + ����from import *��䵼��ʱ��ֻ����__all__�б��ڵ�����
    
    
**ģ�����������**

ģ������'_'��ͷ�����ԣ���from import * ��䵼��ʱ�����������룬ͨ������Щ����Ϊ��������

**���ģ��random**

      ����ģ���������������ģ�� \
  
      python_base_docs_html/���ģ��random.html

**���ֲ���**

##����ģ����� package

��ģ�����ļ��е���֯��ʽ���з�������ķ����������ڷ�ֹ������ͻ����������Ҫʱ����һ����ģ�������ȫ��ģ�顣

**ʾ��**

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
        

**"__init__"�ļ�**        

+ ������б�����ڵ��ļ�    
+ '__init__.py'���ڰ�����ʱ���Զ�����

+ ��д�˰�������
+ ���ڲ���д�ĵ��ַ���
+ ��__init__.py�ڿ��Լ��ش˰���������һЩ����ģ��

**���ĵ���**

����import�����Ե������ͬģ��ĵ������

```python
import ���� [as ������]
import ����.ģ����[as ģ������]
import ����.�Ӱ���.ģ����

from ���� import ģ����[as ģ������] 
from ����.�Ӱ��� import ģ����[as ģ������] 
from ����.�Ӱ���.ģ���� import ������[as ��������]

from ���� import *
from ����.ģ���� import * 
```

**����__init__.py�ڵ�__all__�б�**

+ ������¼�˰�����Щ����ģ������from  �� import *��䵼��ʱ�Ƿ񱻵���
+ ֻ��from import *���������

##������Ե���

��ֵ����ģ����໥����

**�﷨**
```python
from ���·������ģ�� import ���Ի�ģ����

from ���·������ģ�� import *
```
**���·��**

+ . ������ǰĿ¼
+ ..������һ��Ŀ¼
+ ...�����϶���Ŀ¼
+ .....��������

��Ե���ʱ���ܳ��������ⲿ

##���ļ���·��

ͬģ��ļ���·����ͬ

+ �������ļ���
+ sys.path������·��


##�쳣exception

**����**

+ ������ָ�����߼������ȵ���һ�������޷�����ִ�е�����
+ ��Щ�������޷�Ԥ֪��

**�쳣**

+ �쳣ʱ�������ʱ��ʶ��һ��״̬
+ ���쳣����ʱ�����򲻻�������ִ�У���תȥ���ô˺����ĵط����������˴��󲢻ָ�����״̬
  
+ ֪ͨ�ϲ�������д��������Ҫ����
+ �����ź�֪ͨ


###try ���

+ try - except���
+ try - finally���

**try - except**

���Բ�׽�쳣��������תΪ����״̬������ִ��
```python
try:
    ���ܴ����쳣�����
except ��������1[as ����1]:
    �쳣�������1
except ��������2[as ����2]:
    �쳣�������2
except (��������3,��������4,...)[as ����3]:
    �쳣�������3
...
exept:
    �쳣�������other
else:
    δ�����쳣ʱִ�е����
finally:
    ����ִ�е����
```    

**�﷨˵��**

+ as  �Ӿ����ڰ󶨴������ı���������ʡ�Բ�д
+ except �Ӿ������һ��������������Ҫ��һ��
+ else �Ӿ����ֻ����һ����Ҳ����ʡ�Բ�д
+ finally �Ӿ����ֻ����һ����Ҳ����ʡ�Բ�д

**try - finally**

```python
try:
    ���ܴ����쳣�����
finally:
    �������
```

+ finally �Ӿ䲻����ʡ��
+ һ��������except�Ӿ�
+ ͨ��try-finally��������������쳣ʱ����Ҫ���������飬�����쳣�Ƿ�����finally�Ӿ䶼�ᱻִ��
+ try-finally��䲻��ı����ģ�����/�쳣��״̬



###raise���

����һ�������ó�������쳣״̬

```python
raise �쳣����

raise �쳣����
```

###assert��䣨������䣩

**�﷨**

```python
assert ��ֵ����ʽ���������ݣ�ͨ�����ַ�����
```

����ֵ����ʽΪFalseʱ���ô������ݴ���һ��AssertionError���͵Ĵ��󣬲������쳣״̬

**������**
```python
if ��ֵ����ʽ == False:
    raise AssertionError(��������)
```    






   