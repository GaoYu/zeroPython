#2. 写一个读取'phone_book.txt'文件的程序, 把保存的信息以表格的形式打印出来
#     +-----------+-----------------+
#     |  name     |   number        |
#     +-----------+-----------------+
#     | xiaozhang |   1388888888    |
#     +-----------+-----------------+

def read_info_from_file(filename='phone_book.txt'):
    '''读取文件存入列表'''
    L = []
    #读取文件信息，形成元组后放入L
    try:
        f = open(filename)

        while True:
            #读取数据
            s = f.readline()
            if not s:
                break
            s = s.rstrip()#去掉右侧的换行符

            name, number = s.split(',')#拆成['姓名','电话']
            L.append((name, number))
        f.close()
    except OSError:
        print("打开文件失败！")
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
    L = read_info_from_file()
    print_infos(L)