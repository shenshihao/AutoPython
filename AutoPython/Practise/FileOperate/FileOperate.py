# 我这个程序默认是处理不了gbk的,比较笨重,操作权限为r,w,a,a为追加不创建文件，w会创建新的文件
f = open("YesterDay", 'r', encoding='utf-8')  # 文件句柄
# data=f.read()
# #error:io.UnsupportedOperation: not writable
# #默认是创建文件
# #read(),read_line()一行一行读
# f.write('我爱北京')
# f.close()

'''
循环打印文件的每一行,不打印第五行,
可以使用enumerate,这种方法比较low，
当读取文件较大的时候会造成内存不足
的情况,比如内存只有16G,一下子加载进去了
'''
# for index,line in enumerate(f.readlines()):
#
#     if index==5:
#         print('------------------------------')
#         continue
#     print(line.strip())


'''
以下方法会在内存中只保留一条记录
这种循环方法比较高效，针对大文件
处理无压力
'''
count = 0
for line in f:
    if count == 9:
        print('--------------------')
        count += 1
        continue
    print(line)
    count += 1
# print(f.readlines())
