#练习:
#  写一个程序，读入任意行的文字，当输入空行时结束输入．
#  打印带有行号的输入结果:
#  如:
#    $ python3 mytest.py
#    请输入: hello<回车>
#    请输入: world<回车>
#    请输入: bye<回车>
#    请输入: <回车>
#    打印如下:
#    第1行: hello
#    第2行: world
#    第3行: bye

#L = []
#while True :
#    s = input("请输入： ")
#    L.append(s)
#    if s =='':
#        break

#for x in enumerate(L, start = 1):
#    index, element = x
#    print('第',index,'行:',element)
def get_lines():
    L =[]
    while True:
        s = input("请输入： ")
        if not s:
            break
        L.append(s)
    return L

def print_text(lst):
    for numbers,text in enumerate(lst, start = 1):
        print('第',numbers,'行:',text)

if __name__ == '__main___':
    print_text(get_lines())

