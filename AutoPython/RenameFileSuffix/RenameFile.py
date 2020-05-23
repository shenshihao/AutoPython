import os

path = input("请输入文件路径：（结尾加/）：")
fileList = os.listdir(path)
n = 0
for i in fileList:
    print(i)
    oldname = path + os.sep + fileList[n]
    print(oldname)
    # print(i)
    # print(fileList[1])
    # print(type(fileList[n].split('v01')[0] + 'V01.xlsx'))
    newname = path + os.sep + fileList[n].split('v01')[0] + 'V01.xls'
    # print(newname)
    os.rename(oldname, newname)

    # n = n + 1
