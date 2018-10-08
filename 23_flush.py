#flush.py

import time

f = open('infos.txt', 'w')

f.write('hello')
f.flush()  #强制清空缓存区，数据从缓冲区写入磁盘
#for i in range(10000):
#    f.write('helloooooo')
#    time.sleep(0.01)

print("程序开始睡觉......zzz")
time.sleep(15)
print("程序睡醒，继续执行") #睡醒之后infos文件才有内容

f.close()