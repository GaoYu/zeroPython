#1. 写一个程序，以电子时钟格式打印时间:
#    时间格式为:
#        HH:MM:SS
#    时间每隔一秒刷新一次

import time
def clock():
    while True:
        #先获取当前时间，在打印
        #cur_time = time.localtime()
        #c_hms = cur_time[3:6]
        #print("%02d:%02d:%02d" % c_hms)
        #方法二
        c_hms = time.strftime('%X',time.localtime())
        print(c_hms)
        time.sleep(1)
clock()

#2. 编写一个闹钟程序，启动时设置定时时间，到时候后打印出一句语，然后程序退出
#import time
#def clock_2():
#    end = time.strftime('%X',time.strptime(input("请设置定时时间："), '%H:%M:%S'))
#    while True:
#        c_hms = time.strftime('%X',time.localtime(time.time()))
#        time.sleep(1)
#        print(c_hms)
#        if c_hms == end:
#            print("时间到，请起床！")
#            return    
#clock_2()
#while True:
#    c_hms = time.strftime('%X',time.localtime())
#    if c_hms == end:
#        print("时间到，请起床！")

import time
def alarm(hour, minute):
    '''hour代表定时的小时
       minute代表定时的分钟
    '''
    while True:
        cur_time = time.localtime()
        tuple_hm = cur_time[3:5]
        print("%02d:%02d:%02d" % cur_time[3:6])
        if (hour, minute) == tuple_hm:
            break
def main():
    h = int(input("请输入小时： "))
    m = int(input("请输入分钟： "))
    alarm(h, m)  #用函数来计时，函数返回时间到！
    print("时间到....!")

main()

  #3. 请编写函数fun,其功能是计算下列多项式的和
  #   sn = 1 + 1/1! + 2/2! + 3/3! + ... n/n!
  #   计算n为100时的值
  #  看一下求出来的和是什么?
  #  (建议用math.factorial)
#from math import factorial
#def fx(n):
#    L =[]
#    for i in range(n+1):
#         L.append(i/factorial(i))
#    return sum(L) 
#fx(100)


import math
def fun(n):
    formula = lambda x : 1/math.factorial(x)
    return sum(map(formula, range(n+1)))

print('n=100时，fun(100)=', fun(100))