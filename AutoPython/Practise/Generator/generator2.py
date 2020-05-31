'''
    列表元素可以通过某种算法推算出来，这种一边计算一边生成的机制叫做生成器
    这样我们不必完整的列表，节省了大量的空间
    生成器在调用的时候才会生成
    生成器只有__next__()方法，取下一个
    斐波那契函数，（1，1，2，3，5）

'''


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# print(fib(10))
f = fib(10)
print(f)

# for i in f:
#     print(f.__next__())

while True:
    try:
        x = next(f)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
