import os
import os.path
import win32com.client as win32

rootDir = r'C:\Users\user\Downloads\python'
rootDir1 = r'C:\Users\user\Downloads\python\temp'

for parent, dirnames, filenames in os.walk(rootDir):
    for fn in filenames:
        fileDir = os.path.join(parent, fn)
        print(fileDir)
        excel = win32.gencache.EnsureDispatch("Excel.Application")
        wb = excel.Workbooks.Open(fileDir)
        # xlsx: FileFormat=51
        # xls:  FileFormat=56,
        wb.SaveAs(fileDir.replace('Xls', 'xlsx'), FileFormat=51)
        wb.Close()
        excel.Application.Quit()
