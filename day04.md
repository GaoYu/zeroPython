# �б�

##�б�� in / not in
1.�ж�һ��Ԫ���Ƿ���������У��ڷ���True,���򷵻�False

2.not in �� in������෴

ʾ����

x = [1, 'two', 3.14, '��'] \
1 in x           #True    \
3 not in x       #True

##�б������ index  /��Ƭ slice

###�б�������﷨��
   �б�[�������ʽ]

###�÷���
   �б������ȡֵ���ַ���������ȡֵ������ȫ��ͬ
   
   �б��������Ϊ���������ͷ�������

ʾ����   
  x = [1, 'two', 3.14, '��']
  
  print(x[1]) # 'two'
  
##�б��������ֵ
   �б��ǿɱ�����У�����ͨ��������ֵ�ı��б��Ԫ��

###�﷨��
   �б�[����]  = ���ʽ

###ʾ����
   x = [1, 2, 3, 4]
   
   x[2] = 3.14  #�ı������Ԫ��
   
   y = [1, 2, 3, 4]
   
   id(x) 
   
   id(y)          #id(x)��һ��
   
   x[2] = 3.14
   
   id(x)          #id(x)û�仯
   
   x += '123'     
   
   id(x)          #id(x)�Ѿ���һ����,'123'�½���
   
   x += [1,2,3,4] #id(x)û�б仯,�ı�����б���ֵ
   
   
##�б���Ƭ
   - �б�[:]
   - �б��[::]
   - �б����Ƭȡֵ����һ���б������ͬ���ַ�������Ƭ����
   
 ʾ����
   - x = list(range(8))
   - y = x[1:9:2] # y = [1, 3, 5, 7]
   
   
##�б����Ƭ��ֵ�﷨
   �б�[��Ƭ] = �ɵ�������

###˵����
   ��Ƭ���Ƶĸ�ֵ��������Ҳ������һ���ɵ�������

###ʾ����
  - L = [2, 3, 4]  # 0~2
  - L[0:1] =[1.1, 2.2]
  - L[3:3] = [5, 6]
   
###��Ƭ������Ϊ1
���ڲ�����Ϊ1����Ƭ��ֵ����ֵ������Ҳ�Ŀɵ��������ṩ��Ԫ�صĸ���һ��Ҫ������Ƭ�Ķ�����

   - L = list(range(1,9))
   - L[1::2] = [2.2, 4.4, 6.6, 8.8]
   - print(L)

##del���
����ɾ���б�Ԫ��

###�﷨
- del �б�[����]
- del �б�[��Ƭ]

###ʾ����
- L = [1, 2, 3, 4, 5, 6]
- del L[0]
- del L[::2]  #L = [2, 4, 6]

##���������к���
- len(x)
- max(x)
- min(x)
- sum(x)
- any(x) #��ֵ���ԣ�����б���һ��ֵΪ����ΪTrue,���򷵻�False��
- all(x) #��ֵ���ԣ�����б���������Ϊ���򷵻�True��ֻҪһ��Ϊ���򷵻�False

##�б�ķ���

help(list)

 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)  
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 
 
##�ַ����ı��������� split ��join

###S.split(sep=None) 
���ַ�����ʹ��sep��Ϊ�ָ����ָ�S�ַ��������طָ����ַ����б�������������ʱ���ÿհ��ַ���Ϊ�ָ������зָ�
###S.join(iterable)
�ÿɵ��������е��ַ���������һ���м���S���зָ���ַ���

����
- s = 'Beijing is capital'
- L = s.split(' ') #L = ['Beijing','is','capital']
- s1 = "-".join(L)
 
 
##���deep copy��ǳ���� shallow copy

###ǳ����
��ָ�ڸ��ƹ�����ֻ����һ����������Ḵ���������󶨵Ķ���ĸ��ƹ��̡�

ǳ�������Թ���ͬһ������

 - L = [3.1, 3.2]
 - L1 = [1, 2, L] #[1, 2, [3.1, 3.2]]
 - L2 = L1.copy() #[1, 2, [3.1, 3.2]]  
 - L2[2][0] = 3.14
 - print(L)      #[3.14, 3.2]
 - print(L1)     #[1, 2, [3.14, 3.2]]
 - print(L2)     #[1, 2, [3.14, 3.2]]

###���
ֻ�����ɱ�Ĳ��ֱ��������ɱ���󲻿���

- import copy            #����copyģ��
- L = [3.1, 3.2]
- L1 = [1, 2, L]
- L2 = copy.deepcopy(L1)  #���
- print(L1)   #[1, 2, [3.1, 3.2]]
- print(L2)   #[1, 2, [3.1, 3.2]]

- L2[2][0] = 3.14      #L1 ,L2 �ı�Ĳ��ֲ�һ����
- print(L1)     #[1, 2, [3.1, 3.2]]
- print(L2)     #[1, 2, [3.14, 3.2]]


##�б��Ƶ�ʽ
�б��Ƶ�ʽ���ÿɵ��������������ɴ��ж��Ԫ�ص��б�ı��ʽ

###���ã�
   �ü��׵ķ��������б�

###�﷨��
   - [���ʽ for ���� in �ɵ�������]
   
   - [���ʽ for ���� in �ɵ������� if ��ֵ���ʽ]
   
###ʾ����
   #����һ����ֵΪ1~9��ƽ�����б�
   
   - L = [X*X for x in range(1,10)]

##�б��Ƶ�ʽ��Ƕ��

###�﷨
[���ʽ1
  for ����1 in �ɵ�������1 if ��ֵ���ʽ1
    for ����2 in �ɵ�������2 if ��ֵ���ʽ2
      ...]
      
###ʾ��
- L1 = [2, 3, 5]
- L2 = [7, 11, 13]

��L1 �е�ȫ��Ԫ����L2�е�ȫ��Ԫ��������˺�ŵ�L3�б���

L3 = [x * y  for x in L1 
         for y in L2]

print(L3)