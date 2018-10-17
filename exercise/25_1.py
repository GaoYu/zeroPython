
#phone_book_input.py

#练习:
#  1. 写一个程序,从键盘输入如下信息:
#      姓名  和 电话号码
#    如 :
#      请输入姓名: xiaozhang
#      请输入电话: 13888888888
#      请输入姓名: xiaoli
#      请输入电话: 13999999999
#      请输入姓名: <回车>
#    把从键盘读取的信息存入'phone_book.txt'文件中
#      然后用 sublime text 打开并查看写入的内容

def get_number():
    '''此函数用来读取用户输入，形成列表并返回'''
    L = []
    while True:        
        i = int(input("请输入整数："))
        if i < 0:
            break
        L.append(i)  #形成元组列表
    return L

def save_to_file(lst, filename = 'numbers.txt'):
    '''将lst列表内的数据保存到文件filenames中'''
    try:
        f = open(filename, 'w') #打开文件
        #利用循环写入文件
        for i in lst:
            f.write(str(i))
            f.write('\n')#换行

        f.close()                #关闭文件
    except OSError:
        print("写入文件失败！")


if __name__ == '__main__':
    L = get_number()
    print(L)
    save_to_file(L)
