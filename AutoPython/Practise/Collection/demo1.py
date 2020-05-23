list_1 = [1, 1, 1, 2, 3, 4, 5]
# 去重
list_1 = set(list_1)
print(list_1, type(list_1))
#
list_2 = set([2, 3, 99, 6, 5, 4])
print(list_2)

# 取交集
print(list_1.intersection(list_2))

# 并集
print(list_1.union(list_2))

# 差集 in list_1 but not in list_2

print(list_1.difference(list_2))

# 子集

print(list_1.issubset(list_2))

# 父集
print(list_1.issuperset(list_2))

# 增加
list_1.add(11)
list_1.remove(11)
list_1.update([66, 77, 44])
list_1.discard()
print(list_1.pop())
print(1 in list_1)
print(2 not in list_1)
