#myzip.py

#此示例示意zip函数内部实现机制
def myzip(iter1, iter2):
    it1 = iter(iter1)
    it2 = iter(iter2)
    while True:
        x = next(it1) #可能触发StopIteration
        y = next(it2) #可能触发StopIteration,for循环会停止 
        yield(x, y)



numbers = [10086, 10000, 10010, 95588]
names = ['中国移动','中国电信','中国联通']

for x in myzip(numbers, names):
    print (x)
