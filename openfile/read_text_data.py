#练习:
#  自己写一个文件'info.txt' 内部存一些文字信息
#       张三 20 100
#       李四 21 96
#       小王 22 98
#  写程序将这些数据读取出来，打印在屏幕终端上


def read_text_data():
    try:
        f = open("info.txt")
        #读取数据并打印到终端
        while True:
            s = f.readline()
            if not s:       #已读到文件末尾
                break 
            if s[-1] == '\n':  #回车键去掉
                print('---->',s[:-1])
            else:
                print('---->', s)
        #关闭文件    
        f.close()
    except OSError:
        print("打开info.txt文件失败")


if __name__ == '__main__':
    read_text_data()
