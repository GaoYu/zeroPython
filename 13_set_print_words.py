#任意输入一个单词，存入集合中，当输入空字符串时结束输入
#1)打印您输入的单词的种类数
#2）每个单词都打印到终端显示
#思考：如何让打印的次序和输入的次序一致？

L = []
while True:
    word = input("输入单词： ")
    if word == "":
        break
    L.append(word)

s = set(L)
print("您共输入%d种单词" % len(s))
for x in s:
    print(x)

#2）每个单词都打印到终端显示
######方法一
s = set(L)
for x in L:
    if x in s:        #如果x在集合中，说明没打印过
        pirnt(x)
        s.discard(x)  #删除已经打印过的

######方法二
L2 = []
for x in L:
    if x not in L2:
        L2.append(x)  #不重复的添加到L2
for x in L2:
    print(x)