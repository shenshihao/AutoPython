'''
   函数的几种
   1.常规函数，比如func(x,y)
   2.默认参数函数 比如func(host,port=3306),默认参数也可以不赋值
   3.非固定参数,随着业务的发展，参数变了，这样预留这样的参数
'''


def test(*args):
    print(args)


test(1, 2, 3, 4, 5, 6)
test(*[1, 2, 3, 4])  # args =tuple([1,2,3,4])
