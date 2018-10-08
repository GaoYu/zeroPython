#writelines

#此示例示意f.writelines方法

f = open('mynote.txt', 'w')

L = ['我是第一行\n','我是第二行']
f.writelines(L)
f.close()