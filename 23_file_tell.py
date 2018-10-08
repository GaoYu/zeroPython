#file_tell.py

#此示例示意用f.tell方法获取文件当前读写位置

f = open("infos.txt", 'rb') #以二进制模式打开

print("当前的读写位置是：", f.tell()) #0
b = f.read(5)
print("当前的读写位置是：", f.tell()) #5
b = f.read() #读取全部内容
print("文件最后的位置是：", f.tell()) 


f.close()