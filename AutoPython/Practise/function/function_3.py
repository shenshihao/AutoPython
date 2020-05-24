# ab 二进制追加的方式
'''
 当返回值个数=0 返回None
 当返回值个数=1 返回object
 当返回值个数=多个 返回tuple
 为什么要有返回值？查看函数的执行结果，后面的函数可以根据这个执行结果来进行接下来的操作

'''
import time


def test1():
    print('in the test1')


def test2():
    print('in the test2')
    return 0


def test3():
    print('in the test3')
    return 1, 'hello world', ['aa', 'bb']


x = test1()
y = test2()
z = test3()
print(x)
print(y)
print(z)
