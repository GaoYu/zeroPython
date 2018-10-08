#read_binary_file.py

#此示例示意二进制方式读取文件内容

try:
    f = open("infos.txt", 'rb') #以二进制模式打开
    #读取数据，常用f.read读取
    b = f.read(5)  #二进制不分行，5代表5个字节bytes
    print(b)
    b = f.read(2)
    print(b)
    b = f.read() #不加参数读取全部字节，直至文件尾
    print(b)
    f.close

except OSError:
    print("打开文件失败！")