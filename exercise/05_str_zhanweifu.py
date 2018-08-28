#联系：输入三行文字，让这些文字一次以20字符的宽度右对齐输出
#如：
#请输入第一行：hello world
#请输入第二行：abcd
#请输入第三行：a
#输出结果：
#          hello world
#                 abcd
#                    a
#之后，思考：
#能否以最长字符串的长度进行右对齐显示（左侧填充空格）


s1 =input("请输入第一行： ")
s2 =input("请输入第二行： ")
s3 =input("请输入第三行： ")
print('---以下是所有字符串占20个字符串宽度')
print('%20s' % s1)
print('%20s' % s2)
print('%20s' % s3)

print('---一以下按照最长的字符串左对齐')
m = max(len(s1), len(s2), len(s3))
print('最大长度是： ', m)
print(' '*(m - len(s1)) + s1)
print(' '*(m - len(s2)) + s2)
print(' '*(m - len(s3)) + s3)

print("-----------方法3---------")
fmt = '%%%ds' % m #生成一个含占位符的字符串

print('fmt = ', fmt)
print(fmt % s1)
print(fmt % s2)
print(fmt % s3)

