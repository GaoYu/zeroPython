#写程序输入一段字符串，打印出这个字符串中出现过的字符及出现过的次数
#如：
#   输入：ABCDABCABA
#输出：
#   A:4次
#   C:2次
#   B:3次
#   D:1次
#注意：不要求打印的顺序

s = input("输入字符串： ")
d = dict()  #字典的键是出现的字符，字典的值是出现的次数

#for x in s:         #所有的字符都取一遍
#    #如果第一次出现，则把x作为键，把1作为值加入字典中
#    #如果已经出现过，则把x键对应的值 +1操作
#    if x not in d:
#        d[x] = 1
#    else:
#        d[x] +=1
#    print(d)

#for k in d:
#    print(k, ':', d[k],"次")


##方法2：
d = {}
for ch in s:
    if ch not in d:  #把将一次出现的字符加入字典中
        d[ch]  = None
for ch in d:
    print(ch,":",s.count(ch),"次")




