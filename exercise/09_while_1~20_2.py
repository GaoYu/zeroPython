#打印1~20的整数，每行5个，打印四行
#(注：while语句可以嵌入if语句)

i = 1

while i <= 20:
    print(i, end= ' ')

    if i % 5 == 0:
        print('\n')
    i += 1
else:
    print()
print("程序结束！ i= ", i)
        

