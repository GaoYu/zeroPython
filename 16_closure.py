#闭包
def make_power(y):
    def fx(arg):
        return arg ** y
    return fx

power2 = make_power(2)


#求 1**2 + 2**2 + ... + 9**2

#print(sum(map(lambda x:x ** 2, range(1,10))))
print(sum(map(make_power(2),range(1,10))))

#示例，用参数返回数学函数的示例
#y = a*x**2 + b*x + c

def make_function(a,b,c):
    def fx(x):
        return a * x ** 2 + b * x + c
    return fx
#创建一个y = 4*x**2 + 4 * x + c的函数用fx1绑定
fx1 = make_function(4,5,6)
print(fx1(2)) #求x = 2时，y的值
 
