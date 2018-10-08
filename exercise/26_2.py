#2. 写程序,将文件numbers.txt中的整数读入到内存中,重新形成数字组成的列表.计算这些数的最大值,最小值,和他们的和

def read_numbers(filename='numbers.txt', mode='rt'):
    L = []

    try:
        f = open(filename, mode) #以二进制模式打开
        #读取数据，常用f.read读取
        b = f.read()        

        numbers = b.split(',') #按分隔符进行分割
        del numbers[-1]
        for i in numbers:
            i = int(i)
            L.append(i)
        f.close
        return L
    except OSError:
        print("打开文件失败！")



def compute_nubmers(lst):
    max_lst = max(lst)
    min_lst = min(lst)
    sum_lst = sum(lst)
    return max_lst, min_lst, sum_lst


if __name__ == '__main__':
    L = read_numbers()
    #print(L)
    compute_nubmers(L)