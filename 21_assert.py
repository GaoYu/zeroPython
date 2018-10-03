#assert.py

#此示例assert用法

def get_age():
    a = int(input("请输入年龄: "))
    assert 0 <= a <= 140,  '年龄不在合法范围内'
    return a

try:
    age = get_age()
except AssertionError as e:
    print("错误原因是：", e)
    age = 0
print("年龄是：", age)
