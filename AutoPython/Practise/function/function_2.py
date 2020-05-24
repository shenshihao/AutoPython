# ab 二进制追加的方式
import time


def logger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('a.txt', 'a+') as f:
        f.write('%s end action' % time_current)


def test():
    print('this is test1')
    logger()


def test1():
    print('this is test2')
    logger()


def test2():
    print('this is test3')
    logger()


test()
