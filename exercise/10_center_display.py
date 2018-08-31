s1 = input("第一个字符串： ")
s2 = input("第二个字符串：")
s3 = input("第三个字符串：")

# m为最长的字符串长度
m = max(len(s1), len(s2), len(s3))


line1 = '+' + '-'*m + '+'
print(line1)

print('|' +  s1.center(m) + '|')
print('|' +  s2.center(m) + '|')
print('|' +  s3.center(m) + '|')

print(line1)

