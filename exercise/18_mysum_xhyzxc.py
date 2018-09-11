#示例星号元组形参
def func(*args):
    print("参数个数是：", len(args))
    print('args=', args)


func(1,2,3,4)
func("hello", "world", 1, 2, 3)


#写一个函数，mysum，可以传入任意实参的数字，返回所有实参的和
#星号元组形参
#方法1
#def mysum(*args):
#    return sum(args)
#方法2
def mysum(*args):
    s = 0
    for x in args:
        s += x;
    return s

print(mysum(1,2,3,4))
print(mysum(2,4,6))