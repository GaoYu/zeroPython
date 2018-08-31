#计算1 + 3 + 5 + 7 + ... + 99的和，用while和for语句两种方法实现


s = 0       #存储求和结果

#while语句实现
#i = 1
#while i <100:
#    #i 累加 到s
#    s += i
#    i += 2



for x in range(1,100,2):
    s += x
    print("和为",s)
