'''
   函数的几种
   1.常规函数，比如func(x,y)
   2.默认参数函数 比如func(host,port=3306),默认参数也可以不赋值
   3.非固定参数,随着业务的发展，参数变了，这样预留这样的参数
'''


# 接受字典
def test(**kwargs):
    print(kwargs)
    print(kwargs['name'])


def test2(name, **kwargs):
    print(name)
    print(kwargs)


# *args接受n个位置参数，转换成字典的方式，kwargs接受k-v模式
def test3(name, age=18, *args, **kwargs):
    print(name)
    print(age)
    print(kwargs)


# 关键字参数 k-v格式，关键字转换成key
# test(name='alex', age=8, sex='男')
# # test(**{'name': 'alex', 'age': 8, 'sex': '男'})

# test2('Alex', age=16, sex='m')
test3('Alex', sex='m', hobby='tesla', age='3')
