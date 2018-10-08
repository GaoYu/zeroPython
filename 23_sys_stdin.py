#sys_stdin.py

import sys

s = sys.stdin.readline()
print('从键盘读取第一行内容',s)

s = sys.stdin.read() #永远都不到文件尾
print('read读取的信息是',s)

print("程序推出")
