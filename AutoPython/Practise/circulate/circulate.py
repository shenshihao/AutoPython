'''
可以迭代的对象：list,tuple,dict,set,str,generator和带yield的generator function
可以通过isinstance（）判断一个对象是否是iterable对象
可以被next()函数调用并不断返回下一个值的对象叫做迭代器：Iterator
生成器都是Iterator对象，但是，list,dict,str虽然是Iterable，却不是Iterator
把list,dict,str等Iterable变成Iterator可以使用iter()函数
凡是可以作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型
'''
from collections import Iterable

print(isinstance('abc', Iterable))

a = 'abcddfff'.__iter__()

print(a.__next__())
