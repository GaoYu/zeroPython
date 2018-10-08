#练习:
#  自己写一个文件'info.txt' 内部存一些文字信息
#       张三 20 100
#       李四 21 96
#       小王 22 98
#  写程序将这些数据读取出来，打印在屏幕终端上


def readlines_text_data():
    try:
        f = open("info.txt")
        #读取数据并打印到终端
        L = f.readlines()  #返回所有行文字
        print(L)
        f.close()
    except OSError:
        print("打开info.txt文件失败")


if __name__ == '__main__':
    readlines_text_data()

  