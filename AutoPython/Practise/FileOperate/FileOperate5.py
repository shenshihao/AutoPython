import sys

'''
1.修改文件,根据字符串修改

'''
find_str = sys.argv[1]
replace_str = sys.argv[2]
f = open("YesterDay3", 'r', encoding='utf-8')  # 文件句柄
f_new = open('yesterDay3.bak', 'w', encoding='utf-8')

for line in f:
    if find_str in line:
        line = line.replace(find_str, replace_str)
    f_new.write(line)

f.close()
f_new.close()
