'''
装饰器不改变原有的函数调用方法增加额外的功能
高阶函数+嵌套函数--》装饰器


'''

import time


def timmer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('this func run time is %s' % (end_time - start_time))

    return deco


@timmer
def test1():
    time.sleep(3)
    print('welcome')


@timmer  # test2(timmer(test2))=deco  test2()=deco()
def test2(name, age):
    print("this is name %s" % name)


test1()
test2('alex', 19)
