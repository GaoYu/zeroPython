
# 有字符串列表如下：
# L = ['tarena', 'xiaozhang', 'xiaowang']
#生成如下字典：
# d = {'tarena':6, 'xiaozhang':9, 'xiaowang':8}
#注：字典的值是键的长度

L = ['tarena', 'xiaozhang', 'xiaowang']
d = {x : len(x) for x in L}


#编号列表如下：
#Nos = [1001, 1002, 1003, 1004]
#names = ['Tom', 'Jerry', 'Spike', 'Tyke']
#生成用Nos数据为键，以names为值的字典，如下：
#{1001:'Tom',1002:'Jerry',....}
Nos = [1001, 1002, 1003, 1004]
names = ['Tom', 'Jerry', 'Spike', 'Tyke']

d = {}
for i in range(len(Nos)):
    x = Nos[i]
    d[x] = names[i]

d = {Nos[i] : names[i] for i in min(len(Nos),len(names))}
#方法2：
d = {x : names[Nos.index(x)] for Nos}

print(d)

