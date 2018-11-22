---
output:
  html_document: default
  word_document: default
---
#���������
##�쳣(�߼�)
**�ع��쳣��ص����:**
 
+ try-except    ���������쳣֪ͨ
+ try-finally   ������һ��Ҫ��������
+ raise         ���������쳣֪ͨ
+ assert  ������������������AssertionError���͵��쳣֪ͨ

###with ���
**�﷨:**
```python
with ���ʽ1 [as ����1], ���ʽ2 [as ����2]:
    ����
```
**����:**

ʹ���ڶ���Դ���з��ʵĳ���,ȷ��ʹ�ù����в����Ƿ����쳣,����ִ�б����'����'����,���ͷ���Դ����: �ļ�ʹ�ú��Զ��ر�, �߳��������Զ���ȡ���ͷŵ�
  
**ʾ����:**

01_with.py

**˵��:**

�ܹ�����with�����й���Ķ�������ǻ���������

###����������:
+ 1. ������__enter__ �� __exit__ʵ���������౻��Ϊ����������
+ 2. �ܹ���with������Ķ�������ǻ���������
+ 3. __enter__�������ڽ���with���ʱ������,�������� as��������Ķ���
+ 4. __exit__�����뿪with���ʱ������,�ҿ����ò������ж����뿪with���ʱ�Ƿ����쳣������������Ӧ�Ĵ���

**ʾ��:**
```python
class A:
   def __enter__(self):
      print("�ѽ���with���")
      return self  # ���صĶ����� as��
   def __exit__(self, exc_type, exc_val, exc_tb):
      print("���뿪with���")
```      
**���:**

03_context.py

###��������Թ�����

+ getattr(obj, name[, default])	��һ������õ���������ԣ�getattr(x, 'y') ��ͬ��x.y; �����Բ�����ʱ,�������default����,�򷵻�default,���û�и���default�����һ��AttributeError����
+ hasattr(obj, name)	�ø�����name���ض���obj�Ƿ��д�����,�����������Ա�����getattr(obj, name)ʱ��������
+ setattr(obj, name, value)	������obj����Ϊname������������Ӧ��ֵvalue, set(x, 'y', v) ��ͬ�� x.y = v
+ delattr(obj, name)	ɾ������obj�е�name����, delattr(x, 'y') ��ͬ�� del x.y

###�����������

���Զ���������ɵĶ����ܹ�ʹ����������в���

**����**

+ ���Զ�������ʵ���������ڽ�����һ���������������
+ �ó������׶�
+ ���Զ���Ķ��󣬽�����������µ��������


**���������������**

```python
  __add__(self, rhs)        self + rhs   �ӷ�
  __sub__(self, rhs)        self - rhs   ����
  __mul__(self, rhs)        self * rhs   �˷�
  __truediv__(self, rhs)    self / rhs   ����
  __floordiv__(self, rhs)   self // rhs  �ذ����
  __mod__(self, rhs)        self % rhs   ����
  __pow__(self, rhs)        self ** rhs  ��
```

**ʾ��**

06_mynumber.py

###�������������������

�����ֱߵ�����Ϊ�ڽ����ͣ����ֱ�Ϊ�Զ�������ʱ�������·�������

```python
  __radd__(self, lhs)        lhs + self   �ӷ�
  __rsub__(self, lhs)        lhs - self   ����
  __rmul__(self, lhs)        lhs * self   �˷�
  __rtruediv__(self, lhs)    lhs / self   ����
  __rfloordiv__(self, lhs)   lhs // self  �ذ����
  __rmod__(self, lhs)        lhs % self   ����
  __rpow__(self, lhs)        lhs ** self  ��

```

**ʾ����:**

  07_mylist.py

###���ϸ�ֵ���������������
```python
  __iadd__(self, rhs)        self += rhs   �ӷ�
  __isub__(self, rhs)        self -= rhs   ����
  __imul__(self, rhs)        self *= rhs   �˷�
  __itruediv__(self, rhs)    self /= rhs   ����
  __ifloordiv__(self, rhs)   self //= rhs  �ذ����
  __imod__(self, rhs)        self %= rhs   ����
  __ipow__(self, rhs)        self **= rhs  ��
```

**ʾ����:**

  08_mylist.py


**����:**
```python
L = [1,2,3]
# ����1
def f1():
   global L  # Ϊʲô��������global L
   L = L + [4,5,6]����# ��ͬ�� L = L.__add__([4,5,6])
f1()
print(L)
# ����2
def f2():
   # Ϊʲô���¾Ͳ��� global��L
   L += [4,5, 6]  # L.__iadd__([4,5,6])
f2()
print(L)
```

###�Ƚ������������
```python
  __lt__(self, rhs)     self <  rhs   С��
  __le__(self, rhs)     self <= rhs   С�ڵ���
  __gt__(self, rhs)     self >  rhs   ����
  __ge__(self, rhs)     self >= rhs   ���ڵ���
  __eq__(self, rhs)     self == rhs   ����
  __ne__(self, rhs)     self != rhs   ������
```
**ע:**

  �Ƚ������ͨ������True��False

###λ���������
```python
__invert__(self)       �� ~ self   ��������ȡ��(һԪ�����)
__and__(self, rhs)       self & ��rhs  λ��
__or__(self, rhs)        self | ��rhs  λ��
__xor__(self, rhs)       self ^ ��rhs  λ���
__lshift__(self, rhs)    self << rhs  ����
__rshift__(self, rhs)    self >> rhs  ����
```
###����λ���������
```python
  __rand__(self, lhs)       lhs & ��self  λ��
  __ror__(self, lhs)        lhs | ��self  λ��
  __rxor__(self, lhs)       lhs ^ ��self  λ���
  __rlshift__(self, lhs)    lhs << self  ����
  __rrshift__(self, lhs)    lhs >> self  ����
```
###���ϸ�ֵλ���������
```python
  __iand__(self, rhs)       self &= ��rhs  λ��
  __ior__(self, rhs)        self |= ��rhs  λ��
  __ixor__(self, rhs)       self ^= ��rhs  λ���
  __ilshift__(self, rhs)    self <<= rhs  ����
  __irshift__(self, rhs)    self >>= rhs  ����
```

###һԪ�����������
```python
  __neg__(self)        - self   ����
  __pos__(self)����������������+ self   ����
  __invert__(self)     ~ self   ȡ��
````
###һԪ����������ط���:
```python
  class ����:
      def __xxx__(self):
          ...
```
**ʾ����:**

  09_mylist.py

###���������˵��
+ **��������ز��ܸı�����������ȼ�**
+ **python����������շ�������**
    + MyList ���շ�
    + getStudentAge С�շ�

###in / not in �����������

**���ط���**
```python
def __contains__(self, e)   e in self    ��Ա����
```

###��������Ƭ�����������

```python
__getitem__(self, i)     x = self[i]  ����/��Ƭȡֵ
__setitem__(self, i, v)  self[i] = v  ����/��Ƭ��ֵ
__delitem__(self, i)     del self[i] del���ɾ��������
```

**����**

���Զ�������͵Ķ����ܹ�֧����������Ƭ����

**ʾ��**

11_mylist.py


###slice���캯��

**����**

���ڴ���һ��slice��Ƭ���󣬴˶���洢һ����Ƭ����ʼֵ����ֵֹ�Ͳ�����Ϣ

```python
slice(start, stop= None, step= None) 
```

**slice�Ķ�������**

+ s.start ��Ƭ��ʼֵ��Ĭ��ΪNone
+ s.stop  ��Ƭ��ֵֹ��Ĭ��ΪNone
+ s.step  ��Ƭ������  Ĭ��ΪNone

**ʾ��**

12_mylist_slice.py