#iterator.py


#此示例示意用迭代器访问可迭代对象
L = [2, 3, 5, 7]

#for语句访问
for x in L:
    print(x)

print("-------------------------以下是while语句")
#用while语句循环访问列表
it = iter(L)  #用L生成一个迭代器
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        print("迭代结束")
        break
