#经理有：曹操， 刘备，周瑜
#技术员：曹操，周瑜，张飞，赵云
#用集合求；
# 1.既是经理又是技术员的有谁？
# 2.是经理，但不是技术员的有谁？
# 3.是技术员，不是经理的有谁？
# 4.张飞是经理吗？
# 5.身兼一职的有谁？
# 6.经理和技术员共几个人？

managers = {'曹操','刘备', '周瑜'}
techs = {'曹操','周瑜','张飞','赵云'}

print("既是经理又是技术员的有：", managers & techs)
print("是经理不是技术员的有：", managers - techs)
print("是技术员不是经理的有：", techs - managers)
if '张飞' in managers:
    print("张飞是经理")
else:
    print("张飞不是经理")

print("身兼一职的有", managers ^ techs)

print("经理和技术员共有%d人" % len(managers | techs))


