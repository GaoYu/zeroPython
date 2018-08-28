#打印1~20的整数，每行5个，打印四行
#(注：while语句可以嵌入if语句)

i = 1

while i <= 20:
    print(i, end= ' ')
    i += 1
    if i % 5 == 0:
        print('\n')

print("程序结束！ i= ", i)
        

