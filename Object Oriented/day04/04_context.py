#03_context.py
#此示例示意环境管理器的定义及使用
class A:
   def __enter__(self):
      print("已进入with语句")
      return self  # 返回的对象将由 as绑定
   def __exit__(self, exc_type, exc_val, exc_tb):
       '''此方法再退出with语句时自动调用
          exc_type在没有异常时为None，在出现异常时为异常类型
          exc_val在没有异常时为None，在出现异常时异常绑定错误对象
          exc_tb在没有异常时为None,出现异常时绑traceball
       '''

       if exc_type is None:
           print("已离开with语句, 离开时状态异常")
       else:
           print("已离开with语句")
           print("异常类型是：", exc_type)
           print("错误对象是：", exc_val)
           print("traceback是：", exc_tb)
#a = A()

with A() as a:
    print("这是with语句内的一条语句")
    int(input("请输入整数："))
