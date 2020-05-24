'''

    在文件的开头定义的叫做全局变量,简单的数据类型不可以在函数内修改，数组和集合，类是可以的
'''
School = 'XinXING'
names = ['alex', 'wang']


def change_name(name):
    # global name 函数内声明局部变量，但是不会这么写
    print('before change', name)
    # 局部变量只在函数内生效，这个函数就是这个变量的作用域
    names[0] = 'ALEX'
    name = 'Alex Li'
    School = 'xin'
    print('after change', name)


name = 'alex'
change_name(name)
print(names)
