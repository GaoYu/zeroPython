def isodd(x):
    return x % 2 == 1
for x in filter(isodd, range(10)):
    print(x)
    
even = [x for x in filter(lambda x: x%2 ==0, range(10))] 


#练习:
#  1. 将 1 ~20 内的偶数用filter筛选出来，形成列表
even = [x for x in
        filter(lambda x : x%2==0, range(1,20))]
print(even)
even = list(filter(lambda x:x%2==0,range(1,20)))
print(even)
#  2. 用filter函数将1~100之间的所有素数(prime) 放入到列表中

def  isprime(i):#素数从2开始向后遍历      
    if i <= 1:
        return False
    for x in range(2, i):
    #判断能否被2整除的数
        if i % x  == 0:
            return False
    return True

L = list(filter(isprime,range(100)))
print(L)