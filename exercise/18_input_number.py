#写一个函数input_number
#def input_number():
#    ...

#此函数用来获取用户循环输入的整数，当用户输入负数时，结束输入
#将用户输入数以列表的形式返回，再用内建函数max,min,sum显示用户输入的最大值、最小值、及和
#如：
#L = input_number()
#print(L) #打印此列表
#print("用户输入的最大数是：",max(L))
#print("用户输入的最小数是：",min(L))
#print("用户输入的和是：",sum(L))

def input_number():
    L = []
    while True:
        n = int(input("输入的数是："))
        if n < 0 :        #如果n 负数，把之前的值返回L
            return L
        L.append(n)       # 如果n大于0，加入列表  

L = input_number()
print(L) #打印此列表
print("用户输入的最大数是：",max(L))
print("用户输入的最小数是：",min(L))
print("用户输入的和是：",sum(L))
