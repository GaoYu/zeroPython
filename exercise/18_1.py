#练习：
#　　　1. 素数prime函数练习
#      1)  写一个函数isprime(x)  判断x是否为素数，如果是素数，返回True,否则返回False
#      2) 写一个函数prime_m2n(m, n), 返回从m开始到n结束(不包含n)的范围内的素数列表
#        如:
#          L = prime_m2n(1, 10)
#          print(L) # [2,3,5,7]
#      3) 写一个函数primes(n), 返回指定范围内素数(不包含n)的全部素数的列表,并打印这些素数
#        如:
#          L = prime(20)
#          print(L)  # [2,3,5,7,11,13,17,19]
#        1) 打印 100以内的全部素数
#        2) 打印 100以内全部素数的和


#素数：质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。

#判断i是否是素数  
def  isprime(i):#素数从2开始向后遍历      
    for x in range(2, i):
        if i % x  == 0:
            return False
            break
    else:
        return True


#返回m,n素数列表
def prime_m2n(m, n):
    L = []
    for i in range(m, n):
        if i >1:
            if isprime(i):
                L.append(i)
        
    return L

L = prime_m2n(1,10)
print(L)
#frimes()
def primes(n):
    L = []
    for i in range(n):
        if i > 1:
            if isprime(i):
                L.append(i)
    return L

L = primes(20)
print(L)


L = primes(100)
s = 0
for x in L:
    print("100以内的全部素数有：",x)
    s += x
    print("100以内的全部素数的和是：",s)

