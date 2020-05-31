'''
装饰器不改变原有的函数调用方法增加额外的功能
高阶函数+嵌套函数--》装饰器


'''

import time


def timmer(func):
    def deco():
        start_time = time.time()
        func()
        end_time = time.time()
        print('this func run time is %s' % (end_time - start_time))

    return deco


@timmer
def test1():
    time.sleep(3)
    print('in the test1')


test1()
