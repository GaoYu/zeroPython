#练习:
#  １．　用生成器函数primes(begin, end)生成素数，给出起始值begin和终止值stop,　生成此范围内的全部素数，不包含(stop)

#  如:
#  　　　L = [x for x in primes(10, 20)] 
#  　　　将得到列表L = [11, 13, 17, 19]


def is_prime(x):
    '''判断一个数是否为素数'''
    if x<=1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
    
def primes(begin, end):
    '''用生成器函数primes(begin, end)生成素数，给出起始值begin和终止值stop,　生成此范围内的全部素数，不包含(stop)'''
    for i in range(begin, end):
        if is_prime(i) :
            yield i

L = [x for x in primes(10, 20)]
print(L)