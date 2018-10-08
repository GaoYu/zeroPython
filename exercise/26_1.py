#练习:
#   1. 写程序让用户输入一系列整数,当输入小于零的数时结束输入
#      1) 将输入的数字存于列表中
#      2) 将列表中的数字写入到文件numbers.txt中
#      (提示: 需要将整数转为字符串或字节串才能存入文件中)

def input_numbers():
    '''存储用户输入的整数的列表'''
    L = []
    while True:
        n = input("请输入数字： ")
        if int(n) < 0 or not n:
            break
        L.append(n)
    return L

def save_numbers(lst, filename='numbers.txt'):
    '''将列表存储在numbers.txt文件中'''
    try:
        f = open(filename,'wt')
        for n in lst:
            f.write(n)
            f.write(',')
        f.close()
    except OSError:
        print("结束输入")

if __name__ == '__main__':
    L = input_numbers()
    #print(L)
    save_numbers(L)

            
