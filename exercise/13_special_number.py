#求1~100(包含100)之间所有不能被5，7，11整除的数的和是多少
#建议用continue
s = 0          #保存累加和
for x in range(101):
    if x % 5 ==0 or x % 7 ==0 or x % 11 ==0:
        continue
    s += x
    print("和为：",s)
