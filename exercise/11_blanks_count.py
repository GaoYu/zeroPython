#输入一个字符串，判断这个字符串有几个空格‘ ’
#（要求不允许使用s.count方法），建议使用for语句实现

s = input("输入一段字符串： ")
count = 0  #此变量替代,用来记录空格的个数
                                                                                                                                             

for ch in s:
    if ch == ' ':
        count +=1

print("空格的个数是",count)








