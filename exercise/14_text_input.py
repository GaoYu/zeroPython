#练习：输入多行文字，当输入空行时结束输入
#将原输入的所有字符串存于列表L中
#1.将原来的输入的行的顺序反向打印这些行
#  例：
#     输入：hello world
#     输入: welcome to china
#     输入: I like python
#  显示：
#     I like python
#     welcome to china
#     hello world
#2.打印出您共输入多少字符？


L = []


while True:
    s = input("输入： ")
    if not s:  # s为空跳出循环
        break
    L.append(s) #追加到L
print(L)


s = 0  #记录字符的个数
###方法一：while循环
#i = len(L) -1   #最后一行的索引
         
#while i >= 0 :
#    print(L[i])
#    s + = len(L[i])
#    i -= 1
#print("字符的个数是： ",s)


###方法二：for循环
#先反转
L.reverse()
for line in L:
    print(line)
    s += len(line)
print("字符的个数是：",s)
