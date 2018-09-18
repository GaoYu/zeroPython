
#写一个计算器解释执行器：
#已知有如下函数：
#def myadd(x, y): #计算两个数相加
#    return x + y
#def mymul(x, y): #计算两个数相乘
#    return x * y

#def get_op(s):  #s代表操作字符串：'加'，'乘'
#    此处自己实现

#主函数：
#def main():
#    while True:
#        s = input('请输入计算公式： ') #如：10 加 20
#        L = s.split()
#        a, s, b = L
#        a, b = int(a), int(b)
#        fn = get_op(s)
#        print("结果是：", fn(a, b))  #结果是30

def myadd(x, y): #计算两个数相加
    return x + y
def mymul(x, y): #计算两个数相乘
    return x * y

def get_op(s = "加"):  #s代表操作字符串：'加'，'乘'
    if s == '加' or s == '+':
        return myadd
    elif s == '乘' or s == '*':
        return mymul
    else:
        return "输入有误"


#主函数：
def main():
    while True:
        s = input('请输入计算公式：') #如：10 加 20
        L = s.split()
        a, s, b = L
        a, b = int(a), int(b)
        fn = get_op(s)
        print("结果是：", fn(a, b))  #结果是30