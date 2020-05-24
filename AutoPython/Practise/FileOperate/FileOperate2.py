# 实现读取文件到某一行然后重新回到开始
f = open("YesterDay", 'r', encoding='utf-8')  # 文件句柄
print(f.tell())
print(f.readline())
print(f.readline())
print(f.readline())
# 定位读取的位置
print(f.tell())
# 重置文件的读取位置
f.seek(0)
# 文件编码
# print(f.encoding)
# 解决的是比如写入一行，这时候突然断电，对实时数据有影响，flush可以刷新缓存，立刻更新到硬盘上，做到了数据无丢失
f.flush()
