#2. 写一个读取'phone_book.txt'文件的程序, 把保存的信息以表格的形式打印出来
#     +-----------+-----------------+
#     |  name     |   number        |
#     +-----------+-----------------+
#     | xiaozhang |   1388888888    |
#     +-----------+-----------------+

def read_from_file(filename='numbers.txt'):
    '''读取文件存入列表'''
    L = []
    #读取文件信息，形成元组后放入L
    try:
        f = open(filename)
        try:
            #读取数据
            for line in f: #line绑定末尾带"\n"的字符串
                n = int(line.rstrip())
                L.append(n)
        finally:
            f.close()
    except OSError:
        print("打开文件失败！")
    except ValueError:
        print("读取文件错误,数据可能不完整")
    return L

def print_infos(lst):
    print('+----------+------------+')
    print('|    name  |   number   |')
    print('+----------+------------+')

    for d in lst:  #d绑定的是元组
        t = (d[0].center(10), 
             d[1].center(12))
        line = "|%s|%s|" % t   #t是元组
        print(line)
    print('+----------+------------+')



if __name__ == '__main__':
    L = read_from_file()
    print_infos(L)

    print("最大：",max(L))
    print("最小：", min(L))
    print("和：", sum(L))