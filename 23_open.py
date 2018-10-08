#fileopen.py

#此示例示意文件打开关闭及错误处理


try:
    # f = open('/etc/passwd')  # 此时能成功打开

    # f = open('/root/abc.txt')  # 此文件不存在
    #f = open("./abc.txt")
    f = open("./07_run_years.py")
    print("文件打开成功!")

    # 在此外进行文件的读写操作

    f.close()  # 关闭文件
except OSError:
    print("打开文件失败！")