#1.用字符串s = "ABC" 和s2 = "123"生成如下列表
# ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
s = 'ABC'
s2 = '123'
L = [x+y for x in s for y in s2]
print(L)


#2.有一些数存在列表L中，如：
# L = [1, 3, 2, 1, 6, 4, 2,..., 98, 82](此数据自己定义)
# 将列表L中的数存入另一个列表L2中，（要求重复出现多次的数字只在L2列表中保留1分）


L = [1, 3, 2, 1, 6, 4, 2]
L2=[]
#for x in L:
#    if x not in L2:  # 不在L2中将其添加进来
#        L2.append(x)

#方法2
L2 = L.copy()
for x in L2:
    if L2.count(x) > 1:
        L2.remove(x)


print(L)
print(L2)

#


 #3.生产前40个斐波那契数（Fibonacci）1 1 2 3 5 8 13....（自第三个起，之后的数字为前两个数之和）
 #要求，将这些数保存在列表中，最后打印列表中的这些数
 #提示：用循环、列表和变量组合可以实现
 
L = []

a = 0 
b = 1


while len(L) <40:
    a,b = b, a+ b
    L.append(a)
    
#方法2
L = [1,1]

while len(L) < 40:
    L.append(L[-1] + L[-2])

print(L)
    
