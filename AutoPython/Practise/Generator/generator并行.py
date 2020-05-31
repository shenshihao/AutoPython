import time


def consumer(name):
    print("%s 准备吃包子啦!" % name)
    while True:
        baozi = yield

        print("包子[%s]来了,被[%s]吃了!" % (baozi, name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)


# c = consumer('zhao')
# #next只是在调用yield但是不会给yield传值
# c.__next__()
# b1 = '鲜肉'
# #send给yield传值并调用yield
# c.send(b1)
producer("alex")
