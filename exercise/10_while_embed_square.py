#打印指定宽度的正方形
#如：
#请输入：5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

n = int(input("请输入： "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(j, end=" ")
        j += 1
   
    print()#尾行换号
    i += 1
