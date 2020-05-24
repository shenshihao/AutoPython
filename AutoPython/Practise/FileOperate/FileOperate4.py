# 实现读取文件到某一行然后重新回到开始
# 读写对应的也有写读
# f = open("YesterDay", 'r+',encoding='utf-8')#文件句柄
# #f.seek(10) 在这里不好使
# print(f.readline())
# #追加模式，不能指定到某一行
# f.write('-------------------------')

# f = open("YesterDay", 'r+', encoding='utf-8')  # 文件句柄
# f = open("YesterDay", 'a+', encoding='utf-8')  # 文件句柄，追加读写
f = open("YesterDay", 'wb')  # 文件句柄，二进制读rb，二进制写wb

# f.seek(10) 在这里不好使
# print(f.readline())
f.write('hello world \n'.encode('utf-8'))
# 追加模式，不能指定到某一行
# f.write('-------------------------')
