# 实现读取文件到某一行然后重新回到开始
f = open("YesterDay", 'w', encoding='utf-8')  # 文件句柄
# f.seek(10) 在这里不好使
f.truncate(10)
