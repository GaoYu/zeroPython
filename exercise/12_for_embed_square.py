#打印指定宽度的正方形
#如：
#请输入：5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

n = int(input("请输入： "))
for _ in range(n): 
    for x in range(1, n+1):
        print(x, end = " ")
    print()    


    


