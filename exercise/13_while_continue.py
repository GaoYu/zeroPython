#打印10以内的偶数

i  = 0
while i <10:
   
    if i % 2 == 1:
        i += 1         # continue之前想办法修改循环变量，否则容易死循环
        continue
    print(i)
    i +=1
    
    
    
