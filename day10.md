#������iterator��������generator

##������iterator
+ ��ָ��iter(�ɵ�������)�������صĶ���ʾ����
+ ������������next(it)������ȡ�ɵ������������

###����������
+ iter(iterable)  �ӿɵ��������з���һ����������iterable������һ�����ṩ�������Ŀɵ�������
+ next(iterator)  �ӵ�����iterator�л�ȡ��һ����¼������޷���ȡ��һ����¼���򴥷�StopIteration�쳣

**˵��**

+ �������Ƿ��ʿɵ��������һ�ַ�ʽ
+ ������ֻ����ǰȡֵ���������
+ ��iter�������Է���һ���ɵ�������ĵ�����

**ʾ��**
```python
#��while���ѭ�������б�
L = [2, 3, 5, 7]
it = iter(L)  #��L����һ��������
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        print("��������")
        break
```

##������ Generator(python2.5�Ժ���)

���������ܹ���̬�ṩ���ݵĶ�������������Ҳ�ǿɵ�������ʵ����

**����������**

+ 1.����������
+ 2.���������ʽ


###����������

���� **yield**���ĺ������������������˺���������ʱ������һ������������

**yield���**
```python
yield ���ʽ
```
+ yield����def������,Ŀ���ǽ��˺�����Ϊ����������ʹ��
+ yield�����������ݣ���������next(it)����ʹ��

**ʾ��**
```python
def myyield():
    '''�˺���Ϊ����������'''
    print("��������2") #ֻ��next�Ż�ִ��
    yield 2  #����2
    print("��������3")
    yield 3  #����3
    print("��������5")
    yield 5  #����5
    print("myyield��������")  
#��for ������myyield����

for x in myyield():
    print(x)

gen = myyield()
it = iter(gen)
next(it)
```

**����������˵��**

+ �����������ĵ��ý�����һ������������������������һ���ɵ�������
+ ����������������returnʱ������һ��StopIteration�쳣��֪ͨnext(it)�����������ṩ����

###���������ʽ

**�﷨**
```python
(���ʽ for ���� in �ɵ������� [if ��ֵ���ʽ])
```

**����**

���Ƶ�ʽ����ʽ����һ���µ�������

**ʾ��**
```python
gen = (x**2 for x in range(1,5))
it = iter(gen)
next(it) #1
next(it) #4
next(it) #9
next(it) #16
next(it) #StopIteration
```
**�ŵ�**

��ռ���ڴ�ռ�


**�б��Ƶ�ʽ�����������ʽ����**
```python
L = [1,2,3,4]
gen = (x for x in L) #gen ��������
lst = [x for x in L] #lst ���б�
L[1] = 222  #�ı�ԭ�б�ĵڶ���Ԫ��
for x in lst:
    print(x)  #1,2,3,4����

for x in gen:
    print(x)  #1,222,3,4,�ڶ�������222
```

##�������ߺ���

�������ߺ���������������һ�����Ի��Ŀɵ�������

+ zip(iter1 [, iter2, iter3,...])

����һ��zip���󣬴˶�����������һ��Ԫ�飬��Ԫ��ĸ�������С�Ŀɵ����������

+ enumerate(iterable[, start])

���ɴ�������ö�ٶ��󣬷��ص�������Ϊ����-ֵ�ԣ�index-value)�ԣ�Ĭ��������0��ʼ��Ҳ����ʹ��start��

**ʾ��zip**
```python
numbers = [10086, 10000, 10010, 95588]
names = ['�й��ƶ�','�й�����','�й���ͨ']
for n, a in zip(numbers, names):
    print(a, '�Ŀͷ�������', n)
for x in zip(numbers, names):
    print x
#zip����һ���ֵ�
d = dict(zip(names, numbers)    #zip����
```

**ʾ��enumerate**
```python
names = ['�й��ƶ�','�й�����','�й���ͨ']
for x in enumerate(names):
    print(x)
    #����-Ԫ��
    index, element = x
    print('����',index,'��Ӧ��Ԫ����',element)

#������100��ʼ
for x in enumerate(names, start = 100):
    print(x)
```

##�ֽڴ�bytes���ֽ�����bytearray

###�ֽڴ�bytes

**����**

�洢���ֽ�Ϊ��λ������

+ �ֽڴ��ǲ��ɱ���ֽ�����
+ �ֽ���0~255֮�������

**�������ֽڴ�������ֵ**

+ b''
+ b""
+ b''''''
+ b""""""
+ B''
+ B""
+ B''''''
+ B""""""

**�ǿ��ֽڴ�������ֵ**

+ b'ABCD'
+ b'\x41\x41'


**�ֽڴ��Ĺ��캯��**

+ bytes()������һ���յ��ֽڴ�����ͬ��b''
+ bytes(���Ϳɵ�������)  �ÿɵ��������ʼ��һ���ֽڴ�
+ bytes(����n)  ����n��ֵΪ����ֽڴ�
+ bytes(�ַ�����encoding='utf-8')  ���ַ�����ת����������һ���ֽڴ�

**�ֽڴ�������**

+, +=, *,*=

<,<=,>,>=,==,!=

in,not in

����/��Ƭ

**ʾ��**

```python
b = b'abc' + b'123' #b = b'abc123'
b += b'ABC'         #b=b'abc123ABC'
b'ABD'>b'ABC'       #True

b = b'ABCD'
65 in b            #True
b'A' in b          #True

b= b'ABCD'
b[-1]              #68
```

**�������к���**

len,max,min,sum,all,any

**bytes��str����**

+ bytes �洢�ֽڣ�0~255��
+ str�洢Unicode�ַ���0~65535��

**bytes��str��ת��**

+ str -----����(encode)------bytes  \ b=s.encode('utf-8')

+ bytest -----����(decode)-----str  \ s = b.decode('utf-8')

###�ֽ�����bytearray

�ɱ���ֽ�����

**���캯��**
 
+ bytearray() �����յ��ֽ�����
+ bytearray(����)
+ bytearray(�����ɵ�������)
+ bytearray(�ַ���,encoding='utf-8')

���ϲ�����ͬ���ֽڴ�

**�ֽ����������**

+, +=, *,*=

<,<=,>,>=,==,!=

in,not in

����/��Ƭ

**bytearray����ط���**
+ b.clear()         ����ֽ�����
+ b.append(n)       ׷��һ���ֽ�
+ b.remove(value)   ɾ����һ�����ֵ��ֽڣ����û�г��֣������ValueError����
+ b.reverse()       �ֽ�˳����з�ת
+ b.decode(encoding='utf-8')      ����
+ b.find(sub[, start[,end]])      ����