#write_binary_file.py

#此示例示意以二进制方式进行数据写入操作

try:
    f = open("data.bin", "wb")
    #在此处需要以字节串味单位进行操作
    f.write(b'\xe4')
    f.write(b'\xb8')
    f.write(b'\xad')
    f.write(b'\n\x41\x42\x43')

    f.close()
except OSError:
    print("写入失败")
