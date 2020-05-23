import win32com
from win32com.client import Dispatch, constants
import os.path
import os


def xlsToxlsx():
    rootDir = r'C:\Users\user\Downloads\python\xlsx'
    rootDir1 = r'C:\Users\user\Downloads\python\xls'
    files = os.listdir(rootDir)
    nums = len(files)
    for i in range(nums):
        kname = os.path.splitext(files[i])[1]
        if kname == '.xlsx':
            fname = rootDir + "\\" + files[i]
            fname1 = rootDir1 + "\\" + files[i]
            excel = win32com.client.Dispatch('Excel.Application')
            wb = excel.Workbooks.Open(fname)
            wb.SaveAs(fname1[:-1], FileFormat=56)
            # 文件另存为xlsx扩展名的文件
            wb.Close()
            excel.Application.Quit()


if __name__ == '__main__':
    xlsToxlsx()
