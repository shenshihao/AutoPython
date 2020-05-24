import sys

'''
1.修改文件,根据字符串修改
2.为了避免打开文件后忘记关闭，可以通过管理上下文 with open('file','r') as f

'''

# f = open("YesterDay3", 'r', encoding='utf-8')  # 文件句柄
# f_new = open('yesterDay3.bak', 'w', encoding='utf-8')
with open('YesterDay3', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)
