#file_seek.py

#此示例示意用f.seek方法移动文件的读写指针位置

f = open("infos.txt", 'rb') #以二进制模式打开

f.seek(5, 0) #相对于文件头向后移动5个字节
f.seek(-4,2)#相对于文件尾向前移动15个字节 

b = f.read(2)#已经开始读
f.seek(3,1) #从当前位置开始向后移动3个字节

b = f.read(5)         #在读取5个字节
print(b)

f.close()
